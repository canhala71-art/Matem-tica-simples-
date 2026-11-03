import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import { listSavedLessons, queueSize } from '../lib/offline';
import { DailyChallenge } from '../components/DailyChallenge';
import { CATEGORIES } from '../lib/quiz';
import { SUB_PT, TIER_PT, useAccess } from '../lib/billing';

interface AttemptRow { is_correct: boolean; time_spent_seconds: number | null; created_at: string }
interface MasteryRow { competency: string; attempts_count: number; correct_count: number; mastered: boolean }

function greeting(): string {
  const h = new Date().getHours();
  return h < 12 ? 'Bom dia' : h < 19 ? 'Boa tarde' : 'Boa noite';
}
function nudge(total: number, rate: number): string {
  if (total === 0) return 'Vamos começar? O primeiro exercício é sempre o mais importante.';
  if (rate >= 80) return 'Estás a ir muito bem. Que tal subir a fasquia com um quiz avançado?';
  if (rate >= 50) return 'Bom ritmo! Cada exercício te deixa mais perto de dominar a matéria.';
  return 'Está tudo bem errar: é assim que o cérebro aprende. Continua, vais notar a diferença.';
}

const LEVELS = ['Fundamentos', 'Matemática Básica', 'Ensino Secundário', 'Preparação Académica', 'Universidade', 'Especialização'];

export function Dashboard() {
  const { profile, session, refresh } = useAuth();
  const { access } = useAccess();
  const [attempts, setAttempts] = useState<AttemptRow[] | null>(null);
  const [mastery, setMastery] = useState<MasteryRow[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!session) return;
    const uid = session.user.id;
    void (async () => {
      const [a, m] = await Promise.all([
        supabase.from('attempts').select('is_correct, time_spent_seconds, created_at').eq('user_id', uid)
          .order('created_at', { ascending: false }).limit(1000),
        supabase.from('mastery').select('competency, attempts_count, correct_count, mastered').eq('user_id', uid),
      ]);
      if (a.error || m.error) { setError('Não foi possível carregar o progresso.'); return; }
      setAttempts((a.data ?? []) as AttemptRow[]);
      setMastery((m.data ?? []) as MasteryRow[]);
    })();
  }, [session]);

  async function setLevel(n: number) {
    if (!session) return;
    await supabase.from('profiles').update({ academic_level: n }).eq('id', session.user.id);
    await refresh();
  }

  const total = attempts?.length ?? 0;
  const correct = attempts?.filter((a) => a.is_correct).length ?? 0;
  const minutes = Math.round((attempts ?? []).reduce((s, a) => s + (a.time_spent_seconds ?? 0), 0) / 60);
  const mastered = mastery.filter((m) => m.mastered);
  const difficulties = mastery.filter((m) => m.attempts_count >= 3 && m.correct_count / m.attempts_count < 0.5);

  const days = Array.from({ length: 7 }, (_, i) => {
    const d = new Date();
    d.setHours(0, 0, 0, 0);
    d.setDate(d.getDate() - (6 - i));
    return d;
  });
  const perDay = days.map((d) => {
    const next = new Date(d); next.setDate(next.getDate() + 1);
    return (attempts ?? []).filter((a) => { const t = new Date(a.created_at); return t >= d && t < next; }).length;
  });
  const maxDay = Math.max(1, ...perDay);
  const saved = listSavedLessons();
  const pending = queueSize();

  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <h1 className="text-2xl font-bold">{greeting()}, {(profile?.display_name ?? 'estudante').split(' ')[0]}!</h1>
        <p className="muted">{attempts ? nudge(total, total ? Math.round((correct / total) * 100) : 0) : 'A preparar o teu painel…'}</p>
        {access && (
          <p className="text-xs text-slate-500">
            Plano: <strong>{TIER_PT[access.tier]}</strong> ({SUB_PT[access.status]}
            {access.days_left > 0 ? `, ${access.days_left} dias` : ''}) ·{' '}
            <Link className="text-electric-500" to={access.tier === 'free' ? '/planos' : '/assinatura'}>{access.tier === 'free' ? 'Ver planos' : 'Minha assinatura'}</Link>
          </p>
        )}
      </div>

      <DailyChallenge />

      <section className="space-y-2">
        <h2 className="font-semibold">Por onde queres começar?</h2>
        <div className="grid grid-cols-2 gap-2 sm:grid-cols-5">
          {CATEGORIES.map(([k, l]) => (
            <Link key={k} to={`/quiz?categoria=${k}`} className="card card-hover !p-3 text-center text-sm font-medium hover:border-electric-500">{l}</Link>
          ))}
        </div>
        <p className="muted">Ou vai direto às <Link className="text-electric-500" to="/academia">aulas da Academia</Link>.</p>
      </section>

      {profile && profile.academic_level === null && (
        <div className="card space-y-3">
          <h2 className="font-semibold">Em que nível queres começar?</h2>
          <div className="grid gap-2 sm:grid-cols-2">
            {LEVELS.map((l, i) => (
              <button key={l} className="btn-ghost justify-start" onClick={() => void setLevel(i + 1)}>
                <span className="badge">{i + 1}</span> {l}
              </button>
            ))}
          </div>
          <p className="muted">Podes mudar mais tarde. O nível só serve para te sugerir por onde começar.</p>
        </div>
      )}

      {error && <p role="alert" className="text-red-600">{error}</p>}

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        <Stat label="Exercícios feitos" value={attempts ? String(total) : '…'} />
        <Stat label="Taxa de acertos" value={attempts ? (total ? `${Math.round((correct / total) * 100)}%` : '—') : '…'} />
        <Stat label="Tempo de estudo" value={attempts ? `${minutes} min` : '…'} />
        <Stat label="Competências dominadas" value={attempts ? String(mastered.length) : '…'} />
      </div>

      <section className="card">
        <h2 className="mb-3 font-semibold">Evolução desta semana (tentativas por dia)</h2>
        <div className="flex h-28 items-end gap-2" role="img" aria-label="Tentativas por dia nos últimos 7 dias">
          {perDay.map((n, i) => (
            <div key={i} className="flex flex-1 flex-col items-center gap-1">
              <div className="w-full rounded-t bg-electric-500" style={{ height: `${(n / maxDay) * 100}%`, minHeight: n ? 4 : 1 }} title={`${n}`} />
              <span className="text-[10px] text-slate-500">{days[i].toLocaleDateString('pt', { weekday: 'short' })}</span>
            </div>
          ))}
        </div>
        {attempts && total === 0 && <p className="muted mt-3">Ainda não fizeste exercícios, e está tudo bem. Abre uma aula na Academia e resolve o primeiro.</p>}
      </section>

      <div className="grid gap-4 sm:grid-cols-2">
        <section className="card">
          <h2 className="mb-2 font-semibold">Dificuldades identificadas</h2>
          {difficulties.length === 0
            ? <p className="muted">Nenhuma por agora. Quando houver temas em que tropeces, aparecem aqui para os trabalhares com calma.</p>
            : <ul className="space-y-1 text-sm">{difficulties.map((d) => <li key={d.competency}>{d.competency} — {d.correct_count}/{d.attempts_count} certas</li>)}</ul>}
        </section>
        <section className="card">
          <h2 className="mb-2 font-semibold">Próximo passo</h2>
          <p className="muted mb-3">
            {profile?.academic_level ? `Continua no nível ${profile.academic_level}.` : 'Escolhe um nível para começar.'}
          </p>
          <Link to="/academia" className="btn">Ir para a Academia</Link>
        </section>
      </div>

      <section className="card">
        <h2 className="mb-2 font-semibold">Guardado para offline</h2>
        {saved.length === 0
          ? <p className="muted">Abre uma aula e carrega em "Guardar para offline".</p>
          : <ul className="space-y-1 text-sm">{saved.map((s) => <li key={s.slug}><Link className="text-electric-500" to={`/aula/${s.slug}`}>{s.title}</Link></li>)}</ul>}
        {pending > 0 && <p className="muted mt-2">{pending} resposta(s) à espera de ligação para serem corrigidas.</p>}
      </section>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="card">
      <p className="text-2xl font-bold">{value}</p>
      <p className="muted">{label}</p>
    </div>
  );
}

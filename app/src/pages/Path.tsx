import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { CheckCircle2, Circle, ArrowRightCircle } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';

interface Sub { id: string; slug: string; title: string; position: number }
interface Les { id: string; slug: string; title: string; position: number; subject_id: string }
interface Test { kind: string; score: number; subject_id: string | null; created_at: string }
interface Step { to: string; title: string; why: string }

const PASS = 10;

export function PathPage() {
  const { profile } = useAuth();
  const levelNumber = profile?.academic_level ?? 1;
  const [data, setData] = useState<{ levelSlug: string; subs: Sub[]; lessons: Les[]; done: Set<string>; tests: Test[] } | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    void (async () => {
      const { data: lv } = await supabase.from('levels').select('id, slug').eq('number', levelNumber).maybeSingle();
      if (!lv) { setError('Este nível ainda não está publicado.'); return; }
      const { data: s } = await supabase.from('subjects').select('id, slug, title, position').eq('level_id', (lv as { id: string }).id).order('position');
      const subs = (s ?? []) as Sub[];
      const ids = subs.map((x) => x.id);
      const [l, p, t] = await Promise.all([
        supabase.from('lessons').select('id, slug, title, position, topics!inner(subject_id)').in('topics.subject_id', ids).eq('status', 'published'),
        supabase.from('lesson_progress').select('lesson_id').eq('completed', true),
        supabase.from('subject_tests').select('kind, score, subject_id, created_at').order('created_at', { ascending: false }).limit(300),
      ]);
      if (l.error) { setError('Não foi possível carregar o percurso.'); return; }
      const lessons = ((l.data ?? []) as unknown as (Omit<Les, 'subject_id'> & { topics: { subject_id: string } })[])
        .map((x) => ({ id: x.id, slug: x.slug, title: x.title, position: x.position, subject_id: x.topics.subject_id }))
        .sort((a, b) => a.position - b.position);
      setData({ levelSlug: (lv as { slug: string }).slug, subs, lessons, done: new Set(((p.data ?? []) as { lesson_id: string }[]).map((r) => r.lesson_id)), tests: (t.data ?? []) as Test[] });
    })();
  }, [levelNumber]);

  if (error) return <p role="alert" className="card text-sm text-red-600">{error}</p>;
  if (!data) return <p className="muted">A preparar o teu percurso…</p>;

  const { subs, lessons, done, tests, levelSlug } = data;
  const lastOf = (sid: string, kind: string) => tests.find((t) => t.subject_id === sid && t.kind === kind);
  const bySub = (sid: string) => lessons.filter((x) => x.subject_id === sid);

  // Próximo passo: o primeiro tema por terminar, por ordem.
  let step: Step | null = null;
  for (const s of subs) {
    const ls = bySub(s.id);
    if (!ls.length) continue;
    const nDone = ls.filter((x) => done.has(x.id)).length;
    const fin = lastOf(s.id, 'final');
    if (nDone === 0 && !lastOf(s.id, 'diagnostic'))
      { step = { to: `/teste/${s.slug}?tipo=diagnostic`, title: `Diagnóstico de ${s.title}`, why: 'Um teste curto mostra o que já sabes e onde começar. Não conta contra ti.' }; break; }
    if (nDone < ls.length) {
      const next = ls.find((x) => !done.has(x.id))!;
      step = { to: `/aula/${next.slug}`, title: next.title, why: `Próxima aula de ${s.title} (${nDone}/${ls.length} feitas).` }; break;
    }
    if (!fin) { step = { to: `/teste/${s.slug}?tipo=final`, title: `Avaliação final de ${s.title}`, why: 'Já fizeste todas as aulas deste tema. Prova o que aprendeste.' }; break; }
    if (Number(fin.score) < PASS) {
      step = { to: `/teste/${s.slug}?tipo=consolidation`, title: `Consolidar ${s.title}`, why: `A tua última nota final foi ${Number(fin.score).toFixed(1).replace('.', ',')}/20. Treina mais um pouco e repete a avaliação.` }; break;
    }
  }
  if (!step && subs.length) {
    const exam = tests.find((t) => t.kind === 'exam');
    step = exam && Number(exam.score) >= PASS
      ? null
      : { to: `/teste/${levelSlug}?tipo=exam`, title: 'Exame final do nível', why: 'Todos os temas estão feitos e aprovados. Falta só o exame.' };
  }

  return (
    <div className="space-y-4">
      <Link to="/" className="muted">← Painel</Link>
      <h1 className="text-2xl font-bold">O teu percurso</h1>
      {step ? (
        <Link to={step.to} className="card flex items-center justify-between border-electric-500 hover:bg-electric-500/5">
          <span><span className="muted block">Próximo passo sugerido</span><span className="font-semibold">{step.title}</span><span className="muted block text-sm">{step.why}</span></span>
          <ArrowRightCircle className="shrink-0 text-electric-500" />
        </Link>
      ) : (
        <div className="card border-emerald-500">Concluíste todo o percurso deste nível. Parabéns! Explora a <Link to="/academia" className="text-electric-500">Academia</Link> para o nível seguinte.</div>
      )}
      <div className="space-y-4">
        {subs.map((s) => {
          const ls = bySub(s.id);
          if (!ls.length) return null;
          const fin = lastOf(s.id, 'final');
          const nextId = ls.find((x) => !done.has(x.id))?.id;
          return (
            <section key={s.id} className="card space-y-2">
              <div className="flex items-center justify-between">
                <Link to={`/academia/${levelSlug}/${s.slug}`} className="font-semibold hover:text-electric-500">{s.title}</Link>
                <span className="badge">{ls.filter((x) => done.has(x.id)).length}/{ls.length}</span>
              </div>
              <ol className="space-y-1 text-sm">
                {ls.map((x) => (
                  <li key={x.id}>
                    <Link to={`/aula/${x.slug}`} className={`flex items-center gap-2 rounded-lg px-1 py-0.5 hover:bg-slate-200/50 dark:hover:bg-navy-800 ${x.id === nextId ? 'font-semibold' : ''}`}>
                      {done.has(x.id) ? <CheckCircle2 size={16} className="text-emerald-600" /> : x.id === nextId ? <ArrowRightCircle size={16} className="text-electric-500" /> : <Circle size={16} className="opacity-40" />}
                      {x.title}
                    </Link>
                  </li>
                ))}
              </ol>
              <p className="muted text-xs">Avaliação final: {fin ? `${Number(fin.score).toFixed(1).replace('.', ',')}/20` : 'ainda não feita'}</p>
            </section>
          );
        })}
      </div>
    </div>
  );
}

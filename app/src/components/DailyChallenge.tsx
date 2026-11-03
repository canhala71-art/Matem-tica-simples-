import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Flame } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import { RichText } from './RichText';
import { catName, diffName, type AnswerResult } from '../lib/quiz';

interface Daily { id: string; statement: string; options: string[]; category: string; difficulty: string; available: number }

export function DailyChallenge() {
  const { session } = useAuth();
  const [q, setQ] = useState<Daily | null | undefined>(undefined);
  const [best, setBest] = useState<number | null>(null);
  const [picked, setPicked] = useState<number | null>(null);
  const [res, setRes] = useState<AnswerResult | null>(null);

  useEffect(() => {
    void (async () => {
      const { data } = await supabase.rpc('daily_challenge');
      setQ((data as Daily | null) ?? null);
      const b = await supabase.from('quiz_sessions').select('points').eq('user_id', session?.user.id ?? '')
        .not('finished_at', 'is', null).order('points', { ascending: false }).limit(1).maybeSingle();
      setBest(b.data ? (b.data.points as number) : null);
    })();
  }, [session]);

  async function pick(i: number) {
    if (!q || res) return;
    setPicked(i);
    const { data } = await supabase.rpc('daily_challenge_answer', { _question: q.id, _chosen: i });
    if (data) setRes(data as AnswerResult);
  }

  return (
    <section className="card space-y-3 border-electric-500/40 bg-gradient-to-br from-electric-500/10 to-transparent">
      <div>
        <h2 className="flex items-center gap-2 text-lg font-extrabold tracking-wide"><Flame className="text-orange-500" size={20} />DESAFIO MATEMÁTICO DO DIA</h2>
        <p className="muted">Testa os teus conhecimentos. Cada desafio é uma oportunidade para evoluir.</p>
      </div>
      {q === undefined && <p className="muted">A preparar o desafio de hoje…</p>}
      {q === null && <p className="muted">O desafio de hoje ainda está a ser preparado. Volta já já!</p>}
      {q && (
        <>
          <p className="muted">{catName(q.category)} · {diffName(q.difficulty)} · {q.available} perguntas disponíveis · cerca de 5 min</p>
          <RichText text={q.statement} className="font-medium" />
          <div className="grid gap-2 sm:grid-cols-2">
            {q.options.map((o, i) => {
              const right = res && i === res.correct_index;
              const wrong = res && picked === i && !res.is_correct;
              return (
                <button key={i} disabled={Boolean(res)} onClick={() => void pick(i)}
                  className={`btn-ghost !justify-start ${right ? '!border-emerald-500 !bg-emerald-500/10' : ''} ${wrong ? '!border-red-500 !bg-red-500/10' : ''}`}>
                  <span className="badge">{String.fromCharCode(65 + i)}</span> {o}
                </button>
              );
            })}
          </div>
          {res && (
            <div className="rounded-xl bg-slate-100 p-3 text-sm dark:bg-navy-800">
              <p className="mb-1 font-semibold">{res.is_correct ? 'Certo! Começaste o dia em grande.' : 'Não foi desta, mas olha a explicação:'}</p>
              <RichText text={res.explanation} />
            </div>
          )}
          <div className="flex flex-wrap items-center gap-3">
            <Link to={`/quiz?categoria=${q.category}`} className="btn">Começar Quiz</Link>
            {best !== null && <span className="muted">A tua melhor pontuação: {best} pontos</span>}
          </div>
        </>
      )}
    </section>
  );
}

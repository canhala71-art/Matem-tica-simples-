import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import { bestStreak, computeBadges, type Badge, type Stats } from '../lib/achievements';

export function AchievementsPage() {
  const { session } = useAuth();
  const [badges, setBadges] = useState<Badge[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!session) return;
    const uid = session.user.id;
    void (async () => {
      const [a, lp, st, tr] = await Promise.all([
        supabase.from('attempts').select('is_correct, created_at').eq('user_id', uid).order('created_at', { ascending: false }).limit(1000),
        supabase.from('lesson_progress').select('lesson_id').eq('completed', true),
        supabase.from('subject_tests').select('kind, score, subject_id').limit(500),
        supabase.from('tool_runs').select('id', { count: 'exact', head: true }),
      ]);
      if (a.error || lp.error || st.error) { setError('Não foi possível carregar as conquistas.'); return; }
      const att = (a.data ?? []) as { is_correct: boolean | null; created_at: string }[];
      const tests = (st.data ?? []) as { kind: string; score: number; subject_id: string | null }[];
      const passed = new Set(tests.filter((t) => t.kind === 'final' && Number(t.score) >= 10 && t.subject_id).map((t) => t.subject_id));
      const stats: Stats = {
        attempts: att.length, correct: att.filter((x) => x.is_correct).length, bestStreak: bestStreak(att.map((x) => x.created_at)),
        lessonsDone: lp.data?.length ?? 0, tests: tests.length, bestScore: Math.max(0, ...tests.map((t) => Number(t.score))),
        perfectTests: tests.filter((t) => Number(t.score) >= 20).length, subjectsPassed: passed.size,
        examPassed: tests.some((t) => t.kind === 'exam' && Number(t.score) >= 10), toolRuns: tr.count ?? 0,
      };
      setBadges(computeBadges(stats));
    })();
  }, [session]);

  const won = badges?.filter((x) => x.cur >= x.target).length ?? 0;
  return (
    <div className="space-y-4">
      <Link to="/" className="muted">← Painel</Link>
      <h1 className="text-2xl font-bold">Conquistas</h1>
      {error && <p role="alert" className="text-sm text-red-600">{error}</p>}
      {badges && <p className="muted">{won} de {badges.length} conquistas. Cada uma vem do teu estudo real, sem atalhos.</p>}
      <div className="grid gap-3 sm:grid-cols-2">
        {badges?.map((x) => {
          const ok = x.cur >= x.target;
          return (
            <div key={x.id} className={`card flex gap-3 ${ok ? 'border-emerald-500' : 'opacity-70'}`}>
              <span className={`text-3xl ${ok ? '' : 'grayscale'}`} aria-hidden>{x.icon}</span>
              <div className="flex-1 space-y-1">
                <p className="font-semibold">{x.title}{ok && <span className="badge ml-2">conquistada</span>}</p>
                <p className="muted text-sm">{x.desc}</p>
                {!ok && (
                  <div>
                    <div className="h-1.5 overflow-hidden rounded bg-slate-200 dark:bg-navy-800"><div className="h-full bg-electric-500" style={{ width: `${(x.cur / x.target) * 100}%` }} /></div>
                    <p className="muted text-xs">{x.cur}/{x.target}</p>
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

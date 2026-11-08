import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import { ExercisePlayer, type ExerciseView } from '../components/ExercisePlayer';

/** Exercícios cuja tentativa mais recente foi errada: o melhor treino é voltar a eles. */
export function ReviewPage() {
  const { session } = useAuth();
  const [items, setItems] = useState<ExerciseView[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!session) return;
    void (async () => {
      const { data, error: e } = await supabase.from('attempts').select('exercise_id, is_correct, created_at')
        .eq('user_id', session.user.id).order('created_at', { ascending: false }).limit(1000);
      if (e) { setError('Não foi possível carregar os teus erros.'); return; }
      const seen = new Set<string>(); const wrong: string[] = [];
      for (const r of (data ?? []) as { exercise_id: string; is_correct: boolean | null }[]) {
        if (seen.has(r.exercise_id)) continue;
        seen.add(r.exercise_id);
        if (r.is_correct === false) wrong.push(r.exercise_id);
      }
      if (!wrong.length) { setItems([]); return; }
      const { data: ex, error: e2 } = await supabase.from('exercises')
        .select('id, type, difficulty, statement, options').in('id', wrong.slice(0, 10)).eq('status', 'published');
      if (e2) { setError('Não foi possível carregar os exercícios.'); return; }
      setItems((ex ?? []) as ExerciseView[]);
    })();
  }, [session]);

  return (
    <div className="space-y-4">
      <Link to="/" className="muted">← Painel</Link>
      <h1 className="text-2xl font-bold">Rever erros</h1>
      <p className="muted">Exercícios em que a tua última resposta estava errada (até 10). Acertar aqui tira-os desta lista.</p>
      {error && <p role="alert" className="text-sm text-red-600">{error}</p>}
      {items === null && !error && <p className="muted">A carregar…</p>}
      {items?.length === 0 && <div className="card">Não tens erros por rever. Continua na <Link className="text-electric-500" to="/academia">Academia</Link>.</div>}
      {items?.map((x) => <ExercisePlayer key={x.id} exercise={x} />)}
    </div>
  );
}

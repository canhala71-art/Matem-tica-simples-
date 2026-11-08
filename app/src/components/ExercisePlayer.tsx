import { useRef, useState } from 'react';
import { CheckCircle2, XCircle, CloudOff } from 'lucide-react';
import { RichText } from './RichText';
import { submitAnswer, type SubmitResult } from '../lib/offline';
import { supabase } from '../lib/supabase';

export interface ExerciseView {
  id: string;
  type: 'multiple_choice' | 'numeric' | 'algebraic' | 'true_false' | 'written' | 'word_problem';
  difficulty: number;
  statement: string;
  options: { id: string; label: string }[] | null;
}

export function ExercisePlayer({ exercise }: { exercise: ExerciseView }) {
  const [answer, setAnswer] = useState<string | boolean>('');
  const [busy, setBusy] = useState(false);
  const [result, setResult] = useState<SubmitResult | null>(null);
  const [queued, setQueued] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [hint, setHint] = useState<string | null>(null);
  const [hintState, setHintState] = useState<'idle' | 'loading' | 'none'>('idle');
  const started = useRef(Date.now());
  const clientId = useRef(crypto.randomUUID());

  const empty = answer === '' || (typeof answer === 'string' && answer.trim() === '');

  async function send() {
    if (empty || busy) return;
    setBusy(true);
    setError(null);
    const out = await submitAnswer({
      exercise_id: exercise.id,
      answer: typeof answer === 'string' ? answer.trim() : answer,
      client_id: clientId.current,
      time_spent_seconds: Math.round((Date.now() - started.current) / 1000),
    });
    setBusy(false);
    if (out.kind === 'ok') setResult(out.result);
    else if (out.kind === 'queued') setQueued(true);
    else setError(out.message);
  }

  async function showHint() {
    setHintState('loading');
    const { data, error: e } = await supabase.rpc('get_hint', { _exercise_id: exercise.id });
    if (e || !data) { setHintState('none'); return; }
    setHint(String(data));
    setHintState('idle');
  }

  function retry() {
    setHint(null);
    setHintState('idle');
    setResult(null);
    setAnswer('');
    setQueued(false);
    clientId.current = crypto.randomUUID(); // nova tentativa
    started.current = Date.now();
  }

  const locked = !!result || queued;

  return (
    <div className="card space-y-3">
      <div className="flex items-center justify-between">
        <span className="badge">Dificuldade {exercise.difficulty}/5</span>
      </div>
      <RichText text={exercise.statement} />

      {exercise.type === 'multiple_choice' && (
        <div className="space-y-2">
          {(exercise.options ?? []).map((o) => (
            <label key={o.id} className={`flex cursor-pointer items-start gap-3 rounded-xl border p-3 text-sm ${answer === o.id ? 'border-electric-500 bg-electric-500/10' : 'border-slate-300 dark:border-navy-700'}`}>
              <input type="radio" name={exercise.id} disabled={locked} checked={answer === o.id} onChange={() => setAnswer(o.id)} />
              <RichText text={o.label} />
            </label>
          ))}
        </div>
      )}

      {exercise.type === 'true_false' && (
        <div className="flex gap-2">
          {[true, false].map((v) => (
            <button key={String(v)} disabled={locked} onClick={() => setAnswer(v)}
              className={`btn-ghost flex-1 ${answer === v ? 'border-electric-500 bg-electric-500/10' : ''}`}>
              {v ? 'Verdadeiro' : 'Falso'}
            </button>
          ))}
        </div>
      )}

      {(exercise.type === 'numeric' || exercise.type === 'algebraic') && (
        <input className="input" disabled={locked} value={typeof answer === 'string' ? answer : ''}
          onChange={(e) => setAnswer(e.target.value)}
          placeholder={exercise.type === 'numeric' ? 'Ex.: 0,75 ou 3/4' : 'Ex.: 2x+2  ou  2(x+1)'}
          inputMode="text" autoCapitalize="off" autoCorrect="off" spellCheck={false}
          onKeyDown={(e) => { if (e.key === 'Enter') void send(); }} />
      )}

      {(exercise.type === 'written' || exercise.type === 'word_problem') && (
        <textarea className="input min-h-28" disabled={locked} value={typeof answer === 'string' ? answer : ''}
          onChange={(e) => setAnswer(e.target.value)} placeholder="Escreve a tua resolução…" />
      )}

      {!locked && (
        <button className="btn w-full" disabled={empty || busy} onClick={() => void send()}>
          {busy ? 'A verificar…' : 'Verificar'}
        </button>
      )}
      {!locked && !hint && hintState !== 'none' && (
        <button className="btn-ghost w-full" disabled={hintState === 'loading'} onClick={() => void showHint()}>
          {hintState === 'loading' ? 'A procurar pista…' : 'Preciso de uma pista'}
        </button>
      )}
      {!locked && hintState === 'none' && <p className="muted text-sm">Este exercício não tem pista. Vê a resolução depois de verificares.</p>}
      {!locked && hint && (
        <p className="rounded-xl bg-electric-500/10 p-3 text-sm"><strong>Pista: </strong><RichText text={hint} /></p>
      )}
      {error && <p role="alert" className="text-sm text-red-600">{error}</p>}

      {queued && (
        <p className="flex items-center gap-2 rounded-xl bg-amber-500/10 p-3 text-sm">
          <CloudOff size={16} /> Sem ligação: a resposta ficou guardada e será corrigida quando voltares a ter internet.
        </p>
      )}

      {result && (
        <div className="space-y-3">
          {result.graded ? (
            <p className={`flex items-center gap-2 font-semibold ${result.correct ? 'text-emerald-600' : 'text-red-600'}`}>
              {result.correct ? <CheckCircle2 size={20} /> : <XCircle size={20} />}
              {result.correct ? 'Correto!' : 'Ainda não é isso.'}
              {result.mastered && <span className="badge">Competência dominada</span>}
            </p>
          ) : (
            <p className="muted">Resposta escrita: compara a tua resolução com a solução abaixo.</p>
          )}
          {result.explanation && <RichText text={result.explanation} />}
          {result.solution_steps && result.solution_steps.length > 0 && (
            <ol className="list-decimal space-y-2 pl-5">
              {result.solution_steps.map((s, i) => <li key={i}><RichText text={s} /></li>)}
            </ol>
          )}
          <button className="btn-ghost" onClick={retry}>Tentar outra vez</button>
        </div>
      )}
    </div>
  );
}

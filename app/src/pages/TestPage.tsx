import { useEffect, useMemo, useRef, useState } from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { submitAnswer, type SubmitResult } from '../lib/offline';
import { RichText } from '../components/RichText';
import type { ExerciseView } from '../components/ExercisePlayer';

type Kind = 'diagnostic' | 'consolidation' | 'final' | 'exam';
const TITLE: Record<Kind, string> = {
  diagnostic: 'Teste de diagnóstico',
  consolidation: 'Exercícios de consolidação',
  final: 'Avaliação final',
  exam: 'Exame final do nível',
};
const SIZE: Record<Exclude<Kind, 'exam'>, number> = { diagnostic: 8, consolidation: 10, final: 15 };

function shuffle<T>(a: T[]): T[] {
  const r = [...a];
  for (let i = r.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [r[i], r[j]] = [r[j], r[i]];
  }
  return r;
}

interface Done { q: ExerciseView; answer: string | boolean; res: SubmitResult }
type ExRow = ExerciseView & { topics: { subject_id: string } };

export function TestPage() {
  const { scope = '' } = useParams(); // slug da disciplina, ou do nível (exame)
  const [sp] = useSearchParams();
  const kind = (['diagnostic', 'consolidation', 'final', 'exam'].includes(sp.get('tipo') ?? '') ? sp.get('tipo') : 'diagnostic') as Kind;

  const [title, setTitle] = useState('');
  const [questions, setQuestions] = useState<ExerciseView[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [i, setI] = useState(0);
  const [answer, setAnswer] = useState<string | boolean>('');
  const [busy, setBusy] = useState(false);
  const [done, setDone] = useState<Done[]>([]);
  const [saved, setSaved] = useState<{ score: number; correct: number; total: number } | null>(null);
  const [saveErr, setSaveErr] = useState<string | null>(null);
  const clientIds = useRef<string[]>([]);
  const started = useRef(Date.now());
  const qStarted = useRef(Date.now());

  useEffect(() => {
    void (async () => {
      try {
        if (kind === 'exam') {
          const { data: lv } = await supabase.from('levels').select('id, title').eq('slug', scope).maybeSingle();
          if (!lv) { setError('Nível não encontrado.'); return; }
          setTitle((lv as { title: string }).title);
          const { data: subs } = await supabase.from('subjects').select('id').eq('level_id', (lv as { id: string }).id);
          const ids = (subs ?? []).map((s) => (s as { id: string }).id);
          const { data } = await supabase.from('exercises')
            .select('id, type, difficulty, statement, options, topics!inner(subject_id)').in('topics.subject_id', ids);
          const bySub = new Map<string, ExRow[]>();
          for (const e of (data ?? []) as unknown as ExRow[]) {
            const k = e.topics.subject_id;
            bySub.set(k, [...(bySub.get(k) ?? []), e]);
          }
          const picked = [...bySub.values()].flatMap((arr) => shuffle(arr).slice(0, 2));
          if (picked.length < 4) { setError('Ainda não há exercícios suficientes para este exame.'); return; }
          setQuestions(shuffle(picked));
        } else {
          const { data: s } = await supabase.from('subjects').select('id, title').eq('slug', scope).maybeSingle();
          if (!s) { setError('Disciplina não encontrada.'); return; }
          setTitle((s as { title: string }).title);
          const { data } = await supabase.from('exercises')
            .select('id, type, difficulty, statement, options, topics!inner(subject_id)').eq('topics.subject_id', (s as { id: string }).id);
          let pool = (data ?? []) as unknown as ExerciseView[];
          if (kind === 'diagnostic') {
            const easy = pool.filter((e) => e.difficulty <= 2);
            if (easy.length >= 5) pool = easy;
          }
          if (kind === 'final') {
            const hard = pool.filter((e) => e.difficulty >= 2);
            if (hard.length >= 8) pool = hard;
          }
          if (pool.length < 3) { setError('Ainda não há exercícios suficientes nesta disciplina.'); return; }
          setQuestions(shuffle(pool).slice(0, SIZE[kind]));
        }
        started.current = Date.now();
        qStarted.current = Date.now();
      } catch {
        setError('Não foi possível preparar o teste. Verifica a ligação e tenta outra vez.');
      }
    })();
  }, [scope, kind]);

  const q = questions?.[i];
  const empty = answer === '' || (typeof answer === 'string' && answer.trim() === '');
  const finished = !!questions && done.length === questions.length;

  async function next() {
    if (!q || empty || busy) return;
    setBusy(true);
    setError(null);
    const cid = crypto.randomUUID();
    const out = await submitAnswer({
      exercise_id: q.id,
      answer: typeof answer === 'string' ? answer.trim() : answer,
      client_id: cid,
      time_spent_seconds: Math.round((Date.now() - qStarted.current) / 1000),
    });
    setBusy(false);
    if (out.kind !== 'ok') {
      setError(out.kind === 'queued' ? 'Sem ligação: o teste precisa de internet para ser corrigido. Tenta outra vez.' : out.message);
      return;
    }
    clientIds.current.push(cid);
    setDone((d) => [...d, { q, answer, res: out.result }]);
    setAnswer('');
    setI((n) => n + 1);
    qStarted.current = Date.now();
  }

  useEffect(() => {
    if (!finished || saved || saveErr) return;
    void (async () => {
      const { data, error: e } = await supabase.rpc('record_test', {
        _scope: scope, _kind: kind, _client_ids: clientIds.current,
        _seconds: Math.round((Date.now() - started.current) / 1000),
      });
      if (e) setSaveErr('A nota foi calculada mas não ficou guardada no histórico.');
      else setSaved(data as { score: number; correct: number; total: number });
    })();
  }, [finished, saved, saveErr, scope, kind]);

  const localCorrect = useMemo(() => done.filter((d) => d.res.correct).length, [done]);
  const localScore = questions && done.length ? Math.round((localCorrect / questions.length) * 200) / 10 : 0;
  const back = kind === 'exam' ? `/academia/${scope}` : undefined;

  if (error && !questions) return <div className="space-y-3"><Link to="/academia" className="muted">← Academia</Link><p className="card muted" role="alert">{error}</p></div>;
  if (!questions) return <p className="muted">A preparar o teste…</p>;

  if (finished) {
    const score = saved?.score ?? localScore;
    return (
      <div className="space-y-4">
        <Link to={back ?? '/academia'} className="muted">← Voltar</Link>
        <h1 className="text-2xl font-bold">{TITLE[kind]}: {title}</h1>
        <div className="card text-center">
          <p className="text-4xl font-bold">{score.toFixed(1).replace('.', ',')} <span className="text-lg muted">/ 20</span></p>
          <p className="muted">{saved?.correct ?? localCorrect} de {saved?.total ?? questions.length} certas</p>
          <p className="mt-2 text-sm">{score >= 14 ? 'Muito bom! Dominas esta matéria.' : score >= 10 ? 'Positivo. Revê os erros abaixo para subir a nota.' : 'Ainda não chegou. Revê as aulas e tenta de novo, sem pressa.'}</p>
          {saveErr && <p role="alert" className="mt-2 text-sm text-amber-600">{saveErr}</p>}
        </div>
        <h2 className="text-lg font-semibold">Correção</h2>
        {done.map((d, k) => (
          <div key={d.q.id} className={`card space-y-2 ${d.res.correct ? '' : 'border-red-400'}`}>
            <p className="text-sm font-semibold">{k + 1}. {d.res.correct ? 'Certa' : 'Errada'}</p>
            <RichText text={d.q.statement} />
            {d.res.explanation && <RichText text={d.res.explanation} />}
            {!d.res.correct && d.res.solution_steps && (
              <ol className="list-decimal space-y-1 pl-5">{d.res.solution_steps.map((s, n) => <li key={n}><RichText text={s} /></li>)}</ol>
            )}
          </div>
        ))}
        <button className="btn" onClick={() => window.location.reload()}>Repetir o teste</button>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <Link to={back ?? '/academia'} className="muted">← Sair do teste</Link>
      <h1 className="text-xl font-bold">{TITLE[kind]}: {title}</h1>
      <div className="h-2 overflow-hidden rounded-full bg-slate-200 dark:bg-navy-800">
        <div className="h-full bg-electric-500 transition-all" style={{ width: `${(i / questions.length) * 100}%` }} />
      </div>
      <p className="muted">Pergunta {i + 1} de {questions.length}. A correção aparece no fim.</p>
      {q && (
        <div className="card space-y-3">
          <RichText text={q.statement} />
          {q.type === 'multiple_choice' && (q.options ?? []).map((o) => (
            <label key={o.id} className={`flex cursor-pointer items-start gap-3 rounded-xl border p-3 text-sm ${answer === o.id ? 'border-electric-500 bg-electric-500/10' : 'border-slate-300 dark:border-navy-700'}`}>
              <input type="radio" name={q.id} checked={answer === o.id} onChange={() => setAnswer(o.id)} />
              <RichText text={o.label} />
            </label>
          ))}
          {q.type === 'true_false' && (
            <div className="flex gap-2">
              {[true, false].map((v) => (
                <button key={String(v)} onClick={() => setAnswer(v)} className={`btn-ghost flex-1 ${answer === v ? 'border-electric-500 bg-electric-500/10' : ''}`}>{v ? 'Verdadeiro' : 'Falso'}</button>
              ))}
            </div>
          )}
          {(q.type === 'numeric' || q.type === 'algebraic') && (
            <input className="input" value={typeof answer === 'string' ? answer : ''} onChange={(e) => setAnswer(e.target.value)}
              placeholder="A tua resposta" autoCapitalize="off" autoCorrect="off" spellCheck={false}
              onKeyDown={(e) => { if (e.key === 'Enter') void next(); }} />
          )}
          {error && <p role="alert" className="text-sm text-red-600">{error}</p>}
          <button className="btn w-full" disabled={empty || busy} onClick={() => void next()}>
            {busy ? 'A enviar…' : i + 1 === questions.length ? 'Terminar' : 'Seguinte'}
          </button>
        </div>
      )}
    </div>
  );
}

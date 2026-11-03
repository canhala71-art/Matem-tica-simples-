import { useCallback, useEffect, useRef, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { CheckCircle2, Clock, Flame, Trophy, Volume2, VolumeX, XCircle } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import { humanError, loadSettings, useAccess } from '../lib/billing';
import { RichText } from '../components/RichText';
import { Confetti, ProgressRing, buzz, playTone, useCountUp } from '../components/Fx';
import {
  CATEGORIES, DIFFICULTIES, catName, diffName, encourage, grade, mmss,
  type AnswerResult, type QuizQuestion, type QuizSummary,
} from '../lib/quiz';

type View = 'setup' | 'play' | 'result' | 'history' | 'ranking';

interface SessionRow { id: string; category: string | null; difficulty: string | null; correct: number; total: number; points: number; seconds: number; started_at: string }
interface RankRow { display_name: string; points: number; quizzes: number }

export function QuizPage() {
  const [params] = useSearchParams();
  const { session } = useAuth();
  const { access } = useAccess();
  const [view, setView] = useState<View>('setup');
  const [category, setCategory] = useState(params.get('categoria') ?? '');
  const [difficulty, setDifficulty] = useState('facil');
  const [count, setCount] = useState(5);
  const [freeDiffs, setFreeDiffs] = useState<string[]>(['facil', 'intermedio']);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  const [sid, setSid] = useState('');
  const [questions, setQuestions] = useState<QuizQuestion[]>([]);
  const [idx, setIdx] = useState(0);
  const [chosen, setChosen] = useState<number | null>(null);
  const [feedback, setFeedback] = useState<AnswerResult | null>(null);
  const [elapsed, setElapsed] = useState(0);
  const [summary, setSummary] = useState<QuizSummary | null>(null);
  const [review, setReview] = useState(false);
  const [streak, setStreak] = useState(0);
  const [bestStreak, setBestStreak] = useState(0);
  const [score, setScore] = useState(0);
  const [sound, setSound] = useState(false);
  const t0 = useRef(0);

  useEffect(() => {
    void loadSettings().then((s) => {
      const d = (s.free_quiz as { difficulties?: string[] } | undefined)?.difficulties;
      if (d) setFreeDiffs(d);
    });
  }, []);

  useEffect(() => {
    if (view !== 'play') return;
    const t = setInterval(() => setElapsed(Math.round((Date.now() - t0.current) / 1000)), 1000);
    return () => clearInterval(t);
  }, [view]);

  useEffect(() => {
    if (view !== 'play') return;
    const onKey = (e: KeyboardEvent) => {
      const k = e.key.toLowerCase();
      const i = '1234'.includes(k) && k ? Number(k) - 1 : 'abcd'.indexOf(k);
      if (k.length === 1 && i >= 0 && i < 4 && !feedback) { e.preventDefault(); void answer(i); }
      else if (e.key === 'Enter' && feedback) { e.preventDefault(); void next(); }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  });

  const isFree = access?.tier === 'free';
  const locked = (d: string) => isFree && !freeDiffs.includes(d);

  async function start() {
    setBusy(true); setError(null);
    const { data, error: err } = await supabase.rpc('start_quiz', {
      _category: category || null, _difficulty: difficulty, _n: count,
    });
    setBusy(false);
    if (err) { setError(humanError(err)); return; }
    const r = data as { session_id: string; questions: QuizQuestion[] };
    setSid(r.session_id); setQuestions(r.questions); setIdx(0); setChosen(null); setFeedback(null);
    setSummary(null); setReview(false); setElapsed(0); setStreak(0); setBestStreak(0); setScore(0); t0.current = Date.now(); setView('play');
  }

  async function answer(i: number) {
    if (feedback || busy) return;
    setChosen(i); setBusy(true);
    const { data, error: err } = await supabase.rpc('quiz_answer', { _session: sid, _question: questions[idx].id, _chosen: i });
    setBusy(false);
    if (err) { setError(humanError(err)); setChosen(null); return; }
    const fb = data as AnswerResult;
    setFeedback(fb);
    if (fb.is_correct) {
      setStreak((x) => { const n = x + 1; setBestStreak((b) => Math.max(b, n)); return n; });
      setScore((x) => x + 10);
      buzz(25);
      if (sound) playTone('ok');
    } else {
      setStreak(0);
      buzz(120);
      if (sound) playTone('bad');
    }
  }

  async function next() {
    if (idx + 1 < questions.length) { setIdx(idx + 1); setChosen(null); setFeedback(null); return; }
    setBusy(true);
    const { data, error: err } = await supabase.rpc('finish_quiz', { _session: sid });
    setBusy(false);
    if (err) { setError(humanError(err)); return; }
    setSummary(data as QuizSummary); setView('result');
  }

  const tab = (v: View, label: string) => (
    <button className={view === v ? 'btn' : 'btn-ghost'} onClick={() => { setView(v); setError(null); }} disabled={view === 'play'}>{label}</button>
  );

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Quiz</h1>
      <div className="flex gap-2 overflow-x-auto">
        {tab('setup', 'Novo quiz')}{tab('history', 'Histórico')}{tab('ranking', 'Ranking')}
      </div>
      {error && <p role="alert" className="card text-sm text-red-600">{error} {error.includes('Premium') && <Link className="text-electric-500" to="/planos">Ver planos</Link>}</p>}

      {view === 'setup' && (
        <section className="card space-y-4">
          <label className="block space-y-1 text-sm">
            <span className="font-medium">Categoria</span>
            <select className="input" value={category} onChange={(e) => setCategory(e.target.value)}>
              <option value="">Todas as categorias</option>
              {CATEGORIES.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
            </select>
          </label>
          <div className="space-y-1 text-sm">
            <span className="font-medium">Dificuldade</span>
            <div className="flex flex-wrap gap-2">
              {DIFFICULTIES.map(([v, l]) => (
                <button key={v} disabled={locked(v)} onClick={() => setDifficulty(v)} className={difficulty === v ? 'btn' : 'btn-ghost'}>
                  {l}{locked(v) ? ' (Premium)' : ''}
                </button>
              ))}
            </div>
          </div>
          <div className="space-y-1 text-sm">
            <span className="font-medium">Número de perguntas</span>
            <div className="flex gap-2">
              {[5, 10, 20].map((n) => <button key={n} onClick={() => setCount(n)} className={count === n ? 'btn' : 'btn-ghost'}>{n}</button>)}
            </div>
          </div>
          {isFree && <p className="muted">No plano Free tens um número limitado de quizzes por dia. <Link className="text-electric-500" to="/planos">Passa a Premium</Link> para quizzes ilimitados.</p>}
          <button className="btn" disabled={busy || !session} onClick={() => void start()}>{busy ? 'A preparar…' : 'Começar quiz'}</button>
        </section>
      )}

      {view === 'play' && questions[idx] && (
        <section key={idx} className="card anim-slide-in space-y-4" aria-live="polite">
          <div className="flex items-center justify-between text-sm">
            <span>Pergunta {idx + 1} de {questions.length}</span>
            <span className="flex items-center gap-3">
              {streak >= 2 && <span key={streak} className="anim-pop flex items-center gap-1 font-semibold text-orange-500"><Flame size={16} className="anim-flame" />{streak} seguidas</span>}
              <span className="font-semibold">{score} pts</span>
              <span className="flex items-center gap-1 muted"><Clock size={14} />{mmss(elapsed)}</span>
              <button className="btn-ghost !px-2 !py-1" aria-label={sound ? 'Desligar som' : 'Ligar som'} onClick={() => setSound(!sound)}>
                {sound ? <Volume2 size={14} /> : <VolumeX size={14} />}
              </button>
            </span>
          </div>
          <div className="h-2 overflow-hidden rounded bg-slate-200 dark:bg-navy-800" role="progressbar" aria-valuenow={idx + 1} aria-valuemax={questions.length}>
            <div className="h-full bg-electric-500 transition-all" style={{ width: `${((idx + (feedback ? 1 : 0)) / questions.length) * 100}%` }} />
          </div>
          <p className="muted">{catName(questions[idx].category)} · {diffName(questions[idx].difficulty)} · <span className="hidden sm:inline">atalhos: A–D ou 1–4, Enter para avançar</span></p>
          <RichText text={questions[idx].statement} className="text-lg font-medium" />
          <div className="grid gap-2">
            {questions[idx].options.map((o, i) => {
              const right = feedback && i === feedback.correct_index;
              const wrong = feedback && chosen === i && !feedback.is_correct;
              return (
                <button key={i} disabled={Boolean(feedback) || busy} onClick={() => void answer(i)}
                  className={`btn-ghost !justify-start text-left ${chosen === i && !feedback ? 'anim-pop !border-electric-500' : ''} ${right ? 'anim-glow !border-emerald-500 !bg-emerald-500/10' : ''} ${wrong ? 'anim-shake !border-red-500 !bg-red-500/10' : ''}`}>
                  <span className="badge">{String.fromCharCode(65 + i)}</span> <span className="flex-1">{o}</span>
                  {right && <CheckCircle2 size={18} className="anim-pop text-emerald-500" />}
                  {wrong && <XCircle size={18} className="anim-pop text-red-500" />}
                </button>
              );
            })}
          </div>
          {feedback && (
            <div className={`anim-fade-up rounded-xl p-3 text-sm ${feedback.is_correct ? 'bg-emerald-500/10' : 'bg-amber-500/10'}`}>
              <p className="mb-1 flex items-center gap-2 font-semibold">
                {feedback.is_correct ? <><CheckCircle2 className="text-emerald-500" size={18} />Certo! Boa.</> : <><XCircle className="text-red-500" size={18} />Quase. Vamos ver porquê:</>}
              </p>
              <RichText text={feedback.explanation} />
            </div>
          )}
          {feedback && <button className="btn" disabled={busy} onClick={() => void next()}>{idx + 1 < questions.length ? 'Próxima pergunta' : 'Ver resultado'}</button>}
        </section>
      )}

      {view === 'result' && summary && (
        <section className="space-y-4">
          <div className="card anim-pop space-y-3 text-center">
            {summary.percent >= 75 && <Confetti pieces={summary.percent === 100 ? 90 : 50} />}
            <Trophy className="mx-auto text-electric-500" size={30} />
            <ProgressRing percent={summary.percent} />
            <p className="font-semibold">{grade(summary.percent)}</p>
            <p className="muted">{encourage(summary.percent)}</p>
            <div className="grid grid-cols-2 gap-2 text-sm sm:grid-cols-4">
              <PointsMini points={summary.points} />
              <Mini label="Certas" value={String(summary.correct)} />
              <Mini label="Erradas" value={String(summary.wrong)} />
              <Mini label="Tempo" value={mmss(summary.seconds)} />
            </div>
            {bestStreak >= 3 && <p className="text-sm font-semibold text-orange-500"><Flame className="anim-flame mr-1 inline" size={16} />Melhor sequência: {bestStreak} certas seguidas!</p>}
            <div className="flex flex-wrap justify-center gap-2">
              <button className="btn" onClick={() => void start()}>Jogar novamente</button>
              <button className="btn-ghost" onClick={() => setReview(!review)}>{review ? 'Esconder respostas' : 'Rever respostas'}</button>
              <button className="btn-ghost" onClick={() => setView('setup')}>Escolher outro desafio</button>
              <Link className="btn-ghost" to="/">Voltar ao início</Link>
            </div>
          </div>
          {review && summary.details.map((d, i) => (
            <div key={i} className="card space-y-2 text-sm">
              <RichText text={d.statement} className="font-medium" />
              <p>A tua resposta: <strong className={d.is_correct ? 'text-emerald-600' : 'text-red-600'}>{d.options[d.chosen]}</strong></p>
              {!d.is_correct && <p>Resposta certa: <strong className="text-emerald-600">{d.options[d.correct_index]}</strong></p>}
              <RichText text={d.explanation} className="muted" />
            </div>
          ))}
        </section>
      )}

      {view === 'history' && <History />}
      {view === 'ranking' && <Ranking />}
    </div>
  );
}

function PointsMini({ points }: { points: number }) {
  const v = useCountUp(points);
  return <Mini label="Pontos" value={String(v)} />;
}

function Mini({ label, value }: { label: string; value: string }) {
  return <div className="rounded-xl bg-slate-100 p-2 dark:bg-navy-800"><p className="text-lg font-bold">{value}</p><p className="muted">{label}</p></div>;
}

function History() {
  const { session } = useAuth();
  const [rows, setRows] = useState<SessionRow[] | null>(null);
  useEffect(() => {
    void supabase.from('quiz_sessions')
      .select('id, category, difficulty, correct, total, points, seconds, started_at')
      .eq('user_id', session?.user.id ?? '').not('finished_at', 'is', null)
      .order('started_at', { ascending: false }).limit(50)
      .then(({ data }) => setRows((data ?? []) as SessionRow[]));
  }, [session]);
  if (!rows) return <p className="muted">A carregar…</p>;
  if (rows.length === 0) return <p className="card muted">Ainda não fizeste nenhum quiz. O primeiro é o mais difícil de começar, o resto vem sozinho.</p>;
  const best = Math.max(...rows.map((r) => r.points));
  const cats = new Map<string, { pts: number; n: number }>();
  rows.forEach((r) => { const k = catName(r.category); const c = cats.get(k) ?? { pts: 0, n: 0 }; cats.set(k, { pts: c.pts + r.points, n: c.n + 1 }); });
  return (
    <div className="space-y-4">
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
        <Mini label="Quizzes concluídos" value={String(rows.length)} />
        <Mini label="Melhor pontuação" value={String(best)} />
        <Mini label="Média de acertos" value={`${Math.round(rows.reduce((s, r) => s + (100 * r.correct) / Math.max(1, r.total), 0) / rows.length)}%`} />
      </div>
      <section className="card space-y-2">
        <h2 className="font-semibold">Por categoria</h2>
        <ul className="space-y-1 text-sm">{[...cats.entries()].map(([k, v]) => <li key={k}>{k}: {v.n} quiz(zes), {v.pts} pontos</li>)}</ul>
      </section>
      <section className="card space-y-1">
        <h2 className="font-semibold">Últimos quizzes</h2>
        <ul className="divide-y divide-slate-200 text-sm dark:divide-navy-800">
          {rows.map((r) => (
            <li key={r.id} className="py-2">{new Date(r.started_at).toLocaleDateString('pt-PT')} · {catName(r.category)} · {diffName(r.difficulty)} · {r.correct}/{r.total} · {r.points} pts · {mmss(r.seconds)}</li>
          ))}
        </ul>
      </section>
    </div>
  );
}

function Ranking() {
  const { session } = useAuth();
  const [cat, setCat] = useState('');
  const [rows, setRows] = useState<RankRow[] | null>(null);
  const [joined, setJoined] = useState<boolean | null>(null);

  const load = useCallback(async () => {
    const { data } = await supabase.rpc('quiz_leaderboard', { _category: cat || null });
    setRows((data ?? []) as RankRow[]);
  }, [cat]);
  useEffect(() => { void load(); }, [load]);
  useEffect(() => {
    void supabase.from('profiles').select('preferences').eq('id', session?.user.id ?? '').maybeSingle()
      .then(({ data }) => setJoined((data?.preferences as { ranking?: string } | null)?.ranking === 'true'));
  }, [session]);

  async function toggle() {
    if (!session) return;
    const { data } = await supabase.from('profiles').select('preferences').eq('id', session.user.id).maybeSingle();
    const prefs = { ...((data?.preferences as Record<string, unknown> | null) ?? {}), ranking: joined ? 'false' : 'true' };
    await supabase.from('profiles').update({ preferences: prefs }).eq('id', session.user.id);
    setJoined(!joined);
    await load();
  }

  return (
    <div className="space-y-4">
      <section className="card space-y-2">
        <p className="text-sm">O ranking mostra apenas o teu nome público e só se quiseres participar.</p>
        <button className="btn-ghost" disabled={joined === null} onClick={() => void toggle()}>
          {joined ? 'Sair do ranking' : 'Participar no ranking'}
        </button>
      </section>
      <select className="input" value={cat} onChange={(e) => setCat(e.target.value)} aria-label="Categoria do ranking">
        <option value="">Todas as categorias</option>
        {CATEGORIES.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
      </select>
      <section className="card">
        {rows === null && <p className="muted">A carregar…</p>}
        {rows?.length === 0 && <p className="muted">Ainda ninguém no ranking. Sê a primeira pessoa!</p>}
        <ol className="space-y-1 text-sm">
          {rows?.map((r, i) => <li key={`${r.display_name}-${i}`} className="flex justify-between"><span>{i + 1}. {r.display_name}</span><span className="muted">{r.points} pts · {r.quizzes} quizzes</span></li>)}
        </ol>
      </section>
    </div>
  );
}

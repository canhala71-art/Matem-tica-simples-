import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { CheckCircle2, ChevronRight, ClipboardCheck, Clock } from 'lucide-react';
import { supabase } from '../lib/supabase';

interface Level { id: string; slug: string; number: number; title: string; description: string | null; status: string }
interface Subject { id: string; slug: string; title: string; status: string }
interface TestRow { id: string; kind: string; score: number; correct: number; total: number; created_at: string }
const TOOL_FOR: Record<string, string> = { 'numeros-naturais': 'reta', 'numeros-inteiros': 'reta', 'operacoes-basicas': 'operacoes', tabuada: 'tabuada', fracoes: 'fracoes', 'numeros-decimais': 'decimais', percentagens: 'percentagens', potencias: 'potencias', raizes: 'raizes' };
const KIND_PT: Record<string, string> = { diagnostic: 'Diagnóstico', consolidation: 'Consolidação', final: 'Avaliação final' };
interface LessonRow { id: string; slug: string; title: string; summary: string | null; estimated_minutes: number | null; status: string }

function Draft({ status }: { status: string }) {
  return status === 'published' ? null : <span className="badge ml-2">{status === 'draft' ? 'rascunho' : 'em revisão'}</span>;
}
function Empty({ children }: { children: string }) {
  return <p className="card muted">{children}</p>;
}

export function Academy() {
  const [levels, setLevels] = useState<Level[] | null>(null);
  useEffect(() => {
    void supabase.from('levels').select('id, slug, number, title, description, status').order('number')
      .then(({ data }) => setLevels((data ?? []) as Level[]));
  }, []);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Academia</h1>
      <p className="muted">Seis percursos, dos fundamentos à especialização. Só aparece o que foi revisto e publicado.</p>
      {levels === null && <p className="muted">A carregar…</p>}
      {levels?.length === 0 && <Empty>Ainda não há níveis publicados. O administrador tem de rever e publicar os conteúdos.</Empty>}
      <div className="grid gap-3 sm:grid-cols-2">
        {levels?.map((l) => (
          <Link key={l.id} to={`/academia/${l.slug}`} className="card flex items-center justify-between hover:border-electric-500">
            <span><span className="badge mr-2">{l.number}</span>{l.title}<Draft status={l.status} /></span>
            <ChevronRight size={18} />
          </Link>
        ))}
      </div>
    </div>
  );
}

export function LevelPage() {
  const { levelSlug } = useParams();
  const [level, setLevel] = useState<Level | null>(null);
  const [subjects, setSubjects] = useState<Subject[] | null>(null);
  const [missing, setMissing] = useState(false);
  const [lastExam, setLastExam] = useState<number | null>(null);

  useEffect(() => {
    void (async () => {
      const { data: l } = await supabase.from('levels').select('id, slug, number, title, description, status').eq('slug', levelSlug ?? '').maybeSingle();
      if (!l) { setMissing(true); return; }
      setLevel(l as Level);
      const { data: s } = await supabase.from('subjects').select('id, slug, title, status').eq('level_id', (l as Level).id).order('position');
      setSubjects((s ?? []) as Subject[]);
      const { data: ex } = await supabase.from('subject_tests').select('score')
        .eq('level_id', (l as Level).id).eq('kind', 'exam').order('created_at', { ascending: false }).limit(1);
      setLastExam(ex && ex.length ? Number((ex[0] as { score: number }).score) : null);
    })();
  }, [levelSlug]);

  if (missing) return <Empty>Nível não encontrado ou ainda não publicado.</Empty>;
  return (
    <div className="space-y-4">
      <Link to="/academia" className="muted">← Academia</Link>
      <h1 className="text-2xl font-bold">{level?.title ?? '…'}</h1>
      {subjects?.length === 0 && <Empty>Ainda não há disciplinas publicadas neste nível.</Empty>}
      {level?.number === 1 && (subjects?.length ?? 0) > 0 && (
        <Link to={`/teste/${levelSlug}?tipo=exam`} className="card flex items-center justify-between border-electric-500 hover:bg-electric-500/5">
          <span className="flex items-center gap-2"><ClipboardCheck size={18} />Exame final do Nível 1 (todos os temas, nota 0–20){lastExam !== null && <span className="badge">última nota: {lastExam.toFixed(1).replace('.', ',')}</span>}</span>
          <ChevronRight size={18} />
        </Link>
      )}
      <div className="grid gap-3 sm:grid-cols-2">
        {subjects?.map((s) => (
          <Link key={s.id} to={`/academia/${levelSlug}/${s.slug}`} className="card flex items-center justify-between hover:border-electric-500">
            <span>{s.title}<Draft status={s.status} /></span><ChevronRight size={18} />
          </Link>
        ))}
      </div>
    </div>
  );
}

export function SubjectPage() {
  const { levelSlug, subjectSlug } = useParams();
  const [title, setTitle] = useState('…');
  const [lessons, setLessons] = useState<LessonRow[] | null>(null);
  const [missing, setMissing] = useState(false);
  const [done, setDone] = useState<Set<string>>(new Set());
  const [tests, setTests] = useState<TestRow[]>([]);

  useEffect(() => {
    void (async () => {
      const { data: s } = await supabase.from('subjects').select('id, title').eq('slug', subjectSlug ?? '').maybeSingle();
      if (!s) { setMissing(true); return; }
      setTitle((s as { title: string }).title);
      const { data } = await supabase.from('lessons')
        .select('id, slug, title, summary, estimated_minutes, status, topics!inner(subject_id)')
        .eq('topics.subject_id', (s as { id: string }).id).order('position');
      setLessons((data ?? []) as unknown as LessonRow[]);
      const [p, t] = await Promise.all([
        supabase.from('lesson_progress').select('lesson_id').eq('completed', true),
        supabase.from('subject_tests').select('id, kind, score, correct, total, created_at')
          .eq('subject_id', (s as { id: string }).id).order('created_at', { ascending: false }).limit(10),
      ]);
      setDone(new Set(((p.data ?? []) as { lesson_id: string }[]).map((r) => r.lesson_id)));
      setTests((t.data ?? []) as TestRow[]);
    })();
  }, [subjectSlug]);

  if (missing) return <Empty>Disciplina não encontrada ou ainda não publicada.</Empty>;
  return (
    <div className="space-y-4">
      <Link to={`/academia/${levelSlug}`} className="muted">← Voltar</Link>
      <h1 className="text-2xl font-bold">{title}</h1>
      {(lessons?.length ?? 0) > 0 && (() => {
        const total = lessons!.length, n = lessons!.filter((l) => done.has(l.id)).length;
        return (
          <p className="flex flex-wrap items-center gap-2 text-sm">
            <span className="badge">{n}/{total} lições concluídas</span>
            {n === total && <span className="badge border-emerald-500 text-emerald-600">Tema concluído ✓</span>}
          </p>
        );
      })()}
      {lessons?.length === 0 && <Empty>Ainda não há aulas publicadas nesta disciplina.</Empty>}
      {(lessons?.length ?? 0) > 0 && (
        <div className="card space-y-3">
          <p className="flex items-center gap-2 font-semibold"><ClipboardCheck size={18} />Testes desta disciplina (nota 0–20)</p>
          <div className="flex flex-wrap gap-2">
            <Link className="btn-ghost" to={`/teste/${subjectSlug}?tipo=diagnostic`}>Diagnóstico</Link>
            <Link className="btn-ghost" to={`/teste/${subjectSlug}?tipo=consolidation`}>Consolidação</Link>
            <Link className="btn" to={`/teste/${subjectSlug}?tipo=final`}>Avaliação final</Link>
            <Link className="btn-ghost" to={`/associacao/${subjectSlug}`}>Jogo de associação</Link>
            {TOOL_FOR[subjectSlug ?? ''] && <Link className="btn-ghost" to={`/ferramentas?f=${TOOL_FOR[subjectSlug ?? '']}`}>Ferramenta de apoio</Link>}
          </div>
          {tests.length > 0 && (
            <ul className="space-y-1 text-sm">
              {tests.map((t) => (
                <li key={t.id} className="flex justify-between"><span>{KIND_PT[t.kind] ?? t.kind} · {new Date(t.created_at).toLocaleDateString('pt-PT')}</span><span className="font-semibold">{Number(t.score).toFixed(1).replace('.', ',')}/20 ({t.correct}/{t.total})</span></li>
              ))}
            </ul>
          )}
        </div>
      )}
      <div className="space-y-3">
        {lessons?.map((l) => (
          <Link key={l.id} to={`/aula/${l.slug}`} className="card block hover:border-electric-500">
            <p className="flex items-center gap-2 font-semibold">{done.has(l.id) && <CheckCircle2 size={16} className="text-emerald-600" />}{l.title}<Draft status={l.status} /></p>
            {l.summary && <p className="muted">{l.summary}</p>}
            {l.estimated_minutes && <p className="muted mt-1 flex items-center gap-1"><Clock size={14} />{l.estimated_minutes} min</p>}
          </Link>
        ))}
      </div>
    </div>
  );
}

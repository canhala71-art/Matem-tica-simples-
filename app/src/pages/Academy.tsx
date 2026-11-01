import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { ChevronRight, Clock } from 'lucide-react';
import { supabase } from '../lib/supabase';

interface Level { id: string; slug: string; number: number; title: string; description: string | null; status: string }
interface Subject { id: string; slug: string; title: string; status: string }
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

  useEffect(() => {
    void (async () => {
      const { data: l } = await supabase.from('levels').select('id, slug, number, title, description, status').eq('slug', levelSlug ?? '').maybeSingle();
      if (!l) { setMissing(true); return; }
      setLevel(l as Level);
      const { data: s } = await supabase.from('subjects').select('id, slug, title, status').eq('level_id', (l as Level).id).order('position');
      setSubjects((s ?? []) as Subject[]);
    })();
  }, [levelSlug]);

  if (missing) return <Empty>Nível não encontrado ou ainda não publicado.</Empty>;
  return (
    <div className="space-y-4">
      <Link to="/academia" className="muted">← Academia</Link>
      <h1 className="text-2xl font-bold">{level?.title ?? '…'}</h1>
      {subjects?.length === 0 && <Empty>Ainda não há disciplinas publicadas neste nível.</Empty>}
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

  useEffect(() => {
    void (async () => {
      const { data: s } = await supabase.from('subjects').select('id, title').eq('slug', subjectSlug ?? '').maybeSingle();
      if (!s) { setMissing(true); return; }
      setTitle((s as { title: string }).title);
      const { data } = await supabase.from('lessons')
        .select('id, slug, title, summary, estimated_minutes, status, topics!inner(subject_id)')
        .eq('topics.subject_id', (s as { id: string }).id).order('position');
      setLessons((data ?? []) as unknown as LessonRow[]);
    })();
  }, [subjectSlug]);

  if (missing) return <Empty>Disciplina não encontrada ou ainda não publicada.</Empty>;
  return (
    <div className="space-y-4">
      <Link to={`/academia/${levelSlug}`} className="muted">← Voltar</Link>
      <h1 className="text-2xl font-bold">{title}</h1>
      {lessons?.length === 0 && <Empty>Ainda não há aulas publicadas nesta disciplina.</Empty>}
      <div className="space-y-3">
        {lessons?.map((l) => (
          <Link key={l.id} to={`/aula/${l.slug}`} className="card block hover:border-electric-500">
            <p className="font-semibold">{l.title}<Draft status={l.status} /></p>
            {l.summary && <p className="muted">{l.summary}</p>}
            {l.estimated_minutes && <p className="muted mt-1 flex items-center gap-1"><Clock size={14} />{l.estimated_minutes} min</p>}
          </Link>
        ))}
      </div>
    </div>
  );
}

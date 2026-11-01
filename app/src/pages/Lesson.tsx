import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { Download, Trash2 } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { RichText } from '../components/RichText';
import { ExercisePlayer, type ExerciseView } from '../components/ExercisePlayer';
import { loadLessonOffline, removeLessonOffline, saveLessonOffline } from '../lib/offline';

interface Block { id: string; kind: string; position: number; body: string }
interface Bundle {
  lesson: { id: string; slug: string; title: string; summary: string | null };
  blocks: Block[];
  exercises: ExerciseView[];
}

const KIND_LABEL: Record<string, string> = {
  introduction: 'Introdução',
  intuition: 'Explicação intuitiva',
  definition: 'Definição matemática',
  formulas: 'Fórmulas',
  worked_example: 'Exemplo resolvido',
  guided_exercise: 'Exercício orientado',
  independent_exercise: 'Exercício independente',
  challenge: 'Desafio',
  assessment: 'Avaliação',
};

export function LessonPage() {
  const { slug = '' } = useParams();
  const [data, setData] = useState<Bundle | null>(null);
  const [fromCache, setFromCache] = useState(false);
  const [saved, setSaved] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setData(null);
    setError(null);
    void (async () => {
      try {
        const { data: lesson, error: e1 } = await supabase.from('lessons').select('id, slug, title, summary').eq('slug', slug).maybeSingle();
        if (e1) throw e1;
        if (!lesson) { setError('Aula não encontrada ou ainda não publicada.'); return; }
        const [b, x] = await Promise.all([
          supabase.from('lesson_blocks').select('id, kind, position, body').eq('lesson_id', (lesson as Bundle['lesson']).id).order('position'),
          supabase.from('exercises').select('id, type, difficulty, statement, options').eq('lesson_id', (lesson as Bundle['lesson']).id).order('difficulty'),
        ]);
        if (b.error || x.error) throw (b.error ?? x.error);
        setData({ lesson: lesson as Bundle['lesson'], blocks: (b.data ?? []) as Block[], exercises: (x.data ?? []) as unknown as ExerciseView[] });
        setSaved(loadLessonOffline(slug) !== null);
      } catch {
        const cached = loadLessonOffline<Bundle>(slug);
        if (cached) { setData(cached.bundle); setFromCache(true); setSaved(true); }
        else setError('Sem ligação e esta aula não está guardada neste dispositivo.');
      }
    })();
  }, [slug]);

  if (error) return <div className="space-y-3"><Link to="/academia" className="muted">← Academia</Link><p className="card muted" role="alert">{error}</p></div>;
  if (!data) return <p className="muted">A carregar…</p>;

  return (
    <article className="space-y-5">
      <Link to="/academia" className="muted">← Academia</Link>
      <header className="space-y-2">
        <h1 className="text-2xl font-bold">{data.lesson.title}</h1>
        {data.lesson.summary && <p className="muted">{data.lesson.summary}</p>}
        {fromCache && <p className="badge">A ler a versão guardada neste dispositivo</p>}
        <div>
          {saved ? (
            <button className="btn-ghost" onClick={() => { removeLessonOffline(slug); setSaved(false); }}><Trash2 size={16} />Remover do offline</button>
          ) : (
            <button className="btn-ghost" onClick={() => setSaved(saveLessonOffline(slug, data))}><Download size={16} />Guardar para offline</button>
          )}
        </div>
      </header>

      {data.blocks.map((b) => (
        <section key={b.id} className="card space-y-2">
          <h2 className="text-sm font-semibold uppercase tracking-wide text-electric-500">{KIND_LABEL[b.kind] ?? b.kind}</h2>
          <RichText text={b.body} />
        </section>
      ))}

      {data.exercises.length > 0 && (
        <section className="space-y-3">
          <h2 className="text-lg font-semibold">Exercícios</h2>
          {data.exercises.map((e) => <ExercisePlayer key={e.id} exercise={e} />)}
        </section>
      )}
      {data.blocks.length === 0 && data.exercises.length === 0 && <p className="card muted">Esta aula ainda não tem conteúdo.</p>}
    </article>
  );
}

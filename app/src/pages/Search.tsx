import { useEffect, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { Search } from 'lucide-react';
import { supabase } from '../lib/supabase';

interface Hit { slug: string; title: string; summary: string | null }

export function SearchPage() {
  const [params, setParams] = useSearchParams();
  const q = params.get('q') ?? '';
  const [text, setText] = useState(q);
  const [hits, setHits] = useState<Hit[] | null>(null);

  useEffect(() => {
    const term = q.trim().replace(/[%_,()]/g, ' ');
    if (term.length < 2) { setHits(null); return; }
    let alive = true;
    void (async () => {
      const { data } = await supabase.from('lessons').select('slug, title, summary')
        .or(`title.ilike.%${term}%,summary.ilike.%${term}%`).limit(30);
      if (alive) setHits((data ?? []) as Hit[]);
    })();
    return () => { alive = false; };
  }, [q]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Pesquisar aulas</h1>
      <form className="flex gap-2" onSubmit={(e) => { e.preventDefault(); setParams(text.trim() ? { q: text.trim() } : {}); }}>
        <input className="input flex-1" value={text} onChange={(e) => setText(e.target.value)} placeholder="Ex.: frações, potências, percentagem…" aria-label="Pesquisar aulas" />
        <button className="btn" type="submit"><Search size={16} /> Procurar</button>
      </form>
      {hits === null && q.length > 0 && q.length < 2 && <p className="muted">Escreve pelo menos 2 letras.</p>}
      {hits?.length === 0 && <p className="muted">Nada encontrado para «{q}». Tenta outra palavra.</p>}
      <ul className="space-y-2">
        {hits?.map((h) => (
          <li key={h.slug}><Link to={`/aula/${h.slug}`} className="card card-hover block hover:border-electric-500">
            <span className="font-semibold">{h.title}</span>
            {h.summary && <span className="muted block text-sm">{h.summary}</span>}
          </Link></li>
        ))}
      </ul>
    </div>
  );
}

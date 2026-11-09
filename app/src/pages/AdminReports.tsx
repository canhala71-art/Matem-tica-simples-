import { useEffect, useState } from 'react';
import { supabase } from '../lib/supabase';

interface Rep { id: string; kind: string; ref: string | null; message: string; status: string; created_at: string }

export function ReportsTab() {
  const [rows, setRows] = useState<Rep[] | null>(null);
  async function load() {
    const { data } = await supabase.from('reports').select('id, kind, ref, message, status, created_at').order('created_at', { ascending: false }).limit(100);
    setRows((data ?? []) as Rep[]);
  }
  useEffect(() => { void load(); }, []);
  async function setStatus(id: string, status: string) {
    await supabase.from('reports').update({ status }).eq('id', id);
    await load();
  }
  if (!rows) return <p className="muted">A carregar…</p>;
  if (!rows.length) return <p className="card">Sem mensagens de utilizadores.</p>;
  return (
    <ul className="space-y-2">
      {rows.map((r) => (
        <li key={r.id} className="card space-y-1 text-sm">
          <p className="flex flex-wrap items-center gap-2"><span className="badge">{r.kind}</span><span className="badge">{r.status}</span><span className="muted">{new Date(r.created_at).toLocaleString('pt-PT')}</span></p>
          {r.ref && <p className="muted break-all">Ref.: {r.ref}</p>}
          <p className="whitespace-pre-wrap">{r.message}</p>
          <div className="flex gap-2">
            {r.status !== 'visto' && <button className="btn-ghost" onClick={() => void setStatus(r.id, 'visto')}>Marcar visto</button>}
            {r.status !== 'resolvido' && <button className="btn-ghost" onClick={() => void setStatus(r.id, 'resolvido')}>Resolvido</button>}
          </div>
        </li>
      ))}
    </ul>
  );
}

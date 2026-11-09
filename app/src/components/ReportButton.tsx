import { useState } from 'react';
import { Flag } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { humanError } from '../lib/billing';

export function ReportForm({ kind, refId, onDone, placeholder }: { kind: 'exercicio' | 'aula' | 'site' | 'sugestao'; refId?: string; onDone?: () => void; placeholder?: string }) {
  const [text, setText] = useState('');
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<{ ok: boolean; t: string } | null>(null);
  async function send() {
    setBusy(true); setMsg(null);
    const { error } = await supabase.rpc('submit_report', { _kind: kind, _ref: refId ?? null, _message: text });
    setBusy(false);
    if (error) { setMsg({ ok: false, t: humanError(error) }); return; }
    setText(''); setMsg({ ok: true, t: 'Obrigado! Recebemos a tua mensagem.' }); onDone?.();
  }
  return (
    <div className="space-y-2">
      <textarea className="input min-h-20" maxLength={1000} value={text} onChange={(e) => setText(e.target.value)} placeholder={placeholder ?? 'Descreve o problema…'} aria-label="Mensagem" />
      <button className="btn" disabled={busy || text.trim().length < 3} onClick={() => void send()}>{busy ? 'A enviar…' : 'Enviar'}</button>
      {msg && <p role={msg.ok ? 'status' : 'alert'} className={`text-sm ${msg.ok ? 'text-emerald-600' : 'text-red-600'}`}>{msg.t}</p>}
    </div>
  );
}

export function ReportButton({ kind, refId }: { kind: 'exercicio' | 'aula'; refId: string }) {
  const [open, setOpen] = useState(false);
  return (
    <div>
      <button className="muted inline-flex items-center gap-1 text-xs underline" onClick={() => setOpen((o) => !o)}><Flag size={12} /> Reportar erro {kind === 'exercicio' ? 'neste exercício' : 'nesta aula'}</button>
      {open && <div className="mt-2"><ReportForm kind={kind} refId={refId} placeholder="O que está errado? (ex.: a resposta certa não é aceite)" onDone={() => setOpen(false)} /></div>}
    </div>
  );
}

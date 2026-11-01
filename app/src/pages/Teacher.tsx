import { useRef, useState, type FormEvent } from 'react';
import { FunctionsHttpError } from '@supabase/supabase-js';
import { Send } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { RichText } from '../components/RichText';

interface Msg { role: 'user' | 'assistant'; content: string; demo?: boolean }

export function TeacherPage() {
  const [messages, setMessages] = useState<Msg[]>([]);
  const [input, setInput] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const convId = useRef<string | undefined>(undefined);

  async function send(e: FormEvent) {
    e.preventDefault();
    const text = input.trim();
    if (!text || busy) return;
    if (!navigator.onLine) { setError('O professor IA precisa de ligação à internet.'); return; }
    setError(null);
    setBusy(true);
    setMessages((m) => [...m, { role: 'user', content: text }]);
    setInput('');
    const { data, error: err } = await supabase.functions.invoke('ai-teacher', {
      body: { message: text, conversation_id: convId.current },
    });
    setBusy(false);
    if (err) {
      let msg = 'O professor IA não está disponível agora.';
      if (err instanceof FunctionsHttpError) {
        try { msg = ((await err.context.json()) as { error?: string }).error ?? msg; } catch { /* mantém */ }
      }
      setError(msg);
      return;
    }
    const out = data as { reply: string; conversation_id: string; demo: boolean };
    convId.current = out.conversation_id;
    setMessages((m) => [...m, { role: 'assistant', content: out.reply, demo: out.demo }]);
  }

  return (
    <div className="mx-auto max-w-2xl space-y-4">
      <div>
        <h1 className="text-2xl font-bold">Professor IA</h1>
        <p className="muted">Pergunta o que não percebes. O professor guia-te com perguntas, em vez de só dar o resultado.</p>
      </div>
      <div className="space-y-3" aria-live="polite">
        {messages.length === 0 && <p className="card muted">Exemplo: "Não percebo como somar frações com denominadores diferentes."</p>}
        {messages.map((m, i) => (
          <div key={i} className={`card ${m.role === 'user' ? 'ml-8 bg-electric-500/10' : 'mr-8'}`}>
            {m.demo && <p className="badge mb-2">Demonstração — sem IA real</p>}
            <RichText text={m.content} />
          </div>
        ))}
        {busy && <p className="muted">O professor está a pensar…</p>}
      </div>
      {error && <p role="alert" className="text-sm text-red-600">{error}</p>}
      <form onSubmit={(e) => void send(e)} className="flex gap-2">
        <textarea className="input min-h-12 flex-1" rows={2} maxLength={2000} value={input}
          onChange={(e) => setInput(e.target.value)} placeholder="Escreve a tua dúvida…" />
        <button className="btn" disabled={busy || !input.trim()} aria-label="Enviar"><Send size={18} /></button>
      </form>
      <p className="muted">Há um limite diário de mensagens para controlar custos. Não escrevas dados pessoais.</p>
    </div>
  );
}

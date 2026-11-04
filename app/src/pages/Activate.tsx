import { useState, type FormEvent } from 'react';
import { Link } from 'react-router-dom';
import { KeyRound, PartyPopper } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { TIER_PT, fmtDate, humanError, type Access } from '../lib/billing';

export function ActivatePage() {
  const [code, setCode] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [done, setDone] = useState<Access | null>(null);

  async function submit(e: FormEvent) {
    e.preventDefault();
    if (!code.trim() || busy) return;
    setBusy(true); setError(null);
    const { data, error: err } = await supabase.rpc('redeem_code', { _code: code });
    setBusy(false);
    if (err) { setError(humanError(err)); return; }
    const r = data as (Access & { error?: string }) | null;
    if (!r || r.error) { setError(r?.error ?? 'Código inválido ou indisponível.'); return; }
    setDone(r);
  }

  if (done) {
    return (
      <div className="card mx-auto max-w-md space-y-3 text-center">
        <PartyPopper className="mx-auto text-electric-500" size={36} />
        <h1 className="text-xl font-bold">Plano ativado. Bem-vindo(a) ao Premium!</h1>
        <p>{TIER_PT[done.tier]} ativo até <strong>{fmtDate(done.ends_at)}</strong> ({done.days_left} dias).</p>
        <Link to="/academia" className="btn">Começar a estudar</Link>
      </div>
    );
  }

  return (
    <form onSubmit={(e) => void submit(e)} className="card mx-auto max-w-md space-y-4">
      <div className="flex items-center gap-2"><KeyRound className="text-electric-500" /><h1 className="text-xl font-bold">Activar o meu Premium</h1></div>
      <p className="muted">Introduz o código que recebeste no WhatsApp depois de confirmarmos o teu pagamento. O código só funciona na tua conta e só uma vez.</p>
      <input className="input font-mono uppercase tracking-wider" placeholder="MM-XXXXX-XXXXX-XXXXX-XXXXX" value={code}
        autoComplete="off" onChange={(e) => setCode(e.target.value)} aria-label="Código de activação" />
      {error && <p role="alert" className="text-sm text-red-600">{error}</p>}
      <button className="btn w-full" disabled={busy || !code.trim()}>{busy ? 'A verificar…' : 'Activar plano'}</button>
      <p className="muted">Ainda não pagaste? Vê os <Link className="text-electric-500" to="/planos">planos</Link>.</p>
    </form>
  );
}

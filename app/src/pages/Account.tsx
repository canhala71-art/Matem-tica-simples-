import { useState } from 'react';
import { Link } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import { humanError } from '../lib/billing';

const EXPORT_TABLES = ['profiles', 'attempts', 'lesson_progress', 'subject_tests', 'tool_runs', 'mastery', 'quiz_sessions', 'subscriptions', 'payment_requests', 'ai_conversations', 'reports'] as const;

export function AccountPage() {
  const { profile, session, refresh, signOut } = useAuth();
  const [name, setName] = useState(profile?.display_name ?? '');
  const [pw, setPw] = useState('');
  const [pw2, setPw2] = useState('');
  const [confirm, setConfirm] = useState('');
  const [note, setNote] = useState<{ ok: boolean; t: string } | null>(null);
  const [busy, setBusy] = useState(false);

  async function saveName() {
    if (!session || name.trim().length < 2) { setNote({ ok: false, t: 'O nome precisa de pelo menos 2 letras.' }); return; }
    setBusy(true);
    const { error } = await supabase.from('profiles').update({ display_name: name.trim() }).eq('id', session.user.id);
    setBusy(false);
    if (error) { setNote({ ok: false, t: humanError(error) }); return; }
    await refresh(); setNote({ ok: true, t: 'Nome atualizado.' });
  }
  async function savePw() {
    if (pw.length < 8) { setNote({ ok: false, t: 'A palavra-passe precisa de pelo menos 8 caracteres.' }); return; }
    if (pw !== pw2) { setNote({ ok: false, t: 'As palavras-passe não coincidem.' }); return; }
    setBusy(true);
    const { error } = await supabase.auth.updateUser({ password: pw });
    setBusy(false);
    if (error) { setNote({ ok: false, t: humanError(error) }); return; }
    setPw(''); setPw2(''); setNote({ ok: true, t: 'Palavra-passe alterada.' });
  }
  async function exportData() {
    if (!session) return;
    setBusy(true);
    const out: Record<string, unknown> = { exportado_em: new Date().toISOString(), email: session.user.email };
    for (const t of EXPORT_TABLES) {
      const { data } = await supabase.from(t).select('*').limit(5000);
      out[t] = data ?? [];
    }
    setBusy(false);
    const url = URL.createObjectURL(new Blob([JSON.stringify(out, null, 2)], { type: 'application/json' }));
    const a = document.createElement('a'); a.href = url; a.download = 'mentemat-os-meus-dados.json'; a.click(); URL.revokeObjectURL(url);
    setNote({ ok: true, t: 'Cópia dos teus dados descarregada.' });
  }
  async function del() {
    setBusy(true);
    const { error } = await supabase.rpc('delete_my_account');
    setBusy(false);
    if (error) { setNote({ ok: false, t: humanError(error) }); return; }
    await signOut();
    window.location.assign('/');
  }

  return (
    <div className="mx-auto max-w-xl space-y-4">
      <h1 className="text-2xl font-bold">A minha conta</h1>
      <p className="muted">{session?.user.email}</p>
      {note && <p role={note.ok ? 'status' : 'alert'} className={`card text-sm ${note.ok ? 'text-emerald-600' : 'text-red-600'}`}>{note.t}</p>}

      <section className="card space-y-2">
        <h2 className="font-semibold">Nome</h2>
        <input className="input" value={name} onChange={(e) => setName(e.target.value)} aria-label="Nome" maxLength={60} />
        <button className="btn" disabled={busy} onClick={() => void saveName()}>Guardar nome</button>
      </section>

      <section className="card space-y-2">
        <h2 className="font-semibold">Mudar palavra-passe</h2>
        <input className="input" type="password" autoComplete="new-password" value={pw} onChange={(e) => setPw(e.target.value)} placeholder="Nova palavra-passe (mín. 8)" aria-label="Nova palavra-passe" />
        <input className="input" type="password" autoComplete="new-password" value={pw2} onChange={(e) => setPw2(e.target.value)} placeholder="Repete a nova palavra-passe" aria-label="Repetir palavra-passe" />
        <button className="btn" disabled={busy} onClick={() => void savePw()}>Mudar palavra-passe</button>
      </section>

      <section className="card space-y-2">
        <h2 className="font-semibold">Os meus dados</h2>
        <p className="muted text-sm">Descarrega uma cópia do teu perfil, progresso, notas e pedidos. Veja também a <Link className="text-electric-500 underline" to="/privacidade">política de privacidade</Link>.</p>
        <button className="btn-ghost" disabled={busy} onClick={() => void exportData()}>Descarregar os meus dados</button>
      </section>

      <section className="card space-y-2 border-red-500/50">
        <h2 className="font-semibold text-red-600">Apagar a minha conta</h2>
        <p className="muted text-sm">Remove para sempre o teu perfil, progresso, notas, conversas e assinatura. Não dá para desfazer. Para confirmar, escreve <strong>APAGAR</strong>.</p>
        <input className="input" value={confirm} onChange={(e) => setConfirm(e.target.value)} placeholder="APAGAR" aria-label="Confirmação" />
        <button className="btn !bg-red-600" disabled={busy || confirm.trim() !== 'APAGAR'} onClick={() => void del()}>Apagar a minha conta</button>
      </section>
    </div>
  );
}

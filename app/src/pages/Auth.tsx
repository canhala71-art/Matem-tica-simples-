import { useState, type FormEvent } from 'react';
import { Link, Navigate, useNavigate } from 'react-router-dom';
import { supabase, configured } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import { Logo } from '../components/Layout';

type Mode = 'login' | 'register' | 'forgot';

export function AuthPage() {
  const { session, loading } = useAuth();
  const nav = useNavigate();
  const [mode, setMode] = useState<Mode>('login');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [minor, setMinor] = useState(false);
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<{ type: 'ok' | 'err'; text: string } | null>(null);

  if (!loading && session) return <Navigate to="/" replace />;

  async function submit(e: FormEvent) {
    e.preventDefault();
    setBusy(true);
    setMsg(null);
    try {
      if (mode === 'login') {
        const { error } = await supabase.auth.signInWithPassword({ email, password });
        if (error) throw error;
        nav('/');
      } else if (mode === 'register') {
        if (password.length < 8) throw new Error('A palavra-passe deve ter pelo menos 8 caracteres.');
        const { data, error } = await supabase.auth.signUp({
          email, password,
          options: { data: { display_name: name.trim() || 'Estudante', is_minor: minor }, emailRedirectTo: window.location.origin },
        });
        if (error) throw error;
        if (data.session) nav('/');
        else setMsg({ type: 'ok', text: 'Conta criada. Abre o email de confirmação para ativar a conta.' });
      } else {
        const { error } = await supabase.auth.resetPasswordForEmail(email, { redirectTo: `${window.location.origin}/redefinir` });
        if (error) throw error;
        setMsg({ type: 'ok', text: 'Se o email existir, vais receber um link para redefinir a palavra-passe.' });
      }
    } catch (err) {
      const raw = err instanceof Error ? err.message : 'Erro inesperado';
      setMsg({ type: 'err', text: raw.includes('Invalid login') ? 'Email ou palavra-passe incorretos.' : raw });
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="mx-auto flex min-h-screen max-w-md flex-col justify-center px-4 py-10">
      <div className="mb-6 text-center">
        <Logo className="text-3xl" />
        <p className="mt-2 text-sm text-slate-500">A matemática começa na tua mente.</p>
        <p className="text-xs text-slate-400">Aprende. Compreende. Raciocina. Domina.</p>
      </div>
      {!configured && (
        <p role="alert" className="mb-4 rounded-xl bg-red-500/10 p-3 text-sm text-red-600">
          A aplicação ainda não está ligada ao Supabase (faltam VITE_SUPABASE_URL e VITE_SUPABASE_PUBLISHABLE_KEY).
        </p>
      )}
      <form onSubmit={(e) => void submit(e)} className="card space-y-3">
        <h1 className="text-lg font-semibold">
          {mode === 'login' ? 'Entrar' : mode === 'register' ? 'Criar conta de estudante' : 'Recuperar palavra-passe'}
        </h1>
        {mode === 'register' && (
          <input className="input" placeholder="Nome (pode ser só o primeiro)" value={name} maxLength={60}
            onChange={(e) => setName(e.target.value)} autoComplete="given-name" />
        )}
        <input className="input" type="email" required placeholder="Email" value={email}
          onChange={(e) => setEmail(e.target.value)} autoComplete="email" />
        {mode !== 'forgot' && (
          <input className="input" type="password" required minLength={mode === 'register' ? 8 : undefined}
            placeholder="Palavra-passe" value={password} onChange={(e) => setPassword(e.target.value)}
            autoComplete={mode === 'login' ? 'current-password' : 'new-password'} />
        )}
        {mode === 'register' && (
          <label className="flex items-start gap-2 text-sm">
            <input type="checkbox" checked={minor} onChange={(e) => setMinor(e.target.checked)} className="mt-0.5" />
            <span>Tenho menos de 18 anos. <span className="muted">(Só guardamos esta indicação, nunca a data de nascimento.)</span></span>
          </label>
        )}
        {msg && <p role="status" className={`text-sm ${msg.type === 'ok' ? 'text-emerald-600' : 'text-red-600'}`}>{msg.text}</p>}
        <button className="btn w-full" disabled={busy || !configured}>
          {busy ? 'Aguarda…' : mode === 'login' ? 'Entrar' : mode === 'register' ? 'Criar conta' : 'Enviar link'}
        </button>
        <div className="flex justify-between text-sm">
          {mode !== 'login' ? <button type="button" className="text-electric-500" onClick={() => setMode('login')}>Já tenho conta</button> : <span />}
          {mode === 'login' && <button type="button" className="text-electric-500" onClick={() => setMode('forgot')}>Esqueci a palavra-passe</button>}
          {mode === 'login' && <button type="button" className="text-electric-500" onClick={() => setMode('register')}>Criar conta</button>}
        </div>
      </form>
    </div>
  );
}

export function ResetPasswordPage() {
  const nav = useNavigate();
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function submit(e: FormEvent) {
    e.preventDefault();
    if (password.length < 8) { setMsg('A palavra-passe deve ter pelo menos 8 caracteres.'); return; }
    setBusy(true);
    const { error } = await supabase.auth.updateUser({ password });
    setBusy(false);
    if (error) setMsg('Não foi possível alterar. Pede um novo link e tenta de novo.');
    else nav('/');
  }

  return (
    <div className="mx-auto flex min-h-screen max-w-md flex-col justify-center px-4">
      <form onSubmit={(e) => void submit(e)} className="card space-y-3">
        <h1 className="text-lg font-semibold">Nova palavra-passe</h1>
        <input className="input" type="password" required minLength={8} value={password}
          onChange={(e) => setPassword(e.target.value)} autoComplete="new-password" placeholder="Pelo menos 8 caracteres" />
        {msg && <p role="alert" className="text-sm text-red-600">{msg}</p>}
        <button className="btn w-full" disabled={busy}>Guardar</button>
        <Link to="/entrar" className="block text-center text-sm text-electric-500">Voltar</Link>
      </form>
    </div>
  );
}

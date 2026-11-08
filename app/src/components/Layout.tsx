import { useEffect, useState, type ReactNode } from 'react';
import { Link, NavLink, Navigate, Outlet, useLocation } from 'react-router-dom';
import { BookOpen, Bot, CreditCard, FlaskConical, LayoutDashboard, LogOut, Moon, Search, Shield, Sparkles, Sun, Trophy, WifiOff } from 'lucide-react';
import { useAuth } from '../lib/auth';
import { flushQueue } from '../lib/offline';

export function applyTheme(t: 'light' | 'dark') {
  document.documentElement.classList.toggle('dark', t === 'dark');
  try { localStorage.setItem('mm_theme', t); } catch { /* ignora */ }
}
export function initTheme() {
  let t: 'light' | 'dark' = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  try {
    const saved = localStorage.getItem('mm_theme');
    if (saved === 'light' || saved === 'dark') t = saved;
  } catch { /* ignora */ }
  applyTheme(t);
}

export function Logo({ className = '' }: { className?: string }) {
  return (
    <span className={`inline-flex items-center gap-2 font-bold tracking-tight ${className}`}>
      <img src="/icon.svg" alt="" className="h-7 w-7" />
      <span>Mente<span className="text-electric-500">Mat</span></span>
    </span>
  );
}

export function RequireAuth() {
  const { session, loading } = useAuth();
  if (loading) return <p className="p-8 text-center muted">A carregar…</p>;
  if (!session) return <Navigate to="/entrar" replace />;
  return <Layout />;
}

export function RequireAdmin() {
  const { isAdmin, loading } = useAuth();
  if (loading) return <p className="p-8 text-center muted">A carregar…</p>;
  if (!isAdmin) return <Navigate to="/" replace />;
  return <Outlet />;
}

export function Layout({ children }: { children?: ReactNode }) {
  const { profile, isAdmin, signOut } = useAuth();
  const loc = useLocation();
  const [online, setOnline] = useState(navigator.onLine);
  const [dark, setDark] = useState(document.documentElement.classList.contains('dark'));

  useEffect(() => {
    const on = () => { setOnline(true); void flushQueue(); };
    const off = () => setOnline(false);
    window.addEventListener('online', on);
    window.addEventListener('offline', off);
    void flushQueue();
    return () => { window.removeEventListener('online', on); window.removeEventListener('offline', off); };
  }, []);

  const link = ({ isActive }: { isActive: boolean }) =>
    `flex items-center gap-1.5 whitespace-nowrap rounded-lg px-3 py-2 text-sm font-medium ${isActive ? 'bg-electric-500/15 text-electric-500' : 'hover:bg-slate-200/60 dark:hover:bg-navy-800'}`;

  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-10 border-b border-slate-200 bg-white/90 backdrop-blur dark:border-navy-800 dark:bg-navy-950/90">
        <div className="mx-auto flex max-w-5xl items-center gap-3 px-4 py-2">
          <Link to="/" className="shrink-0"><Logo /></Link>
          <nav className="flex flex-1 gap-1 overflow-x-auto" aria-label="Principal">
            <NavLink to="/" end className={link}><LayoutDashboard size={16} />Painel</NavLink>
            <NavLink to="/academia" className={link}><BookOpen size={16} />Academia</NavLink>
            <NavLink to="/quiz" className={link}><Trophy size={16} />Quiz</NavLink>
            <NavLink to="/professor" className={link}><Bot size={16} />Professor IA</NavLink>
            <NavLink to="/laboratorio" className={link}><FlaskConical size={16} />Laboratório</NavLink>
            <NavLink to="/planos" className={link}><Sparkles size={16} />Planos</NavLink>
            <NavLink to="/assinatura" className={link}><CreditCard size={16} />Assinatura</NavLink>
            {isAdmin && <NavLink to="/admin" className={link}><Shield size={16} />Admin</NavLink>}
          </nav>
          <Link to="/pesquisa" className="btn-ghost !px-2.5" aria-label="Pesquisar aulas"><Search size={16} /></Link>
          <button className="btn-ghost !px-2.5" aria-label="Alternar tema claro/escuro"
            onClick={() => { const t = dark ? 'light' : 'dark'; applyTheme(t); setDark(!dark); }}>
            {dark ? <Sun size={16} /> : <Moon size={16} />}
          </button>
          <button className="btn-ghost !px-2.5" aria-label={`Sair${profile ? ` (${profile.display_name})` : ''}`} onClick={() => void signOut()}>
            <LogOut size={16} />
          </button>
        </div>
        {!online && (
          <p className="flex items-center justify-center gap-2 bg-amber-500/15 px-4 py-1.5 text-xs">
            <WifiOff size={14} /> Sem ligação: só as aulas guardadas estão disponíveis; o professor IA precisa de internet.
          </p>
        )}
      </header>
      <main key={loc.pathname} className="anim-fade-up mx-auto max-w-5xl px-4 py-6">
        {profile?.suspended ? (
          <div className="card mx-auto max-w-md space-y-3 text-center">
            <p className="font-semibold">A tua conta está suspensa.</p>
            <p className="muted">Se achas que é um engano, fala connosco pelo WhatsApp de suporte.</p>
          </div>
        ) : (children ?? <Outlet />)}
      </main>
    </div>
  );
}

import { Link } from 'react-router-dom';

export function Footer() {
  return (
    <footer className="mx-auto mt-10 max-w-5xl border-t border-slate-200 px-4 py-6 text-sm dark:border-navy-800">
      <nav aria-label="Informação" className="flex flex-wrap items-center justify-center gap-x-5 gap-y-2">
        <Link to="/ajuda" className="muted hover:text-electric-500">Ajuda e contacto</Link>
        <Link to="/termos" className="muted hover:text-electric-500">Termos de uso</Link>
        <Link to="/privacidade" className="muted hover:text-electric-500">Privacidade</Link>
      </nav>
      <p className="muted mt-3 text-center text-xs">© {new Date().getFullYear()} MenteMat · A matemática começa na tua mente.</p>
    </footer>
  );
}

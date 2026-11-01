import { Link } from 'react-router-dom';
import { Logo } from '../components/Layout';

export function NotFound() {
  return (
    <div className="mx-auto flex min-h-screen max-w-md flex-col items-center justify-center gap-4 px-4 text-center">
      <Logo className="text-2xl" />
      <p className="text-6xl font-bold text-electric-500">404</p>
      <p className="muted">Esta página não existe ou foi movida.</p>
      <Link to="/" className="btn">Voltar ao início</Link>
    </div>
  );
}

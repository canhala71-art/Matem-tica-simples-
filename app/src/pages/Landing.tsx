import { Footer } from '../components/Footer';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Logo } from '../components/Layout';
import { supabase } from '../lib/supabase';
import { kz, type Plan } from '../lib/billing';
import { CATEGORIES } from '../lib/quiz';

export function Landing() {
  const [plans, setPlans] = useState<Plan[]>([]);
  useEffect(() => {
    void supabase.from('plans').select('*').eq('active', true).order('sort').then(({ data }) => setPlans((data ?? []) as Plan[]));
  }, []);
  return (
    <div className="min-h-screen">
      <header className="mx-auto flex max-w-5xl items-center justify-between gap-3 px-4 py-3">
        <Logo className="text-xl" />
        <div className="flex gap-2">
          <Link to="/entrar" className="btn-ghost">Entrar</Link>
          <Link to="/entrar?criar=1" className="btn">Criar conta</Link>
        </div>
      </header>
      <main className="mx-auto max-w-5xl space-y-12 px-4 pb-16">
        <section className="space-y-4 py-10 text-center">
          <h1 className="text-4xl font-extrabold tracking-tight sm:text-5xl">Domina a Matemática ao teu ritmo.</h1>
          <p className="mx-auto max-w-xl text-lg text-slate-600 dark:text-slate-300">
            Aprende com explicações claras, pratica com exercícios corrigidos na hora e prepara-te para os teus exames. Feito a pensar em quem estuda em Angola.
          </p>
          <Link to="/entrar?criar=1" className="btn !px-6 !py-3 text-base">Começar a aprender</Link>
          <p className="muted">É grátis para começar. Sem cartão.</p>
        </section>

        <section className="space-y-3">
          <h2 className="text-xl font-bold">O que queres estudar hoje?</h2>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-5">
            {CATEGORIES.map(([k, l]) => (
              <Link key={k} to="/entrar?criar=1" className="card card-hover text-center text-sm font-medium hover:border-electric-500">{l}</Link>
            ))}
          </div>
        </section>

        <section className="card space-y-2 text-center">
          <h2 className="text-lg font-extrabold tracking-wide">DESAFIO MATEMÁTICO DO DIA</h2>
          <p className="muted">Testa os teus conhecimentos. Cada desafio é uma oportunidade para evoluir.</p>
          <Link to="/entrar?criar=1" className="btn mx-auto">Entrar para ver o desafio de hoje</Link>
        </section>

        {plans.length > 0 && (
          <section className="space-y-3">
            <h2 className="text-xl font-bold">Planos simples, em kwanzas</h2>
            <div className="grid gap-3 sm:grid-cols-4">
              <div className="card"><p className="font-semibold">Free</p><p className="text-xl font-bold">0 Kz</p></div>
              {plans.map((p) => (
                <div key={p.id} className="card">
                  <p className="font-semibold">{p.name}</p>
                  <p className="text-xl font-bold">{kz(p.price_kz)}</p>
                  <p className="muted">{p.period === 'monthly' ? 'por mês' : 'por ano'}</p>
                </div>
              ))}
            </div>
            <p className="muted">Pagamento por Multicaixa Express ou UNITEL Money. Sem cobranças automáticas.</p>
          </section>
        )}
      </main>
      <Footer />
    </div>
  );
}

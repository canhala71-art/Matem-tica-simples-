import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { MessageCircle } from 'lucide-react';
import { Logo } from '../components/Layout';
import { Footer } from '../components/Footer';
import { ReportForm } from '../components/ReportButton';
import { useAuth } from '../lib/auth';
import { loadSettings, whatsappLink } from '../lib/billing';

const FAQ: [string, string][] = [
  ['O MenteMat é gratuito?', 'Há um plano gratuito com aulas e exercícios. Os planos Premium dão acesso completo e estão na página de Planos, em kwanzas.'],
  ['Como pago o plano Premium?', 'Escolhes o plano, pagas por Multicaixa Express ou UNITEL Money e indicas a referência. Um administrador confirma e ativas o acesso. Também podes ativar com um código.'],
  ['Esqueci a palavra-passe.', 'Na página de entrada usa «Esqueci a palavra-passe» e segue o link enviado para o teu email.'],
  ['Como funcionam as notas?', 'Os testes têm nota de 0 a 20, calculada a partir das tuas respostas. Servem para te acompanhares e não têm valor oficial.'],
  ['O professor IA acerta sempre?', 'Não. Pode errar. Confirma sempre com a aula ou com o teu professor.'],
  ['Posso usar sem internet?', 'Podes guardar aulas para ler offline. Os exercícios respondidos sem ligação ficam em fila e são corrigidos quando voltares a ter internet.'],
  ['Como instalo no telemóvel?', 'No Android podes instalar o APK (link abaixo) ou usar «Adicionar ao ecrã inicial» no navegador.'],
  ['Como apago a minha conta?', 'Entra em «A minha conta» e escolhe «Apagar a minha conta».'],
];

export function HelpPage() {
  const { session } = useAuth();
  const [wa, setWa] = useState<string | null>(null);
  const [support, setSupport] = useState<string | null>(null);
  useEffect(() => {
    void loadSettings().then((s) => {
      const n = s.whatsapp?.number;
      setWa(typeof n === 'string' && n.trim() ? n : null);
      const t = s.support?.text;
      setSupport(typeof t === 'string' && t.trim() ? t : null);
    });
  }, []);
  return (
    <div className="min-h-screen">
      <header className="mx-auto flex max-w-3xl items-center justify-between px-4 py-4">
        <Link to="/"><Logo /></Link>
        <Link to="/" className="muted">← Início</Link>
      </header>
      <main id="conteudo" className="mx-auto max-w-3xl space-y-6 px-4 pb-6">
        <h1 className="text-3xl font-bold">Ajuda e contacto</h1>
        <section className="space-y-2">
          <h2 className="text-xl font-semibold">Perguntas frequentes</h2>
          {FAQ.map(([q, a]) => (
            <details key={q} className="card">
              <summary className="cursor-pointer font-medium">{q}</summary>
              <p className="muted mt-2">{a}</p>
            </details>
          ))}
        </section>
        <section className="card space-y-3">
          <h2 className="text-xl font-semibold">Falar connosco</h2>
          {support && <p className="muted">{support}</p>}
          {wa && <a className="btn inline-flex" target="_blank" rel="noreferrer" href={whatsappLink(wa, 'Olá! Preciso de ajuda no MenteMat.')}><MessageCircle size={16} /> WhatsApp</a>}
          {session
            ? <><p className="font-medium">Ou deixa-nos uma mensagem (erro, dúvida ou sugestão):</p><ReportForm kind="sugestao" placeholder="Escreve aqui a tua mensagem…" /></>
            : <p className="muted">Para enviar uma mensagem pelo site, <Link className="text-electric-500 underline" to="/entrar">entra na tua conta</Link>.</p>}
        </section>
        <section className="card space-y-2">
          <h2 className="text-xl font-semibold">Aplicação Android</h2>
          <a className="btn-ghost inline-flex" href="https://github.com/canhala71-art/Matem-tica-simples-/releases/download/apk-latest/MenteMat.apk">Descarregar o APK</a>
          <p className="muted text-sm">Ao instalar, o Android pede para permitir apps de fontes desconhecidas.</p>
        </section>
      </main>
      <Footer />
    </div>
  );
}

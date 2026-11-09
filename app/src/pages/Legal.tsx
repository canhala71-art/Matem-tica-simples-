import { Link } from 'react-router-dom';
import { Logo } from '../components/Layout';
import { Footer } from '../components/Footer';

function Shell({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="min-h-screen">
      <header className="mx-auto flex max-w-3xl items-center justify-between px-4 py-4">
        <Link to="/"><Logo /></Link>
        <Link to="/" className="muted">← Início</Link>
      </header>
      <main id="conteudo" className="mx-auto max-w-3xl space-y-4 px-4 pb-6">
        <h1 className="text-3xl font-bold">{title}</h1>
        <p className="muted text-sm">Última atualização: 9 de novembro de 2026</p>
        <div className="space-y-4 leading-relaxed [&_h2]:mt-6 [&_h2]:text-xl [&_h2]:font-semibold [&_ul]:list-disc [&_ul]:space-y-1 [&_ul]:pl-6">{children}</div>
      </main>
      <Footer />
    </div>
  );
}

export function TermsPage() {
  return (
    <Shell title="Termos de uso">
      <p>Ao criares uma conta no MenteMat aceitas estes termos. Se és menor de idade, deves usar o MenteMat com o conhecimento e a autorização de um encarregado de educação.</p>
      <h2>O que é o MenteMat</h2>
      <p>Uma plataforma de estudo de matemática com aulas, exercícios, testes, ferramentas e um professor virtual com inteligência artificial. É um apoio ao estudo e não substitui a escola nem um professor.</p>
      <h2>A tua conta</h2>
      <ul>
        <li>Fornece dados verdadeiros e mantém a tua palavra-passe em segredo.</li>
        <li>Cada conta é pessoal. Não partilhes o acesso nem uses a conta de outra pessoa.</li>
        <li>Podes apagar a tua conta a qualquer momento em «A minha conta».</li>
      </ul>
      <h2>Uso correto</h2>
      <p>Não podes tentar aceder a dados de outros utilizadores, sobrecarregar o serviço, copiar o conteúdo em massa para o revender, nem usar o professor IA para fins que não sejam o estudo.</p>
      <h2>Conteúdo e exatidão</h2>
      <p>Esforçamo-nos por verificar as aulas e os exercícios, mas podem existir erros. Se encontrares um, usa o botão «Reportar» ou a página de Ajuda. As respostas do professor IA podem conter erros: confirma sempre com a aula, o teu professor ou outra fonte. As notas dos testes do MenteMat servem para o teu acompanhamento e não têm valor oficial.</p>
      <h2>Planos e pagamentos</h2>
      <ul>
        <li>Há um plano gratuito e planos pagos (Premium). Os preços são mostrados em kwanzas na página de Planos.</li>
        <li>O pagamento é feito manualmente (Multicaixa Express ou UNITEL Money) e confirmado por um administrador. Não há cobranças automáticas.</li>
        <li>O acesso Premium começa quando o pagamento é confirmado ou um código de ativação é aceite, e dura o período do plano.</li>
        <li>Só os administradores do MenteMat confirmam pagamentos e emitem códigos. Desconfia de quem diga o contrário.</li>
      </ul>
      <h2>Suspensão</h2>
      <p>Podemos suspender contas que violem estes termos. Se achas que foi um engano, contacta-nos pela página de Ajuda.</p>
      <h2>Alterações</h2>
      <p>Podemos atualizar estes termos. A data de «última atualização» no topo mostra a versão em vigor.</p>
      <h2>Contacto</h2>
      <p>Usa a <Link to="/ajuda" className="text-electric-500 underline">página de Ajuda</Link>.</p>
    </Shell>
  );
}

export function PrivacyPage() {
  return (
    <Shell title="Política de privacidade">
      <p>Esta página explica que dados o MenteMat guarda, porquê, e que controlo tens sobre eles.</p>
      <h2>Que dados guardamos</h2>
      <ul>
        <li><strong>Conta:</strong> email, nome, nível académico escolhido e se és menor de idade.</li>
        <li><strong>Estudo:</strong> exercícios respondidos e resultados, aulas vistas e concluídas, tempo de estudo, notas de testes, resultados guardados das ferramentas, conquistas e quizzes.</li>
        <li><strong>Pagamentos:</strong> pedidos de pagamento (plano, método, referência indicada por ti) e a tua assinatura. Não guardamos dados de cartões nem números de contas bancárias.</li>
        <li><strong>Professor IA:</strong> as mensagens que escreves e as respostas, para continuares a conversa.</li>
        <li><strong>Mensagens de ajuda:</strong> o que escreves quando reportas um erro ou envias uma sugestão.</li>
      </ul>
      <h2>Para que usamos</h2>
      <p>Para fazer o serviço funcionar: guardar o teu progresso, mostrar as tuas notas e conquistas, sugerir o próximo passo de estudo, gerir o teu plano e responder a pedidos de ajuda. Não vendemos os teus dados nem mostramos publicidade.</p>
      <h2>Com quem os partilhamos</h2>
      <ul>
        <li><strong>Supabase</strong>, que aloja a base de dados e a autenticação (servidores na Europa).</li>
        <li><strong>Vercel</strong>, que aloja o site.</li>
        <li><strong>Anthropic</strong>, apenas quando usas o professor IA: a tua mensagem e o teu nível são enviados para gerar a resposta. Não escrevas dados pessoais sensíveis nessas conversas.</li>
      </ul>
      <h2>Menores</h2>
      <p>Se és menor de idade, usa o MenteMat com o conhecimento de um encarregado de educação. O professor IA adapta as respostas à idade.</p>
      <h2>Os teus direitos</h2>
      <ul>
        <li><strong>Ver e exportar:</strong> em «A minha conta» podes descarregar uma cópia dos teus dados.</li>
        <li><strong>Corrigir:</strong> podes mudar o teu nome e a tua palavra-passe em «A minha conta».</li>
        <li><strong>Apagar:</strong> em «A minha conta» podes apagar a conta. Isso remove o teu perfil, progresso, notas, conversas e assinatura. Mensagens de ajuda que enviaste ficam sem ligação à tua conta.</li>
      </ul>
      <h2>Segurança</h2>
      <p>O acesso aos dados é restringido por conta: cada utilizador só vê os seus. Mesmo assim, nenhum sistema é perfeito: usa uma palavra-passe forte e única.</p>
      <h2>Armazenamento no teu dispositivo</h2>
      <p>O site guarda no teu dispositivo a sessão de entrada, o tema claro/escuro e as aulas que guardas para ler offline. Não usamos cookies de publicidade.</p>
      <h2>Contacto</h2>
      <p>Para qualquer pedido sobre os teus dados, usa a <Link to="/ajuda" className="text-electric-500 underline">página de Ajuda</Link>.</p>
    </Shell>
  );
}

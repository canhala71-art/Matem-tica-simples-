// Edge Function: ai-teacher (MenteMat IA)
// A chave ANTHROPIC_API_KEY só existe aqui, no servidor. Sem chave => modo demonstração identificado.
import { createClient } from 'npm:@supabase/supabase-js@2';

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const DAILY_LIMIT = Number(Deno.env.get('AI_DAILY_LIMIT') ?? '20');
const MODEL = Deno.env.get('AI_MODEL') ?? 'claude-sonnet-5-5';

const SYSTEM = `És o professor de matemática do MenteMat. Responde sempre em português de Angola, de forma clara e simpática.
Ensina o raciocínio: faz perguntas curtas, divide em passos, dá uma pista antes da solução completa e verifica a compreensão no fim.
Usa fórmulas em LaTeX entre $...$. Adapta a linguagem ao nível do aluno (1 = fundamentos, 6 = especialização).
Nunca peças nem repitas dados pessoais. Se não tiveres certeza de um resultado, diz que não tens certeza em vez de inventar.
Se o pedido não for sobre matemática ou estudo, recusa com educação e volta ao tema. Respostas com no máximo 250 palavras.`;

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { ...CORS, 'Content-Type': 'application/json' } });
}

const DEMO = (msg: string) =>
  `**[DEMONSTRAÇÃO — esta resposta não vem de uma IA real]**\n\n` +
  `Recebi a tua pergunta: "${msg.slice(0, 120)}".\n\n` +
  `Quando a IA estiver ativada, o professor vai guiar-te passo a passo. Por agora, tenta: ` +
  `1) escrever o que o enunciado pede; 2) identificar os dados; 3) escolher a fórmula ou a operação certa. ` +
  `Qual destes passos achas mais difícil?`;

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: CORS });
  if (req.method !== 'POST') return json({ error: 'Método não permitido' }, 405);

  const admin = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!);
  const token = (req.headers.get('Authorization') ?? '').replace(/^Bearer\s+/i, '');
  const { data: auth, error: authErr } = await admin.auth.getUser(token);
  if (authErr || !auth.user) return json({ error: 'Sessão inválida' }, 401);
  const userId = auth.user.id;

  let body: { message?: string; conversation_id?: string };
  try { body = await req.json(); } catch { return json({ error: 'JSON inválido' }, 400); }
  const message = (body.message ?? '').trim();
  if (!message || message.length > 2000) return json({ error: 'Mensagem vazia ou demasiado longa (máx. 2000)' }, 400);

  // Conversa (só do próprio utilizador)
  let convId = body.conversation_id;
  if (convId) {
    if (!UUID.test(convId)) return json({ error: 'conversation_id inválido' }, 400);
    const { data: c } = await admin.from('ai_conversations').select('id').eq('id', convId).eq('user_id', userId).maybeSingle();
    if (!c) return json({ error: 'Conversa não encontrada' }, 404);
  }

  // Limite diário (atómico)
  const { data: allowed } = await admin.rpc('consume_ai_quota', { _user: userId, _limit: DAILY_LIMIT });
  if (!allowed) return json({ error: `Limite diário de ${DAILY_LIMIT} mensagens atingido. Volta amanhã.`, limit: DAILY_LIMIT }, 429);

  if (!convId) {
    const { data: created, error } = await admin.from('ai_conversations')
      .insert({ user_id: userId, title: message.slice(0, 60) }).select('id').single();
    if (error || !created) return json({ error: 'Não foi possível criar a conversa' }, 500);
    convId = created.id;
  }

  const apiKey = Deno.env.get('ANTHROPIC_API_KEY');
  const isDemo = !apiKey;
  let reply: string;

  if (isDemo) {
    reply = DEMO(message);
  } else {
    const { data: prof } = await admin.from('profiles').select('academic_level, is_minor').eq('id', userId).maybeSingle();
    const { data: hist } = await admin.from('ai_messages').select('role, content')
      .eq('conversation_id', convId).order('created_at', { ascending: false }).limit(10);
    const messages = [...(hist ?? []).reverse(), { role: 'user', content: message }];
    const system = SYSTEM +
      `\nNível do aluno: ${prof?.academic_level ?? 'não definido'}.` +
      (prof?.is_minor ? '\nO aluno é menor de idade: mantém tudo adequado à idade.' : '');
    try {
      const res = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: { 'x-api-key': apiKey!, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
        body: JSON.stringify({ model: MODEL, max_tokens: 800, system, messages }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const out = await res.json();
      reply = out.content?.filter((b: { type: string }) => b.type === 'text').map((b: { text: string }) => b.text).join('\n') ?? '';
      if (!reply) throw new Error('resposta vazia');
    } catch (e) {
      console.error('ai-teacher falhou:', e instanceof Error ? e.message : e);
      return json({ error: 'O professor IA não está disponível agora. Tenta novamente mais tarde.' }, 502);
    }
  }

  await admin.from('ai_messages').insert([
    { conversation_id: convId, role: 'user', content: message, is_demo: isDemo },
    { conversation_id: convId, role: 'assistant', content: reply, is_demo: isDemo },
  ]);
  return json({ conversation_id: convId, reply, demo: isDemo });
});

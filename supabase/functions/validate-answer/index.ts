// Edge Function: validate-answer
// Valida a resposta no servidor (o aluno nunca recebe a solução antes de responder),
// guarda a tentativa (idempotente por client_id) e atualiza o domínio da competência.
import { createClient } from 'npm:@supabase/supabase-js@2';
import { isMastered, validate, type Expected, type ExerciseType } from './math-validator.ts';

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...CORS, 'Content-Type': 'application/json' },
  });
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: CORS });
  if (req.method !== 'POST') return json({ error: 'Método não permitido' }, 405);

  const url = Deno.env.get('SUPABASE_URL')!;
  const admin = createClient(url, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!);

  const token = (req.headers.get('Authorization') ?? '').replace(/^Bearer\s+/i, '');
  const { data: auth, error: authErr } = await admin.auth.getUser(token);
  if (authErr || !auth.user) return json({ error: 'Sessão inválida' }, 401);
  const userId = auth.user.id;

  let body: { exercise_id?: string; answer?: unknown; client_id?: string; time_spent_seconds?: number };
  try { body = await req.json(); } catch { return json({ error: 'JSON inválido' }, 400); }

  const { exercise_id, answer, client_id } = body;
  if (!exercise_id || !UUID.test(exercise_id) || !client_id || !UUID.test(client_id)) {
    return json({ error: 'exercise_id e client_id têm de ser UUID' }, 400);
  }
  if (!(typeof answer === 'string' || typeof answer === 'number' || typeof answer === 'boolean')) {
    return json({ error: 'Resposta inválida' }, 400);
  }
  if (typeof answer === 'string' && answer.length > 200) return json({ error: 'Resposta demasiado longa' }, 400);
  const spent = Number.isFinite(body.time_spent_seconds) ? Math.max(0, Math.min(86400, Math.floor(body.time_spent_seconds!))) : null;

  const { data: ex } = await admin.from('exercises')
    .select('id, type, difficulty, competency, status').eq('id', exercise_id).maybeSingle();
  if (!ex) return json({ error: 'Exercício não encontrado' }, 404);
  if (ex.status !== 'published') {
    const { data: isAdmin } = await admin.from('user_roles').select('role')
      .eq('user_id', userId).eq('role', 'admin').maybeSingle();
    if (!isAdmin) return json({ error: 'Exercício não encontrado' }, 404);
  }

  const { data: key } = await admin.from('exercise_answers')
    .select('answer, tolerance, explanation, solution_steps').eq('exercise_id', exercise_id).maybeSingle();
  if (!key) return json({ error: 'Exercício sem resposta configurada' }, 409);

  const verdict = validate(ex.type as ExerciseType, key.answer as Expected, answer, Number(key.tolerance));
  const reveal = { explanation: key.explanation, solution_steps: key.solution_steps };

  // Escrita / problema prático: sem correção automática, mostra a resolução para autocorreção.
  if (!verdict.graded) return json({ graded: false, ...reveal });

  // Idempotência (sincronização offline pode repetir o envio)
  const { data: prior } = await admin.from('attempts').select('is_correct')
    .eq('user_id', userId).eq('client_id', client_id).maybeSingle();
  if (prior) return json({ graded: true, correct: prior.is_correct, duplicate: true, ...reveal });

  const { error: insErr } = await admin.from('attempts').insert({
    user_id: userId, exercise_id, client_id, answer, is_correct: verdict.correct, time_spent_seconds: spent,
  });
  if (insErr) return json({ error: 'Não foi possível guardar a tentativa' }, 500);

  // Recalcula o domínio da competência a partir de todas as tentativas
  const { data: rows } = await admin.from('attempts')
    .select('is_correct, exercises!inner(competency, difficulty)')
    .eq('user_id', userId).eq('exercises.competency', ex.competency);
  const list = (rows ?? []) as unknown as { is_correct: boolean; exercises: { difficulty: number } }[];
  const correct = list.filter((r) => r.is_correct);
  const distinct = new Set(correct.map((r) => r.exercises.difficulty)).size;
  const { data: prev } = await admin.from('mastery').select('assessment_passed')
    .eq('user_id', userId).eq('competency', ex.competency).maybeSingle();
  const assessmentPassed = prev?.assessment_passed ?? false;
  const mastered = isMastered({
    attempts: list.length, correct: correct.length,
    distinctDifficultiesCorrect: distinct, assessmentPassed,
  });
  await admin.from('mastery').upsert({
    user_id: userId, competency: ex.competency, attempts_count: list.length,
    correct_count: correct.length, distinct_difficulties_correct: distinct,
    assessment_passed: assessmentPassed, mastered,
  });

  return json({ graded: true, correct: verdict.correct, mastered, ...reveal });
});

// Modo offline: aulas guardadas e fila de tentativas, no armazenamento local do dispositivo.
import { FunctionsFetchError, FunctionsHttpError } from '@supabase/supabase-js';
import { supabase } from './supabase';

const QUEUE_KEY = 'mm_queue_v1';
const LESSON_PREFIX = 'mm_lesson_v1_';

export interface SubmitPayload {
  exercise_id: string;
  answer: string | number | boolean;
  client_id: string;
  time_spent_seconds?: number;
}
export interface SubmitResult {
  graded: boolean;
  correct?: boolean;
  mastered?: boolean;
  duplicate?: boolean;
  explanation?: string;
  solution_steps?: string[];
}
export type SubmitOutcome =
  | { kind: 'ok'; result: SubmitResult }
  | { kind: 'queued' }
  | { kind: 'error'; message: string };

function readJson<T>(key: string, fallback: T): T {
  try {
    const raw = localStorage.getItem(key);
    return raw ? (JSON.parse(raw) as T) : fallback;
  } catch {
    return fallback;
  }
}
function writeJson(key: string, value: unknown): boolean {
  try {
    localStorage.setItem(key, JSON.stringify(value));
    return true;
  } catch {
    return false; // armazenamento cheio ou bloqueado
  }
}

export function queueSize(): number {
  return readJson<SubmitPayload[]>(QUEUE_KEY, []).length;
}

function enqueue(p: SubmitPayload) {
  const q = readJson<SubmitPayload[]>(QUEUE_KEY, []);
  if (!q.some((x) => x.client_id === p.client_id)) q.push(p);
  writeJson(QUEUE_KEY, q);
}

export async function submitAnswer(p: SubmitPayload): Promise<SubmitOutcome> {
  if (!navigator.onLine) {
    enqueue(p);
    return { kind: 'queued' };
  }
  const { data, error } = await supabase.functions.invoke('validate-answer', { body: p });
  if (!error) return { kind: 'ok', result: data as SubmitResult };
  if (error instanceof FunctionsFetchError) {
    enqueue(p);
    return { kind: 'queued' };
  }
  if (error instanceof FunctionsHttpError) {
    try {
      const body = await error.context.json();
      return { kind: 'error', message: (body as { error?: string }).error ?? 'Erro ao validar' };
    } catch {
      return { kind: 'error', message: 'Erro ao validar' };
    }
  }
  return { kind: 'error', message: 'Erro ao validar' };
}

/** Envia a fila quando a ligação regressa. Erros permanentes (4xx) descartam o item. */
export async function flushQueue(): Promise<number> {
  const q = readJson<SubmitPayload[]>(QUEUE_KEY, []);
  if (q.length === 0 || !navigator.onLine) return 0;
  const keep: SubmitPayload[] = [];
  let sent = 0;
  for (const item of q) {
    const out = await submitAnswer(item);
    if (out.kind === 'ok') sent++;
    else if (out.kind === 'queued') keep.push(item);
    // 'error': resposta definitiva do servidor — descarta
  }
  writeJson(QUEUE_KEY, keep);
  return sent;
}

export function saveLessonOffline(slug: string, bundle: unknown): boolean {
  return writeJson(LESSON_PREFIX + slug, { savedAt: new Date().toISOString(), bundle });
}
export function loadLessonOffline<T>(slug: string): { savedAt: string; bundle: T } | null {
  return readJson<{ savedAt: string; bundle: T } | null>(LESSON_PREFIX + slug, null);
}
export function removeLessonOffline(slug: string) {
  try { localStorage.removeItem(LESSON_PREFIX + slug); } catch { /* ignora */ }
}
export function listSavedLessons(): { slug: string; title: string; savedAt: string }[] {
  const out: { slug: string; title: string; savedAt: string }[] = [];
  try {
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (!k || !k.startsWith(LESSON_PREFIX)) continue;
      const v = readJson<{ savedAt: string; bundle?: { lesson?: { title?: string } } } | null>(k, null);
      if (v) out.push({ slug: k.slice(LESSON_PREFIX.length), title: v.bundle?.lesson?.title ?? k.slice(LESSON_PREFIX.length), savedAt: v.savedAt });
    }
  } catch { /* ignora */ }
  return out;
}

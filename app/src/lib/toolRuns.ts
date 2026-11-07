import { supabase } from './supabase';

export interface ToolRun { id: string; tool: string; label: string; score: number | null; total: number | null; seconds: number | null; created_at: string }

export async function saveRun(tool: string, label: string, score: number | null = null, total: number | null = null, seconds: number | null = null): Promise<string | null> {
  const { error } = await supabase.rpc('record_tool_run', { _tool: tool, _label: label, _score: score, _total: total, _seconds: seconds });
  return error ? 'Não foi possível guardar. Verifica a ligação e tenta outra vez.' : null;
}
export async function listRuns(tool?: string, limit = 15): Promise<ToolRun[]> {
  let q = supabase.from('tool_runs').select('id, tool, label, score, total, seconds, created_at').order('created_at', { ascending: false }).limit(limit);
  if (tool) q = q.eq('tool', tool);
  const { data } = await q;
  return (data ?? []) as ToolRun[];
}
export async function deleteRun(id: string): Promise<void> {
  await supabase.from('tool_runs').delete().eq('id', id);
}

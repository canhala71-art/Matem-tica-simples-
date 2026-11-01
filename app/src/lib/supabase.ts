import { createClient } from '@supabase/supabase-js';

const url = import.meta.env.VITE_SUPABASE_URL as string | undefined;
const key = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY as string | undefined;

/** false quando as variáveis de ambiente não foram definidas (a app mostra um aviso claro). */
export const configured = Boolean(url && key);

export const supabase = createClient(url ?? 'http://localhost:54321', key ?? 'not-configured', {
  auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true },
});

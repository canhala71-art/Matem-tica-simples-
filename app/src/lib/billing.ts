import { useCallback, useEffect, useState } from 'react';
import { supabase } from './supabase';

export interface Access {
  tier: 'free' | 'student' | 'teacher';
  status: 'FREE' | 'TRIAL' | 'ACTIVE' | 'EXPIRED' | 'CANCELLED';
  plan_id: string | null;
  started_at: string | null;
  ends_at: string | null;
  days_left: number;
}
export interface Plan {
  id: string;
  name: string;
  audience: 'student' | 'teacher';
  period: 'monthly' | 'annual';
  price_kz: number;
  days: number;
  active: boolean;
  features: string[];
  sort: number;
}
export interface PayMethod { number: string; holder: string; active: boolean }
export interface PaymentRow {
  id: string;
  user_id: string;
  plan_id: string;
  amount_kz: number;
  method: 'multicaixa' | 'unitel';
  reference: string | null;
  notes: string | null;
  status: 'PENDING' | 'CONFIRMED' | 'REJECTED' | 'CANCELLED';
  admin_note: string | null;
  created_at: string;
  decided_at: string | null;
}

export const kz = (n: number) => `${n.toLocaleString('pt-PT')} Kz`;
export const METHOD_PT = { multicaixa: 'Multicaixa Express', unitel: 'UNITEL Money' } as const;
export const STATUS_PT = { PENDING: 'Pendente', CONFIRMED: 'Confirmado', REJECTED: 'Rejeitado', CANCELLED: 'Cancelado' } as const;
export const SUB_PT = { FREE: 'Free', TRIAL: 'Teste gratuito', ACTIVE: 'Ativo', EXPIRED: 'Expirado', CANCELLED: 'Cancelado' } as const;
export const PERIOD_PT = { monthly: 'Mensal (30 dias)', annual: 'Anual (365 dias)' } as const;
export const TIER_PT = { free: 'Free', student: 'Premium Estudante', teacher: 'Premium Professor' } as const;

export const fmtDate = (iso: string | null) =>
  iso ? new Date(iso).toLocaleDateString('pt-PT', { day: '2-digit', month: 'long', year: 'numeric' }) : '—';
export const fmtDateTime = (iso: string) =>
  new Date(iso).toLocaleString('pt-PT', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' });

/** Link do WhatsApp (indicativo de Angola 244 quando o número é local de 9 dígitos). */
export function whatsappLink(number: string, text: string): string {
  let digits = number.replace(/\D/g, '');
  if (digits.length === 9) digits = `244${digits}`;
  return `https://wa.me/${digits}?text=${encodeURIComponent(text)}`;
}

export async function loadSettings(): Promise<Record<string, Record<string, unknown>>> {
  const { data } = await supabase.from('app_settings').select('key, value');
  const out: Record<string, Record<string, unknown>> = {};
  for (const r of (data ?? []) as { key: string; value: Record<string, unknown> }[]) out[r.key] = r.value;
  return out;
}

export function useAccess() {
  const [access, setAccess] = useState<Access | null>(null);
  const reload = useCallback(async () => {
    const { data } = await supabase.rpc('get_my_access');
    setAccess((data as Access | null) ?? null);
  }, []);
  useEffect(() => { void reload(); }, [reload]);
  return { access, reload };
}

/** Mensagem curta e humana para erros vindos do servidor. */
export function humanError(e: { message?: string } | null | undefined): string {
  const m = e?.message ?? '';
  if (!m) return 'Algo correu mal. Tenta outra vez daqui a pouco.';
  if (m.includes('Failed to fetch') || m.includes('NetworkError')) return 'Sem ligação à internet. Verifica a rede e tenta outra vez.';
  return m;
}

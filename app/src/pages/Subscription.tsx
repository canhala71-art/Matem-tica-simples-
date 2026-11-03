import { useCallback, useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { MessageCircle } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import {
  METHOD_PT, STATUS_PT, SUB_PT, TIER_PT, fmtDate, fmtDateTime, humanError, kz, loadSettings, useAccess, whatsappLink,
  type PaymentRow,
} from '../lib/billing';

interface CodeRow { id: string; code_hint: string; plan_id: string; status: string; issued_at: string; used_at: string | null; expires_at: string }

const CODE_PT: Record<string, string> = { ISSUED: 'Emitido', USED: 'Utilizado', EXPIRED: 'Expirado', REVOKED: 'Revogado' };

export function SubscriptionPage() {
  const { session, profile } = useAuth();
  const { access, reload } = useAccess();
  const [payments, setPayments] = useState<PaymentRow[] | null>(null);
  const [codes, setCodes] = useState<CodeRow[]>([]);
  const [whatsapp, setWhatsapp] = useState('937007567');
  const [note, setNote] = useState<string | null>(null);

  const load = useCallback(async () => {
    const [p, c, s] = await Promise.all([
      supabase.from('payment_requests').select('*').eq('user_id', session?.user.id ?? '').order('created_at', { ascending: false }).limit(30),
      supabase.from('activation_codes').select('id, code_hint, plan_id, status, issued_at, used_at, expires_at').eq('user_id', session?.user.id ?? '').order('issued_at', { ascending: false }).limit(30),
      loadSettings(),
    ]);
    setPayments((p.data ?? []) as PaymentRow[]);
    setCodes((c.data ?? []) as CodeRow[]);
    const n = (s.whatsapp as { number?: string } | undefined)?.number;
    if (n) setWhatsapp(n);
  }, [session]);
  useEffect(() => { void load(); }, [load]);

  async function cancel(id: string) {
    const { error } = await supabase.rpc('cancel_payment_request', { _id: id });
    setNote(error ? humanError(error) : 'Pedido cancelado.');
    await load();
    await reload();
  }

  const planName = (id: string) => (id.startsWith('teacher') ? TIER_PT.teacher : TIER_PT.student) + (id.endsWith('annual') ? ' (anual)' : ' (mensal)');

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Minha assinatura</h1>

      <section className="card space-y-2">
        {!access ? <p className="muted">A carregar…</p> : (
          <>
            <p className="text-lg font-semibold">{TIER_PT[access.tier]} <span className="badge ml-1">{SUB_PT[access.status]}</span></p>
            {(access.status === 'ACTIVE' || access.status === 'TRIAL') ? (
              <p className="text-sm">Começou em {fmtDate(access.started_at)} e vai até {fmtDate(access.ends_at)}. Restam <strong>{access.days_left}</strong> dias.</p>
            ) : access.status === 'EXPIRED' ? (
              <p className="text-sm">O teu plano terminou em {fmtDate(access.ends_at)}. A conta continua ativa no plano Free e todo o teu histórico está guardado.</p>
            ) : (
              <p className="text-sm">Estás no plano Free. Podes experimentar o Premium ou escolher um plano quando quiseres.</p>
            )}
            <div className="flex flex-wrap gap-2 pt-1">
              <Link to="/planos" className="btn">{access.status === 'ACTIVE' ? 'Renovar' : 'Ver planos'}</Link>
              <Link to="/ativar" className="btn-ghost">Tenho um código</Link>
            </div>
          </>
        )}
      </section>

      {note && <p role="status" className="text-sm text-emerald-600">{note}</p>}

      <section className="card space-y-2">
        <h2 className="font-semibold">Histórico de pagamentos</h2>
        {payments === null && <p className="muted">A carregar…</p>}
        {payments?.length === 0 && <p className="muted">Ainda não fizeste nenhum pedido.</p>}
        <ul className="divide-y divide-slate-200 dark:divide-navy-800">
          {payments?.map((p) => (
            <li key={p.id} className="space-y-1 py-3 text-sm">
              <p><strong>{planName(p.plan_id)}</strong> · {kz(p.amount_kz)} · {METHOD_PT[p.method]}</p>
              <p className="muted">{fmtDateTime(p.created_at)} · {STATUS_PT[p.status]}{p.reference ? ` · Ref. ${p.reference}` : ''}</p>
              {p.admin_note && <p className="muted">Nota: {p.admin_note}</p>}
              {p.status === 'PENDING' && (
                <div className="flex flex-wrap gap-2 pt-1">
                  <a className="btn-ghost !py-1.5" target="_blank" rel="noreferrer"
                    href={whatsappLink(whatsapp, `Olá! Envio o comprovativo do meu pedido.\nNome: ${profile?.display_name ?? ''}\nConta: ${session?.user.email ?? ''}\nPlano: ${planName(p.plan_id)}\nValor: ${kz(p.amount_kz)}\nMétodo: ${METHOD_PT[p.method]}${p.reference ? `\nReferência: ${p.reference}` : ''}`)}>
                    <MessageCircle size={14} /> Enviar comprovativo
                  </a>
                  <button className="btn-ghost !py-1.5" onClick={() => void cancel(p.id)}>Cancelar pedido</button>
                </div>
              )}
            </li>
          ))}
        </ul>
      </section>

      <section className="card space-y-2">
        <h2 className="font-semibold">Histórico de ativações</h2>
        {codes.length === 0 && <p className="muted">Ainda não tens códigos.</p>}
        <ul className="divide-y divide-slate-200 dark:divide-navy-800">
          {codes.map((c) => (
            <li key={c.id} className="py-2 text-sm">
              Código terminado em <span className="font-mono">{c.code_hint}</span> · {planName(c.plan_id)} · {CODE_PT[c.status] ?? c.status}
              <span className="muted"> · emitido a {fmtDate(c.issued_at)}{c.used_at ? `, usado a ${fmtDate(c.used_at)}` : ''}</span>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

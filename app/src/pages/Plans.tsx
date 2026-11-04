import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Check, MessageCircle, Sparkles } from 'lucide-react';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import {
  METHOD_PT, PERIOD_PT, fmtDate, humanError, kz, loadSettings, useAccess, whatsappLink,
  type PayMethod, type Plan,
} from '../lib/billing';

interface Created { id: string; amount_kz: number; plan: string; period: 'monthly' | 'annual'; method: 'multicaixa' | 'unitel' }

export function PlansPage() {
  const { session, profile } = useAuth();
  const { access, reload } = useAccess();
  const [plans, setPlans] = useState<Plan[] | null>(null);
  const [settings, setSettings] = useState<Record<string, Record<string, unknown>>>({});
  const [trialUsed, setTrialUsed] = useState(false);
  const [chosen, setChosen] = useState<Plan | null>(null);
  const [method, setMethod] = useState<'multicaixa' | 'unitel' | ''>('');
  const [reference, setReference] = useState('');
  const [notes, setNotes] = useState('');
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<{ ok: boolean; text: string } | null>(null);
  const [created, setCreated] = useState<Created | null>(null);

  useEffect(() => {
    void (async () => {
      const [p, s, t] = await Promise.all([
        supabase.from('plans').select('*').eq('active', true).order('sort'),
        loadSettings(),
        supabase.from('trials').select('user_id').eq('user_id', session?.user.id ?? '').maybeSingle(),
      ]);
      setPlans((p.data ?? []) as Plan[]);
      setSettings(s);
      setTrialUsed(Boolean(t.data));
    })();
  }, [session]);

  const whatsapp = String((settings.whatsapp as { number?: string } | undefined)?.number ?? '937007567');
  const methods = (['multicaixa', 'unitel'] as const).filter((m) => {
    const c = settings[`pay_${m}`] as unknown as PayMethod | undefined;
    return c && c.active && c.number;
  });
  const trial = settings.trial as { enabled?: boolean; days?: number } | undefined;
  const canTrial = Boolean(trial?.enabled) && !trialUsed && access?.status !== 'ACTIVE' && access?.status !== 'TRIAL';
  const cfg = (m: 'multicaixa' | 'unitel') => settings[`pay_${m}`] as unknown as PayMethod;

  async function startTrial() {
    setBusy(true); setMsg(null);
    const { error } = await supabase.rpc('start_trial');
    setBusy(false);
    if (error) { setMsg({ ok: false, text: humanError(error) }); return; }
    setTrialUsed(true);
    setMsg({ ok: true, text: `Teste gratuito ativo por ${trial?.days ?? 7} dias. Bons estudos!` });
    await reload();
  }

  async function request() {
    if (!chosen || !method) return;
    setBusy(true); setMsg(null);
    const { data, error } = await supabase.rpc('create_payment_request', {
      _plan_id: chosen.id, _method: method, _reference: reference, _notes: notes,
    });
    setBusy(false);
    if (error) { setMsg({ ok: false, text: humanError(error) }); return; }
    setCreated(data as Created);
  }

  function waText(c: Created): string {
    return [
      'Olá! Fiz o pagamento do MenteMat e envio o comprovativo.',
      `Nome: ${profile?.display_name ?? ''}`,
      `Conta: ${session?.user.email ?? ''}`,
      `Plano: ${c.plan} — ${PERIOD_PT[c.period]}`,
      `Valor: ${kz(c.amount_kz)}`,
      `Método: ${METHOD_PT[c.method]}`,
      reference ? `Referência: ${reference}` : '',
    ].filter(Boolean).join('\n');
  }

  const groups: { title: string; list: Plan[] }[] = [
    { title: 'Para estudantes', list: (plans ?? []).filter((p) => p.audience === 'student') },
    { title: 'Para professores', list: (plans ?? []).filter((p) => p.audience === 'teacher') },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold">Escolhe o plano que cabe no teu estudo</h1>
        <p className="muted">Sem cartão, sem cobranças automáticas. Pagas por Multicaixa Express ou UNITEL Money e nós ativamos o teu plano com um código.</p>
      </div>

      {access && access.status === 'ACTIVE' && (
        <p className="card text-sm">Já tens o plano ativo até {fmtDate(access.ends_at)} ({access.days_left} dias). Podes renovar antes de acabar: os dias somam-se.</p>
      )}

      <section className="card space-y-2">
        <h2 className="font-semibold">Free — 0 Kz</h2>
        <p className="muted">Perfil, calculadora, biblioteca básica, exercícios gratuitos com correção automática, quizzes com limite diário e histórico limitado.</p>
        {canTrial && (
          <button className="btn" disabled={busy} onClick={() => void startTrial()}>
            <Sparkles size={16} /> Experimentar Premium {trial?.days ?? 7} dias, grátis
          </button>
        )}
        {trialUsed && <p className="muted">Já usaste o teu teste gratuito.</p>}
      </section>

      {plans === null && <p className="muted">A carregar planos…</p>}
      {groups.map((g) => g.list.length > 0 && (
        <section key={g.title} className="space-y-3">
          <h2 className="font-semibold">{g.title}</h2>
          <div className="grid gap-3 sm:grid-cols-2">
            {g.list.map((p) => (
              <div key={p.id} className={`card space-y-3 ${chosen?.id === p.id ? 'ring-2 ring-electric-500' : ''}`}>
                <div>
                  <p className="font-semibold">{p.name}</p>
                  <p className="text-2xl font-bold">{kz(p.price_kz)} <span className="muted">/ {p.period === 'monthly' ? '30 dias' : '365 dias'}</span></p>
                  {p.period === 'annual' && <p className="muted">Pagas uma vez e estudas o ano inteiro.</p>}
                </div>
                <ul className="space-y-1 text-sm">
                  {p.features.map((f) => <li key={f} className="flex gap-2"><Check size={16} className="mt-0.5 shrink-0 text-emerald-500" />{f}</li>)}
                </ul>
                <button className="btn w-full" onClick={() => { setChosen(p); setCreated(null); setMsg(null); setMethod(methods[0] ?? ''); }}>Escolher</button>
              </div>
            ))}
          </div>
        </section>
      ))}

      {chosen && !created && (
        <section className="card space-y-4" aria-live="polite">
          <h2 className="font-semibold">Pagamento: {chosen.name} ({PERIOD_PT[chosen.period]})</h2>
          <p>Valor a pagar: <strong>{kz(chosen.price_kz)}</strong></p>
          {methods.length === 0 ? (
            <div className="space-y-3">
              <p className="muted">Os métodos de pagamento ainda estão a ser configurados. Fala connosco pelo WhatsApp e indicamos como pagar.</p>
              <a className="btn" target="_blank" rel="noreferrer"
                href={whatsappLink(whatsapp, `Olá! Quero o plano ${chosen.name} (${PERIOD_PT[chosen.period]}). Conta: ${session?.user.email ?? ''}`)}>
                <MessageCircle size={16} /> Falar no WhatsApp
              </a>
            </div>
          ) : (
            <>
              <div className="grid gap-2 sm:grid-cols-2">
                {methods.map((m) => (
                  <label key={m} className={`card flex cursor-pointer items-start gap-2 ${method === m ? 'ring-2 ring-electric-500' : ''}`}>
                    <input type="radio" name="method" checked={method === m} onChange={() => setMethod(m)} className="mt-1" />
                    <span className="text-sm"><strong>{METHOD_PT[m]}</strong><br />
                      Número: {cfg(m).number}<br />Titular: {cfg(m).holder}</span>
                  </label>
                ))}
              </div>
              <ol className="list-decimal space-y-1 pl-5 text-sm">
                <li>Transfere exatamente <strong>{kz(chosen.price_kz)}</strong> para o número acima.</li>
                <li>Guarda o comprovativo (captura ou referência).</li>
                <li>Carrega em "Já paguei" para registar o pedido e envia o comprovativo pelo WhatsApp.</li>
                <li>Quando confirmarmos o dinheiro na conta, recebes um código para ativar o plano.</li>
              </ol>
              <input className="input" placeholder="Referência da transação (opcional)" value={reference} maxLength={80}
                onChange={(e) => setReference(e.target.value)} />
              <input className="input" placeholder="Observações (opcional)" value={notes} maxLength={300}
                onChange={(e) => setNotes(e.target.value)} />
              <button className="btn" disabled={busy || !method || !session} onClick={() => void request()}>Já paguei, registar pedido</button>
            </>
          )}
          {msg && <p role="status" className={msg.ok ? 'text-emerald-600' : 'text-red-600'}>{msg.text}</p>}
        </section>
      )}

      {created && (
        <section className="card space-y-3" aria-live="polite">
          <h2 className="font-semibold">Pedido registado. Falta só o comprovativo.</h2>
          <p className="text-sm">O teu plano <strong>ainda não está ativo</strong>. Envia o comprovativo pelo WhatsApp e aguarda a nossa confirmação do pagamento; só depois recebes o código de ativação.</p>
          <a className="btn" target="_blank" rel="noreferrer" href={whatsappLink(whatsapp, waText(created))}>
            <MessageCircle size={16} /> Enviar comprovativo no WhatsApp
          </a>
          <p className="muted">Acompanha o estado em <Link className="text-electric-500" to="/assinatura">Minha assinatura</Link>. Quando tiveres o código, ativa-o em <Link className="text-electric-500" to="/ativar">Activar o meu Premium</Link>.</p>
        </section>
      )}
      {!chosen && msg && <p role="status" className={msg.ok ? 'text-emerald-600' : 'text-red-600'}>{msg.text}</p>}
    </div>
  );
}

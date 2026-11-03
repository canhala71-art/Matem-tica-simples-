import { useCallback, useEffect, useState, type FormEvent } from 'react';
import { Copy } from 'lucide-react';
import { supabase } from '../lib/supabase';
import {
  METHOD_PT, STATUS_PT, TIER_PT, fmtDate, fmtDateTime, humanError, kz, loadSettings,
  type PaymentRow, type Plan,
} from '../lib/billing';
import { CATEGORIES, DIFFICULTIES, catName, diffName } from '../lib/quiz';

type Note = { ok: boolean; text: string } | null;
function Msg({ n }: { n: Note }) {
  return n ? <p role="status" className={`text-sm ${n.ok ? 'text-emerald-600' : 'text-red-600'}`}>{n.text}</p> : null;
}

// ---------- Visão geral ----------
export function OverviewTab() {
  const [s, setS] = useState<Record<string, number> | null>(null);
  const [err, setErr] = useState<string | null>(null);
  useEffect(() => {
    void supabase.rpc('admin_stats').then(({ data, error }) => {
      if (error) setErr(humanError(error)); else setS(data as Record<string, number>);
    });
  }, []);
  if (err) return <p role="alert" className="text-red-600">{err}</p>;
  if (!s) return <p className="muted">A carregar…</p>;
  const items: [string, string][] = [
    ['Utilizadores', String(s.utilizadores)], ['Gratuitos', String(s.gratuitos)], ['Premium ativos', String(s.premium_ativos)],
    ['Professores Premium', String(s.professores)], ['Assinaturas expiradas', String(s.assinaturas_expiradas)],
    ['Testes gratuitos ativos', String(s.testes_ativos)], ['Pagamentos pendentes', String(s.pagamentos_pendentes)],
    ['Pagamentos confirmados', String(s.pagamentos_confirmados)], ['Receita confirmada', kz(s.receita_confirmada_kz)],
    ['Quizzes realizados', String(s.quizzes_realizados)],
  ];
  return (
    <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
      {items.map(([l, v]) => <div key={l} className="card"><p className="text-xl font-bold">{v}</p><p className="muted">{l}</p></div>)}
    </div>
  );
}

// ---------- Pagamentos ----------
interface PayView extends PaymentRow { name: string; email: string }

export function PaymentsTab() {
  const [rows, setRows] = useState<PayView[] | null>(null);
  const [filter, setFilter] = useState<'ALL' | PaymentRow['status']>('PENDING');
  const [note, setNote] = useState<Note>(null);
  const [issued, setIssued] = useState<{ code: string; who: string } | null>(null);
  const [admNote, setAdmNote] = useState<Record<string, string>>({});
  const [open, setOpen] = useState<string | null>(null);
  const [withCode, setWithCode] = useState<Set<string>>(new Set());

  const load = useCallback(async () => {
    const { data } = await supabase.from('payment_requests').select('*').order('created_at', { ascending: false }).limit(200);
    const pays = (data ?? []) as PaymentRow[];
    const ids = [...new Set(pays.map((p) => p.user_id))];
    const [prof, mails, codes] = await Promise.all([
      supabase.from('profiles').select('id, display_name').in('id', ids),
      supabase.rpc('admin_user_emails', { _ids: ids }),
      supabase.from('activation_codes').select('payment_request_id, status'),
    ]);
    const names = new Map(((prof.data ?? []) as { id: string; display_name: string }[]).map((p) => [p.id, p.display_name]));
    const emails = new Map(((mails.data ?? []) as { id: string; email: string }[]).map((p) => [p.id, p.email]));
    setWithCode(new Set(((codes.data ?? []) as { payment_request_id: string; status: string }[])
      .filter((c) => c.status === 'ISSUED' || c.status === 'USED').map((c) => c.payment_request_id)));
    setRows(pays.map((p) => ({ ...p, name: names.get(p.user_id) ?? '—', email: emails.get(p.user_id) ?? '—' })));
  }, []);
  useEffect(() => { void load(); }, [load]);

  async function decide(p: PayView, decision: PaymentRow['status']) {
    if (decision === 'CONFIRMED' && !window.confirm(
      `Confirmas que o dinheiro (${kz(p.amount_kz)}) já entrou mesmo na conta ${METHOD_PT[p.method]}? Uma captura de ecrã não chega.`)) return;
    const { error } = await supabase.rpc('admin_decide_payment', { _id: p.id, _decision: decision, _note: admNote[p.id] ?? '' });
    setNote(error ? { ok: false, text: humanError(error) } : { ok: true, text: `Pedido marcado como ${STATUS_PT[decision].toLowerCase()}.` });
    await load();
  }
  async function issue(p: PayView) {
    const { data, error } = await supabase.rpc('admin_issue_code', { _payment_id: p.id });
    if (error) { setNote({ ok: false, text: humanError(error) }); return; }
    setIssued({ code: (data as { code: string }).code, who: p.name });
    setNote(null);
    await load();
  }

  const shown = (rows ?? []).filter((r) => filter === 'ALL' || r.status === filter);
  const msgText = issued
    ? `Olá ${issued.who}! O teu pagamento foi confirmado. 🎉\nO teu código de ativação é:\n${issued.code}\nEntra no MenteMat, abre "Ativar Premium" e introduz o código. Só funciona na tua conta e uma única vez.`
    : '';

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap gap-2">
        {(['PENDING', 'CONFIRMED', 'REJECTED', 'CANCELLED', 'ALL'] as const).map((f) => (
          <button key={f} className={filter === f ? 'btn' : 'btn-ghost'} onClick={() => setFilter(f)}>{f === 'ALL' ? 'Todos' : STATUS_PT[f]}</button>
        ))}
      </div>
      <Msg n={note} />
      {issued && (
        <div className="card space-y-2 border-emerald-500">
          <p className="font-semibold">Código gerado. Copia-o agora: por segurança não volta a ser mostrado.</p>
          <p className="break-all rounded-lg bg-slate-100 p-3 font-mono text-lg dark:bg-navy-800">{issued.code}</p>
          <div className="flex flex-wrap gap-2">
            <button className="btn" onClick={() => void navigator.clipboard.writeText(issued.code)}><Copy size={14} /> Copiar código</button>
            <button className="btn-ghost" onClick={() => void navigator.clipboard.writeText(msgText)}><Copy size={14} /> Copiar mensagem para o WhatsApp</button>
            <button className="btn-ghost" onClick={() => setIssued(null)}>Já copiei</button>
          </div>
        </div>
      )}
      {rows === null && <p className="muted">A carregar…</p>}
      {rows && shown.length === 0 && <p className="card muted">Sem pedidos neste estado.</p>}
      {shown.map((p) => (
        <div key={p.id} className="card space-y-2 text-sm">
          <div className="flex flex-wrap items-center justify-between gap-2">
            <p><strong>{p.name}</strong> <span className="muted">· {p.email}</span></p>
            <span className="badge">{STATUS_PT[p.status]}</span>
          </div>
          <p>{p.plan_id.startsWith('teacher') ? TIER_PT.teacher : TIER_PT.student} ({p.plan_id.endsWith('annual') ? 'anual' : 'mensal'}) · <strong>{kz(p.amount_kz)}</strong> · {METHOD_PT[p.method]}</p>
          <p className="muted">{fmtDateTime(p.created_at)}{p.reference ? ` · Ref. ${p.reference}` : ''}</p>
          {open === p.id && (
            <div className="space-y-1">
              {p.notes && <p>Observações do cliente: {p.notes}</p>}
              {p.admin_note && <p>Nota interna: {p.admin_note}</p>}
              {p.decided_at && <p className="muted">Decidido em {fmtDateTime(p.decided_at)}</p>}
            </div>
          )}
          <input className="input" placeholder="Nota interna (opcional)" value={admNote[p.id] ?? ''}
            onChange={(e) => setAdmNote({ ...admNote, [p.id]: e.target.value })} />
          <div className="flex flex-wrap gap-2">
            <button className="btn-ghost !py-1.5" onClick={() => setOpen(open === p.id ? null : p.id)}>{open === p.id ? 'Fechar detalhes' : 'Detalhes'}</button>
            {p.status !== 'CONFIRMED' && <button className="btn !py-1.5" onClick={() => void decide(p, 'CONFIRMED')}>Confirmar pagamento</button>}
            {p.status !== 'REJECTED' && p.status !== 'CONFIRMED' && <button className="btn-ghost !py-1.5" onClick={() => void decide(p, 'REJECTED')}>Rejeitar</button>}
            {p.status !== 'PENDING' && p.status !== 'CONFIRMED' && <button className="btn-ghost !py-1.5" onClick={() => void decide(p, 'PENDING')}>Manter pendente</button>}
            {p.status === 'CONFIRMED' && !withCode.has(p.id) && <button className="btn !py-1.5" onClick={() => void issue(p)}>Gerar código</button>}
            {p.status === 'CONFIRMED' && withCode.has(p.id) && <span className="muted self-center">Código já emitido</span>}
          </div>
        </div>
      ))}
    </div>
  );
}

// ---------- Códigos ----------
interface CodeView { id: string; code_hint: string; user_id: string; plan_id: string; status: string; issued_at: string; expires_at: string; used_at: string | null; name: string }
const CODE_PT: Record<string, string> = { ISSUED: 'Emitido', USED: 'Utilizado', EXPIRED: 'Expirado', REVOKED: 'Revogado' };

export function CodesTab() {
  const [rows, setRows] = useState<CodeView[] | null>(null);
  const [q, setQ] = useState('');
  const [note, setNote] = useState<Note>(null);
  const load = useCallback(async () => {
    const { data } = await supabase.from('activation_codes')
      .select('id, code_hint, user_id, plan_id, status, issued_at, expires_at, used_at').order('issued_at', { ascending: false }).limit(200);
    const list = (data ?? []) as Omit<CodeView, 'name'>[];
    const { data: prof } = await supabase.from('profiles').select('id, display_name').in('id', [...new Set(list.map((c) => c.user_id))]);
    const names = new Map(((prof ?? []) as { id: string; display_name: string }[]).map((p) => [p.id, p.display_name]));
    setRows(list.map((c) => ({ ...c, name: names.get(c.user_id) ?? '—' })));
  }, []);
  useEffect(() => { void load(); }, [load]);

  async function revoke(id: string) {
    if (!window.confirm('Revogar este código? O cliente deixa de o poder usar.')) return;
    const { error } = await supabase.rpc('admin_revoke_code', { _id: id });
    setNote(error ? { ok: false, text: humanError(error) } : { ok: true, text: 'Código revogado.' });
    await load();
  }
  const shown = (rows ?? []).filter((r) => !q || `${r.name} ${r.code_hint} ${r.plan_id}`.toLowerCase().includes(q.toLowerCase()));
  return (
    <div className="space-y-3">
      <input className="input" placeholder="Pesquisar por cliente, plano ou final do código" value={q} onChange={(e) => setQ(e.target.value)} />
      <p className="muted">Por segurança só se guarda o hash do código; aqui vês apenas os 4 últimos caracteres.</p>
      <Msg n={note} />
      {rows === null && <p className="muted">A carregar…</p>}
      {rows && shown.length === 0 && <p className="card muted">Sem códigos.</p>}
      {shown.map((c) => (
        <div key={c.id} className="card flex flex-wrap items-center justify-between gap-2 text-sm">
          <div>
            <p><strong>{c.name}</strong> · …<span className="font-mono">{c.code_hint}</span> · {c.plan_id}</p>
            <p className="muted">{CODE_PT[c.status]} · emitido {fmtDate(c.issued_at)} · válido até {fmtDate(c.expires_at)}{c.used_at ? ` · usado ${fmtDate(c.used_at)}` : ''}</p>
          </div>
          {c.status === 'ISSUED' && <button className="btn-ghost !py-1.5" onClick={() => void revoke(c.id)}>Revogar</button>}
        </div>
      ))}
    </div>
  );
}

// ---------- Planos ----------
export function PlansAdminTab() {
  const [plans, setPlans] = useState<Plan[] | null>(null);
  const [note, setNote] = useState<Note>(null);
  const [edit, setEdit] = useState<Record<string, { price: string; active: boolean }>>({});
  const load = useCallback(async () => {
    const { data } = await supabase.from('plans').select('*').order('sort');
    const list = (data ?? []) as Plan[];
    setPlans(list);
    setEdit(Object.fromEntries(list.map((p) => [p.id, { price: String(p.price_kz), active: p.active }])));
  }, []);
  useEffect(() => { void load(); }, [load]);
  async function save(p: Plan) {
    const e = edit[p.id];
    const price = Number(e.price);
    if (!Number.isInteger(price) || price < 0) { setNote({ ok: false, text: 'O preço tem de ser um número inteiro (Kz).' }); return; }
    const { error } = await supabase.from('plans').update({ price_kz: price, active: e.active }).eq('id', p.id);
    setNote(error ? { ok: false, text: humanError(error) } : { ok: true, text: `Plano guardado: ${p.name}.` });
    await load();
  }
  return (
    <div className="space-y-3">
      <p className="muted">As alterações de preço ficam registadas na auditoria. Os pedidos já feitos mantêm o valor com que foram criados.</p>
      <Msg n={note} />
      {plans?.map((p) => (
        <div key={p.id} className="card flex flex-wrap items-center gap-3 text-sm">
          <span className="min-w-40 flex-1 font-medium">{p.name} · {p.period === 'monthly' ? 'mensal' : 'anual'}</span>
          <label className="flex items-center gap-1">Preço (Kz)
            <input className="input !w-28" inputMode="numeric" value={edit[p.id]?.price ?? ''}
              onChange={(ev) => setEdit({ ...edit, [p.id]: { ...edit[p.id], price: ev.target.value } })} />
          </label>
          <label className="flex items-center gap-1"><input type="checkbox" checked={edit[p.id]?.active ?? false}
            onChange={(ev) => setEdit({ ...edit, [p.id]: { ...edit[p.id], active: ev.target.checked } })} /> Ativo</label>
          <button className="btn !py-1.5" onClick={() => void save(p)}>Guardar</button>
        </div>
      ))}
    </div>
  );
}

// ---------- Configurações ----------
export function SettingsTab() {
  const [s, setS] = useState<Record<string, Record<string, unknown>> | null>(null);
  const [note, setNote] = useState<Note>(null);
  useEffect(() => { void loadSettings().then(setS); }, []);
  if (!s) return <p className="muted">A carregar…</p>;
  const get = (k: string, f: string, d: string | boolean | number = '') => (s[k]?.[f] as string | boolean | number | undefined) ?? d;
  const set = (k: string, f: string, v: string | boolean | number) => setS({ ...s, [k]: { ...s[k], [f]: v } });

  async function save(e: FormEvent) {
    e.preventDefault();
    const days = Number(get('trial', 'days', 7));
    const validity = Number(get('code_validity_days', 'days', 30));
    const limit = Number(get('free_quiz', 'daily_limit', 3));
    if (![days, validity, limit].every((n) => Number.isInteger(n) && n >= 0)) { setNote({ ok: false, text: 'Dias e limites têm de ser números inteiros.' }); return; }
    for (const m of ['pay_multicaixa', 'pay_unitel']) {
      if (get(m, 'active', false) && (!String(get(m, 'number')).trim() || !String(get(m, 'holder')).trim())) {
        setNote({ ok: false, text: 'Para ativar um método de pagamento preenche o número e o nome do titular.' }); return;
      }
    }
    const rows = Object.entries({
      whatsapp: { number: String(get('whatsapp', 'number')).replace(/\s/g, '') },
      pay_multicaixa: { number: String(get('pay_multicaixa', 'number')).trim(), holder: String(get('pay_multicaixa', 'holder')).trim(), active: Boolean(get('pay_multicaixa', 'active', false)) },
      pay_unitel: { number: String(get('pay_unitel', 'number')).trim(), holder: String(get('pay_unitel', 'holder')).trim(), active: Boolean(get('pay_unitel', 'active', false)) },
      trial: { enabled: Boolean(get('trial', 'enabled', true)), days },
      code_validity_days: { days: validity },
      free_quiz: { daily_limit: limit, difficulties: (s.free_quiz?.difficulties as string[] | undefined) ?? ['facil', 'intermedio'] },
      support: { text: String(get('support', 'text')) },
    });
    for (const [key, value] of rows) {
      const { error } = await supabase.from('app_settings').update({ value, updated_at: new Date().toISOString() }).eq('key', key);
      if (error) { setNote({ ok: false, text: humanError(error) }); return; }
    }
    setNote({ ok: true, text: 'Configurações guardadas.' });
  }

  const method = (k: 'pay_multicaixa' | 'pay_unitel', title: string) => (
    <fieldset className="space-y-2 rounded-xl border border-slate-200 p-3 dark:border-navy-700">
      <legend className="px-1 font-medium">{title}</legend>
      <input className="input" placeholder="Número de recebimento" value={String(get(k, 'number'))} onChange={(e) => set(k, 'number', e.target.value)} />
      <input className="input" placeholder="Nome do titular" value={String(get(k, 'holder'))} onChange={(e) => set(k, 'holder', e.target.value)} />
      <label className="flex items-center gap-2 text-sm"><input type="checkbox" checked={Boolean(get(k, 'active', false))} onChange={(e) => set(k, 'active', e.target.checked)} />
        Ativo (só ativa depois de confirmares que este número recebe por este serviço)</label>
    </fieldset>
  );

  return (
    <form onSubmit={(e) => void save(e)} className="card space-y-4 text-sm">
      <label className="block space-y-1"><span className="font-medium">WhatsApp de suporte e comprovativos</span>
        <input className="input" value={String(get('whatsapp', 'number'))} onChange={(e) => set('whatsapp', 'number', e.target.value)} /></label>
      {method('pay_multicaixa', 'Multicaixa Express')}
      {method('pay_unitel', 'UNITEL Money')}
      <fieldset className="space-y-2 rounded-xl border border-slate-200 p-3 dark:border-navy-700">
        <legend className="px-1 font-medium">Teste gratuito</legend>
        <label className="flex items-center gap-2"><input type="checkbox" checked={Boolean(get('trial', 'enabled', true))} onChange={(e) => set('trial', 'enabled', e.target.checked)} /> Ativo</label>
        <label className="flex items-center gap-2">Dias <input className="input !w-24" inputMode="numeric" value={String(get('trial', 'days', 7))} onChange={(e) => set('trial', 'days', e.target.value)} /></label>
      </fieldset>
      <label className="flex items-center gap-2">Validade dos códigos (dias)
        <input className="input !w-24" inputMode="numeric" value={String(get('code_validity_days', 'days', 30))} onChange={(e) => set('code_validity_days', 'days', e.target.value)} /></label>
      <label className="flex items-center gap-2">Quizzes grátis por dia
        <input className="input !w-24" inputMode="numeric" value={String(get('free_quiz', 'daily_limit', 3))} onChange={(e) => set('free_quiz', 'daily_limit', e.target.value)} /></label>
      <label className="block space-y-1"><span className="font-medium">Texto de suporte</span>
        <input className="input" value={String(get('support', 'text'))} onChange={(e) => set('support', 'text', e.target.value)} /></label>
      <Msg n={note} />
      <button className="btn">Guardar configurações</button>
    </form>
  );
}

// ---------- Quizzes ----------
interface QRow { id: string; category: string; difficulty: string; statement: string; status: string }

export function QuizAdminTab() {
  const [rows, setRows] = useState<QRow[] | null>(null);
  const [note, setNote] = useState<Note>(null);
  const [f, setF] = useState({ category: 'aritmetica', difficulty: 'facil', statement: '', o: ['', '', '', ''], correct: 0, explanation: '' });
  const load = useCallback(async () => {
    const { data } = await supabase.from('quiz_questions').select('id, category, difficulty, statement, status').order('created_at', { ascending: false }).limit(200);
    setRows((data ?? []) as QRow[]);
  }, []);
  useEffect(() => { void load(); }, [load]);

  async function setStatus(id: string, status: string) {
    const { error } = await supabase.from('quiz_questions').update({ status }).eq('id', id);
    setNote(error ? { ok: false, text: humanError(error) } : { ok: true, text: 'Estado atualizado.' });
    await load();
  }
  async function publishAll() {
    if (!window.confirm('Publicar todas as perguntas em rascunho? Confirma que já as reviste.')) return;
    const { error } = await supabase.from('quiz_questions').update({ status: 'published' }).eq('status', 'draft');
    setNote(error ? { ok: false, text: humanError(error) } : { ok: true, text: 'Perguntas publicadas.' });
    await load();
  }
  async function create(e: FormEvent) {
    e.preventDefault();
    const opts = f.o.map((x) => x.trim());
    if (!f.statement.trim() || opts.some((x) => !x) || !f.explanation.trim()) { setNote({ ok: false, text: 'Preenche o enunciado, as 4 alternativas e a explicação.' }); return; }
    if (new Set(opts.map((x) => x.toLowerCase())).size !== 4) { setNote({ ok: false, text: 'As alternativas não podem ser repetidas.' }); return; }
    const { data, error } = await supabase.from('quiz_questions').insert({
      category: f.category, difficulty: f.difficulty, statement: f.statement.trim(), options: opts, explanation: f.explanation.trim(), status: 'draft',
    }).select('id').single();
    if (error || !data) { setNote({ ok: false, text: humanError(error) }); return; }
    const a = await supabase.from('quiz_answers').insert({ question_id: data.id as string, correct_index: f.correct });
    setNote(a.error ? { ok: false, text: humanError(a.error) } : { ok: true, text: 'Pergunta criada em rascunho. Revê e publica.' });
    setF({ ...f, statement: '', o: ['', '', '', ''], explanation: '' });
    await load();
  }

  return (
    <div className="space-y-4">
      <Msg n={note} />
      <form onSubmit={(e) => void create(e)} className="card space-y-2 text-sm">
        <h2 className="font-semibold">Nova pergunta</h2>
        <div className="grid gap-2 sm:grid-cols-2">
          <select className="input" value={f.category} onChange={(e) => setF({ ...f, category: e.target.value })}>{CATEGORIES.map(([v, l]) => <option key={v} value={v}>{l}</option>)}</select>
          <select className="input" value={f.difficulty} onChange={(e) => setF({ ...f, difficulty: e.target.value })}>{DIFFICULTIES.map(([v, l]) => <option key={v} value={v}>{l}</option>)}</select>
        </div>
        <textarea className="input" rows={2} placeholder="Enunciado (podes usar fórmulas entre $...$)" value={f.statement} onChange={(e) => setF({ ...f, statement: e.target.value })} />
        {f.o.map((o, i) => (
          <label key={i} className="flex items-center gap-2">
            <input type="radio" name="correct" checked={f.correct === i} onChange={() => setF({ ...f, correct: i })} aria-label={`Alternativa ${i + 1} é a correta`} />
            <input className="input" placeholder={`Alternativa ${String.fromCharCode(65 + i)}`} value={o} onChange={(e) => setF({ ...f, o: f.o.map((x, j) => (j === i ? e.target.value : x)) })} />
          </label>
        ))}
        <textarea className="input" rows={2} placeholder="Explicação (tem de corresponder à resposta certa)" value={f.explanation} onChange={(e) => setF({ ...f, explanation: e.target.value })} />
        <button className="btn">Guardar em rascunho</button>
      </form>
      <div className="flex items-center justify-between">
        <h2 className="font-semibold">Perguntas ({rows?.length ?? 0})</h2>
        <button className="btn-ghost" onClick={() => void publishAll()}>Publicar todos os rascunhos</button>
      </div>
      {rows?.map((r) => (
        <div key={r.id} className="card flex items-center justify-between gap-3 text-sm">
          <span className="min-w-0 flex-1"><span className="muted">{catName(r.category)} · {diffName(r.difficulty)}</span><br />{r.statement.slice(0, 110)}</span>
          <select className="input !w-auto" value={r.status} onChange={(e) => void setStatus(r.id, e.target.value)} aria-label="Estado da pergunta">
            <option value="draft">Rascunho</option><option value="published">Publicada</option><option value="archived">Arquivada</option>
          </select>
        </div>
      ))}
    </div>
  );
}

// ---------- Auditoria ----------
interface AuditRow { id: number; actor: string | null; action: string; entity: string | null; details: Record<string, unknown>; created_at: string }
export function AuditTab() {
  const [rows, setRows] = useState<AuditRow[] | null>(null);
  useEffect(() => {
    void supabase.from('audit_log').select('id, actor, action, entity, details, created_at').order('id', { ascending: false }).limit(100)
      .then(({ data }) => setRows((data ?? []) as AuditRow[]));
  }, []);
  return (
    <section className="card space-y-2">
      <h2 className="font-semibold">Registo de operações importantes</h2>
      {rows === null && <p className="muted">A carregar…</p>}
      {rows?.length === 0 && <p className="muted">Ainda não há operações registadas.</p>}
      <ul className="divide-y divide-slate-200 text-sm dark:divide-navy-800">
        {rows?.map((r) => (
          <li key={r.id} className="py-2"><strong>{r.action.replace(/_/g, ' ')}</strong> <span className="muted">· {fmtDateTime(r.created_at)}</span>
            <p className="muted break-all">{JSON.stringify(r.details).slice(0, 200)}</p></li>
        ))}
      </ul>
    </section>
  );
}

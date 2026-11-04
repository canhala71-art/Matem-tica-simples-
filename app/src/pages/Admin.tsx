import { useCallback, useEffect, useState, type FormEvent } from 'react';
import { supabase } from '../lib/supabase';
import { useAuth } from '../lib/auth';
import { AuditTab, CodesTab, OverviewTab, PaymentsTab, PlansAdminTab, QuizAdminTab, SettingsTab } from './AdminBilling';

type Tab = 'visao' | 'pagamentos' | 'codigos' | 'planos' | 'config' | 'quizzes' | 'conteudo' | 'aula' | 'exercicio' | 'utilizadores' | 'auditoria';
const STATUS = [['draft', 'Rascunho'], ['review', 'Em revisão'], ['published', 'Publicado']] as const;
const BLOCKS = [
  ['introduction', 'Introdução'], ['intuition', 'Explicação intuitiva'], ['definition', 'Definição matemática'],
  ['formulas', 'Fórmulas'], ['worked_example', 'Exemplos resolvidos'], ['guided_exercise', 'Exercícios orientados'],
  ['independent_exercise', 'Exercícios independentes'], ['challenge', 'Desafio'], ['assessment', 'Avaliação'],
] as const;

const slugify = (s: string) =>
  s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 80);

function Notice({ n }: { n: { ok: boolean; text: string } | null }) {
  return n ? <p role="status" className={`text-sm ${n.ok ? 'text-emerald-600' : 'text-red-600'}`}>{n.text}</p> : null;
}

export function AdminPage() {
  const [tab, setTab] = useState<Tab>('visao');
  const tabs: [Tab, string][] = [['visao', 'Visão geral'], ['pagamentos', 'Pagamentos'], ['codigos', 'Códigos'], ['planos', 'Planos'], ['config', 'Configurações'], ['quizzes', 'Quizzes'], ['conteudo', 'Conteúdo'], ['aula', 'Nova aula'], ['exercicio', 'Novo exercício'], ['utilizadores', 'Utilizadores'], ['auditoria', 'Auditoria']];
  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Painel administrativo</h1>
      <div className="flex gap-2 overflow-x-auto">
        {tabs.map(([k, l]) => (
          <button key={k} onClick={() => setTab(k)} className={tab === k ? 'btn' : 'btn-ghost'}>{l}</button>
        ))}
      </div>
      {tab === 'visao' && <OverviewTab />}
      {(tab === 'pagamentos' || tab === 'codigos') && <h2 className="text-lg font-bold">Gestão de Pagamentos e Códigos</h2>}
      {tab === 'pagamentos' && <PaymentsTab />}
      {tab === 'codigos' && <CodesTab />}
      {tab === 'planos' && <PlansAdminTab />}
      {tab === 'config' && <SettingsTab />}
      {tab === 'quizzes' && <QuizAdminTab />}
      {tab === 'auditoria' && <AuditTab />}
      {tab === 'conteudo' && <ContentTab />}
      {tab === 'aula' && <LessonForm />}
      {tab === 'exercicio' && <ExerciseForm />}
      {tab === 'utilizadores' && <UsersTab />}
    </div>
  );
}

// ---------- Rever e publicar ----------
interface Item { id: string; label: string; status: string }

function StatusList({ table, field, title, extra }: { table: string; field: string; title: string; extra?: boolean }) {
  const [items, setItems] = useState<Item[] | null>(null);
  const [note, setNote] = useState<{ ok: boolean; text: string } | null>(null);
  const { session } = useAuth();

  const load = useCallback(async () => {
    const { data } = await supabase.from(table).select(`id, ${field}, status`).order('created_at', { ascending: false }).limit(100);
    setItems(((data ?? []) as unknown as Record<string, string>[]).map((r) => ({ id: r.id, label: String(r[field]).slice(0, 90), status: r.status })));
  }, [table, field]);
  useEffect(() => { void load(); }, [load]);

  async function change(id: string, status: string) {
    const patch: Record<string, unknown> = { status };
    if (extra && status === 'published') { patch.published_at = new Date().toISOString(); patch.reviewed_by = session?.user.id; }
    const { error } = await supabase.from(table).update(patch).eq('id', id);
    setNote(error ? { ok: false, text: `Erro: ${error.message}` } : { ok: true, text: 'Estado atualizado.' });
    await load();
  }

  return (
    <section className="card space-y-2">
      <h2 className="font-semibold">{title}</h2>
      <Notice n={note} />
      {items === null && <p className="muted">A carregar…</p>}
      {items?.length === 0 && <p className="muted">Nada criado ainda.</p>}
      <ul className="divide-y divide-slate-200 dark:divide-navy-800">
        {items?.map((i) => (
          <li key={i.id} className="flex items-center justify-between gap-3 py-2 text-sm">
            <span className="min-w-0 flex-1 truncate">{i.label}</span>
            <select className="input !w-auto" value={i.status} onChange={(e) => void change(i.id, e.target.value)} aria-label={`Estado de ${i.label}`}>
              {STATUS.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
            </select>
          </li>
        ))}
      </ul>
    </section>
  );
}

function ContentTab() {
  return (
    <div className="space-y-4">
      <p className="muted">Nada chega aos alunos até ser marcado como "Publicado" aqui. Revê sempre a matemática antes de publicar.</p>
      <StatusList table="levels" field="title" title="Níveis" />
      <StatusList table="subjects" field="title" title="Disciplinas" />
      <StatusList table="topics" field="title" title="Unidades" />
      <StatusList table="lessons" field="title" title="Aulas" extra />
      <StatusList table="exercises" field="statement" title="Exercícios" />
    </div>
  );
}

// ---------- Nova aula ----------
interface Opt { id: string; title: string }

function useOptions(table: string, label: string) {
  const [opts, setOpts] = useState<Opt[]>([]);
  const reload = useCallback(async () => {
    const { data } = await supabase.from(table).select(`id, ${label}`).order(label).limit(300);
    setOpts(((data ?? []) as unknown as Record<string, string>[]).map((r) => ({ id: r.id, title: r[label] })));
  }, [table, label]);
  useEffect(() => { void reload(); }, [reload]);
  return { opts, reload };
}

function LessonForm() {
  const { session } = useAuth();
  const topics = useOptions('topics', 'title');
  const subjects = useOptions('subjects', 'title');
  const [topicId, setTopicId] = useState('');
  const [newTopic, setNewTopic] = useState({ subject: '', title: '' });
  const [title, setTitle] = useState('');
  const [summary, setSummary] = useState('');
  const [minutes, setMinutes] = useState('');
  const [blocks, setBlocks] = useState<Record<string, string>>({});
  const [note, setNote] = useState<{ ok: boolean; text: string } | null>(null);
  const [busy, setBusy] = useState(false);

  async function createTopic() {
    if (!newTopic.subject || !newTopic.title.trim()) return;
    const { data, error } = await supabase.from('topics')
      .insert({ subject_id: newTopic.subject, title: newTopic.title.trim(), slug: `${slugify(newTopic.title)}-${Date.now().toString(36)}`, kind: 'unit' })
      .select('id').single();
    if (error) { setNote({ ok: false, text: error.message }); return; }
    await topics.reload();
    setTopicId((data as { id: string }).id);
    setNewTopic({ subject: '', title: '' });
  }

  async function save(e: FormEvent) {
    e.preventDefault();
    if (!topicId || !title.trim()) return;
    setBusy(true);
    const { data: lesson, error } = await supabase.from('lessons').insert({
      topic_id: topicId, title: title.trim(), summary: summary.trim() || null,
      slug: `${slugify(title)}-${Date.now().toString(36)}`, status: 'draft',
      estimated_minutes: minutes ? Number(minutes) : null, created_by: session?.user.id,
    }).select('id').single();
    if (error || !lesson) { setBusy(false); setNote({ ok: false, text: error?.message ?? 'Erro' }); return; }
    const rows = BLOCKS.map(([k], i) => ({ lesson_id: (lesson as { id: string }).id, kind: k, position: i, body: (blocks[k] ?? '').trim() })).filter((r) => r.body);
    if (rows.length) {
      const { error: be } = await supabase.from('lesson_blocks').insert(rows);
      if (be) { setBusy(false); setNote({ ok: false, text: `Aula criada, mas os blocos falharam: ${be.message}` }); return; }
    }
    setBusy(false);
    setNote({ ok: true, text: 'Aula guardada como rascunho. Revê-a e publica no separador Conteúdo.' });
    setTitle(''); setSummary(''); setMinutes(''); setBlocks({});
  }

  return (
    <form onSubmit={(e) => void save(e)} className="card space-y-3">
      <h2 className="font-semibold">Nova aula (rascunho)</h2>
      <p className="muted">Escreve em texto. Fórmulas entre $...$ (ex.: $\frac{'{'}1{'}'}{'{'}2{'}'}$). Podes deixar blocos vazios.</p>
      <div className="grid gap-2 sm:grid-cols-[1fr_auto]">
        <select className="input" required value={topicId} onChange={(e) => setTopicId(e.target.value)}>
          <option value="">Escolhe a unidade…</option>
          {topics.opts.map((t) => <option key={t.id} value={t.id}>{t.title}</option>)}
        </select>
      </div>
      <details className="rounded-xl border border-slate-300 p-3 text-sm dark:border-navy-700">
        <summary className="cursor-pointer font-medium">Criar uma unidade nova</summary>
        <div className="mt-2 grid gap-2 sm:grid-cols-[1fr_1fr_auto]">
          <select className="input" value={newTopic.subject} onChange={(e) => setNewTopic({ ...newTopic, subject: e.target.value })}>
            <option value="">Disciplina…</option>
            {subjects.opts.map((s) => <option key={s.id} value={s.id}>{s.title}</option>)}
          </select>
          <input className="input" placeholder="Título da unidade" value={newTopic.title} onChange={(e) => setNewTopic({ ...newTopic, title: e.target.value })} />
          <button type="button" className="btn-ghost" onClick={() => void createTopic()}>Criar</button>
        </div>
      </details>
      <input className="input" required placeholder="Título da aula" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input className="input" placeholder="Resumo (opcional)" value={summary} onChange={(e) => setSummary(e.target.value)} />
      <input className="input" type="number" min={1} max={240} placeholder="Duração estimada (min)" value={minutes} onChange={(e) => setMinutes(e.target.value)} />
      {BLOCKS.map(([k, l]) => (
        <label key={k} className="block text-sm font-medium">{l}
          <textarea className="input mt-1 min-h-24 font-normal" value={blocks[k] ?? ''} onChange={(e) => setBlocks({ ...blocks, [k]: e.target.value })} />
        </label>
      ))}
      <Notice n={note} />
      <button className="btn" disabled={busy || !topicId || !title.trim()}>Guardar rascunho</button>
    </form>
  );
}

// ---------- Novo exercício ----------
const TYPES = [
  ['multiple_choice', 'Escolha múltipla'], ['numeric', 'Resposta numérica'], ['algebraic', 'Resposta algébrica'],
  ['true_false', 'Verdadeiro ou falso'], ['written', 'Exercício escrito'], ['word_problem', 'Problema prático'],
] as const;

function ExerciseForm() {
  const { session } = useAuth();
  const topics = useOptions('topics', 'title');
  const lessons = useOptions('lessons', 'title');
  const [f, setF] = useState({
    topic: '', lesson: '', type: 'numeric', difficulty: '1', competency: '', statement: '', options: '',
    answer: '', accepted: '', tolerance: '0', explanation: '', steps: '',
  });
  const [note, setNote] = useState<{ ok: boolean; text: string } | null>(null);
  const [busy, setBusy] = useState(false);
  const set = (k: keyof typeof f, v: string) => setF((p) => ({ ...p, [k]: v }));

  async function save(e: FormEvent) {
    e.preventDefault();
    setBusy(true);
    setNote(null);
    let options: { id: string; label: string }[] | null = null;
    let expected: Record<string, unknown> = {};
    const accepted = f.accepted.split('\n').map((s) => s.trim()).filter(Boolean);
    if (f.type === 'multiple_choice') {
      const parsedOptions: { id: string; label: string }[] = f.options.split('\n').map((l) => l.trim()).filter(Boolean).map((l) => {
        const [id, ...rest] = l.split('|');
        return { id: id.trim().toLowerCase(), label: rest.join('|').trim() };
      });
      if (parsedOptions.length < 2 || parsedOptions.some((o) => !o.id || !o.label)) { setBusy(false); setNote({ ok: false, text: 'Opções: uma por linha, no formato  a|texto  (mínimo 2).' }); return; }
      if (!parsedOptions.some((o) => o.id === f.answer.trim().toLowerCase())) { setBusy(false); setNote({ ok: false, text: 'A resposta certa tem de ser o id de uma das opções.' }); return; }
      options = parsedOptions;
      expected = { choice: f.answer.trim().toLowerCase() };
    } else if (f.type === 'numeric') expected = { value: f.answer.trim(), accepted };
    else if (f.type === 'algebraic') expected = { expression: f.answer.trim(), accepted };
    else if (f.type === 'true_false') expected = { boolean: f.answer === 'true' };
    if (f.type !== 'written' && f.type !== 'word_problem' && !f.answer.trim()) { setBusy(false); setNote({ ok: false, text: 'Indica a resposta certa.' }); return; }

    const { data: ex, error } = await supabase.from('exercises').insert({
      topic_id: f.topic, lesson_id: f.lesson || null, type: f.type, difficulty: Number(f.difficulty),
      competency: f.competency.trim(), statement: f.statement.trim(), options, status: 'draft',
      created_by: session?.user.id, verified_with_sympy: false,
    }).select('id').single();
    if (error || !ex) { setBusy(false); setNote({ ok: false, text: error?.message ?? 'Erro' }); return; }
    const { error: ae } = await supabase.from('exercise_answers').insert({
      exercise_id: (ex as { id: string }).id, answer: expected, tolerance: Number(f.tolerance) || 0,
      explanation: f.explanation.trim(), solution_steps: f.steps.split('\n').map((s) => s.trim()).filter(Boolean),
    });
    setBusy(false);
    if (ae) { setNote({ ok: false, text: `Exercício criado, mas a resposta falhou: ${ae.message}` }); return; }
    setNote({ ok: true, text: 'Exercício guardado como rascunho. Confirma a resolução e publica no separador Conteúdo.' });
    setF((p) => ({ ...p, statement: '', options: '', answer: '', accepted: '', explanation: '', steps: '' }));
  }

  return (
    <form onSubmit={(e) => void save(e)} className="card space-y-3">
      <h2 className="font-semibold">Novo exercício (rascunho)</h2>
      <select className="input" required value={f.topic} onChange={(e) => set('topic', e.target.value)}>
        <option value="">Unidade…</option>{topics.opts.map((t) => <option key={t.id} value={t.id}>{t.title}</option>)}
      </select>
      <select className="input" value={f.lesson} onChange={(e) => set('lesson', e.target.value)}>
        <option value="">Sem aula associada</option>{lessons.opts.map((t) => <option key={t.id} value={t.id}>{t.title}</option>)}
      </select>
      <div className="grid gap-2 sm:grid-cols-3">
        <select className="input" value={f.type} onChange={(e) => set('type', e.target.value)}>
          {TYPES.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
        </select>
        <select className="input" value={f.difficulty} onChange={(e) => set('difficulty', e.target.value)}>
          {[1, 2, 3, 4, 5].map((d) => <option key={d} value={d}>Dificuldade {d}</option>)}
        </select>
        <input className="input" required placeholder="Competência (ex.: fracoes.soma)" value={f.competency} onChange={(e) => set('competency', e.target.value)} />
      </div>
      <textarea className="input min-h-24" required placeholder="Enunciado (fórmulas entre $...$)" value={f.statement} onChange={(e) => set('statement', e.target.value)} />
      {f.type === 'multiple_choice' && (
        <textarea className="input min-h-24" placeholder={'Opções, uma por linha:\na|1/2\nb|3/4'} value={f.options} onChange={(e) => set('options', e.target.value)} />
      )}
      {f.type === 'true_false' ? (
        <select className="input" value={f.answer} onChange={(e) => set('answer', e.target.value)}>
          <option value="">Resposta certa…</option><option value="true">Verdadeiro</option><option value="false">Falso</option>
        </select>
      ) : f.type !== 'written' && f.type !== 'word_problem' ? (
        <input className="input" placeholder={f.type === 'multiple_choice' ? 'Id da opção certa (ex.: b)' : 'Resposta certa'} value={f.answer} onChange={(e) => set('answer', e.target.value)} />
      ) : <p className="muted">Sem correção automática: o aluno compara a sua resolução com a tua.</p>}
      {(f.type === 'numeric' || f.type === 'algebraic') && (
        <textarea className="input min-h-16" placeholder="Outras formas aceites (uma por linha, opcional)" value={f.accepted} onChange={(e) => set('accepted', e.target.value)} />
      )}
      {f.type === 'numeric' && (
        <input className="input" type="number" step="any" min={0} placeholder="Tolerância (ex.: 0.01)" value={f.tolerance} onChange={(e) => set('tolerance', e.target.value)} />
      )}
      <textarea className="input min-h-16" required placeholder="Explicação" value={f.explanation} onChange={(e) => set('explanation', e.target.value)} />
      <textarea className="input min-h-24" placeholder="Resolução passo a passo (um passo por linha)" value={f.steps} onChange={(e) => set('steps', e.target.value)} />
      <Notice n={note} />
      <button className="btn" disabled={busy || !f.topic}>Guardar rascunho</button>
    </form>
  );
}

// ---------- Utilizadores ----------
interface UserRow { id: string; display_name: string; roles: string[]; suspended: boolean }

function UsersTab() {
  const { session } = useAuth();
  const [rows, setRows] = useState<UserRow[] | null>(null);
  const [note, setNote] = useState<{ ok: boolean; text: string } | null>(null);

  const load = useCallback(async () => {
    const [p, r] = await Promise.all([
      supabase.from('profiles').select('id, display_name, suspended').order('created_at', { ascending: false }).limit(200),
      supabase.from('user_roles').select('user_id, role'),
    ]);
    const roles = (r.data ?? []) as { user_id: string; role: string }[];
    setRows(((p.data ?? []) as { id: string; display_name: string; suspended: boolean }[]).map((u) => ({ ...u, roles: roles.filter((x) => x.user_id === u.id).map((x) => x.role) })));
  }, []);
  useEffect(() => { void load(); }, [load]);

  async function toggleTeacher(u: UserRow) {
    const has = u.roles.includes('teacher');
    const { error } = has
      ? await supabase.from('user_roles').delete().eq('user_id', u.id).eq('role', 'teacher')
      : await supabase.from('user_roles').insert({ user_id: u.id, role: 'teacher' });
    setNote(error ? { ok: false, text: error.message } : { ok: true, text: has ? 'Papel de professor removido.' : 'Papel de professor atribuído.' });
    await load();
  }

  async function toggleSuspend(u: UserRow) {
    if (!window.confirm(u.suspended ? `Reativar a conta de ${u.display_name}?` : `Suspender a conta de ${u.display_name}?`)) return;
    const { error } = await supabase.rpc('admin_set_suspended', { _user: u.id, _value: !u.suspended });
    setNote(error ? { ok: false, text: error.message } : { ok: true, text: u.suspended ? 'Conta reativada.' : 'Conta suspensa.' });
    await load();
  }

  return (
    <section className="card space-y-2">
      <h2 className="font-semibold">Utilizadores</h2>
      <Notice n={note} />
      {rows === null && <p className="muted">A carregar…</p>}
      <ul className="divide-y divide-slate-200 dark:divide-navy-800">
        {rows?.map((u) => (
          <li key={u.id} className="flex items-center justify-between gap-3 py-2 text-sm">
            <span className="min-w-0 flex-1 truncate">{u.display_name} <span className="muted">· {u.roles.join(', ') || 'sem papel'}{u.suspended ? ' · suspensa' : ''}</span></span>
            {u.id !== session?.user.id && !u.roles.includes('admin') && (
              <span className="flex gap-2">
                <button className="btn-ghost !py-1.5" onClick={() => void toggleTeacher(u)}>
                  {u.roles.includes('teacher') ? 'Remover professor' : 'Tornar professor'}
                </button>
                <button className="btn-ghost !py-1.5" onClick={() => void toggleSuspend(u)}>{u.suspended ? 'Reativar' : 'Suspender'}</button>
              </span>
            )}
          </li>
        ))}
      </ul>
    </section>
  );
}

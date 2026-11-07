import { useMemo, useState, type ReactNode } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import * as T from '../lib/tools';

const fmt = (n: number) => String(Math.round(n * 1e6) / 1e6).replace('.', ',');
const num = (s: string) => Number(s.trim().replace(',', '.'));
const isInt = (s: string) => /^-?\d+$/.test(s.trim());
const showFrac = (f: T.Frac) => (f.d === 1 ? String(f.n) : `${f.n}/${f.d}`);

export const TOOLS: { id: string; title: string }[] = [
  { id: 'reta', title: 'Reta numérica' },
  { id: 'operacoes', title: 'Operações' },
  { id: 'tabuada', title: 'Treino de tabuada' },
  { id: 'mdc', title: 'MDC e MMC' },
  { id: 'fracoes', title: 'Frações' },
  { id: 'decimais', title: 'Decimal ↔ fração' },
  { id: 'percentagens', title: 'Percentagens' },
  { id: 'potencias', title: 'Potências' },
  { id: 'raizes', title: 'Raízes' },
];

function Out({ children }: { children: ReactNode }) {
  return <div className="rounded-xl bg-electric-500/10 p-3 text-sm" aria-live="polite">{children}</div>;
}
function Err({ msg }: { msg: string }) { return <p role="alert" className="text-sm text-red-600">{msg}</p>; }
function Field({ label, value, set, ph }: { label: string; value: string; set: (v: string) => void; ph?: string }) {
  return (
    <label className="block text-sm font-medium">{label}
      <input className="input mt-1" value={value} onChange={(e) => set(e.target.value)} placeholder={ph} inputMode="decimal"
        autoCapitalize="off" autoCorrect="off" spellCheck={false} />
    </label>
  );
}
function run<R>(fn: () => R): { ok: R | null; err: string | null } {
  try { return { ok: fn(), err: null }; } catch (e) { return { ok: null, err: e instanceof Error ? e.message : 'Entrada inválida' }; }
}

function NumberLine() {
  const [min, setMin] = useState('-5');
  const [max, setMax] = useState('5');
  const [pts, setPts] = useState('-3, 0, 2,5');
  const r = run(() => {
    const lo = num(min), hi = num(max);
    if (!Number.isFinite(lo) || !Number.isFinite(hi) || hi <= lo) throw new Error('O mínimo tem de ser menor que o máximo.');
    if (hi - lo > 40) throw new Error('Intervalo máximo: 40 unidades.');
    const values = pts.split(/[;\s]+|,\s+/).filter(Boolean).map((p) => num(p));
    if (values.some((v) => !Number.isFinite(v))) throw new Error('Pontos inválidos. Separa por espaço ou ponto e vírgula, ex.: -3; 0; 2,5');
    return { lo, hi, values };
  });
  const W = 640, pad = 24;
  const x = (v: number, lo: number, hi: number) => pad + ((v - lo) / (hi - lo)) * (W - 2 * pad);
  return (
    <div className="space-y-3">
      <div className="grid grid-cols-3 gap-2"><Field label="Mínimo" value={min} set={setMin} /><Field label="Máximo" value={max} set={setMax} /><Field label="Pontos" value={pts} set={setPts} ph="-3; 0; 2,5" /></div>
      {r.err && <Err msg={r.err} />}
      {r.ok && (() => {
        const { lo, hi, values } = r.ok;
        const ticks: number[] = [];
        for (let v = Math.ceil(lo); v <= Math.floor(hi); v++) ticks.push(v);
        const sorted = [...values].sort((a, b) => a - b);
        return (
          <>
            <svg viewBox={`0 0 ${W} 110`} className="w-full rounded-xl border border-slate-200 bg-white dark:border-navy-700 dark:bg-navy-950" role="img" aria-label="Reta numérica">
              <line x1={pad} y1={60} x2={W - pad} y2={60} stroke="currentColor" strokeWidth={2} />
              {ticks.map((t) => (
                <g key={t}><line x1={x(t, lo, hi)} y1={53} x2={x(t, lo, hi)} y2={67} stroke="currentColor" />
                  {(hi - lo <= 20 || t % 5 === 0) && <text x={x(t, lo, hi)} y={86} textAnchor="middle" fontSize={11} fill="currentColor">{t}</text>}</g>
              ))}
              {values.filter((v) => v >= lo && v <= hi).map((v, i) => (
                <g key={i}><circle cx={x(v, lo, hi)} cy={60} r={6} fill="#2f6bff" /><text x={x(v, lo, hi)} y={40} textAnchor="middle" fontSize={12} fontWeight={700} fill="#2f6bff">{fmt(v)}</text></g>
              ))}
            </svg>
            {sorted.length > 1 && <Out>Por ordem crescente: {sorted.map(fmt).join(' < ')}</Out>}
            {values.some((v) => v < lo || v > hi) && <p className="muted">Há pontos fora do intervalo escolhido; não aparecem no desenho.</p>}
          </>
        );
      })()}
    </div>
  );
}

function Operations() {
  const [a, setA] = useState('29');
  const [b, setB] = useState('4');
  const [op, setOp] = useState<'+' | '-' | '*' | '/'>('/');
  const r = run(() => {
    const x = num(a), y = num(b);
    if (!Number.isFinite(x) || !Number.isFinite(y)) throw new Error('Escreve dois números.');
    if (op === '+') return `${fmt(x)} + ${fmt(y)} = ${fmt(x + y)}`;
    if (op === '-') return `${fmt(x)} − ${fmt(y)} = ${fmt(x - y)}`;
    if (op === '*') return `${fmt(x)} × ${fmt(y)} = ${fmt(Math.round(x * y * 1e9) / 1e9)}`;
    if (isInt(a) && isInt(b)) {
      const d = T.divide(x, y);
      return `${x} ÷ ${y}: quociente ${d.q}, resto ${d.r}. Verificação: ${y} × ${d.q} + ${d.r} = ${y * d.q + d.r}`;
    }
    if (y === 0) throw new Error('Não se divide por zero.');
    return `${fmt(x)} ÷ ${fmt(y)} = ${fmt(x / y)}`;
  });
  return (
    <div className="space-y-3">
      <div className="grid grid-cols-3 gap-2 items-end">
        <Field label="Primeiro número" value={a} set={setA} />
        <label className="block text-sm font-medium">Operação
          <select className="input mt-1" value={op} onChange={(e) => setOp(e.target.value as typeof op)}>
            <option value="+">Adição +</option><option value="-">Subtração −</option><option value="*">Multiplicação ×</option><option value="/">Divisão ÷</option>
          </select></label>
        <Field label="Segundo número" value={b} set={setB} />
      </div>
      {r.err ? <Err msg={r.err} /> : <Out>{r.ok}</Out>}
    </div>
  );
}

function TimesTable() {
  const [table, setTable] = useState(7);
  const [qs, setQs] = useState<{ a: number; b: number }[]>([]);
  const [i, setI] = useState(0);
  const [ans, setAns] = useState('');
  const [score, setScore] = useState(0);
  const [wrong, setWrong] = useState<string[]>([]);
  const [t0, setT0] = useState(0);
  const [secs, setSecs] = useState<number | null>(null);
  const active = qs.length > 0 && i < qs.length;
  function start() {
    const list = Array.from({ length: 10 }, () => ({ a: table, b: 1 + Math.floor(Math.random() * 12) }));
    setQs(list); setI(0); setScore(0); setWrong([]); setAns(''); setSecs(null); setT0(Date.now());
  }
  function send() {
    if (!active || ans.trim() === '') return;
    const q = qs[i];
    const ok = Number(ans) === q.a * q.b;
    if (ok) setScore((s) => s + 1); else setWrong((w) => [...w, `${q.a} × ${q.b} = ${q.a * q.b} (respondeste ${ans})`]);
    setAns('');
    if (i + 1 === qs.length) setSecs(Math.round((Date.now() - t0) / 1000));
    setI(i + 1);
  }
  return (
    <div className="space-y-3">
      <div className="flex items-end gap-2">
        <label className="block text-sm font-medium">Tabuada do
          <select className="input mt-1" value={table} onChange={(e) => setTable(Number(e.target.value))}>
            {Array.from({ length: 12 }, (_, k) => k + 1).map((n) => <option key={n} value={n}>{n}</option>)}
          </select></label>
        <button className="btn" onClick={start}>{qs.length ? 'Recomeçar' : 'Começar (10 contas)'}</button>
      </div>
      {active && (
        <div className="card space-y-2">
          <p className="muted">Conta {i + 1} de {qs.length}</p>
          <p className="text-2xl font-bold">{qs[i].a} × {qs[i].b} = ?</p>
          <input className="input" inputMode="numeric" value={ans} autoFocus onChange={(e) => setAns(e.target.value)} onKeyDown={(e) => { if (e.key === 'Enter') send(); }} />
          <button className="btn" disabled={ans.trim() === ''} onClick={send}>Responder</button>
        </div>
      )}
      {qs.length > 0 && !active && (
        <Out>
          <p className="font-semibold">{score} de {qs.length} certas{secs !== null && ` em ${secs} s`}.</p>
          {wrong.length > 0 ? <ul className="mt-1 list-disc pl-5">{wrong.map((w) => <li key={w}>{w}</li>)}</ul> : <p>Sem erros. Tenta outra tabuada!</p>}
        </Out>
      )}
    </div>
  );
}

function GcdLcm() {
  const [txt, setTxt] = useState('12; 18; 30');
  const r = run(() => {
    const ns = txt.split(/[;,\s]+/).filter(Boolean).map(Number);
    if (ns.length < 2 || ns.length > 5) throw new Error('Escreve de 2 a 5 números.');
    if (ns.some((n) => !Number.isInteger(n) || n < 1 || n > 1e6)) throw new Error('Usa inteiros positivos até 1 000 000.');
    const g = ns.reduce(T.gcd);
    const l = ns.reduce(T.lcm);
    if (l > Number.MAX_SAFE_INTEGER) throw new Error('O MMC é grande demais.');
    return { ns, g, l };
  });
  const pf = (n: number) => T.factorize(n).map(([p, e]) => (e > 1 ? `${p}^${e}` : `${p}`)).join(' × ') || '1';
  return (
    <div className="space-y-3">
      <Field label="Números (separados por ; )" value={txt} set={setTxt} ph="12; 18; 30" />
      {r.err ? <Err msg={r.err} /> : r.ok && (
        <Out>
          <p><strong>MDC = {r.ok.g}</strong> · <strong>MMC = {r.ok.l}</strong></p>
          <ul className="mt-1 list-disc pl-5">{r.ok.ns.map((n) => <li key={n}>{n} = {n === 1 ? '1' : pf(n)}</li>)}</ul>
          {r.ok.ns.length === 2 && T.euclidSteps(r.ok.ns[0], r.ok.ns[1]).length > 0 && (
            <><p className="mt-2 font-semibold">Algoritmo de Euclides:</p><ul className="list-disc pl-5">{T.euclidSteps(r.ok.ns[0], r.ok.ns[1]).map((s) => <li key={s}>{s}</li>)}</ul></>
          )}
        </Out>
      )}
    </div>
  );
}

function Fractions() {
  const [f, setF] = useState({ an: '1', ad: '2', bn: '1', bd: '3' });
  const [op, setOp] = useState<'+' | '-' | '*' | '/'>('+');
  const r = run(() => {
    const v = [f.an, f.ad, f.bn, f.bd];
    if (!v.every(isInt)) throw new Error('Usa números inteiros nos numeradores e denominadores.');
    const [an, ad, bn, bd] = v.map(Number);
    if (ad === 0 || bd === 0) throw new Error('O denominador não pode ser zero.');
    const res = T.fracOp({ n: an, d: ad }, { n: bn, d: bd }, op);
    return { res, dec: T.fractionToDecimal(res).text };
  });
  const box = (nk: 'an' | 'bn', dk: 'ad' | 'bd') => (
    <div className="flex w-20 flex-col gap-1">
      <input aria-label="numerador" className="input text-center" value={f[nk]} onChange={(e) => setF({ ...f, [nk]: e.target.value })} inputMode="numeric" />
      <div className="h-0.5 bg-current" />
      <input aria-label="denominador" className="input text-center" value={f[dk]} onChange={(e) => setF({ ...f, [dk]: e.target.value })} inputMode="numeric" />
    </div>
  );
  return (
    <div className="space-y-3">
      <div className="flex items-center gap-3">
        {box('an', 'ad')}
        <select aria-label="operação" className="input !w-auto" value={op} onChange={(e) => setOp(e.target.value as typeof op)}>
          <option value="+">+</option><option value="-">−</option><option value="*">×</option><option value="/">÷</option>
        </select>
        {box('bn', 'bd')}
      </div>
      {r.err ? <Err msg={r.err} /> : r.ok && <Out>Resultado (simplificado): <strong>{showFrac(r.ok.res)}</strong>{r.ok.res.d !== 1 && Math.abs(r.ok.res.n) > r.ok.res.d && <> = {T.mixed(r.ok.res)}</>} · decimal: {r.ok.dec}</Out>}
    </div>
  );
}

function DecFrac() {
  const [dec, setDec] = useState('0,75');
  const [n, setN] = useState('7');
  const [d, setD] = useState('3');
  const a = run(() => T.decimalToFraction(dec));
  const b = run(() => {
    if (!isInt(n) || !isInt(d)) throw new Error('Usa números inteiros.');
    if (Number(d) === 0) throw new Error('O denominador não pode ser zero.');
    return T.fractionToDecimal({ n: Number(n), d: Number(d) });
  });
  return (
    <div className="grid gap-4 sm:grid-cols-2">
      <div className="space-y-2"><h3 className="font-semibold">Decimal → fração</h3>
        <Field label="Número decimal" value={dec} set={setDec} />
        {a.err ? <Err msg={a.err} /> : a.ok && <Out>{dec.trim()} = <strong>{showFrac(a.ok)}</strong></Out>}</div>
      <div className="space-y-2"><h3 className="font-semibold">Fração → decimal</h3>
        <div className="grid grid-cols-2 gap-2"><Field label="Numerador" value={n} set={setN} /><Field label="Denominador" value={d} set={setD} /></div>
        {b.err ? <Err msg={b.err} /> : b.ok && <Out>{n}/{d} = <strong>{b.ok.text}</strong>{b.ok.periodic && <span className="muted"> (o que está entre parênteses repete-se)</span>}</Out>}</div>
    </div>
  );
}

function Percent() {
  const [mode, setMode] = useState<'of' | 'what' | 'up' | 'down'>('of');
  const [x, setX] = useState('15');
  const [y, setY] = useState('200');
  const r = run(() => {
    const p = num(x), v = num(y);
    if (!Number.isFinite(p) || !Number.isFinite(v)) throw new Error('Escreve dois números.');
    if (mode === 'of') return `${fmt(p)}% de ${fmt(v)} = ${fmt(T.percentOf(p, v))}`;
    if (mode === 'what') return `${fmt(p)} é ${fmt(T.whatPercent(p, v))}% de ${fmt(v)}`;
    return `${fmt(v)} ${mode === 'up' ? 'aumentado' : 'diminuído'} em ${fmt(p)}% = ${fmt(T.changeBy(v, p, mode === 'up'))}`;
  });
  const lab = mode === 'what' ? ['Valor', 'Total'] : mode === 'of' ? ['Percentagem (%)', 'Valor'] : ['Percentagem (%)', 'Valor inicial'];
  return (
    <div className="space-y-3">
      <label className="block text-sm font-medium">O que queres calcular?
        <select className="input mt-1" value={mode} onChange={(e) => setMode(e.target.value as typeof mode)}>
          <option value="of">Quanto é p% de um valor</option><option value="what">Que percentagem é um valor de outro</option>
          <option value="up">Aumentar um valor em p%</option><option value="down">Diminuir um valor em p%</option>
        </select></label>
      <div className="grid grid-cols-2 gap-2"><Field label={lab[0]} value={x} set={setX} /><Field label={lab[1]} value={y} set={setY} /></div>
      {r.err ? <Err msg={r.err} /> : <Out>{r.ok}</Out>}
    </div>
  );
}

function Powers() {
  const [b, setB] = useState('2');
  const [e, setE] = useState('10');
  const r = run(() => {
    if (!isInt(b) || !isInt(e)) throw new Error('Usa números inteiros.');
    const bb = Number(b), ee = Number(e);
    const p = T.power(bb, ee);
    const expand = ee >= 1 && ee <= 6 ? `${Array(ee).fill(bb < 0 ? `(${bb})` : bb).join(' × ')} = ` : '';
    return `${bb < 0 ? `(${bb})` : bb}^${ee} = ${expand}${p.text}${ee < 0 ? ` (porque a⁻ⁿ = 1/aⁿ)` : ee === 0 ? ' (todo o número não nulo elevado a 0 é 1)' : ''}`;
  });
  return (
    <div className="space-y-3">
      <div className="grid grid-cols-2 gap-2"><Field label="Base" value={b} set={setB} /><Field label="Expoente" value={e} set={setE} /></div>
      {r.err ? <Err msg={r.err} /> : <Out>{r.ok}</Out>}
    </div>
  );
}

function Roots() {
  const [n, setN] = useState('72');
  const [idx, setIdx] = useState<2 | 3>(2);
  const r = run(() => {
    if (!isInt(n)) throw new Error('Usa um número inteiro.');
    return T.root(Number(n), idx);
  });
  return (
    <div className="space-y-3">
      <div className="grid grid-cols-2 gap-2 items-end">
        <Field label="Número" value={n} set={setN} />
        <label className="block text-sm font-medium">Raiz
          <select className="input mt-1" value={idx} onChange={(e) => setIdx(Number(e.target.value) as 2 | 3)}><option value={2}>Quadrada √</option><option value={3}>Cúbica ∛</option></select></label>
      </div>
      {r.err ? <Err msg={r.err} /> : r.ok && (
        <Out>
          {r.ok.exact !== null ? <>É uma raiz <strong>exata</strong>: {idx === 2 ? '√' : '∛'}{n.trim()} = <strong>{r.ok.exact}</strong></> :
            <>{idx === 2 ? '√' : '∛'}{n.trim()} = <strong>{r.ok.simplified}</strong> ≈ {fmt(r.ok.approx)} (não é exata)</>}
        </Out>
      )}
    </div>
  );
}

const BODY: Record<string, () => ReactNode> = {
  reta: () => <NumberLine />, operacoes: () => <Operations />, tabuada: () => <TimesTable />, mdc: () => <GcdLcm />,
  fracoes: () => <Fractions />, decimais: () => <DecFrac />, percentagens: () => <Percent />, potencias: () => <Powers />, raizes: () => <Roots />,
};

export function ToolsPage() {
  const [sp, setSp] = useSearchParams();
  const id = useMemo(() => (TOOLS.some((t) => t.id === sp.get('f')) ? (sp.get('f') as string) : 'reta'), [sp]);
  return (
    <div className="space-y-4">
      <Link to="/laboratorio" className="muted">← Laboratório</Link>
      <h1 className="text-2xl font-bold">Ferramentas do Nível 1</h1>
      <p className="muted">Nove ferramentas para treinar e conferir contas. Mostram o resultado e o raciocínio; não substituem estudar a aula.</p>
      <div className="flex flex-wrap gap-2" role="tablist">
        {TOOLS.map((t) => (
          <button key={t.id} role="tab" aria-selected={t.id === id} onClick={() => setSp({ f: t.id })}
            className={t.id === id ? 'btn !py-1.5' : 'btn-ghost !py-1.5'}>{t.title}</button>
        ))}
      </div>
      <div className="card" key={id}>{BODY[id]()}</div>
    </div>
  );
}

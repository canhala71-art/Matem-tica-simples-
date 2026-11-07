// Cálculos das ferramentas do Nível 1. Funções puras, exactas (inteiros), sem dependências.

export function gcd(a: number, b: number): number {
  a = Math.abs(a); b = Math.abs(b);
  while (b) [a, b] = [b, a % b];
  return a;
}
export function lcm(a: number, b: number): number {
  return a === 0 || b === 0 ? 0 : Math.abs(a / gcd(a, b) * b);
}

export function factorize(n: number): [number, number][] {
  const out: [number, number][] = [];
  let m = n;
  for (let p = 2; p * p <= m; p++) {
    let e = 0;
    while (m % p === 0) { m /= p; e++; }
    if (e) out.push([p, e]);
  }
  if (m > 1) out.push([m, 1]);
  return out;
}

export function euclidSteps(a: number, b: number): string[] {
  const steps: string[] = [];
  let x = Math.max(a, b), y = Math.min(a, b);
  while (y) {
    steps.push(`${x} = ${Math.floor(x / y)} × ${y} + ${x % y}`);
    [x, y] = [y, x % y];
  }
  return steps;
}

export interface Frac { n: number; d: number }
export function simplify(f: Frac): Frac {
  if (f.d === 0) throw new Error('denominador zero');
  const g = gcd(f.n, f.d) || 1;
  const s = f.d < 0 ? -1 : 1;
  return { n: (s * f.n) / g, d: (s * f.d) / g };
}
export function fracOp(a: Frac, b: Frac, op: '+' | '-' | '*' | '/'): Frac {
  if (a.d === 0 || b.d === 0) throw new Error('denominador zero');
  switch (op) {
    case '+': return simplify({ n: a.n * b.d + b.n * a.d, d: a.d * b.d });
    case '-': return simplify({ n: a.n * b.d - b.n * a.d, d: a.d * b.d });
    case '*': return simplify({ n: a.n * b.n, d: a.d * b.d });
    default:
      if (b.n === 0) throw new Error('divisão por zero');
      return simplify({ n: a.n * b.d, d: a.d * b.n });
  }
}
export function mixed(f: Frac): string {
  const s = simplify(f);
  if (s.d === 1) return String(s.n);
  const w = Math.trunc(s.n / s.d);
  const r = Math.abs(s.n) % s.d;
  return w === 0 ? `${s.n}/${s.d}` : `${w} ${r}/${s.d}`;
}

// "0,75" ou "3.5" -> fracção exacta (sem erros de vírgula flutuante).
export function decimalToFraction(text: string): Frac {
  const t = text.trim().replace(',', '.');
  if (!/^-?\d+(\.\d+)?$/.test(t)) throw new Error('decimal inválido');
  const neg = t.startsWith('-');
  const [i, f = ''] = t.replace('-', '').split('.');
  if (f.length > 9) throw new Error('máximo 9 casas decimais');
  const d = 10 ** f.length;
  return simplify({ n: (neg ? -1 : 1) * (Number(i) * d + Number(f || '0')), d });
}

// Fracção -> decimal por divisão longa; detecta a dízima periódica.
export function fractionToDecimal(f: Frac): { text: string; periodic: boolean } {
  const s = simplify(f);
  const neg = s.n < 0;
  let rem = Math.abs(s.n);
  const intPart = Math.floor(rem / s.d);
  rem %= s.d;
  const digits: number[] = [];
  const seen = new Map<number, number>();
  let start = -1;
  while (rem !== 0 && digits.length < 60) {
    if (seen.has(rem)) { start = seen.get(rem)!; break; }
    seen.set(rem, digits.length);
    rem *= 10;
    digits.push(Math.floor(rem / s.d));
    rem %= s.d;
  }
  const sign = neg ? '-' : '';
  if (!digits.length) return { text: `${sign}${intPart}`, periodic: false };
  if (start === -1) return { text: `${sign}${intPart},${digits.join('')}`, periodic: false };
  const pre = digits.slice(0, start).join('');
  const per = digits.slice(start).join('');
  return { text: `${sign}${intPart},${pre}(${per})`, periodic: true };
}

// Potência de base inteira e expoente inteiro (exacta com BigInt).
export function power(base: number, exp: number): { text: string; frac?: Frac } {
  if (!Number.isInteger(base) || !Number.isInteger(exp)) throw new Error('usa números inteiros');
  if (Math.abs(exp) > 200) throw new Error('expoente demasiado grande (máx. 200)');
  if (base === 0 && exp < 0) throw new Error('0 não tem expoente negativo');
  const v = BigInt(base) ** BigInt(Math.abs(exp));
  if (exp >= 0) return { text: v.toString() };
  return { text: `1/${v.toString()}` };
}

// Raiz de índice 2 ou 3 de um inteiro: exacta quando possível, forma simplificada e aproximação.
export function root(n: number, index: 2 | 3): { exact: number | null; simplified: string; approx: number } {
  if (!Number.isInteger(n)) throw new Error('usa um número inteiro');
  if (index === 2 && n < 0) throw new Error('a raiz quadrada de um negativo não é real');
  const neg = n < 0;
  const a = Math.abs(n);
  const r = Math.round(index === 2 ? Math.sqrt(a) : Math.cbrt(a));
  const sign = neg ? -1 : 1;
  if (r ** index === a) return { exact: sign * r, simplified: String(sign * r), approx: sign * r };
  let out = 1, rest = a;
  for (let p = 2; p ** index <= rest; p++) {
    while (rest % p ** index === 0) { rest /= p ** index; out *= p; }
  }
  const sym = index === 2 ? '√' : '∛';
  const inner = `${sym}${rest}`;
  const text = `${neg ? '-' : ''}${out > 1 ? out : ''}${inner}`;
  return { exact: null, simplified: text, approx: sign * (index === 2 ? Math.sqrt(a) : Math.cbrt(a)) };
}

export function percentOf(p: number, x: number): number { return (p * x) / 100; }
export function whatPercent(x: number, y: number): number {
  if (y === 0) throw new Error('o total não pode ser 0');
  return (x / y) * 100;
}
export function changeBy(x: number, p: number, up: boolean): number { return (x * (up ? 100 + p : 100 - p)) / 100; }

export function divide(a: number, b: number): { q: number; r: number } {
  if (b === 0) throw new Error('não se divide por zero');
  const q = Math.floor(a / b);
  return { q, r: a - q * b };
}

// ---------- Potências com base racional (decimal ou fração) ----------
export interface BigFrac { n: bigint; d: bigint }
function bgcd(a: bigint, b: bigint): bigint { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) [a, b] = [b, a % b]; return a; }
function bsimp(f: BigFrac): BigFrac {
  if (f.d === 0n) throw new Error('denominador zero');
  const g = bgcd(f.n, f.d) || 1n;
  const s = f.d < 0n ? -1n : 1n;
  return { n: (s * f.n) / g, d: (s * f.d) / g };
}
// "-0,5", "3", "2/3", "-7/4" -> fracção exacta
export function parseRational(text: string): BigFrac {
  const t = text.trim().replace(/\s+/g, '').replace(',', '.');
  if (/^-?\d+\/-?\d+$/.test(t)) {
    const [a, b] = t.split('/');
    if (BigInt(b) === 0n) throw new Error('o denominador não pode ser zero');
    return bsimp({ n: BigInt(a), d: BigInt(b) });
  }
  if (!/^-?\d+(\.\d+)?$/.test(t)) throw new Error('escreve um número (3, -0,5 ou 2/3)');
  const neg = t.startsWith('-');
  const [i, f = ''] = t.replace('-', '').split('.');
  if (f.length > 12) throw new Error('máximo 12 casas decimais');
  const d = 10n ** BigInt(f.length);
  return bsimp({ n: (neg ? -1n : 1n) * (BigInt(i) * d + BigInt(f || '0')), d });
}
export function bigFractionToDecimal(f: BigFrac): string {
  const s = bsimp(f);
  const neg = s.n < 0n;
  let rem = neg ? -s.n : s.n;
  const ip = rem / s.d;
  rem %= s.d;
  const digits: string[] = [];
  const seen = new Map<string, number>();
  let start = -1;
  while (rem !== 0n && digits.length < 40) {
    const key = rem.toString();
    if (seen.has(key)) { start = seen.get(key)!; break; }
    seen.set(key, digits.length);
    rem *= 10n;
    digits.push((rem / s.d).toString());
    rem %= s.d;
  }
  const sign = neg ? '-' : '';
  if (!digits.length) return `${sign}${ip}`;
  if (start === -1) return rem === 0n ? `${sign}${ip},${digits.join('')}` : `${sign}${ip},${digits.join('')}…`;
  return `${sign}${ip},${digits.slice(0, start).join('')}(${digits.slice(start).join('')})`;
}
function iroot(x: bigint, q: number): bigint | null {
  if (x < 0n) return null;
  const guess = BigInt(Math.round(Math.pow(Number(x), 1 / q)));
  for (const c of [guess - 1n, guess, guess + 1n]) if (c >= 0n && c ** BigInt(q) === x) return c;
  return null;
}
export interface PowerResult { exact: BigFrac | null; approx: number | null; note: string }
// base racional ^ expoente racional (inteiro, decimal ou fracção).
export function powerRational(baseText: string, expText: string): PowerResult {
  const b = parseRational(baseText);
  const e = parseRational(expText);
  const sgn = b.n < 0n ? -1n : 1n;
  if (b.n === 0n && e.n <= 0n) throw new Error('0 só admite expoentes positivos');
  if (e.d === 1n) {
    const k = e.n < 0n ? -e.n : e.n;
    if (k > 200n) throw new Error('expoente demasiado grande (máx. 200)');
    const kk = BigInt(k);
    let r: BigFrac = { n: b.n ** kk, d: b.d ** kk };
    if (e.n < 0n) r = { n: r.d, d: r.n };
    r = bsimp(r);
    return { exact: r, approx: null, note: e.n < 0n ? 'expoente negativo: inverte-se a base (a⁻ⁿ = 1/aⁿ)' : e.n === 0n ? 'qualquer número diferente de 0 elevado a 0 é 1' : '' };
  }
  // expoente fracionário p/q  =>  raiz de índice q, elevada a p
  const q = Number(e.d);
  const p = e.n;
  if (q > 12 || (p < 0n ? -p : p) > 60n) throw new Error('expoente fracionário demasiado complexo');
  if (sgn < 0n && q % 2 === 0) throw new Error('não existe raiz de índice par de um número negativo');
  const rn = iroot(b.n < 0n ? -b.n : b.n, q);
  const rd = iroot(b.d, q);
  if (rn !== null && rd !== null) {
    const base: BigFrac = { n: (q % 2 === 1 ? sgn : 1n) * rn, d: rd };
    const k = BigInt(p < 0n ? -p : p);
    let r: BigFrac = { n: base.n ** k, d: base.d ** k };
    if (p < 0n) r = { n: r.d, d: r.n };
    return { exact: bsimp(r), approx: null, note: `raiz de índice ${q} exata, depois elevada a ${p}` };
  }
  const val = Math.sign(Number(b.n)) * Math.pow(Math.abs(Number(b.n) / Number(b.d)), Number(p) / q);
  return { exact: null, approx: val, note: 'resultado irracional: só há aproximação' };
}

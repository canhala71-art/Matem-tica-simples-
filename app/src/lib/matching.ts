export interface Pair { left: string; right: string }

const ri = (a: number, b: number) => a + Math.floor(Math.random() * (b - a + 1));
const gcd = (a: number, b: number): number => (b ? gcd(b, a % b) : Math.abs(a));
const dec = (tenths: number) => (tenths / 10).toFixed(1).replace('.', ',');

type Gen = () => Pair;
const GENS: Record<string, Gen> = {
  'numeros-naturais': () => { const a = ri(11, 99), b = ri(2, 9); return { left: `${a} + ${b} × 3`, right: String(a + b * 3) }; },
  'numeros-inteiros': () => { const a = ri(1, 15), b = ri(1, 15); return { left: `(−${a}) + ${b}`, right: String(b - a).replace('-', '−') }; },
  'operacoes-basicas': () => { const a = ri(12, 49), b = ri(3, 9); return { left: `${a} × ${b}`, right: String(a * b) }; },
  tabuada: () => { const a = ri(2, 10), b = ri(2, 10); return { left: `${a} × ${b}`, right: String(a * b) }; },
  fracoes: () => {
    for (;;) {
      const k = ri(2, 5), n = ri(1, 7), d = ri(n + 1, 9);
      if (gcd(n, d) === 1) return { left: `${n * k}/${d * k} simplificada`, right: `${n}/${d}` };
    }
  },
  'numeros-decimais': () => { const a = ri(11, 89), b = ri(11, 89); return { left: `${dec(a)} + ${dec(b)}`, right: dec(a + b) }; },
  percentagens: () => {
    const p = [10, 20, 25, 50][ri(0, 3)], v = ri(2, 20) * 20;
    return { left: `${p}% de ${v}`, right: String((p * v) / 100) };
  },
  potencias: () => { const a = ri(2, 6), n = ri(2, 4); return { left: `${a}^${n}`, right: String(a ** n) }; },
  raizes: () => { const k = ri(2, 15); return { left: `√${k * k}`, right: String(k) }; },
};

export const MATCH_SLUGS = Object.keys(GENS);

/** 5 pares com respostas todas diferentes (para a associação ser inequívoca). */
export function makeRound(slug: string, n = 5): Pair[] {
  const g = GENS[slug];
  if (!g) return [];
  const out: Pair[] = [];
  const rights = new Set<string>(), lefts = new Set<string>();
  let guard = 0;
  while (out.length < n && guard++ < 500) {
    const p = g();
    if (rights.has(p.right) || lefts.has(p.left)) continue;
    rights.add(p.right); lefts.add(p.left); out.push(p);
  }
  return out;
}

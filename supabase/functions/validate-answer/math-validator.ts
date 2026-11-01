// Validador matemático do MenteMat — sem dependências, usado no navegador e na Edge Function.
// Não compara texto: normaliza, interpreta a expressão e compara valores.

export type Ast =
  | { t: 'num'; v: number }
  | { t: 'var'; name: string }
  | { t: 'neg'; a: Ast }
  | { t: 'bin'; op: '+' | '-' | '*' | '/' | '^'; a: Ast; b: Ast }
  | { t: 'fn'; name: string; a: Ast };

const FUNCTIONS: Record<string, (x: number) => number> = {
  sqrt: Math.sqrt, sin: Math.sin, cos: Math.cos, tan: Math.tan,
  ln: Math.log, log: Math.log10, abs: Math.abs, exp: Math.exp,
};
const CONSTANTS: Record<string, number> = { pi: Math.PI, e: Math.E };
const NAMES = [...Object.keys(FUNCTIONS), 'pi'].sort((a, b) => b.length - a.length);

type Tok =
  | { k: 'num'; v: number }
  | { k: 'id'; name: string }
  | { k: 'op'; v: string };

export class ParseError extends Error {}

export function normalizeText(input: string): string {
  return input
    .trim()
    .replace(/[−–—]/g, '-')
    .replace(/[×·]/g, '*')
    .replace(/÷/g, '/')
    .replace(/π/g, 'pi')
    .replace(/√/g, 'sqrt')
    .replace(/²/g, '^2')
    .replace(/³/g, '^3')
    .replace(/\s+/g, '')
    .replace(/(\d),(\d)/g, '$1.$2') // vírgula decimal (pt)
    .toLowerCase();
}

function tokenize(src: string): Tok[] {
  const out: Tok[] = [];
  let i = 0;
  while (i < src.length) {
    const c = src[i];
    if (/[0-9.]/.test(c)) {
      let j = i;
      while (j < src.length && /[0-9.]/.test(src[j])) j++;
      const text = src.slice(i, j);
      if (!/^(\d+\.?\d*|\.\d+)$/.test(text)) throw new ParseError('número inválido');
      out.push({ k: 'num', v: Number(text) });
      i = j;
    } else if (/[a-z]/.test(c)) {
      const known = NAMES.find((n) => src.startsWith(n, i));
      if (known) {
        out.push({ k: 'id', name: known });
        i += known.length;
      } else {
        out.push({ k: 'id', name: c }); // variável de uma letra
        i += 1;
      }
    } else if ('+-*/^()'.includes(c)) {
      out.push({ k: 'op', v: c });
      i++;
    } else {
      throw new ParseError(`símbolo inesperado: ${c}`);
    }
  }
  return out;
}

export function parse(input: string): Ast {
  const toks = tokenize(normalizeText(input).replace(/%/g, ''));
  if (toks.length === 0) throw new ParseError('vazio');
  let p = 0;
  const peek = () => toks[p];
  const isOp = (v: string) => peek()?.k === 'op' && (peek() as { v: string }).v === v;

  const startsAtom = () => {
    const t = peek();
    return !!t && (t.k === 'num' || t.k === 'id' || (t.k === 'op' && t.v === '('));
  };

  function expr(): Ast {
    let left = term();
    while (isOp('+') || isOp('-')) {
      const op = (toks[p++] as { v: '+' | '-' }).v;
      left = { t: 'bin', op, a: left, b: term() };
    }
    return left;
  }
  function term(): Ast {
    let left = unary();
    for (;;) {
      if (isOp('*') || isOp('/')) {
        const op = (toks[p++] as { v: '*' | '/' }).v;
        left = { t: 'bin', op, a: left, b: unary() };
      } else if (startsAtom()) {
        left = { t: 'bin', op: '*', a: left, b: unary() }; // multiplicação implícita
      } else break;
    }
    return left;
  }
  function unary(): Ast {
    if (isOp('-')) { p++; return { t: 'neg', a: unary() }; }
    if (isOp('+')) { p++; return unary(); }
    return power();
  }
  function power(): Ast {
    const base = atom();
    if (isOp('^')) { p++; return { t: 'bin', op: '^', a: base, b: unary() }; }
    return base;
  }
  function atom(): Ast {
    const t = toks[p++];
    if (!t) throw new ParseError('expressão incompleta');
    if (t.k === 'num') return { t: 'num', v: t.v };
    if (t.k === 'op' && t.v === '(') {
      const inner = expr();
      if (!isOp(')')) throw new ParseError('parêntese por fechar');
      p++;
      return inner;
    }
    if (t.k === 'id') {
      if (t.name in FUNCTIONS) {
        if (isOp('(')) {
          p++;
          const arg = expr();
          if (!isOp(')')) throw new ParseError('parêntese por fechar');
          p++;
          return { t: 'fn', name: t.name, a: arg };
        }
        return { t: 'fn', name: t.name, a: power() };
      }
      if (t.name === 'pi') return { t: 'num', v: Math.PI };
      if (t.name === 'e') return { t: 'num', v: Math.E };
      return { t: 'var', name: t.name };
    }
    throw new ParseError('expressão inválida');
  }

  const ast = expr();
  if (p < toks.length) throw new ParseError('sobra texto no fim');
  return ast;
}

export function variables(ast: Ast, acc = new Set<string>()): Set<string> {
  if (ast.t === 'var') acc.add(ast.name);
  else if (ast.t === 'neg' || ast.t === 'fn') variables(ast.a, acc);
  else if (ast.t === 'bin') { variables(ast.a, acc); variables(ast.b, acc); }
  return acc;
}

export function evaluate(ast: Ast, env: Record<string, number>): number {
  switch (ast.t) {
    case 'num': return ast.v;
    case 'var': {
      if (!(ast.name in env)) return NaN;
      return env[ast.name];
    }
    case 'neg': return -evaluate(ast.a, env);
    case 'fn': return FUNCTIONS[ast.name](evaluate(ast.a, env));
    case 'bin': {
      const a = evaluate(ast.a, env);
      const b = evaluate(ast.b, env);
      switch (ast.op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
        case '^': return Math.pow(a, b);
      }
    }
  }
}

function close(a: number, b: number, tol = 0): boolean {
  if (!Number.isFinite(a) || !Number.isFinite(b)) return false;
  const eps = Math.max(tol, 1e-9 * Math.max(1, Math.abs(a), Math.abs(b)));
  return Math.abs(a - b) <= eps;
}

/** Valor numérico de uma resposta ("0,75", "3/4", "sqrt(2)", "2^3"). NaN se inválida. */
export function numericValue(input: string): number {
  try {
    const ast = parse(input);
    if (variables(ast).size > 0) return NaN;
    return evaluate(ast, {});
  } catch {
    return NaN;
  }
}

export function numericEqual(given: string, expected: string | number, tolerance = 0): boolean {
  const g = numericValue(given);
  const e = typeof expected === 'number' ? expected : numericValue(expected);
  return close(g, e, tolerance);
}

// Gerador pseudoaleatório determinístico (resultados reproduzíveis)
function lcg(seed: number) {
  let s = seed >>> 0;
  return () => {
    s = (Math.imul(s, 1664525) + 1013904223) >>> 0;
    return s / 4294967296;
  };
}

/** Equivalência algébrica por avaliação em pontos amostrados. */
export function algebraicEqual(given: string, expected: string): boolean {
  let a: Ast, b: Ast;
  try {
    a = parse(given);
    b = parse(expected);
  } catch {
    return false;
  }
  const vars = [...new Set([...variables(a), ...variables(b)])].sort();
  const rand = lcg(12345);
  let valid = 0;
  for (let i = 0; i < 40 && valid < 8; i++) {
    const env: Record<string, number> = {};
    for (const v of vars) {
      // alterna entre positivos e negativos, evita valores "redondos" para não mascarar diferenças
      const sign = i % 3 === 0 ? -1 : 1;
      env[v] = sign * (0.37 + rand() * 3.1);
    }
    const x = evaluate(a, env);
    const y = evaluate(b, env);
    if (!Number.isFinite(x) || !Number.isFinite(y)) continue; // fora do domínio: ignora o ponto
    if (!close(x, y, 1e-7)) return false;
    valid++;
  }
  return valid >= 4;
}

// ---------- Interface por tipo de exercício ----------
export type ExerciseType =
  | 'multiple_choice' | 'numeric' | 'algebraic' | 'true_false' | 'written' | 'word_problem';

export interface Expected {
  choice?: string;          // escolha múltipla: id da opção
  value?: number | string;  // numérica
  expression?: string;      // algébrica
  accepted?: string[];      // formas alternativas aceites (algébrica/numérica)
  boolean?: boolean;        // verdadeiro/falso
}

export interface Verdict {
  graded: boolean;          // false = precisa de revisão humana
  correct: boolean;
}

export function validate(
  type: ExerciseType, expected: Expected, given: unknown, tolerance = 0,
): Verdict {
  const text = typeof given === 'string' ? given : typeof given === 'number' ? String(given) : '';
  switch (type) {
    case 'multiple_choice':
      return {
        graded: true,
        correct: typeof given === 'string' && !!expected.choice &&
          given.trim().toLowerCase() === expected.choice.trim().toLowerCase(),
      };
    case 'true_false':
      return { graded: true, correct: typeof given === 'boolean' && given === expected.boolean };
    case 'numeric': {
      const targets = [expected.value, ...(expected.accepted ?? [])].filter((v) => v !== undefined);
      return { graded: true, correct: targets.some((t) => numericEqual(text, t as string | number, tolerance)) };
    }
    case 'algebraic': {
      const targets = [expected.expression, ...(expected.accepted ?? [])].filter((v): v is string => !!v);
      return { graded: true, correct: targets.some((t) => algebraicEqual(text, t)) };
    }
    default:
      return { graded: false, correct: false }; // escrita/problema prático: revisão manual
  }
}

/** Regra de domínio: só "dominado" com acertos consistentes em dificuldades distintas + avaliação. */
export interface MasteryInput {
  attempts: number;
  correct: number;
  distinctDifficultiesCorrect: number;
  assessmentPassed: boolean;
}
export function isMastered(m: MasteryInput): boolean {
  if (m.attempts < 5) return false;
  const accuracy = m.correct / m.attempts;
  return accuracy >= 0.8 && m.distinctDifficultiesCorrect >= 3 && m.assessmentPassed;
}

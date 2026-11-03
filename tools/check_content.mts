import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { validate } from '../shared/math-validator.ts';
const root = new URL('../content/', import.meta.url).pathname;
const files = readdirSync(root).filter((d) => existsSync(`${root}${d}`) && d.startsWith('nivel-'))
  .flatMap((d) => readdirSync(`${root}${d}`).filter((x) => x.endsWith('.json')).sort().map((x) => `${root}${d}/${x}`));
let n = 0, bad = 0;
for (const path of files) {
  const f = path.replace(root, '');
  const l = JSON.parse(readFileSync(path, 'utf8'));
  for (const k of ['introduction','intuition','definition','formulas','worked_example','guided_exercise','independent_exercise','challenge','assessment']) {
    if (!l.blocks?.[k] || String(l.blocks[k]).length < 40) { bad++; console.log('BLOCO EM FALTA/CURTO', f, k); }
  }
  if (l.exercises.length < 8) { bad++; console.log('POUCOS EXERCÍCIOS', f, l.exercises.length); }
  for (const e of l.exercises) {
    n++;
    const a = e.answer;
    const givens: unknown[] = e.type === 'multiple_choice' ? [a.choice] : e.type === 'true_false' ? [a.boolean]
      : [a.value, ...(a.accepted ?? [])];
    for (const g of givens) {
      const v = validate(e.type, a, g, e.tolerance);
      if (!v.graded || !v.correct) { bad++; console.log('FALHA', f, e.statement, JSON.stringify(g)); }
    }
    // respostas erradas típicas têm de ser rejeitadas
    if (e.type === 'numeric') {
      const wrong = validate(e.type, a, '9999', e.tolerance);
      if (wrong.correct) { bad++; console.log('ACEITOU ERRADA', f, e.statement); }
    }
    if (e.type === 'multiple_choice' && !e.options.some((o: {id: string}) => o.id === a.choice)) { bad++; console.log('OPÇÃO INEXISTENTE', f); }
  }
}
console.log(`${n} exercícios verificados contra o validador do site; falhas: ${bad}`);
process.exit(bad ? 1 : 0);

import { readFileSync, readdirSync } from 'node:fs';
import { validate } from '../shared/math-validator.ts';
const dir = '../content/nivel-1';
let n = 0, bad = 0;
for (const f of readdirSync(dir).filter((x) => x.endsWith('.json')).sort()) {
  const l = JSON.parse(readFileSync(`${dir}/${f}`, 'utf8'));
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

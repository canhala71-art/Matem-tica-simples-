import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  algebraicEqual, isMastered, numericEqual, numericValue, validate, parse,
} from './math-validator.ts';

test('numérica: vírgula decimal, fração e potência equivalem', () => {
  assert.equal(numericEqual('0,75', '3/4'), true);
  assert.equal(numericEqual('2^3', 8), true);
  assert.equal(numericEqual('sqrt(16)', 4), true);
  assert.equal(numericEqual('1/3', 0.333, 0.001), true);
  assert.equal(numericEqual('1/3', 0.333), false);
  assert.equal(numericEqual('0,76', '3/4'), false);
  assert.equal(numericEqual('50%', 50), true); // % ignorado como unidade
});

test('numérica: entradas inválidas são falsas, nunca lançam', () => {
  assert.ok(Number.isNaN(numericValue('')));
  assert.ok(Number.isNaN(numericValue('abc+')));
  assert.ok(Number.isNaN(numericValue('2x')));
  assert.equal(numericEqual('1/0', 1), false);
});

test('algébrica: formas equivalentes', () => {
  assert.equal(algebraicEqual('2(x+1)', '2x+2'), true);
  assert.equal(algebraicEqual('(x+1)^2', 'x^2+2x+1'), true);
  assert.equal(algebraicEqual('x^2-1', '(x-1)(x+1)'), true);
  assert.equal(algebraicEqual('2 x^2', 'x*x*2'), true);
  assert.equal(algebraicEqual('x−1', '-1+x'), true); // sinal unicode
  assert.equal(algebraicEqual('sin(x)^2+cos(x)^2', '1'), true);
  assert.equal(algebraicEqual('x-x', '0'), true);
  assert.equal(algebraicEqual('(x^2-1)/(x-1)', 'x+1'), true);
});

test('algébrica: formas diferentes são rejeitadas', () => {
  assert.equal(algebraicEqual('x^2+1', '(x+1)^2'), false);
  assert.equal(algebraicEqual('2x+1', '2x+2'), false);
  assert.equal(algebraicEqual('x+y', 'x+z'), false);
  assert.equal(algebraicEqual('(x+', 'x'), false);
  assert.equal(algebraicEqual('', 'x'), false);
});

test('multiplicação implícita e precedência', () => {
  assert.equal(algebraicEqual('3x^2', '3*(x^2)'), true);
  assert.equal(algebraicEqual('-x^2', '-(x^2)'), true);
  assert.equal(algebraicEqual('-x^2', '(-x)^2'), false);
  assert.equal(algebraicEqual('2^3^2', '2^9'), true); // potência associa à direita
  assert.ok(parse('2(x+1)'));
});

test('validate: escolha múltipla e verdadeiro/falso', () => {
  assert.deepEqual(validate('multiple_choice', { choice: 'b' }, ' B '), { graded: true, correct: true });
  assert.deepEqual(validate('multiple_choice', { choice: 'b' }, 'c'), { graded: true, correct: false });
  assert.deepEqual(validate('true_false', { boolean: false }, false), { graded: true, correct: true });
  assert.deepEqual(validate('true_false', { boolean: false }, 'false'), { graded: true, correct: false });
});

test('validate: numérica com formas aceites e tolerância', () => {
  const exp = { value: 0.75, accepted: ['75%'] };
  assert.equal(validate('numeric', exp, '3/4').correct, true);
  assert.equal(validate('numeric', exp, '0,7').correct, false);
  assert.equal(validate('numeric', { value: 3.14 }, '3,1416', 0.01).correct, true);
});

test('validate: escrita precisa de revisão manual', () => {
  assert.deepEqual(validate('written', {}, 'resposta'), { graded: false, correct: false });
});

test('domínio: exige acertos consistentes, dificuldades distintas e avaliação', () => {
  assert.equal(isMastered({ attempts: 10, correct: 9, distinctDifficultiesCorrect: 3, assessmentPassed: true }), true);
  assert.equal(isMastered({ attempts: 10, correct: 9, distinctDifficultiesCorrect: 3, assessmentPassed: false }), false);
  assert.equal(isMastered({ attempts: 3, correct: 3, distinctDifficultiesCorrect: 3, assessmentPassed: true }), false);
  assert.equal(isMastered({ attempts: 10, correct: 6, distinctDifficultiesCorrect: 4, assessmentPassed: true }), false);
  assert.equal(isMastered({ attempts: 10, correct: 9, distinctDifficultiesCorrect: 1, assessmentPassed: true }), false);
});

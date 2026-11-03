export const CATEGORIES: [string, string][] = [
  ['matematica_basica', 'Matemática básica'],
  ['aritmetica', 'Aritmética'],
  ['algebra', 'Álgebra'],
  ['geometria', 'Geometria'],
  ['trigonometria', 'Trigonometria'],
  ['funcoes', 'Funções'],
  ['estatistica', 'Estatística'],
  ['probabilidade', 'Probabilidade'],
  ['matematica_avancada', 'Matemática avançada'],
  ['preparacao_exames', 'Preparação para exames'],
];
export const DIFFICULTIES: [string, string][] = [['facil', 'Fácil'], ['intermedio', 'Intermédio'], ['avancado', 'Avançado']];
export const catName = (k: string | null) => CATEGORIES.find(([v]) => v === k)?.[1] ?? 'Todas as categorias';
export const diffName = (k: string | null) => DIFFICULTIES.find(([v]) => v === k)?.[1] ?? 'Todas';

export interface QuizQuestion { id: string; statement: string; options: string[]; category: string; difficulty: string }
export interface AnswerResult { is_correct: boolean; correct_index: number; explanation: string }
export interface QuizSummary {
  correct: number; wrong: number; total: number; points: number; seconds: number; percent: number;
  details: { statement: string; options: string[]; chosen: number; is_correct: boolean; correct_index: number; explanation: string }[];
}

export function grade(percent: number): string {
  if (percent >= 90) return 'Excelente';
  if (percent >= 75) return 'Muito bom';
  if (percent >= 50) return 'Bom, mas dá para melhorar';
  return 'Precisas de praticar mais';
}
export function encourage(percent: number): string {
  if (percent >= 90) return 'Isso foi brilhante! Já pensaste em desafiar um nível acima?';
  if (percent >= 75) return 'Estás no caminho certo. Revê só os erros e voltas ainda mais forte.';
  if (percent >= 50) return 'Já tens uma boa base. Os erros são onde se aprende mais: lê as explicações.';
  return 'Calma, é assim que se começa. Lê as explicações com atenção e tenta de novo, vais ver a diferença.';
}
export const mmss = (s: number) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;

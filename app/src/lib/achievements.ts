export interface Stats {
  attempts: number; correct: number; bestStreak: number;
  lessonsDone: number; tests: number; bestScore: number; perfectTests: number;
  subjectsPassed: number; examPassed: boolean; toolRuns: number;
}
export interface Badge { id: string; icon: string; title: string; desc: string; cur: number; target: number }

const b = (id: string, icon: string, title: string, desc: string, cur: number, target: number): Badge =>
  ({ id, icon, title, desc, cur: Math.min(cur, target), target });

export function computeBadges(s: Stats): Badge[] {
  const acc = s.attempts >= 20 ? s.correct / s.attempts : 0;
  return [
    b('ex1', '🌱', 'Primeiro passo', 'Resolve o teu primeiro exercício', s.attempts, 1),
    b('ex10', '✏️', 'Aquecimento', 'Resolve 10 exercícios', s.attempts, 10),
    b('ex50', '📘', 'Em ritmo', 'Resolve 50 exercícios', s.attempts, 50),
    b('ex100', '💯', 'Centenário', 'Resolve 100 exercícios', s.attempts, 100),
    b('ex500', '🚀', 'Máquina de calcular', 'Resolve 500 exercícios', s.attempts, 500),
    b('acc', '🎯', 'Pontaria', 'Tem 80% de acertos ou mais, com pelo menos 20 exercícios', Math.round(acc * 100), 80),
    b('st3', '🔥', 'Três dias seguidos', 'Estuda 3 dias seguidos', s.bestStreak, 3),
    b('st7', '🏅', 'Uma semana inteira', 'Estuda 7 dias seguidos', s.bestStreak, 7),
    b('st14', '🏆', 'Duas semanas de ferro', 'Estuda 14 dias seguidos', s.bestStreak, 14),
    b('l1', '📖', 'Primeira aula', 'Conclui uma aula', s.lessonsDone, 1),
    b('l10', '📚', 'Leitor dedicado', 'Conclui 10 aulas', s.lessonsDone, 10),
    b('l25', '🎓', 'Quase lá', 'Conclui 25 aulas', s.lessonsDone, 25),
    b('t1', '📝', 'Primeiro teste', 'Faz um teste', s.tests, 1),
    b('t10', '✅', 'Aprovado', 'Tira 10 ou mais num teste (nota 0–20)', s.bestScore, 10),
    b('t16', '⭐', 'Muito bom', 'Tira 16 ou mais num teste', s.bestScore, 16),
    b('t20', '🌟', 'Nota máxima', 'Tira 20 num teste', s.perfectTests, 1),
    b('sp3', '🧩', 'Três temas ganhos', 'Passa na avaliação final de 3 temas', s.subjectsPassed, 3),
    b('sp9', '👑', 'Todos os temas', 'Passa na avaliação final dos 9 temas do Nível 1', s.subjectsPassed, 9),
    b('exam', '🏛️', 'Mestre do Nível 1', 'Passa no exame final do Nível 1', s.examPassed ? 1 : 0, 1),
    b('tool1', '🧰', 'Explorador', 'Guarda um resultado numa ferramenta', s.toolRuns, 1),
    b('tool10', '🛠️', 'Engenheiro', 'Guarda 10 resultados nas ferramentas', s.toolRuns, 10),
  ];
}

/** Maior sequência de dias consecutivos com atividade. */
export function bestStreak(dates: string[]): number {
  const days = Array.from(new Set(dates.map((d) => { const x = new Date(d); return Math.floor(new Date(x.getFullYear(), x.getMonth(), x.getDate()).getTime() / 86400000 + 0.5); }))).sort((a, b) => a - b);
  let best = 0, run = 0;
  for (let i = 0; i < days.length; i++) {
    run = i > 0 && days[i] === days[i - 1] + 1 ? run + 1 : 1;
    if (run > best) best = run;
  }
  return best;
}

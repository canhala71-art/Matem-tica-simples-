-- Estrutura inicial: percurso, 6 níveis e disciplinas (só títulos, SEM conteúdo matemático).
-- Tudo entra como rascunho: o administrador publica pelo painel.
insert into public.learning_paths (slug, title, description, position)
values ('matematica', 'Matemática', 'Do básico à especialização', 1);

insert into public.levels (path_id, number, slug, title, position)
select p.id, v.number, v.slug, v.title, v.number
from public.learning_paths p,
  (values
    (1, 'nivel-1-fundamentos', 'Nível 1 — Fundamentos'),
    (2, 'nivel-2-matematica-basica', 'Nível 2 — Matemática Básica'),
    (3, 'nivel-3-ensino-secundario', 'Nível 3 — Ensino Secundário'),
    (4, 'nivel-4-preparacao-academica', 'Nível 4 — Preparação Académica'),
    (5, 'nivel-5-universidade', 'Nível 5 — Universidade'),
    (6, 'nivel-6-especializacao', 'Nível 6 — Especialização')
  ) as v(number, slug, title)
where p.slug = 'matematica';

insert into public.subjects (level_id, slug, title, position)
select l.id, s.slug, s.title, s.position
from public.levels l
join (values
  (1, 'numeros-naturais', 'Números naturais', 1),
  (1, 'numeros-inteiros', 'Números inteiros', 2),
  (1, 'operacoes-basicas', 'Operações básicas', 3),
  (1, 'tabuada', 'Tabuada', 4),
  (1, 'fracoes', 'Frações', 5),
  (1, 'numeros-decimais', 'Números decimais', 6),
  (1, 'percentagens', 'Percentagens', 7),
  (1, 'potencias', 'Potências', 8),
  (1, 'raizes', 'Raízes', 9),
  (2, 'expressoes-numericas', 'Expressões numéricas', 1),
  (2, 'divisibilidade', 'Divisibilidade', 2),
  (2, 'razao-e-proporcao', 'Razão e proporção', 3),
  (2, 'regra-de-tres', 'Regra de três', 4),
  (2, 'equacoes', 'Equações', 5),
  (2, 'inequacoes', 'Inequações', 6),
  (2, 'geometria', 'Geometria', 7),
  (2, 'medidas', 'Medidas', 8),
  (3, 'algebra', 'Álgebra', 1),
  (3, 'polinomios', 'Polinómios', 2),
  (3, 'sistemas-de-equacoes', 'Sistemas de equações', 3),
  (3, 'funcoes', 'Funções', 4),
  (3, 'trigonometria', 'Trigonometria', 5),
  (3, 'geometria-analitica', 'Geometria analítica', 6),
  (3, 'estatistica', 'Estatística', 7),
  (3, 'probabilidade', 'Probabilidade', 8),
  (4, 'exames', 'Exames', 1),
  (4, 'simulados', 'Simulados', 2),
  (4, 'problemas-de-raciocinio', 'Problemas de raciocínio', 3),
  (4, 'testes-cronometrados', 'Testes cronometrados', 4),
  (4, 'exames-de-admissao', 'Preparação para exames de admissão', 5),
  (5, 'calculo-diferencial', 'Cálculo diferencial', 1),
  (5, 'calculo-integral', 'Cálculo integral', 2),
  (5, 'algebra-linear', 'Álgebra linear', 3),
  (5, 'matrizes', 'Matrizes', 4),
  (5, 'vetores', 'Vetores', 5),
  (5, 'analise-matematica', 'Análise matemática', 6),
  (5, 'equacoes-diferenciais', 'Equações diferenciais', 7),
  (5, 'estatistica-avancada', 'Estatística avançada', 8),
  (6, 'matematica-discreta', 'Matemática discreta', 1),
  (6, 'analise-real', 'Análise real', 2),
  (6, 'otimizacao', 'Otimização', 3),
  (6, 'teoria-dos-numeros', 'Teoria dos números', 4),
  (6, 'probabilidade-avancada', 'Probabilidade avançada', 5),
  (6, 'matematica-aplicada', 'Matemática aplicada', 6)
) as s(level_number, slug, title, position) on s.level_number = l.number;

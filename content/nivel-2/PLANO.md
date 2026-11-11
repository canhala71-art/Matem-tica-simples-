# Nível 2 — Matemática Básica: auditoria e plano

## Auditoria (11/11/2026)
- Os 8 módulos já existem na base de dados, com os nomes pedidos, publicados e em ordem.
- Conteúdo atual: 3 aulas (Razão e proporção, Regra de três, Equações), 33 exercícios.
- Módulos vazios: Expressões numéricas, Divisibilidade, Inequações, Geometria, Medidas.
- Reutilizável (do Nível 1): importador de aulas por JSON (`mm_load_from_repo`), verificador de exercícios, leitor de exercícios (pista, tentar outra vez), testes 0–20, progresso por aula, jogo de associação, pesquisa, rever erros, percurso, conquistas.
- Em falta (novo): biblioteca de fórmulas com pesquisa, favoritos (aulas e fórmulas), conclusão de módulo, recomendação de revisão após erro.
- Riscos: textos longos de geometria precisam de figuras (usar SVG simples inline, sem imagens pesadas); sobreposição com aulas do Nível 1 (divisibilidade, MDC/MMC, potências, raízes) — o Nível 2 aprofunda, não repete.

## Estrutura proposta (≈57 aulas, ≥10 exercícios cada, 3 básicos / 4 intermédios / 3 avançados)
1. Expressões numéricas (6): conceito, elementos e ordem das operações; propriedades das operações; inteiros e racionais; frações e decimais em expressões; potências e raízes em expressões; expressões combinadas e simplificação.
2. Divisibilidade (7): divisão exata e não exata; divisores e múltiplos; critérios 2,3,4,5,6,8,9,10; critérios 11,12,15,25,100,1000; primos, compostos, pares, ímpares, árvore de fatores; MDC e MMC (métodos); aplicações e problemas.
3. Razão e proporção (7): razão e termos; razões equivalentes e simplificação; proporção e propriedade fundamental; propriedades das proporções; grandezas direta e inversamente proporcionais; escalas; velocidade média, densidade e percentagens.
4. Regra de três (5): conceito e identificação das grandezas; simples direta; simples inversa; composta; problemas com verificação (Angola).
5. Equações (8): igualdade, equação e princípios de equivalência; 1.º grau; parênteses; frações e denominadores; literais; problemas; 2.º grau incompletas e completas; discriminante, fórmula resolvente, soma e produto.
6. Inequações (6): desigualdades e propriedades; 1.º grau e inversão do sentido; parênteses e frações; reta real e intervalos; união, interseção e sistemas; 2.º grau e problemas.
7. Geometria (12): ponto, reta, plano, segmentos, paralelas e perpendiculares; ângulos; triângulos (classificação, soma dos ângulos); perímetro e área do triângulo; Pitágoras e relações métricas; quadriláteros; polígonos; circunferência e círculo; sector e coroa; prisma, cubo, paralelepípedo e pirâmide; cilindro, cone e esfera; Tales, semelhança, congruência, transformações e simetria.
8. Medidas (6): SI e grandezas; comprimento e massa; capacidade e volume; superfície e conversões quadradas e cúbicas; tempo, velocidade e temperatura; problemas com medidas.

## Ordem de execução
1. Módulos 3, 4, 5 (já têm base), depois 1, 2, 6, 8, 7 (o maior, por último).
2. Em cada módulo: gerador → verificação por cálculo → publicação → conferência.
3. Funcionalidades novas só depois de haver conteúdo: biblioteca de fórmulas, favoritos, conclusão de módulo.

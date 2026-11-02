"""Gera as aulas do Nível 1 (rascunho). Todas as respostas são calculadas com aritmética exata."""
import json
from fractions import Fraction as F
from math import lcm, isqrt, gcd

def L(x):  # fração em LaTeX
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    return ("-" if x < 0 else "") + "\\frac{" + str(abs(x.numerator)) + "}{" + str(x.denominator) + "}"
def T(x):  # texto simples a/b
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
def D(x, places=None):  # decimal em português (vírgula)
    x = F(x)
    s = f"{float(x):.10f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")
def DP(x):  # decimal com ponto, para a resposta
    x = F(x); return f"{float(x):.10f}".rstrip("0").rstrip(".")

def num(diff, comp, statement, value, expl, steps, accepted=None, answer_text=None):
    return {"type": "numeric", "difficulty": diff, "competency": comp, "statement": statement, "options": None,
            "answer": {"value": answer_text if answer_text is not None else T(value), "accepted": accepted or []},
            "tolerance": 0, "explanation": expl, "steps": steps}
def mc(diff, comp, statement, labels, correct, expl, steps):
    ids = "abcd"
    return {"type": "multiple_choice", "difficulty": diff, "competency": comp, "statement": statement,
            "options": [{"id": ids[i], "label": l} for i, l in enumerate(labels)],
            "answer": {"choice": ids[correct]}, "tolerance": 0, "explanation": expl, "steps": steps}
def tf(diff, comp, statement, truth, expl, steps):
    return {"type": "true_false", "difficulty": diff, "competency": comp, "statement": statement, "options": None,
            "answer": {"boolean": truth}, "tolerance": 0, "explanation": expl, "steps": steps}

BLOCK_ORDER = ["introduction", "intuition", "definition", "formulas", "worked_example",
               "guided_exercise", "independent_exercise", "challenge", "assessment"]
INDEP = "Resolve os exercícios abaixo sem ajuda e usa **Verificar** para ver se acertaste. Se errares, lê a resolução passo a passo e tenta outra vez."
ASSESS = "Esta competência só fica **dominada** quando acertas de forma consistente em exercícios de dificuldades diferentes e passas na avaliação. Rapidez não conta: conta perceber."

lessons = []

# ---------- 1. Frações: mesmo denominador ----------
C = "fracoes.soma_mesmo_denominador"
a, b = F(3, 8), F(2, 8); r1 = a + b
a2, b2 = F(5, 12), F(4, 12); r2 = a2 + b2
a3, b3 = F(2, 9), F(4, 9); r3 = a3 + b3
a4, b4 = F(3, 10), F(4, 10); r4 = a4 + b4
r5 = F(1, 6) + F(2, 6) + F(3, 6)
assert r1 == F(5, 8) and r2 == F(3, 4) and r3 == F(2, 3) and r4 == F(7, 10) and r5 == 1
lessons.append({
 "subject": "fracoes", "topic_title": "Soma e subtração de frações", "topic_slug": "fracoes-soma-subtracao",
 "lesson_title": "Somar frações com o mesmo denominador", "lesson_slug": "somar-fracoes-mesmo-denominador",
 "summary": "Aprende a somar frações cujas partes têm o mesmo tamanho.", "minutes": 15,
 "blocks": {
  "introduction": "Imagina uma pizza cortada em 8 fatias iguais. Tu comes 3 fatias e o teu amigo come 2. Quantas fatias comeram os dois? Esta pergunta simples é exatamente a soma de frações com o mesmo denominador.",
  "intuition": "O **denominador** diz em quantas partes iguais o todo foi dividido. O **numerador** diz quantas dessas partes estamos a contar. Se as fatias têm o mesmo tamanho (mesmo denominador), basta contá-las: 3 oitavos mais 2 oitavos dão 5 oitavos. O tamanho da fatia não muda, por isso o denominador fica igual.",
  "definition": "Para somar frações com o mesmo denominador, **somam-se os numeradores** e **mantém-se o denominador**. Se for possível, simplifica-se o resultado dividindo o numerador e o denominador pelo mesmo número.",
  "formulas": "$$\\frac{a}{c}+\\frac{b}{c}=\\frac{a+b}{c}$$\n\nPara simplificar, divide em cima e em baixo pelo mesmo número (por exemplo, $\\frac{6}{9}=\\frac{2}{3}$, porque dividimos por 3).",
  "worked_example": "**Exemplo 1.** $" + L(a3) .replace(L(a3), "\\frac{2}{9}+\\frac{4}{9}=\\frac{6}{9}=\\frac{2}{3}") + "$ (dividimos por 3).\n\n**Exemplo 2.** $\\frac{3}{10}+\\frac{1}{10}=\\frac{4}{10}=\\frac{2}{5}$ (dividimos por 2).",
  "guided_exercise": "Vamos fazer juntos $\\frac{1}{7}+\\frac{3}{7}$. Pergunta a ti próprio: 1) Os denominadores são iguais? Sim, são 7. 2) Soma os numeradores: 1+3=4. 3) Mantém o denominador: 7. Resultado: $\\frac{4}{7}$. Não dá para simplificar.",
  "independent_exercise": INDEP,
  "challenge": "Consegues somar **três** frações de uma só vez? O método é o mesmo: somas os três numeradores e manténs o denominador. Experimenta o último exercício.",
  "assessment": ASSESS},
 "exercises": [
  num(1, C, "Calcula $\\frac{3}{8}+\\frac{2}{8}$.", r1, "Os denominadores são iguais (8). Somam-se os numeradores: 3+2=5. O resultado é 5/8.",
      ["Os denominadores são iguais: 8.", "Soma os numeradores: 3+2=5.", "Mantém o denominador: $\\frac{5}{8}$."], ["0,625"]),
  num(2, C, "Calcula $\\frac{5}{12}+\\frac{4}{12}$ e simplifica o resultado.", r2, "5+4=9, logo 9/12. Dividindo por 3, fica 3/4.",
      ["Soma os numeradores: 5+4=9, e fica $\\frac{9}{12}$.", "O maior divisor comum de 9 e 12 é 3.", "Divide por 3: $\\frac{9}{12}=\\frac{3}{4}$."], ["9/12", "0,75"]),
  mc(2, C, "Quanto é $\\frac{2}{9}+\\frac{4}{9}$ na forma mais simples?", ["$\\frac{6}{18}$", "$\\frac{2}{3}$", "$\\frac{8}{9}$", "$\\frac{4}{9}$"], 1,
     "2+4=6, logo 6/9. Dividindo por 3, fica 2/3. A opção 6/18 é o erro de somar também os denominadores.",
     ["Soma os numeradores: 2+4=6, e fica $\\frac{6}{9}$.", "Simplifica dividindo por 3: $\\frac{2}{3}$."]),
  tf(2, C, "Ao somar $\\frac{1}{5}+\\frac{2}{5}$ somam-se também os denominadores, e o resultado é $\\frac{3}{10}$.", False,
     "Falso. O denominador mantém-se, porque o tamanho das partes não muda: 1/5+2/5=3/5.",
     ["Os denominadores não se somam.", "$\\frac{1}{5}+\\frac{2}{5}=\\frac{3}{5}$."]),
  num(2, C, "A Ana comeu $\\frac{3}{10}$ de uma pizza e o Beto comeu $\\frac{4}{10}$. Que fração da pizza comeram juntos?", r4,
      "Somam-se as frações: 3/10+4/10=7/10 da pizza.", ["Soma: $\\frac{3}{10}+\\frac{4}{10}$.", "3+4=7, mantém-se o 10: $\\frac{7}{10}$."], ["0,7"]),
  num(3, C, "Desafio: calcula $\\frac{1}{6}+\\frac{2}{6}+\\frac{3}{6}$.", r5, "1+2+3=6, logo 6/6, que é igual a 1 (a pizza inteira).",
      ["Soma os três numeradores: 1+2+3=6.", "Fica $\\frac{6}{6}$, que é 1 inteiro."], ["6/6"]),
 ]})

# ---------- 2. Frações: denominadores diferentes ----------
C = "fracoes.soma_denominadores_diferentes"
cases = [(F(1, 2), F(1, 3)), (F(3, 4), F(1, 6)), (F(2, 5), F(3, 10)), (F(5, 6), F(1, 3))]
rs = [x + y for x, y in cases]
assert rs == [F(5, 6), F(11, 12), F(7, 10), F(7, 6)] and lcm(4, 6) == 12
def steps_diff(x, y):
    m = lcm(x.denominator, y.denominator)
    x2 = F(x.numerator * (m // x.denominator), m); y2 = F(y.numerator * (m // y.denominator), m)
    nx, ny = x.numerator * (m // x.denominator), y.numerator * (m // y.denominator)
    s = x + y
    st = [f"O m.m.c. de {x.denominator} e {y.denominator} é {m}.",
          "Converte: $\\frac{" + str(x.numerator) + "}{" + str(x.denominator) + "}=\\frac{" + str(nx) + "}{" + str(m) + "}$ e $\\frac{" + str(y.numerator) + "}{" + str(y.denominator) + "}=\\frac{" + str(ny) + "}{" + str(m) + "}$.",
          "Soma: $\\frac{" + str(nx) + "}{" + str(m) + "}+\\frac{" + str(ny) + "}{" + str(m) + "}=\\frac{" + str(nx + ny) + "}{" + str(m) + "}$" + ("" if F(nx + ny, m) == s and s.denominator == m else ", que simplificado é $" + L(s) + "$.")]
    return st
lessons.append({
 "subject": "fracoes", "topic_title": "Soma e subtração de frações", "topic_slug": "fracoes-soma-subtracao",
 "lesson_title": "Somar frações com denominadores diferentes", "lesson_slug": "somar-fracoes-denominadores-diferentes",
 "summary": "Usa o mínimo múltiplo comum para somar frações com partes de tamanhos diferentes.", "minutes": 20,
 "blocks": {
  "introduction": "E se as fatias tiverem tamanhos diferentes? Não podemos somar metades com terços sem primeiro as pôr no mesmo tamanho. Nesta aula vais aprender a fazê-lo.",
  "intuition": "Para contar juntas partes de tamanhos diferentes, cortamos tudo em partes mais pequenas e iguais. Uma metade pode ser vista como 3 sextos, e um terço como 2 sextos. Juntos, dão 5 sextos.",
  "definition": "Para somar frações com denominadores diferentes: 1) encontra o **mínimo múltiplo comum (m.m.c.)** dos denominadores; 2) converte cada fração para esse denominador; 3) soma os numeradores; 4) simplifica, se der.",
  "formulas": "$$\\frac{a}{b}+\\frac{c}{d}=\\frac{a\\cdot\\frac{m}{b}+c\\cdot\\frac{m}{d}}{m},\\qquad m=\\text{m.m.c.}(b,d)$$\n\nPara converter, multiplica o numerador e o denominador pelo mesmo número: $\\frac{1}{2}=\\frac{1\\times 3}{2\\times 3}=\\frac{3}{6}$.",
  "worked_example": "**Exemplo 1.** $\\frac{1}{2}+\\frac{1}{3}$. O m.m.c. de 2 e 3 é 6. $\\frac{1}{2}=\\frac{3}{6}$ e $\\frac{1}{3}=\\frac{2}{6}$. Logo $\\frac{3}{6}+\\frac{2}{6}=\\frac{5}{6}$.\n\n**Exemplo 2.** $\\frac{3}{4}+\\frac{1}{6}$. O m.m.c. de 4 e 6 é 12. $\\frac{9}{12}+\\frac{2}{12}=\\frac{11}{12}$.",
  "guided_exercise": "Vamos fazer juntos $\\frac{1}{4}+\\frac{1}{3}$. O m.m.c. de 4 e 3 é 12. $\\frac{1}{4}=\\frac{3}{12}$ e $\\frac{1}{3}=\\frac{4}{12}$. Soma: $\\frac{3}{12}+\\frac{4}{12}=\\frac{7}{12}$.",
  "independent_exercise": INDEP,
  "challenge": "Quando a soma dá mais do que 1, a fração fica 'maior que o inteiro' (fração imprópria), por exemplo $\\frac{7}{6}$. Experimenta o último exercício.",
  "assessment": ASSESS},
 "exercises": [
  num(1, C, "Calcula $\\frac{1}{2}+\\frac{1}{3}$.", rs[0], "O m.m.c. de 2 e 3 é 6. 1/2=3/6 e 1/3=2/6, logo a soma é 5/6.", steps_diff(*cases[0])),
  num(2, C, "Calcula $\\frac{3}{4}+\\frac{1}{6}$.", rs[1], "O m.m.c. de 4 e 6 é 12. 3/4=9/12 e 1/6=2/12, logo a soma é 11/12.", steps_diff(*cases[1])),
  num(2, C, "Calcula $\\frac{2}{5}+\\frac{3}{10}$.", rs[2], "O m.m.c. de 5 e 10 é 10. 2/5=4/10, logo 4/10+3/10=7/10.", steps_diff(*cases[2]), ["0,7"]),
  mc(2, C, "Qual é o mínimo múltiplo comum de 4 e 6?", ["12", "24", "10", "2"], 0,
     "Os múltiplos de 4 são 4, 8, 12... e os de 6 são 6, 12... O primeiro comum é 12.", ["Múltiplos de 4: 4, 8, 12, 16...", "Múltiplos de 6: 6, 12, 18...", "O primeiro comum é 12."]),
  tf(2, C, "$\\frac{1}{2}+\\frac{1}{4}=\\frac{2}{6}$.", False,
     "Falso. Somar numeradores com numeradores e denominadores com denominadores é um erro. 1/2=2/4, logo 2/4+1/4=3/4.",
     ["Os denominadores são diferentes (2 e 4).", "$\\frac{1}{2}=\\frac{2}{4}$.", "$\\frac{2}{4}+\\frac{1}{4}=\\frac{3}{4}$."]),
  num(3, C, "Desafio: calcula $\\frac{5}{6}+\\frac{1}{3}$.", rs[3], "O m.m.c. de 6 e 3 é 6. 1/3=2/6, logo 5/6+2/6=7/6, que é 1 inteiro e 1/6.", steps_diff(*cases[3]), ["7/6", "1,1666667"]),
 ]})

# ---------- 3. Percentagens ----------
C = "percentagens.calcular_percentagem"
pc = [(10, 250), (25, 80), (15, 200), (50, 90)]
pr = [F(p * v, 100) for p, v in pc]
assert pr == [25, 20, 30, 45]
price, disc = 5000, 20; pay = price - F(disc * price, 100); assert pay == 4000
inc = 2500 + F(10 * 2500, 100); assert inc == 2750
lessons.append({
 "subject": "percentagens", "topic_title": "Percentagem de um valor", "topic_slug": "percentagens-de-um-valor",
 "lesson_title": "Calcular a percentagem de um valor", "lesson_slug": "calcular-percentagem-de-um-valor",
 "summary": "Descobre quanto é 10%, 25% ou 50% de um valor e aplica-o a descontos.", "minutes": 20,
 "blocks": {
  "introduction": "Descontos nas lojas, juros, notas de testes: as percentagens estão em todo o lado. A expressão 'por cento' quer dizer 'por cada cem'.",
  "intuition": "50% significa 50 em cada 100, ou seja, **metade**. 25% é **um quarto**. 10% é a **décima parte**: basta dividir por 10. Com estes atalhos consegues calcular muitas percentagens de cabeça.",
  "definition": "Uma percentagem $p\\%$ é a fração $\\frac{p}{100}$. Calcular $p\\%$ de um valor é multiplicar o valor por $\\frac{p}{100}$.",
  "formulas": "$$p\\%\\text{ de }V=\\frac{p}{100}\\times V$$\n\nAtalhos: **10%** → divide por 10. **50%** → divide por 2. **25%** → divide por 4.",
  "worked_example": "**Exemplo 1.** 10% de 250 = 250 ÷ 10 = 25.\n\n**Exemplo 2.** 20% de 60 = $\\frac{20}{100}\\times 60=12$.",
  "guided_exercise": "Vamos calcular 30% de 70. 10% de 70 é 7. Como 30% é três vezes 10%, fica 3 × 7 = 21.",
  "independent_exercise": INDEP,
  "challenge": "Um **aumento** de 10% também se calcula assim: calcula os 10% e soma ao valor inicial. Experimenta o último exercício.",
  "assessment": ASSESS},
 "exercises": [
  num(1, C, "Calcula 10% de 250.", pr[0], "10% é a décima parte: 250 ÷ 10 = 25.", ["10% = dividir por 10.", "250 ÷ 10 = 25."]),
  num(1, C, "Calcula 25% de 80.", pr[1], "25% é um quarto: 80 ÷ 4 = 20.", ["25% é um quarto.", "80 ÷ 4 = 20."]),
  num(2, C, "Calcula 15% de 200.", pr[2], "10% de 200 é 20 e 5% é 10, logo 15% é 30.", ["10% de 200 = 20.", "5% de 200 = 10.", "20 + 10 = 30."]),
  mc(1, C, "Quanto é 50% de 90?", ["45", "50", "40", "140"], 0, "50% é metade: 90 ÷ 2 = 45.", ["50% = metade.", "90 ÷ 2 = 45."]),
  tf(2, C, "100% de um número é metade desse número.", False, "Falso. 100% é o número todo. A metade é 50%.", ["100% = 100 em cada 100 = tudo.", "A metade é 50%."]),
  num(3, C, "Um telemóvel custa 5000 Kz e tem 20% de desconto. Quanto se paga? (responde só com o número)", pay,
      "20% de 5000 é 1000. O desconto tira 1000, e 5000−1000=4000 Kz.", ["20% de 5000: 5000 ÷ 5 = 1000.", "Preço final: 5000 − 1000 = 4000."]),
  num(3, C, "Desafio: um produto de 2500 Kz sobe 10%. Qual é o novo preço? (só o número)", inc,
      "10% de 2500 é 250. O novo preço é 2500+250=2750 Kz.", ["10% de 2500 = 250.", "2500 + 250 = 2750."]),
 ]})

# ---------- 4. Decimais ----------
C = "decimais.soma_subtracao"
d1 = F("2.5") + F("1.75"); d2 = F(10) - F("3.4"); d3 = F("0.6") + F("0.45"); d4 = F("3.2") + F("0.08"); d5 = F("2.4") + F("1.85")
assert d1 == F("4.25") and d2 == F("6.6") and d3 == F("1.05") and d4 == F("3.28") and d5 == F("4.25")
lessons.append({
 "subject": "numeros-decimais", "topic_title": "Operações com decimais", "topic_slug": "decimais-operacoes",
 "lesson_title": "Somar e subtrair números decimais", "lesson_slug": "somar-subtrair-decimais",
 "summary": "Soma e subtrai números com vírgula alinhando as casas decimais.", "minutes": 15,
 "blocks": {
  "introduction": "Preços, medidas e notas usam números com vírgula. Somar decimais é como somar números inteiros, mas com um cuidado: alinhar as vírgulas.",
  "intuition": "Cada casa depois da vírgula representa partes cada vez mais pequenas: décimas, centésimas, milésimas. Só podemos juntar unidades com unidades, décimas com décimas. Por isso alinhamos as vírgulas, para cada algarismo ficar na coluna certa.",
  "definition": "Para somar ou subtrair decimais: 1) escreve os números com as vírgulas **alinhadas**; 2) completa com zeros à direita se faltarem casas; 3) calcula como se fossem inteiros; 4) coloca a vírgula na mesma coluna.",
  "formulas": "$$2{,}50+1{,}75=4{,}25$$\n\nDica: $2{,}5$ e $2{,}50$ são o mesmo número. Acrescentar zeros à direita da parte decimal não muda o valor.",
  "worked_example": "**Exemplo 1.** $2{,}50+1{,}75$: 250 + 175 = 425, e com a vírgula alinhada fica $4{,}25$.\n\n**Exemplo 2.** $5{,}00-1{,}35$: 500 − 135 = 365, ou seja, $3{,}65$.",
  "guided_exercise": "Vamos fazer juntos $0{,}9+0{,}15$. Escreve $0{,}90+0{,}15$. Calcula 90 + 15 = 105, e fica $1{,}05$.",
  "independent_exercise": INDEP,
  "challenge": "Comparar decimais também é importante: $0{,}5$ é maior que $0{,}45$, mesmo que 45 seja maior que 5. Vê o exercício de verdadeiro ou falso.",
  "assessment": ASSESS},
 "exercises": [
  num(1, C, "Calcula $2{,}5+1{,}75$.", d1, "Alinhando as vírgulas: 2,50 + 1,75 = 4,25.", ["Escreve 2,50 para ter duas casas decimais.", "250 + 175 = 425.", "Fica 4,25."], answer_text=DP(d1)),
  num(1, C, "Calcula $10-3{,}4$.", d2, "10,0 − 3,4 = 6,6.", ["Escreve 10,0 − 3,4.", "100 − 34 = 66.", "Fica 6,6."], answer_text=DP(d2)),
  num(2, C, "Calcula $0{,}6+0{,}45$.", d3, "0,60 + 0,45 = 1,05.", ["Escreve 0,60 + 0,45.", "60 + 45 = 105.", "Fica 1,05."], answer_text=DP(d3)),
  mc(2, C, "Quanto é $3{,}2+0{,}08$?", ["3,28", "3,10", "4", "3,208"], 0, "3,20 + 0,08 = 3,28.", ["Escreve 3,20 + 0,08.", "320 + 8 = 328.", "Fica 3,28."]),
  tf(2, C, "$0{,}5$ é maior que $0{,}45$.", True, "Verdadeiro. 0,5 = 0,50, e 50 centésimas é mais que 45 centésimas.", ["Escreve 0,5 como 0,50.", "50 centésimas > 45 centésimas."]),
  num(3, C, "Uma tábua mede 2,4 m e outra 1,85 m. Quantos metros medem juntas? (só o número)", d5,
      "2,40 + 1,85 = 4,25 m.", ["Alinha: 2,40 + 1,85.", "240 + 185 = 425.", "Fica 4,25 m."], answer_text=DP(d5)),
 ]})

# ---------- 5. Potências ----------
C = "potencias.calcular"
p = [(2, 5), (3, 3), (10, 4), (5, 2), (2, 10), (2, 6)]
pv = [b_ ** e for b_, e in p]
assert pv == [32, 27, 10000, 25, 1024, 64] and 3 ** 4 == 81 and 10 ** 3 == 1000 and 2 ** 4 == 16
lessons.append({
 "subject": "potencias", "topic_title": "Potências de expoente natural", "topic_slug": "potencias-expoente-natural",
 "lesson_title": "O que é uma potência", "lesson_slug": "o-que-e-uma-potencia",
 "summary": "Escreve multiplicações repetidas de forma curta e calcula potências.", "minutes": 15,
 "blocks": {
  "introduction": "Escrever 2×2×2×2×2 é cansativo. As potências dão uma forma curta de escrever multiplicações repetidas.",
  "intuition": "$2^5$ lê-se 'dois elevado a cinco': multiplicas o 2 por si próprio 5 vezes. A **base** (2) é o número que se repete e o **expoente** (5) diz quantas vezes.",
  "definition": "$a^n=a\\times a\\times\\cdots\\times a$, com $n$ fatores iguais a $a$. Casos especiais: $a^1=a$ e, para $a\\neq 0$, $a^0=1$.",
  "formulas": "$$a^n=\\underbrace{a\\times a\\times\\cdots\\times a}_{n\\text{ vezes}}$$\n\nAtenção: $2^3$ **não** é $2\\times 3$. É $2\\times 2\\times 2=8$.",
  "worked_example": "**Exemplo 1.** $3^4=3\\times3\\times3\\times3=81$.\n\n**Exemplo 2.** $10^3=10\\times10\\times10=1000$. Repara: o expoente diz quantos zeros tem o resultado.",
  "guided_exercise": "Vamos calcular $2^4$ passo a passo: 2 × 2 = 4, depois 4 × 2 = 8, depois 8 × 2 = 16. Logo $2^4=16$.",
  "independent_exercise": INDEP,
  "challenge": "Uma bactéria duplica de hora a hora. Partindo de 1 bactéria, quantas há ao fim de 6 horas? Vê o último exercício.",
  "assessment": ASSESS},
 "exercises": [
  num(1, C, "Calcula $2^5$.", pv[0], "2×2×2×2×2 = 32.", ["2×2=4.", "4×2=8; 8×2=16; 16×2=32."]),
  num(1, C, "Calcula $3^3$.", pv[1], "3×3×3 = 27.", ["3×3=9.", "9×3=27."]),
  num(1, C, "Calcula $10^4$.", pv[2], "10×10×10×10 = 10000.", ["O expoente é 4: quatro zeros.", "Resultado: 10000."]),
  mc(1, C, "Quanto é $5^2$?", ["10", "25", "7", "52"], 1, "5² = 5×5 = 25. A opção 10 é o erro de multiplicar a base pelo expoente.", ["5² = 5×5.", "5×5 = 25."]),
  tf(2, C, "$2^3=6$.", False, "Falso. 2³ = 2×2×2 = 8. O erro comum é fazer 2×3.", ["2×2=4.", "4×2=8."]),
  tf(2, C, "Qualquer número diferente de zero elevado a 0 é igual a 1.", True, "Verdadeiro. Por definição, a⁰ = 1 quando a ≠ 0.", ["Por definição, $a^0=1$ se $a\\neq 0$."]),
  num(3, C, "Desafio: uma bactéria duplica a cada hora. Começando com 1, quantas há ao fim de 6 horas? (só o número)", pv[5],
      "Cada hora multiplica por 2: ao fim de 6 horas há 2⁶ = 64.", ["Hora 1: 2; hora 2: 4; hora 3: 8.", "Hora 4: 16; hora 5: 32; hora 6: 64.", "É $2^6=64$."]),
 ]})

# ---------- 6. Raízes ----------
C = "raizes.quadradas_exatas"
rr = [isqrt(n) for n in (49, 144, 225, 81, 64, 2025)]
assert rr == [7, 12, 15, 9, 8, 45] and all(isqrt(n) ** 2 == n for n in (49, 144, 225, 81, 64, 2025, 36, 121))
lessons.append({
 "subject": "raizes", "topic_title": "Raiz quadrada", "topic_slug": "raiz-quadrada",
 "lesson_title": "Raízes quadradas exatas", "lesson_slug": "raizes-quadradas-exatas",
 "summary": "Descobre o número que, multiplicado por si próprio, dá o valor da raiz.", "minutes": 15,
 "blocks": {
  "introduction": "Se um quadrado tem 25 m² de área, quanto mede o lado? Procuramos o número que, multiplicado por si próprio, dá 25.",
  "intuition": "A raiz quadrada desfaz o quadrado. Como $5^2=25$, a raiz quadrada de 25 é 5. É o caminho de volta.",
  "definition": "$\\sqrt{a}$ é o número **não negativo** $b$ tal que $b^2=a$. Quando $a$ é um **quadrado perfeito** (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144...), a raiz é um número inteiro.",
  "formulas": "$$\\sqrt{a}=b\\iff b^2=a\\quad(b\\geq 0)$$\n\nDica: aprende de cor os quadrados de 1 a 12. Ajudam muito.",
  "worked_example": "**Exemplo 1.** $\\sqrt{36}=6$, porque $6\\times6=36$.\n\n**Exemplo 2.** $\\sqrt{121}=11$, porque $11\\times11=121$.",
  "guided_exercise": "Vamos calcular $\\sqrt{64}$. Pergunta: que número vezes ele próprio dá 64? Experimenta 7×7=49 (pouco) e 8×8=64 (certo). Logo $\\sqrt{64}=8$.",
  "independent_exercise": INDEP,
  "challenge": "Números grandes também se resolvem por tentativas: $\\sqrt{2025}$ está entre 40 (1600) e 50 (2500). Experimenta o último exercício.",
  "assessment": ASSESS},
 "exercises": [
  num(1, C, "Calcula $\\sqrt{49}$.", rr[0], "7×7 = 49.", ["Procura um número que vezes ele próprio dê 49.", "7×7=49."]),
  num(2, C, "Calcula $\\sqrt{144}$.", rr[1], "12×12 = 144.", ["Experimenta 11×11=121 (pouco).", "12×12=144."]),
  num(2, C, "Calcula $\\sqrt{225}$.", rr[2], "15×15 = 225.", ["14×14=196 (pouco).", "15×15=225."]),
  mc(1, C, "Quanto é $\\sqrt{81}$?", ["8", "9", "18", "40,5"], 1, "9×9 = 81. A opção 40,5 é o erro de dividir por 2.", ["Procura n com n×n=81.", "9×9=81."]),
  tf(2, C, "$\\sqrt{16}=8$.", False, "Falso. √16 = 4, porque 4×4 = 16. O erro comum é dividir por 2.", ["4×4=16.", "Logo $\\sqrt{16}=4$."]),
  num(3, C, "Um terreno quadrado tem 64 m² de área. Quanto mede cada lado, em metros? (só o número)", rr[4],
      "O lado é √64 = 8 m.", ["Área = lado × lado = 64.", "Lado = √64 = 8."]),
  num(3, C, "Desafio: calcula $\\sqrt{2025}$.", rr[5], "45×45 = 2025.", ["Está entre 40 (1600) e 50 (2500).", "44×44=1936 (pouco).", "45×45=2025."]),
 ]})

# ---------- 7. Inteiros ----------
C = "inteiros.soma"
i1 = -5 + 8; i2 = 4 + (-9); i3 = -7 + (-3); i4 = -3 + 10; i5 = -3 + 9
assert (i1, i2, i3, i4, i5) == (3, -5, -10, 7, 6)
lessons.append({
 "subject": "numeros-inteiros", "topic_title": "Operações com inteiros", "topic_slug": "inteiros-operacoes",
 "lesson_title": "Somar números inteiros", "lesson_slug": "somar-numeros-inteiros",
 "summary": "Soma números positivos e negativos usando a reta numérica.", "minutes": 20,
 "blocks": {
  "introduction": "Temperaturas abaixo de zero, dívidas, saldos negativos: os números inteiros incluem positivos e negativos. Nesta aula aprendes a somá-los.",
  "intuition": "Na reta numérica, somar um número positivo é andar para a **direita**, e somar um negativo é andar para a **esquerda**. Em $-5+8$, começas em −5 e andas 8 para a direita: chegas a 3.",
  "definition": "**Sinais iguais:** somam-se os valores e mantém-se o sinal. **Sinais diferentes:** subtrai-se o valor menor do maior, e fica o sinal do número com maior valor (sem contar o sinal).",
  "formulas": "$$(-a)+(-b)=-(a+b)$$\n$$(-a)+b=b-a\\quad\\text{(se }b>a\\text{)}$$",
  "worked_example": "**Exemplo 1.** $-7+(-3)=-10$ (sinais iguais: 7+3=10, fica negativo).\n\n**Exemplo 2.** $4+(-9)=-5$ (sinais diferentes: 9−4=5, e o 9 é maior e negativo).",
  "guided_exercise": "Vamos fazer $-2+6$. Os sinais são diferentes. 6−2=4. O 6 é maior e positivo, logo o resultado é $4$.",
  "independent_exercise": INDEP,
  "challenge": "Numa manhã a temperatura é de −3 °C e sobe 9 graus. Qual é a nova temperatura? Vê o último exercício.",
  "assessment": ASSESS},
 "exercises": [
  num(1, C, "Calcula $-5+8$.", i1, "Começa em −5 e anda 8 para a direita: 3.", ["Sinais diferentes: 8−5=3.", "O 8 é maior e positivo: 3."]),
  num(2, C, "Calcula $4+(-9)$.", i2, "Sinais diferentes: 9−4=5, e como o 9 é negativo o resultado é −5.", ["9−4=5.", "O número de maior valor é −9, logo −5."]),
  num(2, C, "Calcula $-7+(-3)$.", i3, "Sinais iguais: 7+3=10, e mantém-se o sinal negativo: −10.", ["Sinais iguais: soma 7+3=10.", "Mantém o sinal: −10."]),
  mc(2, C, "Quanto é $-3+10$?", ["-7", "7", "13", "-13"], 1, "Sinais diferentes: 10−3=7, e o 10 é positivo, logo 7.", ["10−3=7.", "O 10 é maior e positivo: 7."]),
  tf(2, C, "$-8$ é maior que $-2$.", False, "Falso. Na reta numérica, −2 está à direita de −8, por isso −2 é maior.", ["Na reta, o que está mais à direita é maior.", "−2 está à direita de −8."]),
  num(3, C, "Desafio: a temperatura de −3 °C sobe 9 graus. Qual é a nova temperatura? (só o número)", i5,
      "−3 + 9 = 6 °C.", ["Começa em −3 e anda 9 para a direita.", "−3 + 9 = 6."]),
 ]})

# ---------- saída ----------
import sys, os
out = sys.argv[1] if len(sys.argv) > 1 else "."
for n, ls in enumerate(lessons, 1):
    for e in ls["exercises"]:
        assert e["statement"] and e["explanation"] and e["steps"]
    with open(os.path.join(out, f"{n:02d}-{ls['lesson_slug']}.json"), "w", encoding="utf-8") as f:
        json.dump(ls, f, ensure_ascii=False, indent=1)
print(f"{len(lessons)} aulas, {sum(len(l['exercises']) for l in lessons)} exercícios. Todas as respostas verificadas.")

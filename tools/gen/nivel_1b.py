"""Enriquece as 7 lições antigas do Nível 1: novos blocos (>=5 exemplos) e exercícios extra (>=12 no total).
Todas as respostas são calculadas e verificadas com asserts."""
from common import *
import json, os, math

DIR = os.path.join(ROOT, 'nivel-1')
def load(prefix):
    fn = [f for f in os.listdir(DIR) if f.startswith(prefix)][0]
    return fn, json.load(open(os.path.join(DIR, fn), encoding='utf-8'))
def save(fn, d):
    assert len(d['exercises']) >= 12, (fn, len(d['exercises']))
    assert d['blocks']['worked_example'].count('**Exemplo') >= 5, fn
    for k, v in d['blocks'].items(): assert len(v) > 60, (fn, k)
    json.dump(d, open(os.path.join(DIR, fn), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
def fr(n, d): return f"\\frac{{{n}}}{{{d}}}"
def dec(x, nd=2):
    return f"{x:.{nd}f}".replace('.', '{,}')
def blocks(d, **kw): d['blocks'].update(kw)

# ---------- 01 Somar frações com o mesmo denominador ----------
fn, d = load('01-')
blocks(d,
 introduction="**Objetivos:** somar e subtrair frações com o mesmo denominador, simplificar o resultado e reconhecer quando dá mais do que um inteiro. **Pré-requisitos:** saber o que é uma fração (numerador e denominador) e a tabuada.\n\nNa vida real aparecem frações a toda a hora: um terço de um bolo, três quartos de um depósito, dois quintos de um terreno. Quando as partes são do **mesmo tamanho**, somá-las é tão natural como contar: três fatias mais duas fatias dão cinco fatias.",
 intuition="Imagina uma pizza cortada em 8 fatias iguais. Cada fatia é $\\frac{1}{8}$ da pizza. Se comes 3 fatias e depois 2, comeste 5 fatias, ou seja $\\frac{5}{8}$.\n\nO que contámos? **Fatias.** O tamanho da fatia (o denominador 8) não mudou, só mudou o número de fatias (o numerador). É por isso que somamos os numeradores e **mantemos** o denominador.\n\nSe a soma der um número de fatias maior que o total da pizza, passaste de um inteiro: $\\frac{12}{8}$ é uma pizza e mais meia. Depois, simplificas dividindo numerador e denominador pelo mesmo número.\n\n**Erros comuns:** (1) somar também os denominadores ($\\frac{1}{5}+\\frac{2}{5}=\\frac{3}{10}$ está errado); (2) esquecer de simplificar; (3) trocar a subtração, fazendo o menor menos o maior sem reparar no sinal.",
 definition="Duas frações têm o **mesmo denominador** quando as partes em que o inteiro foi dividido são iguais. Nesse caso, a **soma** e a **diferença** fazem-se só com os numeradores. Uma fração é **irredutível** (ou simplificada) quando o numerador e o denominador não têm divisores comuns além de 1. Uma fração é **imprópria** quando o numerador é maior ou igual ao denominador (vale 1 ou mais).",
 formulas="$$\\frac{a}{c}+\\frac{b}{c}=\\frac{a+b}{c}\\qquad\\frac{a}{c}-\\frac{b}{c}=\\frac{a-b}{c}\\qquad(c\\neq0)$$\n\nSimplificar: divide numerador e denominador pelo seu máximo divisor comum (m.d.c.).\n\nFração imprópria para número misto: $\\dfrac{12}{8}=1+\\dfrac{4}{8}=1\\dfrac{1}{2}$.",
 worked_example="**Exemplo 1.** $\\frac{2}{9}+\\frac{4}{9}=\\frac{6}{9}=\\frac{2}{3}$ (dividimos por 3).\n\n**Exemplo 2.** $\\frac{3}{10}+\\frac{1}{10}=\\frac{4}{10}=\\frac{2}{5}$ (dividimos por 2).\n\n**Exemplo 3 (subtração).** $\\frac{7}{12}-\\frac{5}{12}=\\frac{2}{12}=\\frac{1}{6}$.\n\n**Exemplo 4 (passa de um inteiro).** $\\frac{5}{8}+\\frac{7}{8}=\\frac{12}{8}=\\frac{3}{2}=1\\frac{1}{2}$.\n\n**Exemplo 5 (três parcelas).** $\\frac{1}{6}+\\frac{2}{6}+\\frac{3}{6}=\\frac{6}{6}=1$.\n\n**Aplicação.** Num depósito de água, na segunda-feira gastaram-se $\\frac{3}{20}$ e na terça $\\frac{5}{20}$. No total gastaram $\\frac{8}{20}=\\frac{2}{5}$ do depósito, e sobram $\\frac{3}{5}$.",
 guided_exercise="Resolve connosco: **o Beto leu $\\frac{3}{14}$ de um livro no sábado e $\\frac{4}{14}$ no domingo. Que fração do livro já leu?**\n\n1) Os denominadores são iguais (14), por isso somam-se os numeradores: 3 + 4 = 7.\n\n2) Fica $\\frac{7}{14}$.\n\n3) Simplifica: 7 e 14 dividem-se por 7, dá $\\frac{1}{2}$.\n\n4) Verifica: leu metade do livro, o que faz sentido porque 7 é metade de 14 ✓.",
 challenge="**Desafio.** Uma receita pede $\\frac{3}{8}$ de litro de leite e outra $\\frac{7}{8}$. Se juntares as duas, chega 1 litro? E quanto sobra ou falta? Escreve o resultado como número misto e explica porquê, com um desenho de garrafas se ajudar.",
 assessment="Consideras a competência dominada quando consegues: (1) somar e subtrair frações de igual denominador sem somar os denominadores; (2) simplificar sempre o resultado; (3) reconhecer e converter frações impróprias em números mistos; (4) resolver problemas com frações de uma quantidade total.")
ex = d['exercises']
C = 'fracoes.soma_mesmo_denominador'
pairs = [(1,5,2,5),(2,7,3,7),(5,9,2,9),(4,15,6,15),(7,20,9,20),(3,11,5,11)]
for a,b,c,e in pairs:
    r = F(a,b)+F(c,e); assert b==e
    ex.append(num(1, C, f"Calcula ${fr(a,b)}+{fr(c,e)}$ e simplifica o resultado.", r, f"Mantém o denominador {b} e soma os numeradores: {a} + {c} = {a+c}, dando ${fr(a+c,b)}$" + (f", que simplifica para ${fr(r.numerator,r.denominator)}$." if F(a+c,b).denominator!=b else "."), [f"Denominador comum: {b}.", f"{a} + {c} = {a+c}.", "Simplifica se for possível."]))
for a,b,c in [(9,13,4),(11,16,5),(7,9,2)]:
    r = F(a,b)-F(c,b)
    ex.append(num(2, 'fracoes.subtracao_mesmo_denominador', f"Calcula ${fr(a,b)}-{fr(c,b)}$ na forma mais simples.", r, f"Subtraem-se os numeradores: {a} − {c} = {a-c}. Fica ${fr(a-c,b)}$" + (f" = ${fr(r.numerator,r.denominator)}$." if r.denominator!=b else "."), [f"{a} − {c} = {a-c}.", "Mantém o denominador e simplifica."]))
r = F(7,10)+F(8,10); assert r == F(3,2)
ex.append(num(2, C, "Calcula $\\frac{7}{10}+\\frac{8}{10}$ e escreve o resultado como fração simplificada.", r, "7 + 8 = 15, logo $\\frac{15}{10}=\\frac{3}{2}$ (dividindo por 5). É maior que 1, é uma fração imprópria.", ["15/10.", "Divide por 5: 3/2."]))
ex.append(tf(2, C, "$\\frac{4}{9}+\\frac{2}{9}=\\frac{6}{18}$.", False, "Só se somam os numeradores; o denominador mantém-se: $\\frac{6}{9}=\\frac{2}{3}$.", ["4 + 2 = 6.", "Denominador continua 9."]))
ex.append(tf(2, C, "$\\frac{3}{5}-\\frac{1}{5}=\\frac{2}{5}$.", True, "3 − 1 = 2 e o denominador mantém-se: $\\frac{2}{5}$.", ["3 − 1 = 2."]))
ex.append(mc(2, C, "Qual é a fração irredutível de $\\frac{5}{12}+\\frac{1}{12}$?", ["$\\frac{1}{2}$", "$\\frac{6}{24}$", "$\\frac{5}{12}$", "$\\frac{1}{3}$"], 0, "5 + 1 = 6, logo $\\frac{6}{12}=\\frac{1}{2}$.", ["6/12.", "Divide por 6: 1/2."]))
r = F(3,20)+F(5,20); assert r == F(2,5)
ex.append(num(2, C, "Num depósito gastaram-se $\\frac{3}{20}$ na segunda e $\\frac{5}{20}$ na terça. Que fração do depósito foi gasta? (forma mais simples)", r, "3 + 5 = 8, logo $\\frac{8}{20}=\\frac{2}{5}$.", ["8/20.", "Divide por 4: 2/5."]))
r = 1 - F(3,20) - F(5,20); assert r == F(3,5)
ex.append(num(3, C, "No mesmo depósito, que fração sobra depois de gastar $\\frac{3}{20}$ e $\\frac{5}{20}$? (forma mais simples)", r, "Tudo é $\\frac{20}{20}$. 20 − 3 − 5 = 12, logo $\\frac{12}{20}=\\frac{3}{5}$.", ["20/20 − 8/20 = 12/20.", "Simplifica por 4: 3/5."]))
save(fn, d)

# ---------- 02 Somar frações com denominadores diferentes ----------
fn, d = load('02-')
blocks(d,
 introduction="**Objetivos:** somar e subtrair frações com denominadores diferentes usando o m.m.c., e perceber porque é preciso um denominador comum. **Pré-requisitos:** múltiplos, m.m.c., frações equivalentes e soma de frações com o mesmo denominador.\n\nSe tens $\\frac{1}{2}$ de uma barra de chocolate e a tua irmã tem $\\frac{1}{3}$ de outra barra igual, quanto chocolate há ao todo? Não podes somar logo 1 + 1, porque as fatias são de tamanhos diferentes. Primeiro é preciso cortar tudo em fatias iguais.",
 intuition="Só se somam coisas do mesmo tipo: maçãs com maçãs. Frações com denominadores diferentes são como fatias de tamanhos diferentes. Para as somar, **trocamos as fatias por outras do mesmo tamanho**, o que se faz com frações equivalentes.\n\nO melhor tamanho comum é o menor que serve a ambas: o **mínimo múltiplo comum** (m.m.c.) dos denominadores. Para 2 e 3 é 6: metade são 3 sextos e um terço são 2 sextos; juntos, 5 sextos.\n\nPassos: (1) acha o m.m.c. dos denominadores; (2) converte cada fração para esse denominador (multiplica numerador e denominador pelo mesmo número); (3) soma os numeradores; (4) simplifica.\n\n**Erros comuns:** somar numeradores e denominadores ($\\frac{1}{2}+\\frac{1}{3}=\\frac{2}{5}$ está errado); mudar só o denominador e esquecer de mudar o numerador; usar um denominador comum que não é múltiplo de ambos.",
 definition="O **mínimo múltiplo comum** de dois números é o menor número positivo que é múltiplo de ambos. **Frações equivalentes** representam o mesmo valor: $\\frac{a}{b}=\\frac{a\\times k}{b\\times k}$ para $k\\neq0$. Reduzir ao **mesmo denominador** é substituir cada fração por uma equivalente cujo denominador é o m.m.c. dos denominadores.",
 formulas="$$\\frac{a}{b}+\\frac{c}{d}=\\frac{a\\times\\frac{m}{b}+c\\times\\frac{m}{d}}{m},\\quad m=\\text{m.m.c.}(b,d)$$\n\nAtalho (sempre funciona, mas pode dar números maiores): $\\dfrac{a}{b}+\\dfrac{c}{d}=\\dfrac{ad+bc}{bd}$, e depois simplifica.\n\nSe $b$ é divisor de $d$, o m.m.c. é simplesmente $d$.",
 worked_example="**Exemplo 1.** $\\frac{1}{2}+\\frac{1}{3}$. O m.m.c. de 2 e 3 é 6. $\\frac{1}{2}=\\frac{3}{6}$ e $\\frac{1}{3}=\\frac{2}{6}$. Logo $\\frac{3}{6}+\\frac{2}{6}=\\frac{5}{6}$.\n\n**Exemplo 2.** $\\frac{3}{4}+\\frac{1}{6}$. O m.m.c. de 4 e 6 é 12. $\\frac{9}{12}+\\frac{2}{12}=\\frac{11}{12}$.\n\n**Exemplo 3 (um denominador divide o outro).** $\\frac{2}{5}+\\frac{3}{10}$. Como 5 divide 10, o m.m.c. é 10: $\\frac{4}{10}+\\frac{3}{10}=\\frac{7}{10}$.\n\n**Exemplo 4 (subtração).** $\\frac{5}{6}-\\frac{3}{8}$. m.m.c.(6, 8) = 24: $\\frac{20}{24}-\\frac{9}{24}=\\frac{11}{24}$.\n\n**Exemplo 5 (resultado simplifica).** $\\frac{1}{6}+\\frac{1}{3}$. m.m.c. = 6: $\\frac{1}{6}+\\frac{2}{6}=\\frac{3}{6}=\\frac{1}{2}$.\n\n**Aplicação.** Uma costureira usou $\\frac{3}{4}$ de metro de fita azul e $\\frac{2}{3}$ de metro de fita vermelha. Ao todo: $\\frac{9}{12}+\\frac{8}{12}=\\frac{17}{12}$ m, ou seja, 1 m e $\\frac{5}{12}$.",
 guided_exercise="Resolve connosco: **calcula $\\frac{2}{3}+\\frac{1}{4}$.**\n\n1) Denominadores 3 e 4. Múltiplos de 3: 3, 6, 9, 12. Múltiplos de 4: 4, 8, 12. O m.m.c. é 12.\n\n2) $\\frac{2}{3}=\\frac{2\\times4}{3\\times4}=\\frac{8}{12}$ e $\\frac{1}{4}=\\frac{1\\times3}{4\\times3}=\\frac{3}{12}$.\n\n3) Soma: $\\frac{8}{12}+\\frac{3}{12}=\\frac{11}{12}$.\n\n4) Já está simplificada (11 é primo e não divide 12). Confere: 8/12 é cerca de 0,67 e 3/12 é 0,25; a soma 0,92 ≈ 11/12 ✓.",
 challenge="**Desafio.** Uma torneira enche $\\frac{1}{4}$ de um tanque por hora e outra enche $\\frac{1}{6}$ por hora. Juntas, que fração do tanque enchem numa hora? E em quantas horas encheriam o tanque todo? (Dica: soma as frações e depois pensa no inverso.)",
 assessment="Consideras a competência dominada quando consegues: (1) calcular o m.m.c. de dois denominadores; (2) escrever frações equivalentes com o denominador comum; (3) somar e subtrair e simplificar o resultado; (4) resolver problemas com comprimentos, líquidos e partes de um todo.")
ex = d['exercises']; C = 'fracoes.soma_denominadores_diferentes'
for a,b,c,e in [(1,4,1,6),(2,3,1,5),(3,8,1,4),(5,6,1,9),(1,2,3,7),(3,10,1,4)]:
    r = F(a,b)+F(c,e)
    ex.append(num(2, C, f"Calcula ${fr(a,b)}+{fr(c,e)}$ (forma mais simples).", r, f"m.m.c.({b}, {e}) = {math.lcm(b,e)}. Resultado: ${fr(r.numerator,r.denominator)}$.", [f"m.m.c.({b}, {e}) = {math.lcm(b,e)}.", "Converte e soma os numeradores.", "Simplifica."]))
for a,b,c,e in [(3,4,1,6),(7,10,2,5),(5,6,1,4)]:
    r = F(a,b)-F(c,e)
    ex.append(num(2, 'fracoes.subtracao_denominadores_diferentes', f"Calcula ${fr(a,b)}-{fr(c,e)}$ (forma mais simples).", r, f"m.m.c.({b}, {e}) = {math.lcm(b,e)}. Resultado: ${fr(r.numerator,r.denominator)}$.", [f"m.m.c.({b}, {e}) = {math.lcm(b,e)}.", "Converte e subtrai os numeradores."]))
ex.append(num(1, C, "Qual é o m.m.c. de 6 e 8?", math.lcm(6,8), "Múltiplos de 6: 6, 12, 18, 24. Múltiplos de 8: 8, 16, 24. O menor comum é 24.", ["Lista os múltiplos.", "O primeiro comum: 24."]))
r = F(3,4)+F(2,3); assert r == F(17,12)
ex.append(num(3, C, "Uma costureira usou $\\frac{3}{4}$ de metro de fita azul e $\\frac{2}{3}$ de metro de fita vermelha. Quantos metros, como fração, usou ao todo?", r, "m.m.c.(4, 3) = 12: $\\frac{9}{12}+\\frac{8}{12}=\\frac{17}{12}$ m.", ["9/12 + 8/12.", "= 17/12."]))
r = F(1,4)+F(1,6); assert r == F(5,12)
ex.append(num(3, C, "Uma torneira enche $\\frac{1}{4}$ de um tanque por hora e outra $\\frac{1}{6}$ por hora. Que fração do tanque enchem juntas numa hora?", r, "m.m.c.(4, 6) = 12: $\\frac{3}{12}+\\frac{2}{12}=\\frac{5}{12}$.", ["3/12 + 2/12.", "= 5/12."]))
ex.append(tf(2, C, "Para somar $\\frac{1}{3}+\\frac{1}{4}$ pode usar-se o denominador comum 12.", True, "12 é múltiplo de 3 e de 4: $\\frac{4}{12}+\\frac{3}{12}=\\frac{7}{12}$.", ["12 = 3×4.", "4/12 + 3/12 = 7/12."]))
ex.append(mc(2, C, "Qual é o resultado de $\\frac{1}{2}+\\frac{2}{3}$?", ["$\\frac{7}{6}$", "$\\frac{3}{5}$", "$\\frac{3}{6}$", "$\\frac{2}{6}$"], 0, "m.m.c. = 6: $\\frac{3}{6}+\\frac{4}{6}=\\frac{7}{6}$, que é maior que 1.", ["3/6 + 4/6.", "= 7/6."]))
save(fn, d)

# ---------- 03 Percentagem de um valor ----------
fn, d = load('03-')
blocks(d,
 introduction="**Objetivos:** perceber o que significa «por cento», calcular a percentagem de um valor de cabeça e por escrito, e usá-la em descontos, aumentos e comissões. **Pré-requisitos:** multiplicar e dividir, noção de fração e de decimal.\n\n«Por cento» está em todo o lado: descontos de 20% nas lojas, 5% de comissão numa venda, 15% de gorjeta, a bateria do telemóvel a 30%. Saber calcular percentagens de cabeça poupa dinheiro e evita enganos.",
 intuition="**Percentagem** quer dizer «por cada cem». 25% significa 25 em cada 100, ou seja, $\\frac{25}{100}=\\frac{1}{4}$. Tirar 25% de um valor é tirar um quarto.\n\nAtalhos que valem ouro: 50% é metade; 25% é um quarto (divide por 4); 10% é dividir por 10; 1% é dividir por 100; 20% é 10% a dobrar; 5% é metade de 10%; 15% é 10% mais 5%.\n\nPara qualquer percentagem: **escreve como fração de 100 e multiplica**: $p\\%$ de $V$ é $\\frac{p}{100}\\times V$.\n\n**Erros comuns:** (1) confundir 10% de 250 com 250 ÷ 10 por esquecer que é «por cem» (aqui coincide, mas 15% não é 250 ÷ 15); (2) esquecer de subtrair o desconto do preço original; (3) pensar que 100% é metade (100% é o todo).",
 definition="A **percentagem** $p\\%$ é a fração $\\frac{p}{100}$. A **percentagem de um valor** $V$ é o produto $\\frac{p}{100}\\times V$. O **valor final** depois de um desconto de $p\\%$ é $V-\\frac{p}{100}V$, e depois de um aumento de $p\\%$ é $V+\\frac{p}{100}V$.",
 formulas="$$p\\%\\text{ de }V=\\frac{p}{100}\\times V=p\\times\\frac{V}{100}$$\n\nDesconto: $V_{\\text{final}}=V\\times\\left(1-\\dfrac{p}{100}\\right)$. Aumento: $V_{\\text{final}}=V\\times\\left(1+\\dfrac{p}{100}\\right)$.\n\nCorrespondências úteis: 50% = ½, 25% = ¼, 75% = ¾, 10% = 1/10, 20% = 1/5, 5% = 1/20.",
 worked_example="**Exemplo 1.** 10% de 250 = 250 ÷ 10 = 25.\n\n**Exemplo 2.** 20% de 60 = $\\frac{20}{100}\\times 60=12$.\n\n**Exemplo 3 (25%).** 25% de 180 = 180 ÷ 4 = 45.\n\n**Exemplo 4 (15% = 10% + 5%).** 15% de 300: 10% = 30, 5% = 15, juntos 45.\n\n**Exemplo 5 (desconto).** Uns sapatos custam 8 000 Kz e têm 30% de desconto. 30% de 8 000 = 2 400. Pagas 8 000 − 2 400 = 5 600 Kz.\n\n**Aplicação.** Um vendedor ganha 8% de comissão sobre uma venda de 50 000 Kz: 8% de 50 000 = 8 × 500 = 4 000 Kz.",
 guided_exercise="Resolve connosco: **um telemóvel custa 40 000 Kz e tem 15% de desconto. Quanto pagas?**\n\n1) Calcula 10% de 40 000: divide por 10, dá 4 000.\n\n2) Calcula 5%, que é metade de 10%: 2 000.\n\n3) 15% = 4 000 + 2 000 = 6 000 Kz de desconto.\n\n4) Preço final: 40 000 − 6 000 = 34 000 Kz.\n\n5) Verifica: 85% de 40 000 = 0,85 × 40 000 = 34 000 ✓.",
 challenge="**Desafio.** Uma loja sobe o preço de um artigo em 20% e, na semana seguinte, faz um desconto de 20% sobre o novo preço. O artigo volta ao preço inicial? Experimenta com 1 000 Kz antes de responderes.",
 assessment="Consideras a competência dominada quando consegues: (1) explicar o que é «por cento»; (2) calcular 10%, 25%, 50%, 5% e 1% de cabeça; (3) calcular qualquer percentagem de um valor; (4) resolver problemas de desconto, aumento e comissão.")
ex = d['exercises']; C = 'percentagens.de_um_valor'
for p,v in [(30,900),(75,240),(5,1400),(12,500),(40,350),(60,1500)]:
    r = F(p*v,100)
    ex.append(num(1 if p in (30,5,40) else 2, C, f"Calcula {p}% de {v}.", r, f"{p}% de {v} = {p}/100 × {v} = {T(r)}.", [f"{p} × {v} = {p*v}.", "Divide por 100.", f"= {T(r)}."]))
for p,v in [(15,40000),(20,12500)]:
    r = v - F(p*v,100)
    ex.append(num(2, 'percentagens.desconto', f"Um artigo custa {v} Kz e tem {p}% de desconto. Quanto pagas, em Kz?", r, f"Desconto: {p}% de {v} = {T(F(p*v,100))}. Preço final: {v} − {T(F(p*v,100))} = {T(r)} Kz.", ["Calcula o desconto.", "Subtrai ao preço."]))
r = 1000*F(120,100)*F(80,100); assert r == 960
ex.append(num(3, 'percentagens.sucessivas', "Um artigo de 1 000 Kz sobe 20% e depois desce 20% sobre o novo preço. Quanto custa no fim, em Kz?", r, "Depois da subida: 1 200 Kz. 20% de 1 200 = 240. No fim: 1 200 − 240 = 960 Kz, ou seja, menos que o inicial.", ["1 000 × 1,2 = 1 200.", "1 200 × 0,8 = 960."]))
r = F(8*50000,100); assert r == 4000
ex.append(num(2, C, "Um vendedor ganha 8% de comissão sobre uma venda de 50 000 Kz. Quanto recebe de comissão, em Kz?", r, "8% de 50 000 = 8 × 500 = 4 000 Kz.", ["1% = 500.", "8 × 500 = 4 000."]))
ex.append(tf(2, C, "25% de um valor é o mesmo que a quarta parte desse valor.", True, "25/100 = 1/4.", ["25% = 1/4."]))
ex.append(tf(2, C, "Um desconto de 50% seguido de outro desconto de 50% faz o artigo ficar de graça.", False, "Depois do primeiro desconto fica metade; o segundo tira metade dessa metade, restando um quarto do preço.", ["100 → 50 → 25."]))
ex.append(mc(2, C, "Quanto é 15% de 300?", ["45", "30", "15", "20"], 0, "10% = 30 e 5% = 15; 30 + 15 = 45.", ["10% de 300 = 30.", "5% de 300 = 15.", "Soma: 45."]))
save(fn, d)

# ---------- 04 Somar e subtrair decimais ----------
fn, d = load('04-')
blocks(d,
 introduction="**Objetivos:** somar e subtrair números decimais alinhando a vírgula, comparar decimais e resolver problemas de dinheiro e medidas. **Pré-requisitos:** somar e subtrair naturais; saber o valor de cada ordem decimal (décimas, centésimas).\n\nOs preços, as medidas e os pesos usam decimais: 2,50 m de tecido, 1,75 kg de arroz, 3,2 litros de água. Para somar e subtrair estes números sem enganos há uma regra simples: **vírgula debaixo de vírgula**.",
 intuition="Num decimal, cada algarismo tem o seu valor: em $4{,}25$ há 4 unidades, 2 décimas e 5 centésimas. Só se podem somar coisas do mesmo tipo: décimas com décimas, centésimas com centésimas. Por isso alinhamos a vírgula: assim cada ordem fica na sua coluna.\n\nSe um número tem menos casas decimais, completa com zeros à direita (não muda o valor): $3{,}2=3{,}20$. Depois soma ou subtrai como nos naturais, coluna a coluna, e **põe a vírgula alinhada no resultado**.\n\nPara comparar decimais, iguala as casas: $0{,}5=0{,}50$ e $0{,}45$. Como 50 > 45, tem-se $0{,}5>0{,}45$ (muita gente acha que 0,45 é maior porque «45 é maior que 5»).\n\n**Erros comuns:** alinhar pela direita em vez de pela vírgula ($3{,}2+0{,}08$ não é $0{,}40$); esquecer a vírgula na resposta; achar que mais algarismos significa número maior.",
 definition="Um **número decimal** escreve-se com uma parte inteira e uma parte decimal separadas por vírgula. As ordens decimais são **décimas** ($\\frac{1}{10}$), **centésimas** ($\\frac{1}{100}$), **milésimas** ($\\frac{1}{1000}$). Dois decimais são iguais se só diferem em zeros à direita da parte decimal.",
 formulas="Regra: alinhar a vírgula, completar com zeros, operar como nos naturais e manter a vírgula alinhada.\n\n$$2{,}50+1{,}75=4{,}25\\qquad 5{,}00-1{,}35=3{,}65$$\n\nTruque do troco: 10 − 3,4 = 6,6, porque 3,4 + 6,6 = 10.\n\nEquivalências: $0{,}5=\\frac{5}{10}=\\frac{1}{2}$; $0{,}25=\\frac{1}{4}$; $0{,}75=\\frac{3}{4}$.",
 worked_example="**Exemplo 1.** $2{,}50+1{,}75$: 250 + 175 = 425, e com a vírgula alinhada fica $4{,}25$.\n\n**Exemplo 2.** $5{,}00-1{,}35$: 500 − 135 = 365, ou seja, $3{,}65$.\n\n**Exemplo 3 (casas diferentes).** $3{,}2+0{,}08=3{,}20+0{,}08=3{,}28$.\n\n**Exemplo 4 (troco).** Pagas com 1 000 Kz uma compra de 647,50 Kz. Troco: $1000{,}00-647{,}50=352{,}50$ Kz.\n\n**Exemplo 5 (comparar).** Ordena $0{,}7$; $0{,}65$; $0{,}705$. Com três casas: 0,700; 0,650; 0,705. Ordem crescente: 0,65 < 0,7 < 0,705.\n\n**Aplicação.** Uma tábua mede 2,4 m e outra 1,85 m. Juntas: $2{,}40+1{,}85=4{,}25$ m. A diferença é $2{,}40-1{,}85=0{,}55$ m.",
 guided_exercise="Resolve connosco: **compras pão por 1,35 € e leite por 2,80 €. Quanto gastas? E se pagares com uma nota de 5 €, quanto recebes de troco?**\n\n1) Alinha a vírgula: 1,35 + 2,80.\n\n2) Soma as centésimas: 5 + 0 = 5. Décimas: 3 + 8 = 11, escreve 1 e leva 1. Unidades: 1 + 2 + 1 = 4. Resultado: 4,15.\n\n3) Troco: 5,00 − 4,15 = 0,85.\n\n4) Verifica: 4,15 + 0,85 = 5,00 ✓.",
 challenge="**Desafio.** Quantas casas decimais tem, no máximo, a soma de dois números, um com 3 casas decimais e outro com 1? Dá um exemplo e verifica. E se subtraíres, o resultado pode ter mais casas decimais do que qualquer dos números? Experimenta.",
 assessment="Consideras a competência dominada quando consegues: (1) alinhar corretamente a vírgula; (2) completar com zeros sem mudar o valor; (3) somar e subtrair decimais; (4) comparar e ordenar decimais; (5) resolver problemas de dinheiro e medidas.")
ex = d['exercises']; C = 'decimais.soma_subtracao'
for a,b in [(3.75,2.5),(12.4,0.65),(0.29,0.71),(100.5,49.75),(8.04,1.9)]:
    r = F(str(a))+F(str(b))
    ex.append(num(1 if a<5 else 2, C, f"Calcula ${dec(a)}+{dec(b)}$.", r, f"Alinha a vírgula e soma: ${dec(float(r),3).rstrip('0').rstrip('{,}') if False else str(float(r)).replace('.',',')}$.", ["Completa com zeros.", "Soma coluna a coluna.", "Mantém a vírgula alinhada."]))
for a,b in [(9.5,3.25),(20,7.68),(15.3,0.45),(6.07,2.9)]:
    r = F(str(a))-F(str(b))
    ex.append(num(2, C, f"Calcula ${dec(a)}-{dec(b)}$.", r, f"Alinha a vírgula e subtrai: ${str(float(r)).replace('.',',')}$.", ["Completa com zeros à direita.", "Subtrai coluna a coluna."]))
r = F(1000)-F('647.5'); assert r == F('352.5')
ex.append(num(2, C, "Pagas com 1 000 Kz uma compra de 647,50 Kz. Quanto recebes de troco, em Kz?", r, "1 000,00 − 647,50 = 352,50.", ["Alinha a vírgula.", "= 352,50."]))
ex.append(tf(2, C, "$0{,}45>0{,}5$.", False, "0,5 = 0,50 e 50 > 45, logo 0,5 é maior.", ["Iguala as casas: 0,50 e 0,45."]))
ex.append(mc(2, C, "Qual é a ordem crescente de $0{,}7$; $0{,}65$; $0{,}705$?", ["$0{,}65<0{,}7<0{,}705$", "$0{,}7<0{,}65<0{,}705$", "$0{,}705<0{,}7<0{,}65$", "$0{,}65<0{,}705<0{,}7$"], 0, "Com três casas: 0,650 < 0,700 < 0,705.", ["0,650; 0,700; 0,705."]))
save(fn, d)

# ---------- 05 Potência ----------
fn, d = load('05-')
blocks(d,
 introduction="**Objetivos:** perceber o que é uma potência (base e expoente), calcular potências simples, conhecer os casos especiais (expoente 0 e 1) e usar potências em problemas de crescimento. **Pré-requisitos:** multiplicação e tabuada.\n\nUma bactéria que se divide em duas, cada uma dividindo-se outra vez, e assim por diante: 1, 2, 4, 8, 16… Para não escrever $2\\times2\\times2\\times2\\times2\\times2$, usa-se uma notação curta: $2^6$. As potências são a forma de escrever multiplicações repetidas.",
 intuition="Numa potência $a^n$, a **base** $a$ é o número que se repete e o **expoente** $n$ diz quantas vezes ele aparece como fator. Cuidado: $2^3$ **não** é $2\\times3=6$, é $2\\times2\\times2=8$.\n\nOs expoentes crescem depressa: $2^{10}=1\\,024$ e $2^{20}$ já passa de um milhão. É por isso que a poupança com juros, o crescimento de uma epidemia e a capacidade de um disco se descrevem com potências.\n\nCasos especiais: $a^1=a$ e $a^0=1$ (se $a\\neq0$). Potências de 10 são as mais fáceis: $10^n$ é o 1 seguido de $n$ zeros.\n\nSinais: base negativa com expoente par dá positivo ($(-2)^2=4$); com expoente ímpar dá negativo ($(-2)^3=-8$). Nota a diferença: $-2^2=-4$ (o sinal fica fora) e $(-2)^2=4$.\n\n**Erros comuns:** multiplicar base por expoente; achar que $a^0=0$; trocar $(-3)^2$ por $-3^2$.",
 definition="Para $n$ natural maior que 1, a **potência** $a^n$ é o produto de $n$ fatores iguais a $a$. Chama-se **base** a $a$ e **expoente** a $n$. Por convenção, $a^1=a$ e $a^0=1$ para $a\\neq0$.",
 formulas="$$a^n=\\underbrace{a\\times a\\times\\cdots\\times a}_{n\\text{ vezes}}$$\n\nPropriedades (mesma base): $a^m\\times a^n=a^{m+n}$ e $\\dfrac{a^m}{a^n}=a^{m-n}$. Potência de potência: $(a^m)^n=a^{m\\times n}$.\n\nAtenção: $2^3\\neq 2\\times3$; $2^3=8$.",
 worked_example="**Exemplo 1.** $3^4=3\\times3\\times3\\times3=81$.\n\n**Exemplo 2.** $10^3=10\\times10\\times10=1000$. Repara: o expoente diz quantos zeros tem o resultado.\n\n**Exemplo 3 (sinais).** $(-2)^3=(-2)\\times(-2)\\times(-2)=-8$, mas $(-2)^4=16$.\n\n**Exemplo 4 (expoente 0 e 1).** $7^1=7$ e $7^0=1$.\n\n**Exemplo 5 (mesma base).** $2^3\\times2^4=2^{3+4}=2^7=128$.\n\n**Aplicação.** Uma bactéria duplica a cada hora. Começando com 1, ao fim de 6 horas há $2^6=64$ bactérias; ao fim de 10 horas há $2^{10}=1024$.",
 guided_exercise="Resolve connosco: **calcula $(-3)^3$ e $(-3)^2$ e diz qual é positivo.**\n\n1) $(-3)^2=(-3)\\times(-3)=9$.\n\n2) $(-3)^3=(-3)^2\\times(-3)=9\\times(-3)=-27$.\n\n3) O positivo é $(-3)^2=9$: expoente par dá resultado positivo, ímpar dá negativo.\n\n4) Verifica o sinal: $(-3)^3$ tem três fatores negativos, e três negativos multiplicados dão negativo ✓.",
 challenge="**Desafio.** Um boato é partilhado por 2 pessoas; cada uma partilha com outras 2 uma hora depois, e assim por diante. Quantas pessoas recebem o boato na 8.ª hora? E quantas o terão recebido, ao todo, desde o início (soma de $2^1$ a $2^8$)? Experimenta primeiro com poucas horas.",
 assessment="Consideras a competência dominada quando consegues: (1) distinguir base de expoente; (2) calcular potências com bases e expoentes pequenos; (3) aplicar os casos $a^0=1$ e $a^1=a$; (4) tratar corretamente os sinais; (5) usar potências para resolver problemas de crescimento.")
ex = d['exercises']; C = 'potencias.calcular'
for a,n in [(4,3),(6,2),(2,8),(7,2),(5,3),(3,5)]:
    ex.append(num(1 if n<=3 else 2, C, f"Calcula ${a}^{n}$.", a**n, f"${a}^{n}$ = {a} multiplicado por si próprio {n} vezes = {a**n}.", [f"{' × '.join([str(a)]*n)}.", f"= {a**n}."]))
ex.append(num(2, C, "Calcula $(-2)^5$.", (-2)**5, "Cinco fatores negativos: o resultado é negativo. $2^5=32$, logo $(-2)^5=-32$.", ["2^5 = 32.", "Expoente ímpar: sinal negativo."]))
ex.append(num(2, C, "Calcula $(-4)^2$.", (-4)**2, "Dois fatores negativos: o resultado é positivo, $4\\times4=16$.", ["(-4) × (-4).", "= 16."]))
ex.append(num(3, C, "Calcula $-3^2$ (o sinal menos está fora da potência).", -(3**2), "Primeiro calcula-se $3^2=9$ e só depois se aplica o sinal: −9.", ["3² = 9.", "Sinal fora: −9."]))
ex.append(num(2, C, "Calcula $2^3\\times2^4$.", 2**7, "Mesma base: somam-se os expoentes, $2^7=128$.", ["3 + 4 = 7.", "2^7 = 128."]))
ex.append(num(2, C, "Quantas bactérias há ao fim de 10 horas se começa com 1 e duplica a cada hora?", 2**10, "$2^{10}=1\\,024$.", ["Duplica 10 vezes.", "2^10 = 1024."]))
ex.append(num(2, C, "Quantos zeros tem $10^6$ escrito por extenso?", 6, "$10^6=1\\,000\\,000$ tem 6 zeros.", ["O expoente é o número de zeros."]))
ex.append(tf(2, C, "$(-3)^2=-9$.", False, "$(-3)^2=(-3)\\times(-3)=9$, positivo.", ["Dois fatores negativos dão positivo."]))
ex.append(mc(2, C, "Qual é o valor de $5^0$?", ["1", "0", "5", "Não existe"], 0, "Qualquer número diferente de 0 elevado a 0 é 1.", ["a^0 = 1."]))
save(fn, d)

# ---------- 06 Raízes quadradas exatas ----------
fn, d = load('06-')
blocks(d,
 introduction="**Objetivos:** perceber o que é uma raiz quadrada, conhecer os quadrados perfeitos até 20² e calcular raízes exatas, usando-as em problemas de área e lado. **Pré-requisitos:** tabuada e potências ao quadrado.\n\nUm terreno quadrado tem 64 m² de área. Quanto mede cada lado? Procuras um número que multiplicado por si próprio dê 64: é o 8. Esse caminho inverso chama-se **raiz quadrada**.",
 intuition="Elevar ao quadrado e tirar a raiz quadrada são operações **inversas**, como somar e subtrair. Se $6^2=36$, então $\\sqrt{36}=6$.\n\nA raiz quadrada de um número é o lado de um quadrado com aquela área. Os números que têm raiz inteira chamam-se **quadrados perfeitos**: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225…\n\nComo calcular de cabeça: usa a tabuada ao contrário. Para $\\sqrt{196}$ vê que $14\\times14=196$. Se o número termina em 5, a raiz termina em 5 ($\\sqrt{225}=15$). Para números grandes, decompõe: $\\sqrt{2025}$: $45\\times45=2025$.\n\n**Erros comuns:** confundir $\\sqrt{16}$ com 16 ÷ 2 = 8 (a raiz de 16 é 4); dizer que $\\sqrt{a+b}=\\sqrt a+\\sqrt b$ (por exemplo, $\\sqrt{9+16}=5$, não $3+4=7$); pensar que se pode tirar raiz quadrada de um número negativo nos reais.",
 definition="A **raiz quadrada** de um número $a\\ge0$, escrita $\\sqrt{a}$, é o número **não negativo** $b$ tal que $b^2=a$. Um **quadrado perfeito** é um número natural cuja raiz quadrada é natural.",
 formulas="$$\\sqrt{a}=b\\iff b^2=a\\ (b\\ge0)$$\n\nQuadrados perfeitos: $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225$.\n\nPropriedades: $\\sqrt{a\\times b}=\\sqrt a\\times\\sqrt b$ e $\\sqrt{\\dfrac ab}=\\dfrac{\\sqrt a}{\\sqrt b}$ (para $a,b\\ge0$, $b\\ne0$). Não vale para a soma.",
 worked_example="**Exemplo 1.** $\\sqrt{36}=6$, porque $6\\times6=36$.\n\n**Exemplo 2.** $\\sqrt{121}=11$, porque $11\\times11=121$.\n\n**Exemplo 3 (termina em 5).** $\\sqrt{225}=15$, porque $15\\times15=225$.\n\n**Exemplo 4 (fração).** $\\sqrt{\\dfrac{9}{25}}=\\dfrac{3}{5}$.\n\n**Exemplo 5 (produto).** $\\sqrt{4\\times9}=\\sqrt{36}=6$, e também $\\sqrt4\\times\\sqrt9=2\\times3=6$.\n\n**Aplicação.** Um terreno quadrado tem 64 m² de área. O lado mede $\\sqrt{64}=8$ m, e o perímetro é $4\\times8=32$ m.",
 guided_exercise="Resolve connosco: **um quadrado tem 169 cm² de área. Quanto mede o lado e qual é o perímetro?**\n\n1) O lado é $\\sqrt{169}$.\n\n2) Procura na tabuada: $13\\times13=169$.\n\n3) Lado = 13 cm.\n\n4) Perímetro = $4\\times13=52$ cm.\n\n5) Verifica: $13^2=169$ ✓.",
 challenge="**Desafio.** Entre que dois números inteiros consecutivos está $\\sqrt{50}$? Sabendo que $7^2=49$ e $8^2=64$, o que concluis? Experimenta o mesmo com $\\sqrt{90}$.",
 assessment="Consideras a competência dominada quando consegues: (1) dizer de cabeça os quadrados perfeitos até 15²; (2) calcular raízes quadradas exatas; (3) usar a raiz inversa do quadrado em problemas de área; (4) evitar o erro de somar raízes.")
ex = d['exercises']; C = 'raizes.quadradas_exatas'
for n in [25, 100, 169, 196, 400, 900]:
    r = int(math.isqrt(n)); assert r*r == n
    ex.append(num(1 if n<=100 else 2, C, f"Calcula $\\sqrt{{{n}}}$.", r, f"${r}\\times{r}={n}$, logo $\\sqrt{{{n}}}={r}$.", [f"{r} × {r} = {n}."]))
ex.append(num(2, C, "Calcula $\\sqrt{\\dfrac{49}{100}}$ como fração.", F(7,10), "$\\sqrt{49}=7$ e $\\sqrt{100}=10$, logo $\\frac{7}{10}$.", ["Raiz do numerador: 7.", "Raiz do denominador: 10."]))
ex.append(num(2, C, "Calcula $\\sqrt{9+16}$.", 5, "Soma primeiro: 9 + 16 = 25, e $\\sqrt{25}=5$. Não é $3+4$.", ["9 + 16 = 25.", "√25 = 5."]))
ex.append(num(2, C, "Um quadrado tem 169 cm² de área. Qual é o seu perímetro, em cm?", 52, "Lado $\\sqrt{169}=13$, perímetro $4\\times13=52$.", ["Lado = 13.", "4 × 13 = 52."]))
ex.append(num(3, C, "Um terreno quadrado tem 2 500 m² de área. Quantos metros de rede são precisos para o vedar à volta?", 200, "Lado $\\sqrt{2500}=50$ m. Perímetro $4\\times50=200$ m.", ["√2500 = 50.", "4 × 50 = 200."]))
ex.append(tf(2, C, "$\\sqrt{16}=8$.", False, "A raiz quadrada de 16 é 4, porque $4\\times4=16$. Dividir por 2 é outra operação.", ["4 × 4 = 16."]))
ex.append(tf(2, C, "$\\sqrt{25}+\\sqrt{144}=\\sqrt{169}$.", False, "5 + 12 = 17, mas $\\sqrt{169}=13$. A raiz não se distribui pela soma.", ["5 + 12 = 17.", "√169 = 13."]))
ex.append(mc(2, C, "Entre que dois inteiros consecutivos está $\\sqrt{50}$?", ["7 e 8", "6 e 7", "8 e 9", "5 e 6"], 0, "$7^2=49<50<64=8^2$.", ["49 < 50 < 64."]))
save(fn, d)

# ---------- 07 Somar números inteiros ----------
fn, d = load('07-')
blocks(d,
 introduction="**Objetivos:** somar e subtrair números inteiros (positivos e negativos), comparar inteiros e aplicar à temperatura, saldos e altitudes. **Pré-requisitos:** somar e subtrair naturais; ideia de reta numérica.\n\nA temperatura pode descer abaixo de zero, uma conta bancária pode ficar negativa, um mergulhador está a −12 m. Para lidar com ganhos e perdas precisamos de números com sinal.",
 intuition="Pensa na **reta numérica**: os positivos estão à direita do zero, os negativos à esquerda. Somar um positivo é andar para a direita; somar um negativo é andar para a esquerda.\n\nOutra imagem: dinheiro e dívidas. $+5$ é teres 5; $-5$ é deveres 5. Se tens 4 e deves 9, ficas a dever 5: $4+(-9)=-5$.\n\nRegras de bolso: **sinais iguais**, somam-se os valores e mantém-se o sinal; **sinais diferentes**, subtrai-se o menor ao maior e fica o sinal do que tem mais valor.\n\nSubtrair é somar o simétrico: $a-b=a+(-b)$. E menos com menos dá mais: $5-(-3)=5+3=8$.\n\n**Erros comuns:** achar que $-8>-2$ (o mais perto do zero é o maior); somar valores com sinais diferentes como se fossem iguais; esquecer o sinal no resultado.",
 definition="Os **números inteiros** são $\\ldots,-3,-2,-1,0,1,2,3,\\ldots$. O **simétrico** de $a$ é $-a$ e a sua soma é zero. O **valor absoluto** $|a|$ é a distância de $a$ ao zero: $|-7|=7$. Dados dois inteiros, o maior é o que está mais à direita na reta.",
 formulas="Sinais iguais: $(-7)+(-3)=-(7+3)=-10$.\n\nSinais diferentes: $4+(-9)=-(9-4)=-5$ e $(-4)+9=+(9-4)=5$.\n\nSubtração: $a-b=a+(-b)$, por exemplo $5-(-3)=5+3=8$.\n\nSimétrico: $a+(-a)=0$.",
 worked_example="**Exemplo 1.** $-7+(-3)=-10$ (sinais iguais: 7+3=10, fica negativo).\n\n**Exemplo 2.** $4+(-9)=-5$ (sinais diferentes: 9−4=5, e o 9 é maior e negativo).\n\n**Exemplo 3.** $-4+9=5$ (sinais diferentes: 9−4=5, o 9 é positivo).\n\n**Exemplo 4 (subtração).** $5-(-3)=5+3=8$.\n\n**Exemplo 5 (várias parcelas).** $-6+10+(-8)=4+(-8)=-4$.\n\n**Aplicação.** A temperatura de manhã era −3 °C e subiu 9 graus: $-3+9=6$ °C. À noite desceu 10 graus: $6-10=-4$ °C.",
 guided_exercise="Resolve connosco: **calcula $-12+7-(-5)$.**\n\n1) Subtrair $-5$ é somar $5$: $-12+7+5$.\n\n2) $-12+7=-5$ (sinais diferentes: 12−7=5, o 12 é maior e negativo).\n\n3) $-5+5=0$.\n\n4) Verifica pela reta: de −12 anda 7 para a direita, ficas em −5; mais 5 para a direita, chegas a 0 ✓.",
 challenge="**Desafio.** Um elevador parte do 3.º andar, sobe 5, desce 9 e sobe 2. Em que andar fica? (Se o rés-do-chão é 0, o subsolo é negativo.) Usa uma reta numérica e depois confirma com a soma.",
 assessment="Consideras a competência dominada quando consegues: (1) comparar inteiros pela reta numérica; (2) somar com sinais iguais e diferentes; (3) transformar subtrações em somas do simétrico; (4) resolver problemas de temperatura, saldos e altitudes.")
ex = d['exercises']; C = 'inteiros.somar'
for a,b in [(-6,-9),(12,-20),(-15,8),(-4,-4),(25,-25),(-30,45)]:
    ex.append(num(1 if abs(a)<10 else 2, C, f"Calcula ${a}+({b})$.", a+b, f"Resultado: ${a+b}$.", ["Sinais iguais: soma e mantém o sinal; diferentes: subtrai e fica o sinal do maior.", f"= {a+b}."]))
for a,b in [(5,-3),(-2,-7),(10,12),(-8,-8)]:
    ex.append(num(2, 'inteiros.subtrair', f"Calcula ${a}-({b})$.", a-b, f"Subtrair {b} é somar {-b}: ${a}+({-b})={a-b}$.", ["a − b = a + (−b).", f"= {a-b}."]))
ex.append(num(3, C, "Calcula $-6+10+(-8)$.", -4, "−6 + 10 = 4 e 4 + (−8) = −4.", ["−6 + 10 = 4.", "4 − 8 = −4."]))
ex.append(num(2, C, "A temperatura de manhã era −3 °C e subiu 9 graus. Qual é a nova temperatura, em °C?", 6, "−3 + 9 = 6.", ["Anda 9 para a direita a partir de −3."]))
ex.append(num(3, C, "Um elevador parte do andar 3, sobe 5, desce 9 e sobe 2. Em que andar fica?", 3+5-9+2, "3 + 5 = 8; 8 − 9 = −1; −1 + 2 = 1. Fica no andar 1.", ["3 + 5 − 9 + 2.", "= 1."]))
ex.append(tf(2, C, "$-2>-8$.", True, "Na reta numérica, −2 está à direita de −8, logo é maior.", ["−8 < −2."]))
ex.append(tf(2, C, "$5-(-3)=2$.", False, "Subtrair −3 é somar 3: $5+3=8$.", ["5 − (−3) = 5 + 3 = 8."]))
ex.append(mc(2, C, "Qual é o resultado de $-7+(-3)$?", ["−10", "−4", "10", "4"], 0, "Sinais iguais: soma 7 + 3 = 10 e mantém o sinal negativo.", ["7 + 3 = 10.", "Sinal negativo."]))
save(fn, d)
print('ok')

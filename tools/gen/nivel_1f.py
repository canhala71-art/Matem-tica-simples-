"""Nível 1 — Tema 6 (Números decimais: 30–33) e Tema 7 (Percentagens: 34–36)."""
from common import *
import math
def dc(x):
    """Fraction -> texto decimal com vírgula (exato)."""
    x = F(x); neg = x < 0; x = abs(x)
    den = x.denominator
    while den % 2 == 0: den //= 2
    while den % 5 == 0: den //= 5
    assert den == 1, x
    k = 0
    while (x * 10 ** k).denominator != 1: k += 1
    n = int(x * 10 ** k)
    s = str(n).rjust(k + 1, '0')
    out = s if k == 0 else s[:-k] + ',' + s[-k:]
    return ('-' if neg else '') + out
def dnum(d, comp, st, val, expl, steps):
    s = dc(val)
    return {"type": "numeric", "difficulty": d, "competency": comp, "statement": st, "options": None,
            "answer": {"value": s.replace(',', '.'), "accepted": [s] if ',' in s else []}, "tolerance": 0, "explanation": expl, "steps": steps}
def L(x): return "$" + dc(x).replace(',', '{,}') + "$"

# ===== 30. Conceito de decimal, ordens, leitura, decomposição, comparação =====
C = 'decimais.conceito'; ex = []
ex.append(num(1, C, "Qual é a parte inteira de 36,847?", 36, "A parte inteira é o que está antes da vírgula: 36.", ["Antes da vírgula."]))
ex.append(num(1, C, "Quantos décimos tem 0,7?", 7, "0,7 = 7 décimos.", ["Primeira casa decimal."]))
ex.append(num(1, C, "Quantas centésimas tem 0,35?", 35, "0,35 = 35 centésimas.", ["Duas casas decimais."]))
ex.append(num(2, C, "No número 5,248, qual é o algarismo das milésimas?", 8, "As casas são: décimas 2, centésimas 4, milésimas 8.", ["Três casas decimais."]))
ex.append(dnum(2, C, "Escreve em decimal: $3+\\frac{4}{10}+\\frac{5}{100}$.", F(345, 100), "3 + 0,4 + 0,05 = 3,45.", ["Cada fração é uma casa decimal."]))
ex.append(dnum(2, C, "Escreve em decimal: sete unidades, quatro décimas e nove milésimas.", F(7409, 1000), "7 + 0,4 + 0,009 = 7,409 (centésimas: 0).", ["Centésimas é 0."]))
ex.append(dnum(2, C, "Escreve $\\frac{27}{100}$ em decimal.", F(27, 100), "27/100 = 0,27.", ["Duas casas decimais."]))
ex.append(dnum(2, C, "Qual é o maior: 0,5 ou 0,45? Escreve o maior.", F(1, 2), "0,5 = 0,50 > 0,45.", ["Iguala as casas."]))
ex.append(dnum(3, C, "Qual é o menor de 0,305; 0,35; 0,3; 0,299?", F(299, 1000), "Em milésimas: 305, 350, 300, 299. O menor é 0,299.", ["Escreve com 3 casas."]))
ex.append(dnum(3, C, "Qual é o decimal que está a meio entre 1,2 e 1,3?", F(125, 100), "(1,2 + 1,3) ÷ 2 = 1,25.", ["Ponto médio."]))
ex.append(tf(1, C, "0,50 e 0,5 representam o mesmo número.", True, "Acrescentar zeros à direita da parte decimal não muda o valor.", ["Zeros à direita."]))
ex.append(tf(2, C, "0,09 é maior que 0,1.", False, "0,09 < 0,10, porque 9 centésimas é menos que 10.", ["Iguala as casas."]))
ex.append(mc(2, C, "Como se lê 2,05?", ["Dois inteiros e cinco centésimas", "Dois inteiros e cinco décimas", "Vinte e cinco centésimas", "Dois inteiros e cinquenta"], 0, "Duas casas decimais: centésimas.", ["Duas casas → centésimas."]))
ex.append(mc(2, C, "Qual é a ordem crescente de 1,4; 1,04; 1,404; 1,44?", ["1,04 < 1,4 < 1,404 < 1,44", "1,4 < 1,04 < 1,44 < 1,404", "1,04 < 1,404 < 1,4 < 1,44", "1,404 < 1,44 < 1,4 < 1,04"], 0, "Em milésimas: 1,040 < 1,400 < 1,404 < 1,440.", ["Três casas."]))
A = lesson('numeros-decimais', 'Conceito de número decimal', 'conceito-decimal', 'Números decimais: ordens decimais, leitura, decomposição e comparação', 'decimais-conceito-ordens-comparacao',
 'Compreende as ordens decimais (décimas, centésimas, milésimas), lê, decompõe, compara e ordena números decimais.', 25,
 "**Objetivos:** compreender o número decimal, identificar parte inteira e parte decimal, ler, escrever, decompor, comparar e ordenar. **Pré-requisitos:** sistema decimal e frações com denominador 10, 100 e 1000.\n\nOs preços (1 250,50 Kz), as alturas (1,72 m), os pesos (3,5 kg) e os resultados desportivos usam números **decimais**. Servem para exprimir quantidades que não são inteiras.",
 "Um número decimal tem **parte inteira** (antes da vírgula) e **parte decimal** (depois). Cada casa decimal vale **um décimo** da anterior: **décimas** ($\\frac{1}{10}$), **centésimas** ($\\frac{1}{100}$), **milésimas** ($\\frac{1}{1000}$). Assim, $5{,}248=5+\\frac{2}{10}+\\frac{4}{100}+\\frac{8}{1000}$.\n\n**Leitura:** $2{,}05$ lê-se «dois inteiros e cinco centésimas» (duas casas decimais). Também se pode ler «dois vírgula zero cinco».\n\n**Decomposição:** $5{,}248=5\\times1+2\\times0{,}1+4\\times0{,}01+8\\times0{,}001$.\n\n**Zeros à direita** da parte decimal não alteram o valor: $0{,}5=0{,}50=0{,}500$. Zeros no meio importam: $2{,}05\\neq2{,}5$.\n\n**Comparar:** compara primeiro a parte inteira; se for igual, compara casa a casa, igualando o número de casas com zeros. Assim $0{,}5>0{,}45$ (0,50 > 0,45), mesmo parecendo que «45 é maior que 5».\n\n**Erros comuns:** achar que mais algarismos decimais dá número maior; confundir centésimas com décimas; ler 0,05 como «cinco décimas».",
 "Um **número decimal** é um número com parte inteira e parte decimal, separadas por vírgula. As ordens decimais são: décimas $10^{-1}$, centésimas $10^{-2}$, milésimas $10^{-3}$. Um decimal com $k$ casas decimais é uma fração de denominador $10^k$.",
 "$$0{,}d_1d_2d_3=\\frac{d_1}{10}+\\frac{d_2}{100}+\\frac{d_3}{1000}$$\n\n$$0{,}7=\\frac{7}{10},\\quad0{,}35=\\frac{35}{100},\\quad0{,}125=\\frac{125}{1000}$$\n\nComparação: igualar as casas decimais e comparar como se fossem naturais.",
 "**Exemplo 1 (leitura).** $0{,}7$: sete décimas. $0{,}35$: trinta e cinco centésimas. $0{,}125$: cento e vinte e cinco milésimas.\n\n**Exemplo 2 (decomposição).** $36{,}847=30+6+0{,}8+0{,}04+0{,}007$.\n\n**Exemplo 3 (de fração).** $3+\\frac{4}{10}+\\frac{5}{100}=3{,}45$.\n\n**Exemplo 4 (comparar).** $0{,}5$ e $0{,}45$: $0{,}50>0{,}45$.\n\n**Exemplo 5 (ordenar).** $1{,}4;\\ 1{,}04;\\ 1{,}404;\\ 1{,}44$ em milésimas: $1{,}040<1{,}400<1{,}404<1{,}440$.\n\n**Aplicação.** Um atleta fez 11,85 s e outro 11,9 s. Como $11{,}85<11{,}90$, o primeiro foi mais rápido.",
 "Resolve connosco: **escreve em decimal «7 unidades, 4 décimas e 9 milésimas» e compara com 7,41.**\n\n1) 7 inteiros, 4 décimas, 0 centésimas, 9 milésimas: $7{,}409$.\n\n2) $7{,}41=7{,}410$.\n\n3) Compara: $7{,}409<7{,}410$.\n\n4) Logo $7{,}409<7{,}41$.",
 "**Desafio.** Quantos números decimais com uma casa decimal há entre 2 e 3? E com duas casas decimais? E existe um número decimal entre 2,34 e 2,35? Quantos?",
 "Consideras a competência dominada quando consegues: (1) identificar parte inteira e parte decimal; (2) ler e decompor decimais; (3) igualar casas decimais com zeros; (4) comparar e ordenar corretamente.", ex)
write(1, 30, A)

# ===== 31. Multiplicação de decimais; ×10, ×100, ×1000 =====
C = 'decimais.multiplicar'; ex = []
for a, b in [(F(32, 10), F(5, 1)), (F(125, 100), F(4, 1)), (F(15, 10), F(12, 10)), (F(25, 100), F(8, 10)), (F(6, 10), F(7, 100)), (F(204, 100), F(25, 10))]:
    ex.append(dnum(2, C, f"Calcula {L(a)}$\\times$ {L(b)}.", a * b, f"Multiplica como inteiros e conta as casas decimais: {dc(a)} × {dc(b)} = {dc(a*b)}.", ["Ignora as vírgulas.", "Soma o número de casas decimais."]))
for x, k in [(F(347, 100), 10), (F(25, 1000), 100), (F(8, 10), 1000), (F(1234, 100), 100)]:
    ex.append(dnum(1 if k == 10 else 2, C, f"Calcula {L(x)}$\\times{k}$.", x * k, f"Multiplicar por {k} desloca a vírgula {len(str(k))-1} casa(s) para a direita: {dc(x*k)}.", ["Desloca a vírgula para a direita."]))
ex.append(dnum(3, C, "Uma bobina de fio custa 2,75 € por metro. Quanto custam 8 metros?", F(275, 100) * 8, "2,75 × 8 = 22.", ["275 × 8 = 2 200.", "Duas casas: 22,00."]))
ex.append(dnum(3, C, "Um litro de gasóleo custa 1,35 €. Quanto custam 40 litros?", F(135, 100) * 40, "1,35 × 40 = 54.", ["135 × 4 = 540.", "× 10 → 54,00."]))
ex.append(tf(2, C, "0,2 × 0,3 = 0,6.", False, "2 × 3 = 6 e há duas casas decimais: 0,06.", ["Conta as casas."]))
ex.append(tf(2, C, "Multiplicar um decimal por 100 desloca a vírgula duas casas para a direita.", True, "Ex.: 3,47 × 100 = 347.", ["2 zeros = 2 casas."]))
ex.append(mc(2, C, "Quantas casas decimais tem o produto de 1,25 por 0,4?", ["3", "2", "1", "5"], 0, "2 casas + 1 casa = 3 casas (1,25 × 0,4 = 0,500).", ["Soma as casas."]))
A = lesson('numeros-decimais', 'Operações com decimais', 'operacoes-decimais', 'Multiplicação de decimais e multiplicação por 10, 100 e 1 000', 'decimais-multiplicacao-potencias-de-10',
 'Multiplica números decimais contando as casas decimais e multiplica por 10, 100 e 1 000 deslocando a vírgula.', 25,
 "**Objetivos:** multiplicar decimais por naturais e entre si, multiplicar por 10, 100 e 1 000. **Pré-requisitos:** multiplicação de naturais e ordens decimais.\n\nSe um metro de fio custa 2,75 €, quanto custam 8 metros? É uma multiplicação de decimal por natural. Se um sumo tem 0,3 L e comes 0,5 da garrafa... 0,5 de 0,3 L é uma multiplicação de decimais.",
 "**Regra:** multiplica como se não houvesse vírgulas; depois coloca a vírgula no resultado de modo que ele tenha tantas casas decimais **como a soma** das casas dos fatores. $1{,}25\\times0{,}4$: $125\\times4=500$; $2+1=3$ casas → $0{,}500=0{,}5$.\n\nPorquê? $1{,}25=\\frac{125}{100}$ e $0{,}4=\\frac{4}{10}$, logo o produto é $\\frac{500}{1000}$: três casas.\n\n**Por 10, 100, 1 000:** desloca a vírgula 1, 2 ou 3 casas **para a direita** (acrescenta zeros se faltar): $3{,}47\\times100=347$; $0{,}8\\times1\\,000=800$. O valor torna-se 10, 100, 1 000 vezes maior.\n\nEstimativa: arredonda para verificar a ordem de grandeza. $2{,}75\\times8$ ronda $3\\times8=24$, e o resultado 22 é razoável.\n\n**Erros comuns:** alinhar a vírgula como na soma (não é preciso na multiplicação); esquecer-se de contar casas de **ambos** os fatores; achar que multiplicar sempre aumenta (0,2 × 0,3 = 0,06 é menor).",
 "O **produto** de dois decimais com $m$ e $n$ casas decimais obtém-se multiplicando os números sem vírgula e colocando a vírgula de modo a ter $m+n$ casas. Multiplicar por $10^k$ desloca a vírgula $k$ casas para a direita.",
 "$$a\\times10^k:\\ \\text{vírgula }k\\text{ casas para a direita}$$\n\n$$\\text{casas}(a\\times b)=\\text{casas}(a)+\\text{casas}(b)$$\n\nExemplos: $0{,}2\\times0{,}3=0{,}06$; $4{,}5\\times0{,}1=0{,}45$ (×0,1 equivale a ÷10).",
 "**Exemplo 1.** $3{,}2\\times5=16$ ($32\\times5=160$; 1 casa → 16,0).\n\n**Exemplo 2.** $1{,}5\\times1{,}2=1{,}8$ ($15\\times12=180$; 2 casas → 1,80).\n\n**Exemplo 3.** $0{,}6\\times0{,}07=0{,}042$ ($6\\times7=42$; 3 casas → 0,042).\n\n**Exemplo 4 (por 100).** $12{,}34\\times100=1\\,234$.\n\n**Exemplo 5 (por 1 000).** $0{,}8\\times1\\,000=800$.\n\n**Aplicação.** 40 L de gasóleo a 1,35 € o litro custam $1{,}35\\times40=54$ €.",
 "Resolve connosco: **calcula $2{,}04\\times2{,}5$.**\n\n1) Sem vírgulas: $204\\times25=5\\,100$.\n\n2) Casas decimais: $2+1=3$.\n\n3) Coloca a vírgula: $5{,}100=5{,}1$.\n\n4) Estimativa: $2\\times2{,}5=5$ ✓.",
 "**Desafio.** Calcula $0{,}1\\times0{,}1$, $0{,}01\\times0{,}1$ e $0{,}1\\times0{,}1\\times0{,}1$. Que padrão observas nas casas decimais e nos zeros? E para $0{,}1^{6}$?",
 "Consideras a competência dominada quando consegues: (1) multiplicar decimais contando as casas; (2) multiplicar por 10, 100 e 1 000; (3) estimar o resultado; (4) resolver problemas com preços e medidas.", ex)
write(1, 31, A)

# ===== 32. Divisão de decimais; ÷10, ÷100, ÷1000 =====
C = 'decimais.dividir'; ex = []
for a, b in [(F(84, 10), 4), (F(135, 100), 5), (F(72, 10), F(6, 10)), (F(45, 100), F(15, 100)), (F(9, 1), F(2, 1)), (F(1, 1), 8)]:
    ex.append(dnum(2 if b != 4 else 1, C, f"Calcula {L(a)}$\\div$ {L(b)}.", F(a) / F(b), f"{dc(a)} ÷ {dc(b)} = {dc(F(a)/F(b))}.", ["Iguala as casas ou desloca as vírgulas.", "Divide como inteiros."]))
for x, k in [(F(347, 10), 10), (F(25, 1), 100), (F(8, 1), 1000), (F(1234, 10), 100)]:
    ex.append(dnum(2, C, f"Calcula {L(x)}$\\div{k}$.", x / k, f"Dividir por {k} desloca a vírgula {len(str(k))-1} casa(s) para a esquerda: {dc(x/k)}.", ["Vírgula para a esquerda."]))
ex.append(dnum(3, C, "Repartem-se 7,5 kg de arroz por 6 sacos iguais. Quantos kg tem cada saco?", F(75, 10) / 6, "7,5 ÷ 6 = 1,25 kg.", ["75 ÷ 6 = 12,5.", "Divide por 10: 1,25."]))
ex.append(dnum(3, C, "Uma corda de 12,6 m é cortada em pedaços de 0,9 m. Quantos pedaços saem?", F(126, 10) / F(9, 10), "12,6 ÷ 0,9 = 126 ÷ 9 = 14.", ["Multiplica por 10 os dois."]))
ex.append(tf(2, C, "Dividir por 0,5 é o mesmo que multiplicar por 2.", True, "0,5 = 1/2 e dividir por 1/2 é multiplicar por 2.", ["Quantas metades cabem."]))
ex.append(tf(2, C, "Dividir um número positivo por 0,1 dá um resultado menor.", False, "Dividir por 0,1 equivale a multiplicar por 10: o resultado é maior.", ["÷ 0,1 = × 10."]))
ex.append(mc(2, C, "Qual é o resultado de 4,8 ÷ 0,6?", ["8", "0,8", "80", "2,88"], 0, "4,8 ÷ 0,6 = 48 ÷ 6 = 8.", ["Multiplica por 10 os dois números."]))
A = lesson('numeros-decimais', 'Operações com decimais', 'operacoes-decimais', 'Divisão de decimais e divisão por 10, 100 e 1 000', 'decimais-divisao-potencias-de-10',
 'Divide números decimais igualando casas decimais e divide por 10, 100 e 1 000 deslocando a vírgula.', 25,
 "**Objetivos:** dividir decimais por naturais e por decimais, dividir por 10, 100 e 1 000. **Pré-requisitos:** divisão de naturais e multiplicação de decimais.\n\nRepartir 7,5 kg de arroz por 6 sacos, cortar uma corda de 12,6 m em pedaços de 0,9 m: são divisões com decimais, muito comuns no dia a dia.",
 "**Decimal ÷ natural:** divide como nos naturais e, ao baixar a primeira casa decimal, põe a vírgula no quociente. $7{,}5\\div6=1{,}25$.\n\n**Divisor decimal:** multiplica o dividendo e o divisor pela **mesma potência de 10** até o divisor ficar inteiro (o quociente não muda). $12{,}6\\div0{,}9=126\\div9=14$.\n\n**Por 10, 100, 1 000:** desloca a vírgula 1, 2 ou 3 casas **para a esquerda**: $347\\div100=3{,}47$; $8\\div1\\,000=0{,}008$.\n\nDividir por um número menor que 1 **aumenta** o resultado: $4\\div0{,}5=8$ (em 4 inteiros cabem 8 metades). Dividir por 0,1 equivale a multiplicar por 10.\n\nAlgumas divisões **não são exatas** e produzem dízimas periódicas ($1\\div3=0{,}333\\ldots$) ou têm de ser arredondadas.\n\n**Erros comuns:** esquecer a vírgula no quociente; deslocar a vírgula para o lado errado; achar que dividir sempre diminui.",
 "A **divisão** $a\\div b$ de decimais com $b\\neq0$ é o número $q$ tal que $b\\times q=a$. Dividir por $10^k$ desloca a vírgula $k$ casas para a esquerda. Multiplicar dividendo e divisor pela mesma potência de 10 não altera o quociente.",
 "$$\\frac{a}{b}=\\frac{a\\times10^k}{b\\times10^k}\\qquad a\\div10^k:\\ \\text{vírgula }k\\text{ casas para a esquerda}$$\n\n$$a\\div0{,}1=a\\times10\\qquad a\\div0{,}5=a\\times2$$",
 "**Exemplo 1.** $8{,}4\\div4=2{,}1$.\n\n**Exemplo 2.** $7{,}2\\div0{,}6=72\\div6=12$.\n\n**Exemplo 3.** $9\\div2=4{,}5$.\n\n**Exemplo 4 (por 100).** $25\\div100=0{,}25$.\n\n**Exemplo 5 (por 1 000).** $8\\div1\\,000=0{,}008$.\n\n**Aplicação.** 7,5 kg de arroz repartidos por 6 sacos: $7{,}5\\div6=1{,}25$ kg em cada.",
 "Resolve connosco: **calcula $4{,}5\\div0{,}15$.**\n\n1) Para tornar o divisor inteiro, multiplica ambos por 100: $450\\div15$.\n\n2) $450\\div15=30$.\n\n3) Prova: $0{,}15\\times30=4{,}5$ ✓.",
 "**Desafio.** Calcula $1\\div0{,}1$, $1\\div0{,}01$ e $1\\div0{,}001$. Que padrão aparece? Quantas moedas de 0,05 € cabem em 1 €?",
 "Consideras a competência dominada quando consegues: (1) dividir decimal por natural e por decimal; (2) dividir por 10, 100 e 1 000; (3) perceber que dividir por números menores que 1 aumenta; (4) resolver problemas de repartição.", ex)
write(1, 32, A)

# ===== 33. Arredondamento, fração↔decimal, dízimas periódicas, dinheiro e medidas =====
C = 'decimais.arredondar_converter'; ex = []
for x, k, r in [(F(3768, 1000), 1, F(38, 10)), (F(2345, 1000), 2, F(235, 100)), (F(9996, 1000), 2, F(1000, 100)), (F(5049, 1000), 1, F(50, 10)), (F(1255, 1000), 2, F(126, 100))]:
    ex.append(dnum(2, C, f"Arredonda {L(x)} às {'décimas' if k==1 else 'centésimas'}.", r, f"Olha para a casa seguinte: arredonda para {dc(r)}.", ["Se a casa seguinte for ≥ 5, sobe.", "Se < 5, fica."]))
ex.append(dnum(2, C, "Converte 7/8 em decimal.", F(7, 8), "7 ÷ 8 = 0,875.", ["Divide 7 por 8."]))
ex.append(dnum(2, C, "Converte 3/20 em decimal.", F(3, 20), "3/20 = 15/100 = 0,15.", ["Multiplica por 5."]))
ex.append(num(2, C, "Escreve 0,375 como fração irredutível (a/b).", F(3, 8), "375/1000 = 3/8.", ["m.d.c. = 125."]))
ex.append(num(2, C, "Escreve 1,25 como fração irredutível (a/b).", F(5, 4), "125/100 = 5/4.", ["m.d.c. = 25."]))
ex.append(num(2, C, "Qual é o período da dízima 0,(27)? Quantos algarismos tem o período?", 2, "O período é 27, com dois algarismos.", ["27 repete-se."]))
ex.append(dnum(3, C, "Um tecido custa 3,45 € por metro. Quanto custam 2,5 metros?", F(345, 100) * F(5, 2), "3,45 × 2,5 = 8,625 € (valor exato; a pagar seria 8,63 € arredondado às centésimas).", ["345 × 25 = 8 625.", "3 casas: 8,625."]))
ex.append(dnum(3, C, "Uma pessoa tem 1,68 m. Quantos centímetros são?", F(168, 1), "1 m = 100 cm: 1,68 × 100 = 168 cm.", ["× 100."]))
ex.append(tf(2, C, "$\\frac{1}{3}$ é uma dízima periódica.", True, "1 ÷ 3 = 0,333…, o 3 repete-se.", ["Divisão que não termina."]))
ex.append(tf(2, C, "Arredondar 4,25 às décimas dá 4,3.", True, "A casa seguinte é 5, por isso arredonda-se para cima: 4,3.", ["5 sobe."]))
ex.append(mc(2, C, "Qual das frações dá uma dízima periódica?", ["$\\frac{2}{3}$", "$\\frac{3}{4}$", "$\\frac{1}{8}$", "$\\frac{7}{20}$"], 0, "Os denominadores 4, 8 e 20 só têm os fatores 2 e 5; o 3 não.", ["Fatores 2 e 5 só."]))
A = lesson('numeros-decimais', 'Arredondamento e conversões', 'arredondamento-conversoes-decimais', 'Arredondamento, fração e decimal, dízimas periódicas, dinheiro e medidas', 'decimais-arredondamento-conversoes-dizimas',
 'Arredonda decimais, converte entre fração e decimal, reconhece dízimas periódicas e aplica a dinheiro e medidas.', 30,
 "**Objetivos:** arredondar decimais, converter fração em decimal e vice-versa, reconhecer dízimas periódicas e resolver problemas com dinheiro e medidas. **Pré-requisitos:** frações, divisão e ordens decimais.\n\nNo supermercado, os preços aparecem com duas casas decimais. Numa divisão que não termina, é preciso parar numa certa casa. É o **arredondamento**, usado constantemente para falar de dinheiro, distâncias e médias.",
 "**Arredondamento:** para arredondar a certa casa, olha para a casa seguinte. Se for 5 ou mais, **sobe** uma unidade; se for 4 ou menos, **fica**. $3{,}768\\approx3{,}8$ (às décimas) e $\\approx3{,}77$ (às centésimas). $4{,}25\\approx4{,}3$.\n\n**Fração → decimal:** divide numerador por denominador. $\\frac{7}{8}=0{,}875$. Se a divisão termina, o decimal é **exato**; se não termina e os algarismos se repetem, é uma **dízima periódica**: $\\frac{1}{3}=0{,}333\\ldots=0{,}(3)$ e $\\frac{3}{11}=0{,}(27)$.\n\n**Decimal exato → fração:** escreve sobre 10, 100, 1 000 e simplifica: $0{,}375=\\frac{375}{1000}=\\frac{3}{8}$.\n\nUma fração irredutível dá decimal exato apenas se o denominador só tiver os fatores 2 e 5.\n\n**Dinheiro e medidas:** 1 m = 100 cm = 1 000 mm; 1 kg = 1 000 g; 1 L = 1 000 mL. Converter é multiplicar ou dividir por potências de 10: $1{,}68\\text{ m}=168\\text{ cm}$.\n\n**Erros comuns:** arredondar olhando duas casas à frente; achar que 0,333… termina; esquecer de simplificar a fração obtida.",
 "O **arredondamento** de um decimal a uma ordem é o número mais próximo com essa precisão. Uma **dízima periódica** é um decimal infinito em que, a partir de certa casa, se repete um grupo de algarismos (o **período**). Um decimal **exato** tem um número finito de casas.",
 "$$x\\approx\\text{arredondado a }10^{-k}:\\ \\text{observa a casa }k+1$$\n\n$$\\frac{a}{b}\\text{ é decimal exato}\\iff b\\text{ (irredutível) só tem fatores }2\\text{ e }5$$\n\n$$0{,}\\overline{3}=\\frac{1}{3}\\qquad0{,}\\overline{9}=1$$",
 "**Exemplo 1.** $3{,}768$ às décimas: 3,8 (a casa seguinte é 6).\n\n**Exemplo 2.** $2{,}345$ às centésimas: 2,35 (a casa seguinte é 5).\n\n**Exemplo 3 (fração).** $\\frac{3}{20}=\\frac{15}{100}=0{,}15$.\n\n**Exemplo 4 (decimal → fração).** $1{,}25=\\frac{125}{100}=\\frac{5}{4}$.\n\n**Exemplo 5 (dízima).** $\\frac{2}{3}=0{,}666\\ldots=0{,}(6)$.\n\n**Aplicação.** O metro de tecido custa 3,45 €. Para 2,5 m: $3{,}45\\times2{,}5=8{,}625\\approx8{,}63$ €. A Maria tem 1,68 m, ou seja, 168 cm.",
 "Resolve connosco: **converte $\\frac{5}{6}$ em decimal e arredonda às centésimas.**\n\n1) $5\\div6=0{,}8333\\ldots$ (o 3 repete-se).\n\n2) Às centésimas: a casa seguinte é 3 (< 5), fica 0,83.\n\n3) É uma dízima periódica: $0{,}8(3)$.\n\n4) Verifica: $0{,}83\\times6=4{,}98\\approx5$ ✓.",
 "**Desafio.** Mostra que $0{,}999\\ldots=1$: seja $x=0{,}999\\ldots$; calcula $10x-x$. Em que passo o raciocínio usa a repetição infinita?",
 "Consideras a competência dominada quando consegues: (1) arredondar às décimas, centésimas e milésimas; (2) converter fração em decimal e o inverso; (3) reconhecer dízimas periódicas; (4) converter unidades de medida e usar dinheiro.", ex)
write(1, 33, A)

# ======================= TEMA 7 — PERCENTAGENS =======================
# ===== 34. Conceito, símbolo, relação % fração decimal =====
C = 'percentagens.conversao'; ex = []
for p, n, d in [(50, 1, 2), (25, 1, 4), (20, 1, 5), (75, 3, 4), (5, 1, 20), (40, 2, 5)]:
    ex.append(num(1 if p in (50, 25) else 2, C, f"Escreve {p}% como fração irredutível (a/b).", F(n, d), f"{p}% = {p}/100 = {n}/{d}.", [f"{p}/100.", "Simplifica."]))
for p in [35, 8, 120, 0.5]:
    v = F(str(p)) / 100
    ex.append(dnum(2, C, f"Escreve {str(p).replace('.', ',')}% em número decimal.", v, f"{str(p).replace('.', ',')}% = {str(p).replace('.', ',')} ÷ 100 = {dc(v)}.", ["Divide por 100.", "Vírgula 2 casas à esquerda."]))
for x, pc in [(F(3, 5), 60), (F(7, 20), 35), (F(9, 4), 225), (F(1, 8), 12.5)]:
    ex.append(num(2, C, f"Escreve {dc(x)} em percentagem (só o número, sem %).".replace('0,', '0,') if False else f"Escreve ${('\\frac{%d}{%d}' % (x.numerator, x.denominator))}$ em percentagem (só o número, sem %).", F(str(pc)), f"{x.numerator}/{x.denominator} = {dc(x)} = {str(pc).replace('.', ',')}%.", ["Passa a decimal.", "× 100."]))
ex.append(num(3, C, "Numa turma de 25 alunos, 7 faltaram. Que percentagem faltou?", 28, "7/25 = 28/100 = 28%.", ["Escreve com denominador 100."]))
ex.append(tf(1, C, "100% de um valor é o valor todo.", True, "100% = 100/100 = 1.", ["100/100 = 1."]))
ex.append(tf(2, C, "50% é o mesmo que 1/5.", False, "50% = 1/2; 1/5 é 20%.", ["50/100 = 1/2."]))
ex.append(mc(2, C, "Qual é a relação correta?", ["25% = 0,25 = 1/4", "25% = 2,5 = 1/4", "25% = 0,025 = 1/25", "25% = 0,25 = 1/2"], 0, "25% = 25/100 = 0,25 = 1/4.", ["Divide por 100."]))
A = lesson('percentagens', 'Conceito de percentagem', 'conceito-percentagem', 'Percentagem: símbolo, relação com fração e decimal, conversões', 'percentagem-conceito-fracao-decimal',
 'Compreende a percentagem como fração de denominador 100 e converte entre percentagem, fração e decimal.', 25,
 "**Objetivos:** compreender o símbolo %, relacionar percentagem, fração e decimal e converter entre as três formas. **Pré-requisitos:** frações, decimais e divisão por 100.\n\n«Desconto de 30%», «a bateria está a 15%», «aumento de 5% no preço do pão»: a percentagem está em todo o lado. Dá-nos uma maneira comum de comparar partes de quantidades diferentes.",
 "**Percentagem** quer dizer «por cada cem». $25\\%$ são 25 em cada 100, ou seja, $\\frac{25}{100}=\\frac{1}{4}=0{,}25$. O símbolo % é uma forma abreviada de escrever «/100».\n\nAs três formas descrevem o mesmo número: **percentagem** $35\\%$, **fração** $\\frac{35}{100}=\\frac{7}{20}$ e **decimal** $0{,}35$.\n\n**Percentagem → decimal:** divide por 100 (desloca a vírgula duas casas para a esquerda): $8\\%=0{,}08$, $120\\%=1{,}2$, $0{,}5\\%=0{,}005$.\n\n**Decimal → percentagem:** multiplica por 100: $0{,}6=60\\%$.\n\n**Fração → percentagem:** passa a decimal e multiplica por 100: $\\frac{3}{5}=0{,}6=60\\%$; ou usa denominador 100: $\\frac{7}{25}=\\frac{28}{100}=28\\%$.\n\nValores de referência: 100% = o todo (1); 50% = metade; 25% = um quarto; 75% = três quartos; 10% = um décimo; 200% = o dobro. Pode haver percentagens maiores que 100% (quando é mais que o todo).\n\n**Erros comuns:** escrever $5\\%=0{,}5$ (é 0,05); achar que 50% é um quinto; esquecer o 100 no denominador.",
 "A **percentagem** $p\\%$ é a fração $\\frac{p}{100}$. Para um número $x$, $x$ «em percentagem» é $(x\\times100)\\%$. O todo corresponde a $100\\%$.",
 "$$p\\%=\\frac{p}{100}=p\\div100\\qquad x=(x\\times100)\\%$$\n\nReferências: $1\\%=0{,}01$; $10\\%=\\frac{1}{10}$; $20\\%=\\frac{1}{5}$; $25\\%=\\frac{1}{4}$; $50\\%=\\frac{1}{2}$; $75\\%=\\frac{3}{4}$; $100\\%=1$.",
 "**Exemplo 1.** $50\\%=\\frac{50}{100}=\\frac{1}{2}$.\n\n**Exemplo 2.** $35\\%=0{,}35$ e $8\\%=0{,}08$.\n\n**Exemplo 3 (decimal).** $0{,}6=60\\%$ e $1{,}25=125\\%$.\n\n**Exemplo 4 (fração).** $\\frac{3}{5}=\\frac{60}{100}=60\\%$.\n\n**Exemplo 5 (parte de um todo).** Numa turma de 25 alunos faltaram 7: $\\frac{7}{25}=\\frac{28}{100}=28\\%$.\n\n**Aplicação.** Se 40% dos 60 alunos de uma escola vão a pé: $0{,}4\\times60=24$ alunos.",
 "Resolve connosco: **num teste de 40 perguntas, a Maria acertou 34. Que percentagem acertou?**\n\n1) Fração: $\\frac{34}{40}$.\n\n2) Decimal: $34\\div40=0{,}85$.\n\n3) Percentagem: $0{,}85\\times100=85\\%$.\n\n4) Verifica: 85% de 40 = $0{,}85\\times40=34$ ✓.",
 "**Desafio.** Explica o que significa «120% do preço» e «0,5% de juros». Dá um exemplo de cada, com valores em Kwanzas.",
 "Consideras a competência dominada quando consegues: (1) ler % como «por cada cem»; (2) passar entre %, fração e decimal; (3) reconhecer as referências 50%, 25%, 10%; (4) interpretar percentagens superiores a 100%.", ex)
write(1, 34, A)

# ===== 35. Aumentos, descontos, variação percentual, percentagens sucessivas =====
C = 'percentagens.variacao'; ex = []
for v, p in [(8000, 30), (45000, 15), (12000, 25), (250, 12)]:
    r = F(v) * F(100 - p, 100)
    ex.append(dnum(2, C, f"Um artigo custa {v} Kz e tem {p}% de desconto. Quanto custa agora, em Kz?", r, f"Desconto: {p}% de {v} = {dc(F(v)*F(p,100))}. Preço final: {v} − {dc(F(v)*F(p,100))} = {dc(r)} Kz.", ["Calcula o desconto.", "Subtrai."]))
for v, p in [(20000, 10), (350, 20), (15000, 8)]:
    r = F(v) * F(100 + p, 100)
    ex.append(dnum(2, C, f"Um salário de {v} Kz sobe {p}%. Qual é o novo valor, em Kz?", r, f"Aumento: {dc(F(v)*F(p,100))}. Novo valor: {dc(r)} Kz.", ["Calcula o aumento.", "Soma."]))
for a, b in [(80, 100), (50, 40), (200, 250)]:
    var = F(b - a, a) * 100
    ex.append(dnum(3, C, f"O preço passou de {a} Kz para {b} Kz. Qual foi a variação percentual (só o número, sem %)?", var, f"Variação = (novo − antigo) ÷ antigo × 100 = ({b} − {a}) ÷ {a} × 100 = {dc(var)}%.", ["Diferença ÷ valor inicial.", "× 100."]))
r = 1000 * F(12, 10) * F(8, 10)
ex.append(dnum(3, C, "Um artigo de 1 000 Kz sobe 20% e depois desce 20% sobre o novo preço. Quanto custa no fim, em Kz?", r, "1 000 × 1,2 = 1 200; 1 200 × 0,8 = 960 Kz.", ["Fator 1,2.", "Fator 0,8."]))
r = 5000 * F(9, 10) * F(9, 10)
ex.append(dnum(3, C, "Dois descontos sucessivos de 10% sobre 5 000 Kz. Qual é o preço final, em Kz?", r, "5 000 × 0,9 = 4 500; 4 500 × 0,9 = 4 050 Kz (não é 20% de desconto: seria 4 000).", ["Fator 0,9 duas vezes."]))
ex.append(tf(2, C, "Um desconto de 50% seguido de um aumento de 50% volta ao preço inicial.", False, "100 → 50 → 75. O aumento incide sobre o novo valor, que é menor.", ["50 × 1,5 = 75."]))
ex.append(tf(2, C, "Um aumento de 10% equivale a multiplicar por 1,1.", True, "100% + 10% = 110% = 1,1.", ["Fator de aumento."]))
ex.append(mc(2, C, "Qual é o fator multiplicativo de um desconto de 25%?", ["0,75", "0,25", "1,25", "0,025"], 0, "100% − 25% = 75% = 0,75.", ["1 − 0,25."]))
A = lesson('percentagens', 'Variações percentuais', 'variacoes-percentuais', 'Aumentos, descontos, variação percentual e percentagens sucessivas', 'percentagens-aumentos-descontos-sucessivas',
 'Calcula aumentos, descontos e variações percentuais e compreende percentagens sucessivas com fatores multiplicativos.', 30,
 "**Objetivos:** calcular aumentos e descontos, achar a variação percentual entre dois valores e perceber porque as percentagens sucessivas não se somam. **Pré-requisitos:** percentagem de um valor e conversões.\n\nOs preços sobem e descem, os salários são aumentados, as lojas fazem promoções. Para saber exatamente quanto custa um artigo depois de «30% de desconto» ou quanto vale um salário depois de «8% de aumento», usa-se a percentagem como **fator multiplicativo**.",
 "**Desconto de $p\\%$:** o novo valor é $V\\times\\left(1-\\frac{p}{100}\\right)$. Ex.: 30% de desconto → multiplica por $0{,}7$. **Aumento de $p\\%$:** $V\\times\\left(1+\\frac{p}{100}\\right)$. Ex.: 12% de aumento → multiplica por $1{,}12$. Estes números chamam-se **fatores multiplicativos**.\n\n**Variação percentual:** $\\dfrac{\\text{valor novo}-\\text{valor inicial}}{\\text{valor inicial}}\\times100\\%$. Se o resultado é positivo, é aumento; se é negativo, é diminuição. De 80 para 100: $\\frac{20}{80}=25\\%$ de aumento.\n\n**Percentagens sucessivas:** multiplicam-se os fatores, **não** se somam as percentagens. Subir 20% e depois descer 20% dá $1{,}2\\times0{,}8=0{,}96$, ou seja, **menos 4%**. Dois descontos de 10% dão $0{,}9\\times0{,}9=0{,}81$: desconto total de 19%, não de 20%.\n\nO que faz diferença é sobre **que valor** se calcula a percentagem: a segunda percentagem incide sobre o valor já alterado.\n\n**Erros comuns:** somar percentagens sucessivas; calcular a variação percentual dividindo pelo valor novo em vez do inicial; esquecer de subtrair o desconto.",
 "Um **fator multiplicativo** é o número pelo qual se multiplica o valor inicial para obter o final. A **variação percentual** entre $V_i$ e $V_f$ é $\\dfrac{V_f-V_i}{V_i}\\times100\\%$. **Percentagens sucessivas** são variações aplicadas uma depois da outra.",
 "$$V_f=V_i\\times(1\\pm\\tfrac{p}{100})\\qquad\\Delta\\%=\\frac{V_f-V_i}{V_i}\\times100$$\n\nSucessivas: $V_f=V_i\\times f_1\\times f_2\\times\\cdots$",
 "**Exemplo 1 (desconto).** Um artigo de 8 000 Kz com 30% de desconto: $8\\,000\\times0{,}7=5\\,600$ Kz.\n\n**Exemplo 2 (aumento).** Salário de 20 000 Kz com 10% de aumento: $20\\,000\\times1{,}1=22\\,000$ Kz.\n\n**Exemplo 3 (variação).** De 80 Kz para 100 Kz: $\\frac{100-80}{80}\\times100=25\\%$ de aumento.\n\n**Exemplo 4 (sucessivas).** 1 000 Kz sobem 20% e descem 20%: $1\\,000\\times1{,}2\\times0{,}8=960$ Kz.\n\n**Exemplo 5 (dois descontos).** Dois descontos de 10% sobre 5 000 Kz: $5\\,000\\times0{,}9\\times0{,}9=4\\,050$ Kz.\n\n**Aplicação.** O preço do pão passou de 200 para 250 Kz: variação $\\frac{50}{200}=25\\%$.",
 "Resolve connosco: **um telemóvel custava 60 000 Kz. Subiu 10% e depois baixou 10%. Quanto custa agora? Qual foi a variação total?**\n\n1) Depois da subida: $60\\,000\\times1{,}1=66\\,000$.\n\n2) Depois da descida: $66\\,000\\times0{,}9=59\\,400$.\n\n3) Variação: $\\frac{59\\,400-60\\,000}{60\\,000}=-0{,}01=-1\\%$.\n\n4) Custa menos 1% do que no início.",
 "**Desafio.** Um artigo desce 50% e depois sobe 100%. Volta ao preço inicial? E se subir 100% e depois descer 50%? Calcula os fatores e explica as diferenças.",
 "Consideras a competência dominada quando consegues: (1) calcular aumentos e descontos com fatores; (2) achar a variação percentual; (3) compor percentagens sucessivas multiplicando; (4) evitar o erro de somar percentagens.", ex)
write(1, 35, A)

# ===== 36. Lucro, prejuízo e aplicações comerciais =====
C = 'percentagens.comercial'; ex = []
for custo, venda in [(4000, 5000), (7500, 6000), (12000, 15000)]:
    l = F(venda - custo, custo) * 100
    ex.append(dnum(3, C, f"Compraste por {custo} Kz e vendeste por {venda} Kz. Qual é a percentagem de {'lucro' if venda>custo else 'prejuízo'} (só o número, sem sinal e sem %), calculada sobre o custo?", abs(l), f"({venda} − {custo}) ÷ {custo} × 100 = {dc(l)}%.", ["Diferença ÷ custo.", "× 100."]))
for custo, p in [(8000, 25), (15000, 20), (2400, 15)]:
    v = F(custo) * F(100 + p, 100)
    ex.append(dnum(2, C, f"Um comerciante compra um artigo a {custo} Kz e quer ganhar {p}% sobre o custo. Por quanto o deve vender, em Kz?", v, f"{custo} × {dc(F(100+p,100))} = {dc(v)} Kz.", ["Fator de lucro."]))
ex.append(dnum(3, C, "Vendeste um artigo por 11 000 Kz com 10% de lucro sobre o custo. Quanto tinha custado, em Kz?", F(10000), "Custo × 1,1 = 11 000, logo custo = 11 000 ÷ 1,1 = 10 000 Kz.", ["Divide pelo fator 1,1."]))
ex.append(dnum(3, C, "Um vendedor ganha 6% de comissão sobre vendas de 350 000 Kz. Quanto recebe, em Kz?", F(21000), "6% de 350 000 = 0,06 × 350 000 = 21 000.", ["0,06 × 350 000."]))
ex.append(dnum(3, C, "Um depósito de 200 000 Kz rende 5% de juro ao fim do ano. Qual é o valor final, em Kz?", F(210000), "200 000 × 1,05 = 210 000.", ["Fator 1,05."]))
ex.append(dnum(3, C, "Um artigo custa 12 000 Kz sem IVA. Quanto custa com 14% de IVA, em Kz?", F(13680), "12 000 × 1,14 = 13 680 Kz.", ["Fator 1,14."]))
ex.append(tf(2, C, "Há prejuízo quando o preço de venda é menor que o custo.", True, "Prejuízo = custo − venda > 0.", ["Venda < custo."]))
ex.append(tf(2, C, "Um lucro de 20% sobre o custo é o mesmo que 20% sobre o preço de venda.", False, "Sobre o custo de 100 Kz: venda 120 Kz; o lucro de 20 Kz é 16,7% de 120 Kz.", ["Muda o valor de referência."]))
ex.append(mc(2, C, "Qual é a fórmula do lucro?", ["Lucro = Venda − Custo", "Lucro = Custo − Venda", "Lucro = Venda + Custo", "Lucro = Venda ÷ Custo"], 0, "Quando Venda > Custo há lucro; a diferença é o lucro.", ["Diferença positiva."]))
A = lesson('percentagens', 'Aplicações comerciais', 'aplicacoes-comerciais-percentagens', 'Lucro, prejuízo, comissões, juros e IVA: aplicações com Kwanzas', 'percentagens-lucro-prejuizo-comercial',
 'Aplica percentagens a lucro, prejuízo, comissões, juros simples e impostos, em Kwanzas.', 30,
 "**Objetivos:** calcular lucro e prejuízo, determinar preços de venda, comissões, juros e impostos usando percentagens. **Pré-requisitos:** percentagem de um valor, aumentos e descontos.\n\nUm comerciante compra por 8 000 Kz e quer vender com 25% de lucro. Um vendedor recebe comissão de 6% sobre as vendas. Um banco paga juros sobre um depósito. Em todos os casos usamos as mesmas ideias de percentagem, aplicadas ao dinheiro.",
 "**Custo** é o que pagaste; **venda** é o que recebes. **Lucro** = venda − custo (quando positivo); **prejuízo** = custo − venda (quando venda < custo). A **percentagem de lucro** calcula-se, em regra, **sobre o custo**: $\\frac{\\text{lucro}}{\\text{custo}}\\times100\\%$.\n\n**Preço de venda com lucro $p\\%$:** custo $\\times(1+\\frac{p}{100})$. Ex.: custo 8 000 Kz com 25% de lucro → $8\\,000\\times1{,}25=10\\,000$ Kz.\n\n**Para achar o custo** conhecendo a venda e o lucro: custo $=\\dfrac{\\text{venda}}{1+p/100}$.\n\n**Comissão:** percentagem das vendas que o vendedor recebe: $6\\%$ de 350 000 = 21 000 Kz.\n\n**Juro simples:** juro $=$ capital $\\times$ taxa $\\times$ tempo. Um depósito de 200 000 Kz a 5% ao ano rende 10 000 Kz num ano e fica em 210 000 Kz.\n\n**Imposto (IVA):** sobe o preço: com 14% de IVA, multiplica por 1,14.\n\nNota: as percentagens de lucro sobre o custo e sobre a venda são **diferentes**. Diz sempre sobre que valor se calcula.\n\n**Erros comuns:** calcular o lucro sobre a venda quando se pede sobre o custo; confundir lucro com preço de venda; esquecer de somar o imposto.",
 "O **lucro** é a diferença positiva entre o preço de venda e o custo; o **prejuízo** é a diferença quando o preço de venda é inferior ao custo. A **comissão** é uma percentagem sobre o valor das vendas. O **juro simples** é $J=C\\times i\\times t$. O **IVA** é um imposto percentual sobre o preço.",
 "$$\\text{Lucro}=V-C\\qquad\\%\\text{lucro}=\\frac{V-C}{C}\\times100$$\n\n$$V=C\\times(1+\\tfrac{p}{100})\\qquad C=\\frac{V}{1+p/100}\\qquad J=C\\times i\\times t$$",
 "**Exemplo 1 (lucro).** Compra 4 000 Kz, venda 5 000 Kz: lucro 1 000 Kz, ou seja, $\\frac{1\\,000}{4\\,000}=25\\%$ sobre o custo.\n\n**Exemplo 2 (prejuízo).** Compra 7 500 Kz, venda 6 000 Kz: prejuízo 1 500 Kz, ou seja 20% do custo.\n\n**Exemplo 3 (preço de venda).** Custo 8 000 Kz com 25% de lucro: $8\\,000\\times1{,}25=10\\,000$ Kz.\n\n**Exemplo 4 (comissão).** 6% de 350 000 Kz = 21 000 Kz.\n\n**Exemplo 5 (juros).** 200 000 Kz a 5% ao ano rendem $200\\,000\\times0{,}05=10\\,000$ Kz num ano.\n\n**Aplicação.** Um artigo de 12 000 Kz com IVA de 14%: $12\\,000\\times1{,}14=13\\,680$ Kz.",
 "Resolve connosco: **vendeste um artigo por 11 000 Kz e ganhaste 10% sobre o custo. Quanto tinha custado?**\n\n1) Venda $=$ custo $\\times1{,}1$.\n\n2) Custo $=11\\,000\\div1{,}1=10\\,000$ Kz.\n\n3) Lucro $=1\\,000$ Kz, que é 10% de 10 000 ✓.\n\n4) Atenção: não é 11 000 − 10% de 11 000 (= 9 900), porque o lucro é sobre o custo.",
 "**Desafio.** Um comerciante compra 50 sacos de farinha a 6 000 Kz cada. Vende 40 sacos com 25% de lucro e os 10 restantes com 10% de prejuízo. Ganhou ou perdeu no total? Quanto?",
 "Consideras a competência dominada quando consegues: (1) calcular lucro e prejuízo e as suas percentagens; (2) determinar o preço de venda e o custo; (3) calcular comissões, juros simples e IVA; (4) dizer sobre que valor incide a percentagem.", ex)
write(1, 36, A)
print('D/P ok')

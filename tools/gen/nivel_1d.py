"""Nível 1 — Tema 3 (Operações básicas: 18–21) e Tema 4 (Tabuada: 22–24)."""
from common import *
import math

# ===== 18. Adição e subtração: propriedades e operações inversas =====
C = 'operacoes.adicao_subtracao'; ex = []
for a, b in [(4538, 2765), (12907, 8486), (60000, 24875), (3049, 987)]:
    ex.append(num(1 if a < 5000 else 2, C, f"Calcula {a} + {b}.", a + b, f"{a} + {b} = {a+b}.", ["Alinha as ordens.", f"= {a+b}."]))
for a, b in [(9000, 3478), (15204, 7899), (100000, 46321)]:
    ex.append(num(2, C, f"Calcula {a} − {b}.", a - b, f"{a} − {b} = {a-b}. Verifica: {a-b} + {b} = {a}.", ["Subtrai coluna a coluna, pedindo emprestado quando preciso.", f"Prova: {a-b} + {b} = {a}."]))
ex.append(num(2, C, "Calcula de forma esperta 25 + 48 + 75 usando as propriedades.", 148, "Agrupa 25 + 75 = 100 e soma 48: 148.", ["Comutativa e associativa.", "(25 + 75) + 48 = 148."]))
ex.append(num(2, C, "Qual é o número que somado a 3 456 dá 5 000?", 5000 - 3456, "É a operação inversa: 5 000 − 3 456 = 1 544.", ["Subtrai.", "= 1 544."]))
ex.append(num(2, C, "Subtraindo 2 487 a um número obtém-se 6 513. Qual é esse número?", 6513 + 2487, "Operação inversa: 6 513 + 2 487 = 9 000.", ["Soma o subtraendo à diferença."]))
ex.append(num(3, C, "Estima 4 987 + 3 012 arredondando às centenas e dá a soma estimada.", 5000 + 3000, "4 987 ≈ 5 000 e 3 012 ≈ 3 000; a soma estimada é 8 000.", ["Arredonda às centenas.", "5 000 + 3 000."]))
ex.append(num(3, C, "O Paulo tinha 15 000 Kz, gastou 4 750 em comida e 3 250 em transporte. Quanto lhe sobra, em Kz?", 15000 - 4750 - 3250, "4 750 + 3 250 = 8 000 gastos; 15 000 − 8 000 = 7 000 Kz.", ["Soma os gastos.", "Subtrai ao que tinha."]))
ex.append(tf(2, C, "A subtração é comutativa: 9 − 4 = 4 − 9.", False, "9 − 4 = 5 mas 4 − 9 = −5 (nem existe nos naturais). A subtração não é comutativa.", ["Troca a ordem e vê."]))
ex.append(tf(2, C, "(20 + 5) + 7 = 20 + (5 + 7).", True, "Propriedade associativa da adição: ambos dão 32.", ["Associativa."]))
ex.append(mc(2, C, "Qual é o elemento neutro da adição?", ["0", "1", "10", "Não existe"], 0, "a + 0 = a, qualquer que seja a.", ["a + 0 = a."]))
ex.append(mc(2, C, "A operação inversa da adição é…", ["A subtração", "A multiplicação", "A divisão", "A potenciação"], 0, "Se a + b = c, então c − b = a.", ["Desfaz a soma."]))
A = lesson('operacoes-basicas', 'Adição e subtração', 'adicao-subtracao', 'Adição e subtração: propriedades, operações inversas e estimativa',
 'adicao-subtracao-propriedades-estimativa', 'Domina a adição e a subtração, as suas propriedades, a prova dos nove por operação inversa e a estimativa.', 25,
 "**Objetivos:** somar e subtrair com segurança, usar as propriedades comutativa, associativa e do elemento neutro, verificar resultados com a operação inversa e estimar. **Pré-requisitos:** sistema decimal e tabuada da adição.\n\nSomar e subtrair é o que fazemos todos os dias: contar o troco, somar despesas, ver quanto falta para poupar uma quantia. Fazê-lo bem e depressa é a base de toda a matemática seguinte.",
 "**Adição:** juntar quantidades. As parcelas são os números que se juntam e a **soma** é o resultado. **Subtração:** tirar, comparar ou achar o que falta. O **aditivo** (ou minuendo) é o número de onde se tira, o **subtrativo** é o que se tira e a **diferença** (ou resto) é o resultado.\n\nPropriedades da adição: **comutativa** ($a+b=b+a$), **associativa** ($(a+b)+c=a+(b+c)$) e **elemento neutro** 0. Servem para calcular de cabeça: $25+48+75=(25+75)+48=148$.\n\nA subtração **não** é comutativa nem associativa. Mas tem uma prova simples: a **operação inversa**. Se $a-b=d$, então $d+b=a$. Se $a+b=s$, então $s-b=a$. Usa sempre para confirmar contas.\n\nPara estimar, arredonda os números (à dezena, centena ou milhar) e calcula de cabeça. Assim detetas resultados absurdos: $4\\,987+3\\,012$ ronda os 8 000.\n\n**Erros comuns:** desalinhar as ordens; esquecer de «levar» na soma ou de «pedir emprestado» na subtração; trocar os termos da subtração.",
 "A **adição** de naturais $a+b$ é o número de elementos de dois conjuntos disjuntos com $a$ e $b$ elementos. A **subtração** $a-b$ ($a\\ge b$) é o número $d$ tal que $b+d=a$. A subtração é a **operação inversa** da adição.",
 "$$a+b=b+a\\quad(a+b)+c=a+(b+c)\\quad a+0=a$$\n\n$$a-b=d\\iff d+b=a\\qquad a-(b+c)=a-b-c$$\n\nCompensação: $a-b=(a+k)-(b+k)$, útil para calcular de cabeça ($83-29=84-30=54$).",
 "**Exemplo 1.** $4\\,538+2\\,765=7\\,303$ (alinha, soma e leva).\n\n**Exemplo 2.** $9\\,000-3\\,478=5\\,522$. Prova: $5\\,522+3\\,478=9\\,000$ ✓.\n\n**Exemplo 3 (esperto).** $25+48+75=(25+75)+48=100+48=148$.\n\n**Exemplo 4 (compensação).** $83-29=84-30=54$ (soma 1 aos dois números).\n\n**Exemplo 5 (inversa).** Qual o número que somado a 3 456 dá 5 000? É $5\\,000-3\\,456=1\\,544$.\n\n**Aplicação.** O Paulo tinha 15 000 Kz e gastou 4 750 e 3 250: $4\\,750+3\\,250=8\\,000$ e $15\\,000-8\\,000=7\\,000$ Kz restantes.",
 "Resolve connosco: **calcula 7 204 − 3 897 e confirma o resultado.**\n\n1) Sem empréstimos: $7\\,204-3\\,900=3\\,304$ (3 900 é um arredondamento).\n\n2) Como tirámos 3 a mais ($3\\,900-3\\,897=3$), soma de volta: $3\\,304+3=3\\,307$.\n\n3) Prova: $3\\,307+3\\,897=7\\,204$ ✓.\n\n4) Estimativa: $7\\,200-3\\,900=3\\,300$, próximo ✓.",
 "**Desafio.** Soma mentalmente os números de 1 a 100 emparelhando extremos (1+100, 2+99, …). Quantos pares há e qual é cada soma? Qual é o total?",
 "Consideras a competência dominada quando consegues: (1) somar e subtrair com reserva e empréstimo; (2) usar as propriedades para facilitar contas; (3) verificar com a operação inversa; (4) estimar o resultado antes de calcular.", ex)
write(1, 18, A)

# ===== 19. Multiplicação e divisão =====
C = 'operacoes.multiplicacao_divisao'; ex = []
for a, b in [(47, 6), (253, 8), (36, 25), (128, 15)]:
    ex.append(num(1 if a < 100 else 2, C, f"Calcula {a} × {b}.", a * b, f"{a} × {b} = {a*b}.", ["Multiplica por cada algarismo.", f"= {a*b}."]))
for a, b in [(1536, 12), (4875, 25), (9000, 36)]:
    ex.append(num(2, C, f"Calcula {a} ÷ {b}.", a // b, f"{a} ÷ {b} = {a//b} (exata, porque {b} × {a//b} = {a}).", [f"{b} × {a//b} = {a}."]))
ex.append(num(2, C, "Usa a propriedade distributiva para calcular 7 × 102.", 714, "7 × 102 = 7 × 100 + 7 × 2 = 700 + 14 = 714.", ["Decompõe 102 = 100 + 2."]))
ex.append(num(2, C, "Usa a propriedade distributiva para calcular 9 × 98.", 882, "9 × 98 = 9 × 100 − 9 × 2 = 900 − 18 = 882.", ["98 = 100 − 2."]))
ex.append(num(3, C, "Um autocarro leva 52 passageiros. Quantos passageiros levam 18 autocarros cheios?", 52 * 18, "52 × 18 = 936.", ["52 × 18 = 52 × 10 + 52 × 8.", "520 + 416 = 936."]))
ex.append(num(3, C, "Repartem-se 1 260 Kz por 15 pessoas em partes iguais. Quanto recebe cada uma, em Kz?", 1260 // 15, "1 260 ÷ 15 = 84.", ["15 × 84 = 1 260."]))
ex.append(num(2, C, "Qual é o número que multiplicado por 14 dá 238?", 238 // 14, "Operação inversa: 238 ÷ 14 = 17.", ["14 × 17 = 238."]))
ex.append(tf(2, C, "Qualquer número multiplicado por zero dá zero.", True, "O zero é elemento absorvente da multiplicação.", ["a × 0 = 0."]))
ex.append(tf(2, C, "A divisão é comutativa: 12 ÷ 4 = 4 ÷ 12.", False, "12 ÷ 4 = 3 e 4 ÷ 12 não é natural. A divisão não é comutativa.", ["Troca e vê."]))
ex.append(mc(2, C, "Qual é o elemento neutro da multiplicação?", ["1", "0", "10", "Não existe"], 0, "a × 1 = a.", ["a × 1 = a."]))
A = lesson('operacoes-basicas', 'Multiplicação e divisão', 'multiplicacao-divisao', 'Multiplicação e divisão: propriedades e operações inversas',
 'multiplicacao-divisao-propriedades-inversas', 'Multiplica e divide naturais, usa as propriedades comutativa, associativa e distributiva e relaciona as duas operações.', 25,
 "**Objetivos:** multiplicar e dividir naturais, distinguir divisão exata de não exata, usar as propriedades e a operação inversa. **Pré-requisitos:** tabuada e adição.\n\nSe uma caixa tem 24 garrafas, quantas há em 18 caixas? Quantos autocarros de 52 lugares são precisos para 300 alunos? São perguntas de **multiplicação** e **divisão**, as operações do dia a dia do comércio e da construção.",
 "**Multiplicação:** soma de parcelas iguais. $a\\times b$: $a$ e $b$ são os **fatores** e o resultado é o **produto**. **Divisão:** repartir ou medir quantas vezes cabe. $D\\div d=q$ (resto $r$): $D$ é o dividendo, $d$ o divisor, $q$ o quociente e $r$ o resto; vale sempre $D=d\\times q+r$ com $r<d$. Se $r=0$ a divisão é **exata**.\n\nPropriedades da multiplicação: **comutativa** ($ab=ba$), **associativa** ($(ab)c=a(bc)$), **elemento neutro** 1, **absorvente** 0 e **distributiva** em relação à soma: $a(b+c)=ab+ac$. A distributiva permite calcular de cabeça: $7\\times102=7\\times100+7\\times2=714$ e $9\\times98=9\\times100-9\\times2=882$.\n\nA divisão é a **operação inversa** da multiplicação: se $a\\times b=c$ então $c\\div a=b$. Por isso, para dividir, pergunta-te «o que multiplicado pelo divisor dá o dividendo?». E nunca se divide por zero.\n\n**Erros comuns:** esquecer de deslocar a linha na multiplicação por dezenas; achar que $a\\div b=b\\div a$; deixar resto maior ou igual ao divisor; dividir por zero.",
 "O **produto** de $a$ por $b$ (naturais) é $a\\times b=\\underbrace{a+a+\\cdots+a}_{b\\text{ vezes}}$. A **divisão euclidiana** de $D$ por $d\\neq0$ dá o **quociente** $q$ e o **resto** $r$ com $D=d\\times q+r$ e $0\\le r<d$. A divisão é **exata** se $r=0$.",
 "$$ab=ba\\quad(ab)c=a(bc)\\quad a\\times1=a\\quad a\\times0=0\\quad a(b+c)=ab+ac$$\n\n$$D=d\\times q+r,\\quad 0\\le r<d,\\ d\\ne0$$\n\nOperação inversa: $a\\times b=c\\iff c\\div b=a$.",
 "**Exemplo 1.** $47\\times6=282$ ($40\\times6=240$ e $7\\times6=42$).\n\n**Exemplo 2.** $36\\times25=900$ ($36\\times100\\div4$).\n\n**Exemplo 3 (distributiva).** $7\\times102=700+14=714$.\n\n**Exemplo 4 (divisão exata).** $1\\,536\\div12=128$, porque $12\\times128=1\\,536$.\n\n**Exemplo 5 (com resto).** $85\\div8=10$ resto 5, porque $8\\times10+5=85$.\n\n**Aplicação.** Um autocarro leva 52 passageiros: 18 autocarros cheios levam $52\\times18=936$. Para 300 alunos são precisos $300\\div52=5$ resto 40, logo 6 autocarros (o sexto vai incompleto).",
 "Resolve connosco: **divide 1 260 por 15 e confirma.**\n\n1) 126 ÷ 15 = 8 (15 × 8 = 120), resto 6. Baixa o 0: 60.\n\n2) 60 ÷ 15 = 4.\n\n3) Quociente 84, resto 0 (divisão exata).\n\n4) Prova: $15\\times84=1\\,260$ ✓.",
 "**Desafio.** Calcula $25\\times48$ de três maneiras: (a) $25\\times48$ direto; (b) $100\\times48\\div4$; (c) $48\\div4\\times100$. Qual é mais rápida e porquê?",
 "Consideras a competência dominada quando consegues: (1) multiplicar e dividir com vários algarismos; (2) escrever $D=d\\times q+r$; (3) usar a distributiva para calcular de cabeça; (4) usar a operação inversa para confirmar.", ex)
write(1, 19, A)

# ===== 20. Expressões numéricas, parênteses, colchetes, chavetas; cálculo mental =====
C = 'operacoes.expressoes'; ex = []
E = [("2+3\\times4", 2 + 3 * 4), ("(2+3)\\times4", (2 + 3) * 4), ("20-6\\div3", 20 - 2), ("(20-6)\\div2", 7), ("5\\times(8-3)+4", 29), ("[12-(3+4)]\\times3", 15), ("2\\times\\{3+[10-(4+2)]\\}", 14), ("100-4\\times(6+9)", 40), ("(18+6)\\div(4\\times2)", 3), ("3+2\\times[15-3\\times(2+1)]", 15)]
for k, (s, v) in enumerate(E):
    ex.append(num(1 if k < 3 else 2 if k < 8 else 3, C, f"Calcula ${s}$.", v, f"Respeitando a ordem das operações: ${s}={v}$.", ["Parênteses (de dentro para fora).", "× e ÷.", "+ e −."]))
ex.append(num(2, C, "Calcula de cabeça 50 × 18 usando 50 × 20 − 50 × 2.", 900, "1 000 − 100 = 900.", ["50 × 20 = 1 000.", "50 × 2 = 100."]))
ex.append(num(2, C, "Calcula de cabeça 4 × 35 × 25.", 3500, "35 × (4 × 25) = 35 × 100 = 3 500.", ["Agrupa 4 × 25 = 100."]))
ex.append(tf(2, C, "$6+4\\times5=50$.", False, "Primeiro a multiplicação: 4×5 = 20, depois 6 + 20 = 26.", ["× antes de +."]))
ex.append(mc(2, C, "Quais são os símbolos de agrupamento, do mais interior para o mais exterior?", ["( ), [ ], { }", "{ }, [ ], ( )", "[ ], ( ), { }", "( ), { }, [ ]"], 0, "Resolvem-se de dentro para fora: primeiro (), depois [], depois {}.", ["Dentro para fora."]))
A = lesson('operacoes-basicas', 'Expressões numéricas', 'expressoes-numericas-operacoes', 'Expressões numéricas: parênteses, colchetes, chavetas e cálculo mental',
 'expressoes-numericas-agrupamentos-calculo-mental', 'Resolve expressões com parênteses, colchetes e chavetas pela ordem correta e calcula de cabeça com truques.', 25,
 "**Objetivos:** calcular expressões numéricas com as quatro operações e símbolos de agrupamento, e usar estratégias de cálculo mental. **Pré-requisitos:** as quatro operações e a ordem de resolução.\n\nQuanto é $2+3\\times4$? Se somares primeiro obténs 20; se multiplicares primeiro, 14. Para todos obtermos o mesmo resultado há uma regra universal: a **ordem das operações**.",
 "**Ordem:** (1) resolvem-se os agrupamentos, de dentro para fora: primeiro $(\\,)$, depois $[\\,]$, depois $\\{\\,\\}$; (2) potências e raízes; (3) multiplicações e divisões, da esquerda para a direita; (4) adições e subtrações, da esquerda para a direita.\n\nOs parênteses mudam a ordem: $(2+3)\\times4=20$ mas $2+3\\times4=14$.\n\n**Cálculo mental:** usa as propriedades. Compensação: $83-29=84-30$. Distributiva: $50\\times18=50\\times20-50\\times2$. Associatividade: $4\\times35\\times25=35\\times(4\\times25)=3\\,500$. Dobros e metades: $15\\times12=30\\times6$. Estima antes de calcular.\n\n**Erros comuns:** fazer as contas da esquerda para a direita sem prioridade; esquecer que $\\times$ e $\\div$ têm a mesma prioridade; resolver o parêntese mais exterior antes do interior.",
 "Uma **expressão numérica** é uma sequência de números e operações. Os **símbolos de agrupamento** são parênteses $(\\,)$, colchetes $[\\,]$ e chavetas $\\{\\,\\}$. O **valor** da expressão é o resultado de a resolver pela ordem das operações.",
 "Ordem: agrupamentos (dentro → fora) → potências/raízes → $\\times,\\div$ → $+,-$.\n\n$$a+b\\times c=a+(b\\times c)\\qquad(a+b)\\times c=ac+bc$$",
 "**Exemplo 1.** $2+3\\times4=2+12=14$.\n\n**Exemplo 2.** $(2+3)\\times4=5\\times4=20$.\n\n**Exemplo 3.** $5\\times(8-3)+4=5\\times5+4=29$.\n\n**Exemplo 4 (colchetes).** $[12-(3+4)]\\times3=[12-7]\\times3=5\\times3=15$.\n\n**Exemplo 5 (chavetas).** $2\\times\\{3+[10-(4+2)]\\}=2\\times\\{3+[10-6]\\}=2\\times\\{3+4\\}=14$.\n\n**Aplicação.** Compraste 4 cadernos a 250 Kz e 3 canetas a 120 Kz e pagaste com 2 000 Kz. Troco: $2\\,000-(4\\times250+3\\times120)=2\\,000-1\\,360=640$ Kz.",
 "Resolve connosco: **calcula $3+2\\times[15-3\\times(2+1)]$.**\n\n1) Parênteses: $2+1=3$.\n\n2) Dentro do colchete: $3\\times3=9$ e $15-9=6$.\n\n3) Fora: $2\\times6=12$.\n\n4) Soma: $3+12=15$.\n\n5) Confere o fim: nenhuma operação ficou por fazer ✓.",
 "**Desafio.** Com os algarismos 4, 4, 4, 4 e quaisquer operações e parênteses, consegues obter todos os números de 0 a 5? Por exemplo, $(4+4)\\div(4+4)=1$. Descobre pelo menos quatro.",
 "Consideras a competência dominada quando consegues: (1) resolver expressões respeitando a ordem; (2) resolver de dentro para fora com (), [] e {}; (3) usar truques de cálculo mental; (4) detetar o erro de calcular sempre da esquerda para a direita.", ex)
write(1, 20, A)

# ===== 21. Problemas com as quatro operações =====
C = 'operacoes.problemas'; ex = []
ex.append(num(1, C, "Uma loja vendeu 125 sacos de arroz de manhã e 187 à tarde. Quantos sacos vendeu no dia?", 125 + 187, "125 + 187 = 312.", ["Soma."]))
ex.append(num(1, C, "Um depósito tinha 5 000 litros e gastaram-se 1 875. Quantos litros restam?", 5000 - 1875, "5 000 − 1 875 = 3 125.", ["Subtrai."]))
ex.append(num(2, C, "Cada caixa tem 24 latas. Quantas latas há em 15 caixas?", 24 * 15, "24 × 15 = 360.", ["Multiplica."]))
ex.append(num(2, C, "Repartem-se 504 lápis por 18 alunos. Quantos lápis recebe cada um?", 504 // 18, "504 ÷ 18 = 28.", ["Divide."]))
ex.append(num(2, C, "Compraste 3 cadernos a 450 Kz cada e uma caneta a 275 Kz. Pagaste com 2 000 Kz. Quanto recebes de troco?", 2000 - (3 * 450 + 275), "3 × 450 = 1 350; 1 350 + 275 = 1 625; 2 000 − 1 625 = 375 Kz.", ["Calcula o total.", "Subtrai ao que deste."]))
ex.append(num(3, C, "Um livro de 288 páginas é lido em 12 dias, lendo o mesmo número de páginas por dia. Quantas páginas por dia?", 288 // 12, "288 ÷ 12 = 24.", ["Divide."]))
ex.append(num(3, C, "O Manuel tem o triplo da idade da irmã. Juntos têm 48 anos. Quantos anos tem a irmã?", 12, "Se a irmã tem x, o Manuel tem 3x e 4x = 48, logo x = 12.", ["x + 3x = 48.", "x = 12."]))
ex.append(num(3, C, "Uma fábrica produz 450 peças por dia. Em 12 dias produziu 5 000 peças. Quantas faltam para chegar a 6 000 depois desses 12 dias, sabendo que 12 × 450 = 5 400?", 6000 - 12 * 450, "12 × 450 = 5 400; faltam 6 000 − 5 400 = 600.", ["Total produzido: 5 400.", "6 000 − 5 400 = 600."]))
ex.append(num(3, C, "Uma turma tem 36 alunos e cada mesa leva 4. Quantas mesas são precisas?", 36 // 4, "36 ÷ 4 = 9 mesas.", ["Divide."]))
ex.append(num(3, C, "Para levar 130 pessoas em autocarros de 45 lugares, quantos autocarros são precisos?", -(-130 // 45), "130 ÷ 45 = 2 resto 40, por isso precisa-se de mais um: 3 autocarros.", ["2 autocarros levam 90.", "Faltam 40: um terceiro."]))
ex.append(tf(2, C, "Num problema de «repartir em partes iguais» usa-se normalmente a divisão.", True, "Repartir em partes iguais é dividir.", ["Dividir = repartir."]))
ex.append(mc(2, C, "Quando se pede «quantas vezes cabe», qual é a operação?", ["Divisão", "Subtração apenas", "Multiplicação", "Potenciação"], 0, "Quantas vezes um número cabe noutro é uma divisão.", ["Medir = dividir."]))
A = lesson('operacoes-basicas', 'Problemas com as quatro operações', 'problemas-quatro-operacoes', 'Problemas com as quatro operações e estimativa de resultados',
 'problemas-quatro-operacoes-estimativa', 'Resolve problemas do dia a dia escolhendo a operação certa, estimando e verificando o resultado.', 30,
 "**Objetivos:** ler um problema, escolher as operações, calcular, verificar e interpretar o resultado, estimando antes. **Pré-requisitos:** as quatro operações e a ordem de resolução.\n\nSaber calcular não basta: é preciso saber **qual** conta fazer. Num mercado, numa obra ou numa loja, os problemas vêm em palavras, e traduzi-los em contas é a competência que mais se usa na vida.",
 "Método em 5 passos: (1) **Lê** com atenção e identifica o que se pede; (2) **Organiza** os dados (faz um desenho ou um esquema); (3) **Escolhe** a operação; (4) **Calcula** e **estima** para ver se faz sentido; (5) **Responde** com uma frase, com a unidade (Kz, metros, kg).\n\nPalavras-pista: *juntar, ao todo, acrescentar* → adição; *sobra, falta, diferença, tirar* → subtração; *cada, vezes, em ... grupos iguais* → multiplicação; *repartir, em partes iguais, quantos cabem* → divisão.\n\nAtenção ao **resto**: se há 130 pessoas e cada autocarro leva 45, $130\\div45=2$ resto 40, mas precisas de **3** autocarros, porque as 40 pessoas também têm de viajar. Interpreta o resto no contexto.\n\nProblemas em dois passos: calcula primeiro o que o enunciado não diz diretamente (o total das compras) e depois o que pede (o troco).\n\n**Erros comuns:** escolher a operação pela palavra sem ler o problema todo; esquecer a unidade; não verificar se a resposta é razoável.",
 "Um **problema** é uma situação com dados e uma pergunta. **Resolver** é modelar o problema com operações, calcular e interpretar. A **estimativa** é um valor aproximado obtido com arredondamentos, usado para validar o resultado.",
 "Total = soma das partes. Resto = total − parte. Total = valor unitário × quantidade. Cada parte = total ÷ nº de partes.\n\n$$\\text{Troco}=\\text{Pago}-\\text{Custo total}$$",
 "**Exemplo 1 (adição).** Vendidos 125 sacos de manhã e 187 à tarde: $125+187=312$ sacos.\n\n**Exemplo 2 (subtração).** Depósito de 5 000 L, gastaram-se 1 875 L: sobram $5\\,000-1\\,875=3\\,125$ L.\n\n**Exemplo 3 (multiplicação).** 15 caixas de 24 latas: $24\\times15=360$ latas.\n\n**Exemplo 4 (divisão).** 504 lápis por 18 alunos: $504\\div18=28$ cada.\n\n**Exemplo 5 (dois passos).** 3 cadernos a 450 Kz e uma caneta a 275 Kz; pagas com 2 000 Kz. Total: $3\\times450+275=1\\,625$. Troco: $2\\,000-1\\,625=375$ Kz.\n\n**Aplicação.** Para 130 pessoas em autocarros de 45 lugares: $130\\div45$ dá 2 e resto 40, logo são precisos 3 autocarros.",
 "Resolve connosco: **uma costureira faz 12 camisas por dia. Em 15 dias fez as camisas todas e ainda lhe encomendaram mais 40. Quantas camisas fez ao todo?**\n\n1) Em 15 dias: $12\\times15=180$ camisas.\n\n2) Mais as 40 encomendadas: $180+40=220$.\n\n3) Estimativa: $12\\times15$ é cerca de $10\\times15=150$ mais $2\\times15=30$, 180 ✓.\n\n4) Resposta: fez 220 camisas ao todo.",
 "**Desafio.** Um taxista cobra 500 Kz de bandeirada mais 120 Kz por quilómetro. Quanto custa uma viagem de 15 km? E até quantos quilómetros podes ir com 3 000 Kz? Escreve as duas contas e explica o resto.",
 "Consideras a competência dominada quando consegues: (1) traduzir problemas em operações; (2) resolver problemas de dois passos; (3) interpretar o resto no contexto; (4) estimar e responder com unidade.", ex)
write(1, 21, A)

# ===== 22. Introdução à multiplicação, tabuadas 1–5 e propriedades =====
C = 'tabuada.1_a_5'; ex = []
import random; random.seed(7)
for t, n in [(2, 7), (3, 9), (4, 6), (5, 8), (3, 12), (4, 9), (5, 11), (2, 12)]:
    ex.append(num(1, C, f"Quanto é {t} × {n}?", t * n, f"{t} × {n} = {t*n}.", [f"{t} × {n} = {t*n}."]))
ex.append(num(1, C, "Quanto é 1 × 37?", 37, "O 1 é o elemento neutro: 1 × n = n.", ["1 × n = n."]))
ex.append(num(2, C, "Completa a sequência da tabuada do 4: 4, 8, 12, 16, ☐. Qual o número em falta?", 20, "Somam-se 4 de cada vez: 16 + 4 = 20.", ["Soma 4."]))
ex.append(num(2, C, "Qual o 9.º número da tabuada do 3 (3 × 9)?", 27, "3 × 9 = 27.", ["3 × 9."]))
ex.append(num(2, C, "Quantas patas têm 7 gatos?", 28, "7 × 4 = 28 patas.", ["4 patas por gato."]))
ex.append(num(2, C, "Cada mesa tem 5 cadeiras. Quantas cadeiras há em 12 mesas?", 60, "12 × 5 = 60.", ["12 × 5."]))
ex.append(num(3, C, "Qual é o resultado de 20 ÷ 5 + 3 × 4?", 4 + 12, "20 ÷ 5 = 4; 3 × 4 = 12; 4 + 12 = 16.", ["Primeiro × e ÷."]))
ex.append(tf(1, C, "Os resultados da tabuada do 5 acabam sempre em 0 ou 5.", True, "5, 10, 15, 20, 25…", ["Observa os resultados."]))
ex.append(tf(2, C, "3 × 8 = 8 × 3.", True, "A multiplicação é comutativa.", ["Comutativa."]))
ex.append(mc(2, C, "Qual é o dobro de 4 × 6?", ["48", "24", "10", "12"], 0, "4 × 6 = 24 e o dobro é 48.", ["24 × 2 = 48."]))
A = lesson('tabuada', 'Tabuadas do 1 ao 12', 'tabuadas-1-a-12', 'Introdução à multiplicação e tabuadas do 1 ao 5',
 'tabuadas-1-ao-5-introducao', 'Compreende a multiplicação como soma repetida e domina as tabuadas do 1, 2, 3, 4 e 5 com padrões.', 20,
 "**Objetivos:** compreender o que é multiplicar, dominar as tabuadas do 1 ao 5 e descobrir os seus padrões. **Pré-requisitos:** contar e somar.\n\nSe um gato tem 4 patas, quantas patas têm 7 gatos? Podes somar $4+4+4+4+4+4+4=28$, ou multiplicar $7\\times4=28$. Multiplicar é uma **soma repetida** em forma curta, e a **tabuada** é a lista desses resultados.",
 "**Tabuada do 1:** $1\\times n=n$ (o 1 não muda nada). **Tabuada do 2:** o dobro; os resultados são os números pares. **Tabuada do 3:** 3, 6, 9, 12, 15…; a soma dos algarismos de cada resultado é sempre múltipla de 3. **Tabuada do 4:** o dobro do dobro. **Tabuada do 5:** 5, 10, 15, 20…; termina sempre em 5 ou 0, e cada resultado é metade do da tabuada do 10.\n\nPropriedade fundamental: $a\\times b=b\\times a$. Se sabes $3\\times8=24$, já sabes $8\\times3$. Isto reduz muito o que há para aprender.\n\nUsa a tabuada de várias formas: de memória, a contar em saltos (2, 4, 6, 8…), e pelas relações (4 é o dobro de 2).\n\n**Erros comuns:** confundir $3\\times4$ com $3+4$; esquecer que $1\\times n=n$ e $0\\times n=0$; decorar sem entender o padrão.",
 "A **multiplicação** $a\\times b$ é a soma de $b$ parcelas iguais a $a$. O **produto** é o resultado e $a$, $b$ os **fatores**. A **tabuada do n** é a lista $n\\times1,n\\times2,n\\times3,\\ldots$",
 "$$a\\times b=b\\times a\\qquad1\\times n=n\\qquad0\\times n=0$$\n\n$4\\times n=2\\times(2\\times n)$ e $5\\times n=\\dfrac{10\\times n}{2}$.\n\nTabuada do 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36.",
 "**Exemplo 1.** $3\\times9=27$ (9 + 9 + 9).\n\n**Exemplo 2.** $4\\times6=24$ (dobro de 12, ou dobro do dobro de 6).\n\n**Exemplo 3.** $5\\times8=40$ (metade de $10\\times8=80$).\n\n**Exemplo 4.** $1\\times37=37$ e $0\\times37=0$.\n\n**Exemplo 5 (comutativa).** Se $3\\times8=24$ então $8\\times3=24$.\n\n**Aplicação.** 12 mesas com 5 cadeiras cada têm $12\\times5=60$ cadeiras.",
 "Resolve connosco: **uma caixa tem 4 filas de 5 ovos. Quantos ovos há em 3 caixas?**\n\n1) Ovos por caixa: $4\\times5=20$.\n\n2) Em 3 caixas: $3\\times20=60$.\n\n3) Verifica com a associativa: $3\\times4\\times5=12\\times5=60$ ✓.",
 "**Desafio.** Escreve a tabuada do 3 e soma os algarismos de cada resultado (3, 6, 9, 3, 6, 9…). Que padrão encontras? E na tabuada do 9? Experimenta.",
 "Consideras a competência dominada quando consegues: (1) explicar a multiplicação como soma repetida; (2) responder às tabuadas do 1 ao 5 sem demora; (3) usar a comutativa; (4) descobrir padrões.", ex)
write(1, 22, A)

# ===== 23. Tabuadas 6–9 =====
C = 'tabuada.6_a_9'; ex = []
for t, n in [(6, 7), (7, 8), (8, 9), (9, 6), (6, 8), (7, 9), (8, 8), (9, 9), (6, 12), (7, 12)]:
    ex.append(num(1 if t * n < 50 else 2, C, f"Quanto é {t} × {n}?", t * n, f"{t} × {n} = {t*n}.", [f"{t} × {n} = {t*n}."]))
ex.append(num(2, C, "Quanto é 9 × 7 usando 10 × 7 − 7?", 63, "70 − 7 = 63.", ["10 × 7 = 70."]))
ex.append(num(2, C, "Que número multiplicado por 8 dá 72?", 9, "8 × 9 = 72.", ["72 ÷ 8 = 9."]))
ex.append(num(3, C, "Uma caixa tem 6 garrafas e uma carrinha leva 9 caixas. Quantas garrafas leva a carrinha?", 54, "6 × 9 = 54.", ["6 × 9."]))
ex.append(tf(2, C, "7 × 8 = 54.", False, "7 × 8 = 56.", ["7 × 8 = 56."]))
ex.append(mc(2, C, "Qual das contas tem resultado 56?", ["7 × 8", "6 × 9", "8 × 6", "9 × 7"], 0, "7 × 8 = 56; 6 × 9 = 54; 8 × 6 = 48; 9 × 7 = 63.", ["Verifica cada uma."]))
A = lesson('tabuada', 'Tabuadas do 1 ao 12', 'tabuadas-1-a-12', 'Tabuadas do 6 ao 9', 'tabuadas-6-ao-9',
 'Domina as tabuadas do 6, 7, 8 e 9 com truques para os produtos mais difíceis.', 20,
 "**Objetivos:** dominar as tabuadas do 6 ao 9 usando padrões e relações com tabuadas já conhecidas. **Pré-requisitos:** tabuadas do 1 ao 5.\n\nAs tabuadas mais temidas são a do 6, do 7, do 8 e a do 9. A boa notícia: pela propriedade comutativa, já conheces $6\\times1$ até $6\\times5$, $7\\times1$ até $7\\times5$, etc. Sobram poucos produtos novos, e há truques para eles.",
 "**Tabuada do 6:** 5 vezes + mais 1 vez. $6\\times7=5\\times7+7=35+7=42$. **Tabuada do 7:** usa $7\\times7=49$ como âncora; $7\\times8=49+7=56$; $7\\times6=42$. **Tabuada do 8:** o dobro da do 4; $8\\times6=2\\times24=48$. **Tabuada do 9:** $9\\times n=10\\times n-n$; $9\\times7=70-7=63$; os algarismos do resultado somam sempre 9 (63 → 6+3=9); com os dedos: dobras o dedo $n$ e lês dezenas à esquerda, unidades à direita.\n\nProdutos que se confundem: $7\\times8=56$ (sequência 5, 6, 7, 8!) e $6\\times9=54$. Uma boa regra: $56=7\\times8$ lembra 5, 6, 7, 8.\n\nPadrão cruzado: os produtos «próximos» ($7\\times7=49$ e $6\\times8=48$) diferem de 1: $n\\times n$ e $(n-1)(n+1)$ diferem sempre de 1.\n\n**Erros comuns:** confundir 54 com 56; esquecer de usar a comutativa; decorar sem treinar em ordem aleatória.",
 "As tabuadas do 6, 7, 8 e 9 são os produtos $n\\times m$ com $n\\in\\{6,7,8,9\\}$ e $m\\in\\{1,\\ldots,12\\}$. Os **quadrados** da tabuada ($n\\times n$) são 36, 49, 64 e 81 para estes valores.",
 "$$9\\times n=10n-n\\qquad6\\times n=5n+n\\qquad8\\times n=2\\times(4\\times n)$$\n\nQuadrados: $6^2=36,\\ 7^2=49,\\ 8^2=64,\\ 9^2=81$.\n\n$(n-1)(n+1)=n^2-1$: por exemplo $6\\times8=7^2-1=48$.",
 "**Exemplo 1.** $6\\times7=5\\times7+7=42$.\n\n**Exemplo 2.** $7\\times8=56$ (lembra 5, 6, 7, 8).\n\n**Exemplo 3.** $8\\times9=72$, porque $9\\times8=80-8$.\n\n**Exemplo 4.** $9\\times6=60-6=54$; e $5+4=9$.\n\n**Exemplo 5.** $6\\times8=7^2-1=48$.\n\n**Aplicação.** Uma carrinha leva 9 caixas de 6 garrafas: $9\\times6=54$ garrafas.",
 "Resolve connosco: **calcula $8\\times7$ de duas maneiras.**\n\n1) Dobro do dobro: $2\\times7=14$, $4\\times7=28$, $8\\times7=56$.\n\n2) Com a âncora $7\\times7=49$: $49+7=56$.\n\n3) As duas dão 56 ✓.",
 "**Desafio.** Constrói a tabuada do 9 só com os dedos: dobra o dedo $n$ e conta os dedos à esquerda (dezenas) e à direita (unidades). Explica porque funciona usando $9\\times n=10n-n$.",
 "Consideras a competência dominada quando consegues: (1) responder às tabuadas do 6 ao 9 sem demora; (2) usar âncoras e truques; (3) reconhecer os quadrados da tabuada; (4) não confundir produtos parecidos.", ex)
write(1, 23, A)

# ===== 24. Tabuadas 10, 11, 12, padrões, divisão relacionada e problemas =====
C = 'tabuada.10_a_12'; ex = []
for t, n in [(10, 17), (11, 7), (11, 12), (12, 5), (12, 9), (12, 12), (11, 11), (12, 7)]:
    ex.append(num(1 if t * n < 80 else 2, C, f"Quanto é {t} × {n}?", t * n, f"{t} × {n} = {t*n}.", [f"{t} × {n} = {t*n}."]))
for D, d in [(132, 12), (121, 11), (96, 12), (770, 10)]:
    ex.append(num(2, C, f"Quanto é {D} ÷ {d}?", D // d, f"{d} × {D//d} = {D}.", ["Usa a tabuada ao contrário."]))
ex.append(num(3, C, "Um ano tem 12 meses. Quantos meses há em 15 anos?", 180, "12 × 15 = 180 meses.", ["12 × 15 = 120 + 60."]))
ex.append(num(3, C, "Uma dúzia tem 12 ovos. Quantos ovos há em 11 dúzias?", 132, "12 × 11 = 132.", ["120 + 12."]))
ex.append(tf(2, C, "Na tabuada do 11, 11 × 5 = 55 e 11 × 9 = 99.", True, "Até 9 o resultado repete o algarismo.", ["Repete o algarismo."]))
ex.append(mc(2, C, "Qual é a divisão relacionada com 12 × 7 = 84?", ["84 ÷ 12 = 7", "84 ÷ 7 = 11", "12 ÷ 7 = 84", "84 − 12 = 7"], 0, "Se a × b = c então c ÷ a = b.", ["Divisão inversa."]))
A = lesson('tabuada', 'Tabuadas do 1 ao 12', 'tabuadas-1-a-12', 'Tabuadas do 10, 11 e 12, divisão e desafios cronometrados',
 'tabuadas-10-11-12-divisao-desafios', 'Completa a tabuada até 12, relaciona-a com a divisão e treina com desafios cronometrados e problemas.', 25,
 "**Objetivos:** dominar as tabuadas do 10, 11 e 12, relacionar multiplicação e divisão, e treinar velocidade e memorização. **Pré-requisitos:** tabuadas do 1 ao 9.\n\nOs números 10, 11 e 12 aparecem em tudo: o 10 é a base do nosso sistema, o 12 dá-nos meses, dúzias e horas do relógio. Dominá-los completa a tabuada.",
 "**Tabuada do 10:** acrescenta um zero ($10\\times17=170$). **Tabuada do 11:** até $11\\times9$ repete o algarismo (11, 22, …, 99); para outros, $11\\times n=10n+n$ ($11\\times12=132$). **Tabuada do 12:** $12\\times n=10n+2n$ ($12\\times7=70+14=84$).\n\n**Divisão relacionada:** a divisão é a tabuada ao contrário. Se $12\\times11=132$, então $132\\div12=11$ e $132\\div11=12$. Cada produto dá duas divisões.\n\n**Padrões:** os múltiplos de 5 acabam em 0 ou 5; os pares alternam com ímpares; na tabuada do 9 os algarismos somam 9; na do 11 até 9 o resultado é capicua.\n\n**Treino cronometrado:** escolhe uma tabuada, responde a 10 contas e mede o tempo. Tenta bater o teu recorde, e usa o Treino de tabuada nas Ferramentas, que guarda os teus resultados.\n\n**Erros comuns:** pôr 11 × 12 = 122; esquecer o zero em $10\\times n$; não ligar multiplicação e divisão.",
 "A **divisão relacionada** de $a\\times b=c$ são as duas divisões $c\\div a=b$ e $c\\div b=a$. Uma **dúzia** é um grupo de 12 unidades. Um **recorde pessoal** é o melhor resultado (mais certas, menor tempo) que obtiveste num treino.",
 "$$10n=n\\text{ com um zero}\\qquad11n=10n+n\\qquad12n=10n+2n$$\n\n$$a\\times b=c\\iff c\\div a=b\\iff c\\div b=a$$\n\nQuadrados: $10^2=100,\\ 11^2=121,\\ 12^2=144$.",
 "**Exemplo 1.** $10\\times17=170$.\n\n**Exemplo 2.** $11\\times7=77$ e $11\\times12=132$.\n\n**Exemplo 3.** $12\\times7=70+14=84$.\n\n**Exemplo 4 (divisão).** $132\\div12=11$, porque $12\\times11=132$.\n\n**Exemplo 5 (problema).** 15 anos têm $12\\times15=180$ meses.\n\n**Aplicação.** 11 dúzias de ovos têm $11\\times12=132$ ovos.",
 "Resolve connosco: **calcula $12\\times13$ de cabeça.**\n\n1) $12\\times10=120$.\n\n2) $12\\times3=36$.\n\n3) $120+36=156$.\n\n4) Prova: $156\\div12=13$ ✓.",
 "**Desafio cronometrado.** Em 60 s, quantas destas consegues? 12×12, 11×8, 7×12, 9×9, 6×11, 12×5, 8×12, 10×10, 11×11, 4×12. Anota o resultado e repete amanhã para bater o recorde.",
 "Consideras a competência dominada quando consegues: (1) tabuadas do 10, 11 e 12 sem demora; (2) encontrar as duas divisões de cada produto; (3) usar padrões e truques; (4) melhorar o recorde nos treinos.", ex)
write(1, 24, A)
print('O/T ok')

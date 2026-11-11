"""Nível 2 — Módulo 3: Razão e proporção (aulas novas 04–09)."""
from n2h import *
SUB = 'razao-e-proporcao'

# ---------- R1: razão ----------
C = 'razao.conceito'; ex = []
ex += [num(1, C, "Qual é o valor da razão de 15 para 25? Escreve a fração irredutível.", F(15,25), "15/25 = 3/5 (divide por 5).", ["mdc(15, 25) = 5.", "15 ÷ 5 = 3 e 25 ÷ 5 = 5."]),
       num(1, C, "Numa turma há 12 rapazes e 18 raparigas. Qual é a razão rapazes : raparigas, na forma irredutível?", F(12,18), "12/18 = 2/3.", ["mdc(12, 18) = 6.", "12 ÷ 6 = 2; 18 ÷ 6 = 3."]),
       num(1, C, "A razão $3:4$ escrita como número decimal é?", F(3,4), "3 ÷ 4 = 0,75.", ["Razão é uma divisão: 3 ÷ 4."], ["0,75"])]
ex += [num(2, C, "Qual é a razão entre 2,5 m e 50 cm? (Converte para a mesma unidade primeiro.)", F(250,50), "2,5 m = 250 cm; 250 ÷ 50 = 5.", ["Mesma unidade: 2,5 m = 250 cm.", "250 : 50 = 5."]),
       num(2, C, "Qual é a razão de $\\frac{3}{4}$ para $\\frac{1}{2}$?", F(3,4)/F(1,2), "(3/4) ÷ (1/2) = 3/4 × 2 = 3/2.", ["Razão é um quociente.", "Dividir por 1/2 é multiplicar por 2."]),
       num(2, C, "Num mercado, 3 kg de feijão custam 1 200 Kz. Qual é a razão Kz por kg (preço de 1 kg)?", F(1200,3), "1 200 ÷ 3 = 400 Kz/kg.", ["Razão preço : quantidade.", "1 200 ÷ 3 = 400."]),
       num(2, C, "Se $3:5 = x:20$ (razões equivalentes), quanto vale x?", F(3*20,5), "20 = 5 × 4, logo x = 3 × 4 = 12.", ["Fator entre 5 e 20: 4.", "3 × 4 = 12."])]
ex += [num(3, C, "Mistura de água e sumo na razão $3:2$. Numa jarra de 40 litros, quantos litros são de água?", F(3*40,5), "Partes: 3 + 2 = 5; cada parte = 40 ÷ 5 = 8 L; água = 3 × 8 = 24 L.", ["Total de partes: 5.", "1 parte = 8 L.", "Água: 3 partes = 24 L."]),
       num(3, C, "A razão entre as idades de pai e filho é $7:2$ e o pai tem 42 anos. Quantos anos tem o filho?", F(42*2,7), "42 ÷ 7 = 6 por parte; filho = 2 × 6 = 12 anos.", ["7 partes = 42 anos.", "1 parte = 6.", "Filho: 2 partes = 12."]),
       tf(2, C, "A razão entre 30 cm e 2 m é $15$.", False, "Têm unidades diferentes: 2 m = 200 cm, logo 30 : 200 = 3/20. Só se compara depois de converter.", ["Converte 2 m para cm."]),
       mc(3, C, "Qual das razões é equivalente a $4:6$?", ["$10:15$", "$6:8$", "$5:7$", "$8:10$"], 0, "4:6 = 2:3 e 10:15 = 2:3. As outras simplificam para 3:4, 5:7 e 4:5.", ["Simplifica todas."])]
ex_ok = ex
A = std(SUB, 'Razão', 'razao', 'Razão: termos, leitura, simplificação e razões equivalentes', 'razao-termos-simplificacao-equivalentes',
 'Compreende a razão entre duas grandezas, lê-a, simplifica-a e reconhece razões equivalentes.', 25,
 'definir razão, identificar antecedente e consequente, simplificar razões e reconhecer razões equivalentes.', 'frações, simplificação, mdc e conversão de unidades.',
 'Para comparar quantos rapazes há por cada rapariga numa turma, ou quanto custa cada quilo de feijão, não basta olhar para os números isolados: comparamos duas quantidades por **divisão**. É isso que se chama razão.',
 "A **razão** entre duas grandezas é o quociente entre as suas medidas, **na mesma unidade**. A razão de $a$ para $b$ escreve-se $a:b$ ou $\\frac{a}{b}$ e lê-se «$a$ para $b$». Em $a:b$, $a$ é o **antecedente** e $b$ é o **consequente** ($b\\ne0$).\n\n**Atenção à ordem:** $3:4$ não é o mesmo que $4:3$. A razão de rapazes para raparigas (12:18) é diferente da razão de raparigas para rapazes (18:12).\n\n**Mesma unidade:** para dividir 30 cm por 2 m, converte primeiro: 2 m = 200 cm, e a razão é $30:200=3:20$. Quando as unidades são diferentes por natureza (Kz e kg), a razão traz unidade: 1 200 Kz : 3 kg = 400 Kz/kg.\n\n**Simplificar uma razão** é dividir antecedente e consequente pelo mesmo número (o mdc): $15:25=3:5$. A razão fica **irredutível** quando mdc = 1. Duas razões são **equivalentes** se têm o mesmo valor: $3:5=12:20$ (multiplicámos os dois termos por 4). Se os termos são frações ou decimais, converte para números inteiros multiplicando pelo mesmo fator.\n\n**Divisão em partes:** repartir 40 L na razão $3:2$ significa 5 partes iguais, de 8 L cada: 24 L e 16 L.\n\n**Erros comuns:** trocar a ordem; comparar sem converter unidades; simplificar só o antecedente.",
 'Razão de $a$ para $b$ ($b\\ne0$): $\\dfrac{a}{b}$, com $a$ o antecedente e $b$ o consequente, medidos na mesma unidade. Razões **equivalentes**: $\\dfrac{a}{b}=\\dfrac{ka}{kb}$ ($k\\ne0$).',
 '$$\\text{razão}=\\frac{a}{b}\\qquad\\frac{a}{b}=\\frac{a\\div d}{b\\div d}\\qquad\\frac{a}{b}=\\frac{ka}{kb}$$\n\n$a$: antecedente; $b$: consequente ($b\\ne0$); $d$: divisor comum; $k$: fator de multiplicação ($k\\ne0$). Divisão em partes: se o total $T$ é repartido na razão $p:q$, cada parte vale $\\frac{T}{p+q}$.',
 ['Razão de 15 para 25: $15:25=\\frac{15}{25}=\\frac{3}{5}$ (dividimos por 5).',
  'Rapazes e raparigas: 12 e 18. Razão $12:18=2:3$. Por cada 2 rapazes há 3 raparigas.',
  '30 cm para 2 m: $2\\text{ m}=200\\text{ cm}$, então $30:200=3:20$.',
  'Preço por quilo: $1\\,200\\text{ Kz}:3\\text{ kg}=400$ Kz/kg.',
  'Equivalência: $3:5=x:20$. Como $20=5\\times4$, $x=3\\times4=12$.',
  'Repartição: 40 L na razão $3:2$: $40\\div5=8$ L por parte; $3\\times8=24$ L e $2\\times8=16$ L.'],
 "Resolve connosco: **num talho, 4,5 kg de carne custam 9 000 Kz. Qual é a razão preço : quantidade? E quanto custam 7 kg?**\n\n1) Razão: $9\\,000:4{,}5=2\\,000$ Kz por kg.\n\n2) Para 7 kg: $7\\times2\\,000=14\\,000$ Kz.\n\n3) Verifica: $14\\,000:7=2\\,000$ ✓.",
 '**Desafio.** Uma tinta é feita misturando pigmento e base na razão $2:7$. Para 18 litros de tinta, quantos litros de pigmento são precisos? E se só tens 3 litros de pigmento, quantos litros de tinta consegues fazer?',
 ['escrever uma razão pela ordem certa', 'converter unidades antes de dividir', 'simplificar até à forma irredutível', 'reconhecer razões equivalentes', 'repartir um total numa razão dada'], ex_ok)
write(2, 4, A)

# ---------- R2: proporção ----------
C = 'razao.proporcao'; ex = []
for a, b, c in [(3, 4, 12), (5, 2, 10), (7, 3, 21)]:
    x = F(b*c, a)
    ex.append(num(1, C, f"Calcula x na proporção $\\frac{{{a}}}{{{b}}}=\\frac{{x}}{{{c}}}$.", x, f"Produto dos meios = produto dos extremos: {a}x = {b}×{c}, logo x = {T(x)}.", [f"{a}·{c}... usa a propriedade fundamental: {a} × {c} = {b} × x? Atenção à posição de x.", f"x = {T(x)}."]) if False else
        num(1, C, f"Calcula x na proporção $\\frac{{x}}{{{b}}}=\\frac{{{a}}}{{{c}}}$.", F(a*b, c), f"Produto cruzado: {c}·x = {a}·{b}, logo x = {T(F(a*b,c))}.", ["Multiplica em cruz.", f"x = {a*b} ÷ {c}."]))
ex += [num(2, C, "Calcula x em $\\frac{4}{x}=\\frac{6}{15}$.", F(4*15,6), "6x = 4 × 15 = 60, logo x = 10.", ["Produto cruzado: 6x = 60.", "x = 10."]),
       num(2, C, "Calcula x em $\\frac{x+2}{5}=\\frac{9}{15}$.", F(9*5,15)-2, "15(x+2) = 45, logo x+2 = 3 e x = 1.", ["Produto cruzado.", "x + 2 = 3."]),
       num(2, C, "Os números 6, 9, 10 e $x$ formam, por esta ordem, uma proporção $\\frac{6}{9}=\\frac{10}{x}$. Qual é x?", F(9*10,6), "6x = 90, logo x = 15.", ["Produto dos extremos e dos meios.", "x = 15."]),
       num(2, C, "Num mapa, 3 cm representam 12 km. Quantos km representam 5 cm?", F(12*5,3), "A razão cm : km é constante: 3/12 = 5/x, logo 3x = 60 e x = 20 km.", ["Proporção cm/km.", "x = 20."]),
       num(3, C, "A média proporcional $m$ entre 4 e 25 satisfaz $\\frac{4}{m}=\\frac{m}{25}$ ($m>0$). Quanto vale m?", 10, "m² = 4 × 25 = 100 e m = 10.", ["Produto cruzado: m² = 100."]),
       num(3, C, "Os preços de dois produtos estão na proporção 3 : 5. Se o mais barato custa 1 800 Kz, quanto custa o outro, em Kz?", F(1800*5,3), "3/5 = 1800/x → x = 1800 × 5 ÷ 3 = 3 000 Kz.", ["Proporção 3/5 = 1800/x.", "x = 3 000."]),
       tf(1, C, "A igualdade $\\frac{2}{3}=\\frac{8}{12}$ é uma proporção.", True, "2 × 12 = 24 e 3 × 8 = 24: produtos cruzados iguais.", ["Multiplica em cruz."]),
       tf(2, C, "Se $\\frac{a}{b}=\\frac{c}{d}$, então $a\\times b=c\\times d$.", False, "A propriedade fundamental diz $a\\times d=b\\times c$ (extremos × meios), não $a\\times b$.", ["Extremos: a e d. Meios: b e c."]),
       mc(3, C, "Qual dos pares forma uma proporção com $\\frac{6}{8}$?", ["$\\frac{9}{12}$", "$\\frac{8}{10}$", "$\\frac{7}{9}$", "$\\frac{12}{18}$"], 0, "6×12 = 72 = 8×9; as outras falham o produto cruzado.", ["Testa o produto cruzado em cada uma."])]
A = std(SUB, 'Proporção', 'proporcao', 'Proporção: extremos, meios e propriedade fundamental', 'proporcao-propriedade-fundamental',
 'Reconhece uma proporção e usa a propriedade fundamental para calcular o termo desconhecido.', 25,
 'definir proporção, identificar extremos e meios, aplicar a propriedade fundamental e calcular termos desconhecidos.', 'razão, frações equivalentes e equações simples.',
 'No mercado, se 3 kg de arroz custam 2 400 Kz, quanto custam 5 kg? A resposta nasce de uma igualdade entre duas razões: uma **proporção**.',
 "Uma **proporção** é a igualdade de duas razões: $\\frac{a}{b}=\\frac{c}{d}$, que se lê «$a$ está para $b$ assim como $c$ está para $d$» e se escreve também $a:b=c:d$ (com $b,d\\ne0$).\n\nOs quatro termos têm nomes: $a$ e $d$ são os **extremos**; $b$ e $c$ são os **meios**. Em cada razão, o primeiro termo é o **antecedente** ($a$ e $c$) e o segundo o **consequente** ($b$ e $d$).\n\n**Propriedade fundamental:** numa proporção, o produto dos extremos é igual ao produto dos meios: $a\\times d=b\\times c$. É a famosa «multiplicação em cruz».\n\n**Para que serve:** se três termos são conhecidos, calculamos o quarto. De $\\frac{3}{4}=\\frac{x}{12}$ tiramos $3\\times12=4x$, logo $x=9$. Para verificar se quatro números formam uma proporção, testamos se os produtos cruzados são iguais.\n\n**Cuidado:** só funciona quando temos **uma igualdade entre duas razões**. Se $x$ está no meio ou no extremo, a regra é a mesma, mas atenção a quem multiplica quem.\n\n**Média proporcional:** em $\\frac{a}{m}=\\frac{m}{b}$ o número $m$ aparece duas vezes e $m^2=a\\times b$.\n\n**Erros comuns:** multiplicar $a\\times b$ em vez de $a\\times d$; esquecer de dividir pelo número que acompanha o $x$.",
 'Proporção: $\\frac{a}{b}=\\frac{c}{d}$ ($b,d\\ne0$). Extremos: $a$, $d$. Meios: $b$, $c$.',
 '$$\\frac{a}{b}=\\frac{c}{d}\\iff a\\times d=b\\times c\\qquad\\text{se }\\frac{a}{b}=\\frac{c}{x}\\text{ então }x=\\frac{b\\times c}{a}$$\n\nMédia proporcional $m$ entre $a$ e $b$ (positivos): $m=\\sqrt{a\\times b}$.',
 ['$\\frac{2}{3}=\\frac{8}{12}$ é proporção: $2\\times12=24=3\\times8$.',
  '$\\frac{3}{4}=\\frac{x}{12}$: $3\\times12=4x$, $x=36\\div4=9$.',
  '$\\frac{4}{x}=\\frac{6}{15}$: $6x=60$, $x=10$.',
  '$\\frac{x+2}{5}=\\frac{9}{15}$: $15(x+2)=45$, $x+2=3$, $x=1$.',
  'Média proporcional entre 4 e 25: $m^2=100$, $m=10$.',
  'Mapa: 3 cm ↔ 12 km; 5 cm ↔ $x$: $\\frac{3}{12}=\\frac{5}{x}$, $x=20$ km.'],
 "Resolve connosco: **3 kg de arroz custam 2 400 Kz. Quanto custam 5 kg?**\n\n1) Proporção: $\\frac{3}{2\\,400}=\\frac{5}{x}$.\n\n2) Produto cruzado: $3x=5\\times2\\,400=12\\,000$.\n\n3) $x=4\\,000$ Kz.\n\n4) Verifica: 1 kg custa 800 Kz; $5\\times800=4\\,000$ ✓.",
 '**Desafio.** Mostra que se $\\frac{a}{b}=\\frac{c}{d}$ então também $\\frac{a}{c}=\\frac{b}{d}$ (troca dos meios). Testa com $\\frac{3}{4}=\\frac{9}{12}$ e explica porquê.',
 ['reconhecer uma proporção pelos produtos cruzados', 'nomear extremos e meios', 'aplicar a propriedade fundamental', 'calcular o termo desconhecido', 'usar proporções em problemas de preços e mapas'], ex)
write(2, 5, A)

# ---------- R3: propriedades das proporções ----------
C = 'razao.propriedades'; ex = []
ex += [num(1, C, "Se $\\frac{a}{b}=\\frac{3}{4}$, qual é o valor de $\\frac{a+b}{b}$?", F(7,4), "(a+b)/b = a/b + 1 = 3/4 + 1 = 7/4.", ["Soma o consequente ao antecedente.", "3 + 4 = 7."]),
       num(1, C, "Se $\\frac{a}{b}=\\frac{2}{5}$, qual é o valor de $\\frac{b-a}{b}$?", F(3,5), "(b−a)/b = 1 − a/b = 1 − 2/5 = 3/5.", ["1 − 2/5."]),
       num(1, C, "Troca dos meios: se $\\frac{3}{4}=\\frac{9}{12}$, então $\\frac{3}{9}=\\frac{4}{x}$. Quanto vale x?", 12, "Troca dos meios mantém a proporção: 3/9 = 4/12.", ["3/9 = 1/3 e 4/12 = 1/3."])]
ex += [num(2, C, "Se $\\frac{a}{b}=\\frac{c}{d}=\\frac{2}{3}$, quanto vale $\\frac{a+c}{b+d}$?", F(2,3), "Em razões iguais, (a+c)/(b+d) = a/b = 2/3.", ["Soma antecedentes e consequentes."]),
       num(2, C, "Dois números estão na razão $3:4$ e a sua soma é 84. Qual é o maior?", F(84*4,7), "Partes 3+4 = 7; 84 ÷ 7 = 12; o maior é 4 × 12 = 48.", ["Soma dos termos: 7.", "12 por parte."]),
       num(2, C, "Dois números estão na razão $5:2$ e a diferença é 36. Qual é o maior?", F(36*5,3), "Diferença de partes 5−2 = 3; 36 ÷ 3 = 12; maior = 5 × 12 = 60.", ["3 partes = 36.", "Maior: 5 partes."]),
       num(2, C, "Reparte 1 200 Kz em partes proporcionais a 1, 2 e 3. Quanto recebe a maior parte?", F(1200*3,6), "Soma 1+2+3 = 6; 1 200 ÷ 6 = 200; maior = 3 × 200 = 600 Kz.", ["6 partes.", "200 Kz por parte."])]
ex += [num(3, C, "Três sócios investem 2, 3 e 5 milhares de Kz e dividem um lucro de 150 000 Kz proporcionalmente ao investimento. Quanto recebe o sócio que investiu 3?", F(150000*3,10), "Soma 2+3+5 = 10; 150 000 ÷ 10 = 15 000; 3 × 15 000 = 45 000 Kz.", ["10 partes.", "15 000 por parte."]),
       num(3, C, "Se $\\frac{x}{y}=\\frac{5}{3}$ e $x+y=64$, quanto vale $x$?", F(64*5,8), "x+y partes = 8; 64 ÷ 8 = 8; x = 5 × 8 = 40.", ["Propriedade da soma.", "x = 40."]),
       tf(2, C, "Se $\\frac{a}{b}=\\frac{c}{d}$, então $\\frac{a+c}{b+d}=\\frac{a}{b}$.", True, "É a propriedade de razões iguais: somar antecedentes e consequentes mantém a razão (com $b+d\\neq0$).", ["Testa com 1/2 = 3/6: 4/8 = 1/2."]),
       mc(3, C, "De $\\frac{a}{b}=\\frac{c}{d}$ não se pode concluir que:", ["$\\frac{a+c}{b+d}=\\frac{a}{b}$", "$\\frac{a+b}{b}=\\frac{c+d}{d}$", "$\\frac{a}{c}=\\frac{b}{d}$", "$a+d=b+c$"], 3, "A propriedade fundamental envolve produtos (ad = bc), não somas. Por exemplo, 1/2 = 2/4 mas 1+4 ≠ 2+2.", ["Testa com 1/2 = 2/4."])]
A = std(SUB, 'Proporção', 'proporcao', 'Propriedades das proporções e divisão proporcional', 'propriedades-das-proporcoes-divisao-proporcional',
 'Aplica as propriedades da soma, da diferença e das razões iguais e reparte quantidades proporcionalmente.', 30,
 'aplicar as propriedades das proporções e fazer divisões proporcionais.', 'razão, proporção e propriedade fundamental.',
 'Dois sócios investem valores diferentes num negócio. Como dividir o lucro de forma justa? As propriedades das proporções respondem a esta pergunta.',
 "Seja $\\frac{a}{b}=\\frac{c}{d}$. Então valem:\n\n**1) Troca dos meios (ou dos extremos):** $\\frac{a}{c}=\\frac{b}{d}$ (com $c,d\\ne0$).\n\n**2) Propriedade da soma:** $\\frac{a+b}{b}=\\frac{c+d}{d}$. Somamos 1 aos dois lados da igualdade.\n\n**3) Propriedade da diferença:** $\\frac{a-b}{b}=\\frac{c-d}{d}$.\n\n**4) Razões iguais:** $\\frac{a+c}{b+d}=\\frac{a}{b}=\\frac{c}{d}$ (com $b+d\\neq0$). Em geral, numa série de razões iguais, a soma dos antecedentes sobre a soma dos consequentes dá a mesma razão.\n\n**Quando usar:** sempre que sabes a **soma** (ou a **diferença**) de dois termos e a razão entre eles. Exemplo: dois números na razão $3:4$ com soma 84. Cada «parte» vale $84\\div7=12$; os números são 36 e 48.\n\n**Divisão proporcional:** repartir um total $T$ em partes proporcionais a $p,q,r$ dá partes $\\frac{T}{p+q+r}\\times p$, etc. Se um sócio investe $2$, outro $3$ e outro $5$ e o lucro é 150 000 Kz, cada parte vale $150\\,000\\div10=15\\,000$ Kz.\n\n**Cuidado:** a soma nunca se aplica à propriedade fundamental. De $\\frac{1}{2}=\\frac{2}{4}$ não se conclui $1+4=2+2$.\n\n**Erros comuns:** usar a soma dos termos quando o enunciado dá a diferença; esquecer de dividir pelo total de partes.",
 'Em $\\frac{a}{b}=\\frac{c}{d}$ ($b,d\\neq0$) valem a troca dos meios, a propriedade da soma, da diferença e a das razões iguais.',
 '$$\\frac{a}{c}=\\frac{b}{d}\\qquad\\frac{a+b}{b}=\\frac{c+d}{d}\\qquad\\frac{a-b}{b}=\\frac{c-d}{d}\\qquad\\frac{a+c}{b+d}=\\frac{a}{b}$$\n\nDivisão proporcional a $p,q,r$ de um total $T$: parte $=\\dfrac{T}{p+q+r}\\times p$ (e analogamente para $q$ e $r$).',
 ['$\\frac{a}{b}=\\frac{3}{4}$: $\\frac{a+b}{b}=\\frac{3}{4}+1=\\frac{7}{4}$.',
  'Dois números na razão $3:4$ com soma 84: partes $=84\\div7=12$; números $=36$ e $48$.',
  'Dois números na razão $5:2$ com diferença 36: $36\\div3=12$; números $=60$ e $24$.',
  'Razões iguais: $\\frac{2}{3}=\\frac{4}{6}$, logo $\\frac{2+4}{3+6}=\\frac{6}{9}=\\frac{2}{3}$.',
  'Repartir 1 200 Kz em partes proporcionais a 1, 2 e 3: $1\\,200\\div6=200$; partes 200, 400 e 600 Kz.',
  'Lucro de 150 000 Kz com investimentos 2, 3 e 5: $150\\,000\\div10=15\\,000$; recebem 30 000, 45 000 e 75 000 Kz.'],
 "Resolve connosco: **dois irmãos repartem 18 000 Kz na razão $4:5$. Quanto recebe cada um?**\n\n1) Total de partes: $4+5=9$.\n\n2) Cada parte: $18\\,000\\div9=2\\,000$ Kz.\n\n3) Um recebe $4\\times2\\,000=8\\,000$ Kz; o outro $5\\times2\\,000=10\\,000$ Kz.\n\n4) Verifica: $8\\,000+10\\,000=18\\,000$ ✓.",
 '**Desafio.** Três amigos compram um bilhete de lotaria com contribuições de 500, 700 e 800 Kz. Ganham 60 000 Kz. Quanto recebe cada um se a divisão é proporcional à contribuição? Verifica que a soma dá 60 000.',
 ['usar a propriedade da soma e da diferença', 'aplicar razões iguais', 'resolver problemas de soma ou diferença conhecida', 'fazer divisões proporcionais', 'reconhecer o que NÃO se pode concluir de uma proporção'], ex)
write(2, 6, A)

# ---------- R4: grandezas direta e inversamente proporcionais ----------
C = 'razao.grandezas'; ex = []
ex += [num(1, C, "Um carro gasta 6 litros por 100 km. Quantos litros gasta em 250 km (grandezas diretamente proporcionais)?", F(6*250,100), "6/100 = x/250 → x = 15 L.", ["A distância e o consumo aumentam juntos.", "x = 15."]),
       num(1, C, "Se 4 cadernos custam 1 000 Kz, qual é a constante de proporcionalidade (preço de 1 caderno), em Kz?", F(1000,4), "k = 1 000 ÷ 4 = 250 Kz.", ["k = y ÷ x."]),
       tf(1, C, "Quando o número de pedreiros aumenta, o tempo para acabar a obra diminui: as grandezas são inversamente proporcionais.", True, "Mais pessoas, menos tempo: o produto (pessoas × dias) fica constante.", ["Se um aumenta, o outro diminui."])]
ex += [num(2, C, "Duas grandezas inversamente proporcionais: quando $x=4$, $y=15$. Qual é o produto constante $k$?", 60, "k = x·y = 4 × 15 = 60.", ["Inversa: x·y constante."]),
       num(2, C, "Com a constante $xy=60$, se $x=12$, quanto vale $y$?", 5, "y = 60 ÷ 12 = 5.", ["y = k/x."]),
       num(2, C, "6 operários fazem um muro em 10 dias. Em quantos dias 12 operários fazem o mesmo muro (mesmo ritmo)?", F(6*10,12), "Inversa: 6 × 10 = 12 × d → d = 5 dias.", ["Produto constante: 60.", "d = 60 ÷ 12."]),
       num(2, C, "Uma torneira enche um tanque a 15 L/min. Quantos litros enche em 8 minutos (direta)?", 15*8, "15 × 8 = 120 L.", ["Constante k = 15 L/min."])]
ex += [num(3, C, "Um autocarro viaja a 60 km/h e demora 3 horas. Se viajar a 90 km/h, quantas horas demora a mesma distância?", F(60*3,90), "Velocidade e tempo são inversamente proporcionais: 60 × 3 = 180 = 90 × t → t = 2 h.", ["Distância constante: 180 km.", "t = 180 ÷ 90."]),
       num(3, C, "Se $y$ é diretamente proporcional a $x$ e $y=21$ quando $x=7$, quanto vale $y$ quando $x=12$?", F(21*12,7), "k = 21/7 = 3; y = 3 × 12 = 36.", ["k = 3.", "y = 36."]),
       tf(3, C, "A idade de uma pessoa e a sua altura são grandezas diretamente proporcionais.", False, "Embora aumentem juntas até certa idade, a razão altura/idade não é constante. Proporcionalidade exige razão constante.", ["Uma criança de 2 anos não tem metade da altura de uma de 4."]),
       mc(2, C, "Qual das situações envolve grandezas inversamente proporcionais?", ["Velocidade e tempo para percorrer uma distância fixa", "Quantidade de arroz e preço a pagar", "Litros de combustível e distância percorrida", "Número de bilhetes e total pago"], 0, "Se a velocidade aumenta, o tempo diminui na mesma proporção, com a distância fixa. As outras são diretas.", ["Qual aumenta enquanto o outro diminui?"])]
A = std(SUB, 'Grandezas proporcionais', 'grandezas-proporcionais', 'Grandezas diretamente e inversamente proporcionais', 'grandezas-direta-inversamente-proporcionais',
 'Distingue proporcionalidade direta de inversa, calcula a constante e resolve problemas.', 30,
 'reconhecer grandezas diretamente e inversamente proporcionais, determinar a constante de proporcionalidade e resolver problemas.', 'razão, proporção e propriedade fundamental.',
 'Se compras mais pão, pagas mais. Se há mais pedreiros na obra, acabam mais cedo. Nos dois casos há uma relação entre grandezas, mas de tipo diferente.',
 "Duas grandezas são **diretamente proporcionais** quando a razão entre os valores correspondentes é constante: $\\frac{y}{x}=k$ ($k$ é a **constante de proporcionalidade**). Se $x$ duplica, $y$ duplica; se $x$ triplica, $y$ triplica. Exemplo: o preço $y$ de $x$ cadernos a 250 Kz cada: $y=250x$.\n\nDuas grandezas são **inversamente proporcionais** quando o **produto** dos valores correspondentes é constante: $x\\times y=k$. Se $x$ duplica, $y$ fica metade. Exemplo: com uma obra de 60 «pessoas-dia», o número de pessoas $x$ e os dias $y$ satisfazem $xy=60$.\n\n**Como decidir:** pergunta «se uma grandeza aumenta, a outra aumenta ou diminui?». Aumentar com aumentar (e na mesma proporção) é direta; aumentar com diminuir é inversa. Mas atenção: nem todas as grandezas que crescem juntas são proporcionais. A altura de uma pessoa cresce com a idade, mas a razão não é constante.\n\n**Uso:** encontra a constante $k$ com um par de valores e usa-a para os outros. Direta: $y=kx$. Inversa: $y=\\frac{k}{x}$.\n\n**Gráficos:** a proporcionalidade direta dá uma reta que passa pela origem. A inversa dá uma curva (hipérbole).\n\n**Erros comuns:** tratar tudo como direto; usar razão quando devia usar produto; esquecer unidades.",
 '**Diretamente proporcionais:** $\\frac{y}{x}=k$ constante, $y=kx$. **Inversamente proporcionais:** $xy=k$ constante, $y=\\frac{k}{x}$ ($x\\ne0$).',
 '$$\\text{direta: }\\ \\frac{y_1}{x_1}=\\frac{y_2}{x_2}=k\\qquad\\text{inversa: }\\ x_1y_1=x_2y_2=k$$\n\n$k$ é a constante de proporcionalidade (com unidade, quando existe: Kz/kg, L/min, pessoas·dias…).',
 ['Direta: 4 cadernos custam 1 000 Kz; $k=1\\,000\\div4=250$ Kz/caderno; 9 cadernos custam $9\\times250=2\\,250$ Kz.',
  'Direta: um carro gasta 6 L por 100 km; em 250 km: $\\frac{6}{100}=\\frac{x}{250}$, $x=15$ L.',
  'Inversa: 6 operários fazem um muro em 10 dias; $6\\times10=60$; com 12 operários: $12\\,d=60$, $d=5$ dias.',
  'Inversa: 60 km/h durante 3 h dá 180 km; a 90 km/h: $t=180\\div90=2$ h.',
  'Direta com $k$: $y=21$ para $x=7$; $k=3$; para $x=12$, $y=36$.',
  'Contraexemplo: altura e idade crescem juntas, mas altura/idade muda: não são proporcionais.'],
 "Resolve connosco: **8 pedreiros acabam uma parede em 9 dias. Quantos pedreiros são precisos para a acabar em 6 dias?**\n\n1) Mais pessoas, menos dias: inversa.\n\n2) Constante: $8\\times9=72$ pessoas-dia.\n\n3) $x\\times6=72$, logo $x=12$ pedreiros.\n\n4) Verifica: $12\\times6=72$ ✓.",
 '**Desafio.** Uma torneira enche um depósito em 12 minutos. Se abrires duas torneiras iguais, quanto tempo demora? E três? Escreve o que se passa com o produto «torneiras × minutos».',
 ['distinguir direta de inversa', 'calcular a constante k', 'usar y = kx e y = k/x', 'resolver problemas de preços, consumos e tempos', 'reconhecer quando NÃO há proporcionalidade'], ex)
write(2, 7, A)

# ---------- R5: escalas ----------
C = 'razao.escalas'; ex = []
ex += [num(1, C, "Num mapa de escala $1:50\\,000$, 4 cm no mapa correspondem a quantos cm na realidade?", 4*50000, "4 × 50 000 = 200 000 cm.", ["Multiplica pela escala."]),
       num(1, C, "200 000 cm quantos km são? (1 km = 100 000 cm)", 2, "200 000 ÷ 100 000 = 2 km.", ["Divide por 100 000."]),
       num(1, C, "A escala de um mapa é $1:1\\,000$. Uma rua tem 150 m reais. Quantos cm tem no mapa?", F(150*100,1000), "150 m = 15 000 cm; 15 000 ÷ 1 000 = 15 cm.", ["Converte para cm.", "Divide pela escala."])]
ex += [num(2, C, "Duas cidades distam 60 km. Num mapa de escala $1:1\\,000\\,000$, quantos cm separam as duas cidades no mapa?", F(60*100000,1000000), "60 km = 6 000 000 cm; ÷ 1 000 000 = 6 cm.", ["1 km = 100 000 cm.", "6 000 000 ÷ 1 000 000."]),
       num(2, C, "No mapa, 5 cm representam 25 km. Qual é o denominador da escala $1:n$ (em cm)?", F(25*100000,5), "25 km = 2 500 000 cm; ÷ 5 = 500 000. Escala 1 : 500 000.", ["Converte 25 km para cm.", "Divide pelos 5 cm."]),
       num(2, C, "Numa planta de escala $1:50$, uma sala mede 8 cm × 6 cm. Qual é a área real da sala, em m²?", F(8*50,100)*F(6*50,100), "Real: 4 m × 3 m = 12 m².", ["8 × 50 = 400 cm = 4 m.", "6 × 50 = 300 cm = 3 m."]),
       num(2, C, "Uma maquete é feita à escala $1:20$. Se o prédio real tem 18 m de altura, que altura tem a maquete, em cm?", F(1800,20), "18 m = 1 800 cm; ÷ 20 = 90 cm.", ["Divide pela escala."])]
ex += [num(3, C, "Dois mapas do mesmo percurso têm escalas $1:200\\,000$ e $1:500\\,000$. Se no primeiro o percurso mede 25 cm, quanto mede no segundo, em cm?", F(25*200000,500000), "Real: 25 × 200 000 = 5 000 000 cm; no 2.º: ÷ 500 000 = 10 cm.", ["Real = 5 000 000 cm.", "10 cm."]),
       num(3, C, "Numa planta de escala $1:100$, a área de um terreno desenhado é 24 cm². Qual é a área real, em m²?", F(24*100*100,10000), "As áreas multiplicam pelo quadrado da escala: 24 × 10 000 = 240 000 cm² = 24 m².", ["Área real em cm²: 24 × 100².", "1 m² = 10 000 cm²."]),
       tf(2, C, "Uma escala $1:25\\,000$ é maior (mostra mais pormenor) do que uma escala $1:250\\,000$.", True, "Quanto menor o denominador, maior a escala e maior o pormenor.", ["1/25 000 > 1/250 000."]),
       mc(3, C, "Uma escala $1:50$ significa que:", ["1 cm no desenho representa 50 cm na realidade", "50 cm no desenho representam 1 cm na realidade", "1 cm no desenho representa 50 m na realidade", "O desenho é 50% da realidade"], 0, "Escala = medida no desenho : medida real. 1 : 50 → 1 cm representa 50 cm.", ["Lê primeiro o desenho."])]
A = std(SUB, 'Escalas', 'escalas', 'Escalas em mapas, plantas e maquetes', 'escalas-mapas-plantas-maquetes',
 'Interpreta e usa escalas para passar do desenho para a realidade e vice-versa.', 25,
 'interpretar escalas, calcular distâncias reais e no desenho, e comparar escalas.', 'razão, proporção e conversão de unidades de comprimento.',
 'Num mapa de Angola, uma distância de poucos centímetros representa centenas de quilómetros. A escala diz-nos exatamente quantas vezes a realidade foi reduzida.',
 "A **escala** é a razão entre uma medida no desenho e a **medida correspondente** na realidade, **na mesma unidade**:\n\n$$\\text{escala}=\\frac{\\text{medida no desenho}}{\\text{medida real}}$$\n\nEscreve-se $1:n$. Em $1:50\\,000$, 1 cm no mapa representa 50 000 cm = 500 m na realidade.\n\n**Escala de redução** ($1:n$ com $n>1$) é usada em mapas e plantas; **escala de ampliação** ($n:1$) em objetos minúsculos (por exemplo, $5:1$ para uma formiga). **Escala natural:** $1:1$.\n\n**Escala maior ou menor:** compara os valores. $\\frac{1}{25\\,000}>\\frac{1}{250\\,000}$: a escala $1:25\\,000$ é **maior** e mostra mais pormenor.\n\n**Distâncias:** dividir a medida real pela escala dá a medida no desenho; multiplicar a medida do desenho pela escala dá a real. Converte sempre para a **mesma unidade** antes e depois (1 km = 100 000 cm; 1 m = 100 cm).\n\n**Áreas:** a escala é linear. Se o comprimento aumenta $n$ vezes, a **área aumenta $n^2$ vezes**. Numa planta $1:100$, 24 cm² representam $24\\times100^2=240\\,000$ cm² = 24 m².\n\n**Escala gráfica:** uma barra graduada desenhada no mapa mostra distâncias reais e continua certa se o mapa for ampliado ou reduzido numa fotocopiadora (a escala numérica não).\n\n**Erros comuns:** multiplicar pela escala quando devia dividir; esquecer a conversão de cm para km; aplicar a escala linear às áreas.",
 '**Escala** $=\\dfrac{\\text{desenho}}{\\text{real}}=1:n$, com ambas as medidas na mesma unidade. Real $=\\text{desenho}\\times n$. Área real $=\\text{área no desenho}\\times n^2$.',
 '$$d_{\\text{real}}=d_{\\text{desenho}}\\times n\\qquad d_{\\text{desenho}}=\\frac{d_{\\text{real}}}{n}\\qquad A_{\\text{real}}=A_{\\text{desenho}}\\times n^2$$\n\n$1\\text{ km}=1\\,000\\text{ m}=100\\,000\\text{ cm}$. $1\\text{ m}^2=10\\,000\\text{ cm}^2$.',
 ['Mapa $1:50\\,000$: 4 cm representam $4\\times50\\,000=200\\,000$ cm $=2$ km.',
  'Duas cidades a 60 km, mapa $1:1\\,000\\,000$: $6\\,000\\,000\\div1\\,000\\,000=6$ cm.',
  'No mapa, 5 cm representam 25 km: $25\\text{ km}=2\\,500\\,000$ cm; escala $1:500\\,000$.',
  'Planta $1:50$: sala de 8 cm × 6 cm representa 4 m × 3 m $=12$ m².',
  'Maquete $1:20$ de um prédio de 18 m: $1\\,800\\div20=90$ cm.',
  'Planta $1:100$: 24 cm² no desenho dão $24\\times10\\,000=240\\,000$ cm² $=24$ m² reais.'],
 "Resolve connosco: **num mapa de escala $1:200\\,000$ duas cidades distam 7,5 cm. Qual é a distância real?**\n\n1) $7{,}5\\times200\\,000=1\\,500\\,000$ cm.\n\n2) Converte: $1\\,500\\,000\\div100\\,000=15$ km.\n\n3) Verifica: 1 cm no mapa = 2 km; $7{,}5\\times2=15$ ✓.",
 '**Desafio.** Um terreno retangular de 40 m × 25 m vai ser desenhado numa folha A4 (29,7 cm × 21 cm). Qual é a maior escala $1:n$ (com $n$ inteiro) que lhe cabe? Verifica as duas medidas.',
 ['interpretar a escala 1:n', 'calcular distâncias reais e no desenho', 'converter unidades de comprimento', 'comparar escalas', 'passar de áreas no desenho a áreas reais'], ex)
write(2, 8, A)

# ---------- R6: velocidade, densidade, percentagens ----------
C = 'razao.aplicacoes'; ex = []
ex += [num(1, C, "Um autocarro percorre 240 km em 3 horas. Qual é a velocidade média, em km/h?", F(240,3), "v = d/t = 240 ÷ 3 = 80 km/h.", ["v = d ÷ t."]),
       num(1, C, "Um bloco de metal tem massa 540 g e volume 200 cm³. Qual é a densidade, em g/cm³?", F(540,200), "ρ = m/V = 540 ÷ 200 = 2,7 g/cm³.", ["ρ = m ÷ V."], ["2,7"]),
       num(1, C, "Numa turma de 40 alunos, 10 faltaram. Qual é a percentagem de faltosos?", 25, "10/40 = 25/100 = 25%.", ["Razão 10:40 = 1/4."])]
ex += [num(2, C, "Um carro viaja a 72 km/h. Quantos metros percorre em 1 segundo?", 20, "72 km/h = 72 000 m ÷ 3 600 s = 20 m/s.", ["1 km = 1 000 m; 1 h = 3 600 s."]),
       num(2, C, "Quantas horas demora um comboio a 90 km/h a percorrer 315 km?", F(315,90), "t = d/v = 315 ÷ 90 = 3,5 h.", ["t = d ÷ v."], ["3,5"]),
       num(2, C, "Um tijolo tem densidade 1,8 g/cm³ e volume 1 500 cm³. Qual é a massa, em kg?", F(18,10)*1500/1000, "m = ρ·V = 1,8 × 1 500 = 2 700 g = 2,7 kg.", ["m = ρ × V.", "2 700 g ÷ 1 000."], ["2,7"]),
       num(2, C, "Numa escola, 36 dos 120 alunos vão a pé. Que percentagem vai a pé?", 30, "36/120 = 3/10 = 30%.", ["Razão 36:120.", "Multiplica por 100."])]
ex += [num(3, C, "Um motorista faz 120 km a 60 km/h e depois 120 km a 120 km/h. Qual é a velocidade média de toda a viagem, em km/h?", 80, "Tempos: 2 h + 1 h = 3 h; distância 240 km; v = 240 ÷ 3 = 80 km/h (não é a média aritmética 90).", ["Soma das distâncias ÷ soma dos tempos.", "t = 2 + 1 = 3 h."]),
       num(3, C, "Um produto custava 5 000 Kz e passou a custar 5 750 Kz. De quantos por cento foi o aumento?", 15, "Aumento 750; 750/5 000 = 0,15 = 15%.", ["Diferença sobre o valor inicial."]),
       tf(3, C, "A velocidade média de uma viagem é sempre a média aritmética das duas velocidades.", False, "A velocidade média é distância total ÷ tempo total. Só coincide com a média aritmética em casos especiais (tempos iguais).", ["Confirma com 120 km a 60 km/h e 120 km a 120 km/h: dá 80, não 90."]),
       mc(2, C, "Qual é a unidade da densidade?", ["g/cm³", "km/h", "Kz/kg", "m²"], 0, "Densidade é massa por volume: g/cm³, kg/m³…", ["Massa ÷ volume."])]
A = std(SUB, 'Aplicações da proporcionalidade', 'aplicacoes-proporcionalidade', 'Velocidade média, densidade e percentagens como razões', 'velocidade-densidade-percentagem-razoes',
 'Usa razões para calcular velocidades, densidades, preços unitários e percentagens.', 30,
 'calcular velocidade média, densidade e percentagens como razões e resolver problemas contextualizados.', 'razão, proporção e unidades de medida.',
 'Quando alguém diz «80 quilómetros por hora» ou «20% de desconto», está a usar razões. Esta aula junta essas ideias em fórmulas úteis do dia a dia.',
 "Muitas grandezas do dia a dia são **razões entre duas grandezas**.\n\n**Velocidade média:** distância dividida pelo tempo, $v=\\frac{d}{t}$. Unidades: km/h, m/s. Para converter: $1\\text{ km/h}=\\frac{1\\,000}{3\\,600}\\text{ m/s}$, ou seja, divide por 3,6 para passar de km/h a m/s. 72 km/h $=20$ m/s. Rearranjando: $d=v\\,t$ e $t=\\frac{d}{v}$.\n\n**Atenção:** a velocidade média de uma viagem é a **distância total ÷ tempo total**, não a média das velocidades. Se fazes 120 km a 60 km/h (2 h) e 120 km a 120 km/h (1 h), a viagem de 240 km dura 3 h e a velocidade média é $\\frac{240}{3}=80$ km/h, não 90.\n\n**Densidade:** massa por unidade de volume, $\\rho=\\frac{m}{V}$ (g/cm³, kg/m³). A água tem densidade aproximada de 1 g/cm³ (1 000 kg/m³). Rearranjando: $m=\\rho V$ e $V=\\frac{m}{\\rho}$.\n\n**Preço unitário:** preço ÷ quantidade (Kz/kg, Kz/L), ótimo para comparar o que compensa comprar.\n\n**Percentagem:** razão com consequente 100. $\\frac{36}{120}=\\frac{30}{100}=30\\%$. Aumento percentual $=\\frac{\\text{aumento}}{\\text{valor inicial}}\\times100\\%$.\n\n**Erros comuns:** esquecer de converter unidades de tempo (minutos para horas); fazer a média das velocidades; dividir pelo valor final em vez do inicial nas percentagens de variação.",
 '**Velocidade média** $v=\\frac{d}{t}$; **densidade** $\\rho=\\frac{m}{V}$; **percentagem** de $a$ em $b$ $=\\frac{a}{b}\\times100\\%$; **aumento percentual** $=\\frac{\\text{novo}-\\text{inicial}}{\\text{inicial}}\\times100\\%$.',
 '$$v=\\frac{d}{t}\\qquad\\rho=\\frac{m}{V}\\qquad p\\%=\\frac{a}{b}\\times100$$\n\n$d$: distância (km, m); $t$: tempo (h, s); $m$: massa (g, kg); $V$: volume (cm³, m³). Converter: km/h ÷ 3,6 = m/s.',
 ['Autocarro: 240 km em 3 h: $v=240\\div3=80$ km/h.',
  'Conversão: 72 km/h $=72\\div3{,}6=20$ m/s.',
  'Comboio a 90 km/h durante 315 km: $t=315\\div90=3{,}5$ h.',
  'Bloco de 540 g e 200 cm³: $\\rho=540\\div200=2{,}7$ g/cm³.',
  'Tijolo de 1,8 g/cm³ e 1 500 cm³: $m=1{,}8\\times1\\,500=2\\,700$ g $=2{,}7$ kg.',
  'Aumento de 5 000 para 5 750 Kz: $\\frac{750}{5\\,000}=0{,}15=15\\%$.'],
 "Resolve connosco: **uma viagem de 380 km demorou 5 h e 30 min. Qual foi a velocidade média?**\n\n1) Tempo em horas: $5{,}5$ h.\n\n2) $v=380\\div5{,}5\\approx69{,}1$ km/h.\n\n3) Verifica: $69{,}1\\times5{,}5\\approx380$ ✓.",
 '**Desafio.** Dois sacos de arroz: 5 kg por 4 500 Kz e 12 kg por 9 960 Kz. Qual compensa mais? Calcula o preço por kg de cada um e diz qual a diferença percentual.',
 ['calcular v, d e t', 'converter km/h e m/s', 'aplicar densidade', 'calcular percentagens como razões', 'resolver problemas com preços unitários'], ex)
write(2, 9, A)
print('M3 ok')

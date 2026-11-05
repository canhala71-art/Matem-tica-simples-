from common import *
import math

def solve2(a1, b1, c1, a2, b2, c2):
    d = a1*b2 - a2*b1; assert d != 0
    x = F(c1*b2 - c2*b1, d); y = F(a1*c2 - a2*c1, d)
    assert a1*x + b1*y == c1 and a2*x + b2*y == c2
    return x, y

# ================= 1. Função afim =================
C = "funcoes.afim"
f = lambda a, b, x: a*x + b
ex = []
ex.append(num(1, C, "Sendo $f(x)=3x+2$, calcula $f(4)$.", f(3,2,4), "Substitui x por 4: 3·4 + 2 = 14.", ["f(4) = 3·4 + 2.", "= 12 + 2 = 14."]))
ex.append(num(1, C, "Sendo $f(x)=-2x+7$, calcula $f(5)$.", f(-2,7,5), "Substitui x por 5: −2·5 + 7 = −3.", ["f(5) = −2·5 + 7.", "= −10 + 7 = −3."]))
ex.append(num(1, C, "Qual é a ordenada na origem (o valor de $f(0)$) da função $f(x)=5x-3$?", f(5,-3,0), "Em f(0) o termo com x desaparece e sobra o termo independente: −3.", ["f(0) = 5·0 − 3.", "= −3."]))
ex.append(num(2, C, "Calcula o zero da função $f(x)=2x-10$ (o valor de x para o qual $f(x)=0$).", F(10,2), "Resolve 2x − 10 = 0: 2x = 10, logo x = 5.", ["Faz f(x) = 0: 2x − 10 = 0.", "2x = 10.", "x = 5."]))
ex.append(num(2, C, "Calcula o zero da função $f(x)=3x+12$.", F(-12,3), "3x + 12 = 0 dá 3x = −12, logo x = −4.", ["3x + 12 = 0.", "3x = −12.", "x = −4."]))
# declive por dois pontos
a = F(7-3, 3-1); assert a == 2
ex.append(num(2, C, "O gráfico de uma função afim passa pelos pontos $(1,3)$ e $(3,7)$. Qual é o declive (coeficiente de x)?", a, "O declive é a variação de y a dividir pela variação de x: (7 − 3) ÷ (3 − 1) = 2.", ["Variação de y: 7 − 3 = 4.", "Variação de x: 3 − 1 = 2.", "Declive = 4 ÷ 2 = 2."]))
# f(2)=7, f(5)=16 -> a=3,b=1, f(10)
a = F(16-7, 5-2); b = 7 - a*2; assert (a, b) == (3, 1)
ex.append(num(3, C, "Uma função afim verifica $f(2)=7$ e $f(5)=16$. Calcula $f(10)$.", f(a,b,10), "O declive é (16 − 7) ÷ (5 − 2) = 3. De f(2) = 7 sai b = 7 − 6 = 1, logo f(x) = 3x + 1 e f(10) = 31.", ["Declive: (16 − 7) ÷ (5 − 2) = 3.", "3·2 + b = 7, logo b = 1.", "f(10) = 3·10 + 1 = 31."]))
ex.append(num(2, C, "Um táxi cobra 400 Kz de bandeirada mais 150 Kz por quilómetro. Quanto custa uma corrida de 12 km, em Kz?", f(150,400,12), "Custo = 150·x + 400 com x = 12: 1800 + 400 = 2200.", ["Função: C(x) = 150x + 400.", "C(12) = 150·12 + 400 = 1800 + 400 = 2200 Kz."]))
# menor inteiro com 2x-6>0
x0 = 4; assert f(2,-6,x0) > 0 and f(2,-6,x0-1) <= 0
ex.append(num(3, C, "Qual é o menor número inteiro x para o qual $2x-6>0$?", x0, "2x − 6 > 0 equivale a x > 3, e o menor inteiro maior que 3 é 4.", ["2x > 6.", "x > 3.", "O menor inteiro maior que 3 é 4."]))
# interseção 2x+1 = x+5
xi = F(5-1, 2-1); assert f(2,1,xi) == f(1,5,xi)
ex.append(num(3, C, "Os gráficos de $f(x)=2x+1$ e $g(x)=x+5$ cruzam-se num ponto. Qual é o valor de x desse ponto?", xi, "Iguala as funções: 2x + 1 = x + 5, logo x = 4 (e y = 9).", ["2x + 1 = x + 5.", "2x − x = 5 − 1.", "x = 4."]))
ex.append(tf(1, C, "A função $f(x)=-4x+1$ é decrescente.", True, "O declive é −4, que é negativo: quando x aumenta, f(x) diminui.", ["Olha para o coeficiente de x: −4.", "Declive negativo, função decrescente."]))
ex.append(mc(2, C, "Qual destas funções afins é crescente?", ["$f(x)=-x+5$", "$f(x)=2x-3$", "$f(x)=5-2x$", "$f(x)=-3x$"], 1,
    "Uma função afim é crescente quando o declive é positivo. Só 2x − 3 tem declive positivo (2).", ["Identifica o coeficiente de x em cada uma.", "−1, 2, −2 e −3.", "Só o 2 é positivo."]))
ex.append(mc(2, C, "O gráfico de $f(x)=2x+3$ corta o eixo vertical (eixo dos yy) em que ponto?", ["$(0,3)$", "$(3,0)$", "$(0,2)$", "$(-3/2,0)$"], 0,
    "O eixo vertical corresponde a x = 0 e f(0) = 3, logo o ponto é (0, 3). O ponto (−3/2, 0) é onde corta o eixo horizontal.", ["Faz x = 0.", "f(0) = 3.", "Ponto (0, 3)."]))

afim = dict(subject="funcoes", topic_title="Função afim", topic_slug="funcao-afim", lesson_title="Função afim: o gráfico que é uma reta", lesson_slug="funcao-afim-grafico-zero-sinal",
  summary="Percebe a função f(x) = ax + b, o significado dos dois coeficientes, o zero e o crescimento.", minutes=30,
  blocks=dict(
  introduction="Quando apanhas um táxi em Luanda, pagas uma quantia fixa de partida (a bandeirada) e depois um valor por cada quilómetro. Se a bandeirada é 400 Kz e cada quilómetro custa 150 Kz, o preço da corrida depende da distância de uma forma muito regular: cada km a mais soma sempre os mesmos 150 Kz. Esta regularidade tem nome: **função afim**.\n\nFunções afins aparecem nas recargas de dados, no salário com comissão, na poupança semanal, na renda de uma casa. Nesta aula vais aprender a escrever uma função afim, a ler o que cada número dela significa, a calcular o seu zero e a decidir se ela cresce ou desce, tudo sem precisar de decorar nada às cegas.",
  intuition="Uma função afim escreve-se $f(x)=ax+b$. Pensa no táxi: **b é o que pagas antes de andar um metro** (400 Kz) e **a é o que pagas por cada unidade de x** (150 Kz por km). Por isso b chama-se **ordenada na origem** (o valor de f quando x = 0) e a chama-se **declive** (quanto f muda quando x aumenta uma unidade).\n\nO gráfico é sempre uma **reta**. O declive diz a inclinação: se a > 0 a reta sobe da esquerda para a direita (função crescente); se a < 0 desce (decrescente); se a = 0 fica horizontal (função constante). A ordenada na origem diz onde a reta corta o eixo vertical.\n\nO **zero** da função é o valor de x onde a reta corta o eixo horizontal, isto é, onde f(x) = 0. Para o encontrar resolves a equação ax + b = 0, que dá $x=-b/a$.\n\n**Erros comuns:** (1) confundir declive com ordenada na origem (a é o número que multiplica o x, b é o que está sozinho); (2) esquecer que o sinal de a manda no crescimento, e não o sinal de b; (3) no zero, trocar o sinal: em 3x + 12 = 0 o zero é −4, não 4. Defesa simples: substitui o x encontrado na função e confirma que dá 0.",
  definition="Chama-se **função afim** a toda a função $f:\\mathbb{R}\\to\\mathbb{R}$ definida por $f(x)=ax+b$, com a e b números reais. O número a é o **declive** (ou coeficiente angular) e b a **ordenada na origem**. Se b = 0, a função diz-se **linear** e o seu gráfico passa na origem; se a = 0, é **constante**. O gráfico de uma função afim é uma reta. A função é **crescente** se a > 0, **decrescente** se a < 0. O **zero** da função, quando a ≠ 0, é o único número x tal que f(x) = 0.",
  formulas="$$f(x)=ax+b$$\n\n$$\\text{zero: } x=-\\frac{b}{a}\\quad (a\\neq 0)$$\n\n$$\\text{declive por dois pontos: } a=\\frac{y_2-y_1}{x_2-x_1}$$\n\nSinal: se a > 0, f(x) > 0 para x à direita do zero e f(x) < 0 à esquerda; se a < 0 é o contrário. Mnemónica: **\"a manda no crescimento, b manda na altura inicial\"**.",
  worked_example="**Exemplo 1.** Sendo $f(x)=3x-5$, calcula f(4) e o zero.\n\nf(4) = 3·4 − 5 = 7. Para o zero: 3x − 5 = 0, logo x = 5/3.\n\n**Exemplo 2.** Descobre a função afim cujo gráfico passa por (1, 5) e (4, 11).\n\n**Passo 1.** Declive: (11 − 5) ÷ (4 − 1) = 2.\n\n**Passo 2.** Usa um ponto para achar b: 5 = 2·1 + b, logo b = 3. Então f(x) = 2x + 3. Confirma com o outro ponto: 2·4 + 3 = 11 ✓.\n\n**Exemplo 3 (sinal).** Para que valores de x é $f(x)=-2x+6$ positiva?\n\nZero: −2x + 6 = 0 dá x = 3. Como a = −2 é negativo, a função é decrescente: é positiva à esquerda do zero, isto é, para x < 3.\n\n**Exemplo 4 (problema).** Uma operadora cobra 1 000 Kz de mensalidade mais 20 Kz por cada minuto de chamada. Se o cliente pagou 2 600 Kz, quantos minutos falou?\n\nC(m) = 20m + 1000 = 2600, logo 20m = 1600 e m = 80 minutos.",
  guided_exercise="Resolve connosco: **a Marta poupa 500 Kz por semana e já tinha 3 000 Kz. A partir de quando terá mais de 10 000 Kz?**\n\n1) Qual é a função? S(t) = 500t + 3000, em que t é o número de semanas.\n\n2) Qual é o declive e o que significa? 500: o que ela junta por semana.\n\n3) Que inequação queremos? 500t + 3000 > 10000.\n\n4) Resolve: 500t > 7000, logo t > 14.\n\n5) Resposta: a partir da 15.ª semana. Prova: com t = 14 tem exatamente 10 000 Kz (ainda não é mais), com t = 15 tem 10 500 Kz.",
  independent_exercise=INDEP,
  challenge="**Dois planos de internet.** O plano A custa 2 000 Kz fixos mais 100 Kz por GB. O plano B custa 500 Kz fixos mais 200 Kz por GB. A partir de quantos GB o plano A fica mais barato?\n\nPista: escreve as duas funções, iguala-as para descobrir onde os gráficos se cruzam e pensa qual das retas é mais inclinada. Que plano compensa para quem usa poucos dados?",
  assessment="Consideras a competência dominada quando consegues: (1) calcular f(x) para vários valores; (2) ler o declive e a ordenada na origem numa expressão e no contexto de um problema; (3) calcular o zero e dizer se a função cresce ou desce; (4) encontrar a expressão de uma função afim a partir de dois pontos; (5) resolver uma inequação simples ax + b > 0. A consistência em exercícios fáceis, médios e difíceis conta mais do que a rapidez."),
  exercises=ex)

# ================= 2. Função quadrática =================
C = "funcoes.quadratica"
def disc(a, b, c): return b*b - 4*a*c
def roots(a, b, c):
    d = disc(a, b, c); s = math.isqrt(d); assert s*s == d
    return F(-b - s, 2*a), F(-b + s, 2*a)
ex = []
ex.append(num(1, C, "Calcula $f(0)$ para $f(x)=x^2-3x+7$.", 7, "Em f(0) só resta o termo independente c = 7.", ["f(0) = 0 − 0 + 7.", "= 7."]))
ex.append(num(1, C, "Calcula o discriminante $\\Delta=b^2-4ac$ da equação $x^2+2x-8=0$.", disc(1,2,-8), "Δ = 2² − 4·1·(−8) = 4 + 32 = 36.", ["a = 1, b = 2, c = −8.", "Δ = 4 − 4·1·(−8) = 4 + 32 = 36."]))
r1, r2 = roots(1,-5,6); assert (r1, r2) == (2, 3)
ex.append(num(2, C, "Calcula o maior zero da função $f(x)=x^2-5x+6$.", r2, "Δ = 25 − 24 = 1; x = (5 ± 1) ÷ 2, logo os zeros são 2 e 3, e o maior é 3.", ["Δ = (−5)² − 4·1·6 = 1.", "x = (5 ± 1) ÷ 2.", "Zeros: 2 e 3; o maior é 3."]))
xv = F(6, 2); assert xv == 3
ex.append(num(2, C, "Calcula a abcissa do vértice da parábola $y=x^2-6x+5$.", xv, "A abcissa do vértice é −b ÷ (2a) = 6 ÷ 2 = 3.", ["a = 1, b = −6.", "x_v = −b/(2a) = 6/2 = 3."]))
ex.append(num(3, C, "Qual é o valor mínimo da função $f(x)=x^2-6x+5$?", 3*3 - 6*3 + 5, "O mínimo ocorre no vértice, x = 3: f(3) = 9 − 18 + 5 = −4.", ["Vértice em x = 3.", "f(3) = 9 − 18 + 5 = −4."]))
ex.append(num(2, C, "Quantos zeros reais tem a função $f(x)=x^2+4x+4$?", 1, "Δ = 16 − 16 = 0, logo existe um único zero (x = −2).", ["Δ = 4² − 4·1·4 = 0.", "Δ = 0: um só zero, x = −2."]))
ex.append(num(3, C, "Calcula o valor máximo de $f(x)=-x^2+4x$.", -4+8 if False else (-(2**2)+4*2), "O vértice está em x = −4 ÷ (2·(−1)) = 2 e f(2) = −4 + 8 = 4.", ["x_v = −b/(2a) = −4/(−2) = 2.", "f(2) = −4 + 8 = 4."]))
# soma das raízes de 2x^2 - 10x + 8
a,b,c = 2,-10,8; s = F(-b, a); assert sum(roots(a,b,c)) == s == 5
ex.append(num(3, C, "Sem resolver a equação, calcula a soma dos zeros de $2x^2-10x+8=0$.", s, "A soma dos zeros é −b ÷ a = 10 ÷ 2 = 5 (confirma: os zeros são 1 e 4).", ["Soma = −b/a.", "−(−10)/2 = 5."]))
# bola h(t) = -5t^2+20t
tv = F(-20, -10); hmax = -5*tv*tv + 20*tv; assert (tv, hmax) == (2, 20)
ex.append(num(3, C, "Uma bola é atirada ao ar e a sua altura (em metros) é $h(t)=-5t^2+20t$, com t em segundos. Qual é a altura máxima atingida, em metros?", hmax, "O máximo está no vértice, t = 20 ÷ 10 = 2 s, e h(2) = −20 + 40 = 20 m.", ["t_v = −b/(2a) = −20/(−10) = 2.", "h(2) = −5·4 + 20·2 = 20 m."]))
# retângulo perímetro 40: A(x) = x(20-x), máx = 100
Amax = max(x*(20-x) for x in range(0, 21)); assert Amax == 100
ex.append(num(3, C, "Um retângulo tem perímetro de 40 m. Qual é a maior área, em m², que ele pode ter?", Amax, "Se um lado mede x, o outro mede 20 − x e A = x(20 − x) = −x² + 20x. O vértice está em x = 10, e A = 10·10 = 100.", ["Lados x e 20 − x.", "A(x) = −x² + 20x.", "Máximo em x = 10: A = 100 m² (um quadrado)."]))
ex.append(tf(1, C, "A parábola de $y=3x^2-2$ tem a concavidade voltada para cima.", True, "O coeficiente de x² é 3, positivo, por isso a concavidade está para cima.", ["Olha para o sinal de a.", "a = 3 > 0: concavidade para cima."]))
assert disc(1,1,1) < 0
ex.append(mc(2, C, "Quantos zeros reais tem a função $f(x)=x^2+x+1$?", ["Nenhum", "Um", "Dois", "Três"], 0, "Δ = 1 − 4 = −3 < 0, por isso a equação não tem soluções reais.", ["Δ = 1² − 4·1·1 = −3.", "Δ < 0: sem zeros reais."]))

quad = dict(subject="funcoes", topic_title="Função quadrática", topic_slug="funcao-quadratica", lesson_title="Função quadrática: parábola, zeros e vértice", lesson_slug="funcao-quadratica-parabola-vertice",
  summary="Compreende a parábola f(x) = ax² + bx + c, calcula zeros com o discriminante e encontra o máximo ou mínimo no vértice.", minutes=35,
  blocks=dict(
  introduction="Quando um jogador chuta uma bola ao ar, ela sobe, para um instante e volta a descer. O caminho que desenha é uma **parábola**. O mesmo acontece com um jato de água numa fonte, a ponte em arco, a antena parabólica e até com a conta do lucro de uma loja: vender muito barato dá prejuízo, vender muito caro afasta clientes, e há um preço no meio em que o lucro é o maior possível.\n\nTodas estas situações são descritas por **funções quadráticas**. Nesta aula vais aprender a calcular os zeros (onde a parábola corta o eixo horizontal), a encontrar o vértice (o ponto mais alto ou mais baixo) e a usar isso para resolver problemas de máximos e mínimos.",
  intuition="Uma função quadrática escreve-se $f(x)=ax^2+bx+c$, com a ≠ 0. O gráfico é uma parábola. O sinal de a decide a forma: se a > 0 a parábola abre para cima (como um sorriso) e tem um **mínimo**; se a < 0 abre para baixo e tem um **máximo**.\n\nA parábola é simétrica em torno de uma reta vertical, o **eixo de simetria**, que passa pelo **vértice**. A abcissa do vértice é $x_v=-b/(2a)$, e o valor máximo (ou mínimo) é $f(x_v)$. É por isso que, nos problemas de \"qual é o maior valor\", não é preciso testar números ao acaso: vais direto ao vértice.\n\nOs **zeros** são os x onde f(x) = 0. Calculam-se com a fórmula resolvente. O número $\\Delta=b^2-4ac$ (discriminante) diz quantos zeros existem: Δ > 0 dá dois, Δ = 0 dá um, Δ < 0 não dá nenhum real (a parábola não toca o eixo).\n\n**Erros comuns:** (1) esquecer o sinal de b na fórmula (o numerador começa por −b); (2) dizer que o vértice está em x = b/(2a) sem o sinal menos; (3) calcular o máximo como se fosse o valor de x, quando o máximo é o valor de f. Defesa simples: o vértice fica no meio dos dois zeros, quando existem.",
  definition="Chama-se **função quadrática** (ou função polinomial do 2.º grau) a toda a função $f:\\mathbb{R}\\to\\mathbb{R}$ dada por $f(x)=ax^2+bx+c$, com a, b, c reais e a ≠ 0. O gráfico é uma **parábola** de eixo vertical. O **vértice** é o ponto $V\\left(-\\frac{b}{2a},\\,-\\frac{\\Delta}{4a}\\right)$. Os **zeros** são as soluções reais de ax² + bx + c = 0, que existem se e só se Δ ≥ 0. Se a > 0 a função tem um mínimo absoluto no vértice; se a < 0 tem um máximo absoluto.",
  formulas="$$x=\\frac{-b\\pm\\sqrt{\\Delta}}{2a},\\qquad \\Delta=b^2-4ac$$\n\n$$x_v=-\\frac{b}{2a},\\qquad y_v=f(x_v)=-\\frac{\\Delta}{4a}$$\n\n$$\\text{soma dos zeros}=-\\frac{b}{a},\\qquad \\text{produto dos zeros}=\\frac{c}{a}$$\n\nMnemónica: **\"Δ conta os zeros, o vértice guarda o máximo ou o mínimo\"**.",
  worked_example="**Exemplo 1.** Calcula os zeros de $x^2-7x+10$.\n\nΔ = 49 − 40 = 9. x = (7 ± 3) ÷ 2, logo x = 2 ou x = 5. Prova: 2 + 5 = 7 e 2·5 = 10 ✓.\n\n**Exemplo 2.** Encontra o vértice de $f(x)=x^2-4x+1$ e diz se é máximo ou mínimo.\n\nx_v = 4 ÷ 2 = 2. f(2) = 4 − 8 + 1 = −3. Como a = 1 > 0 é um **mínimo**: V(2, −3).\n\n**Exemplo 3 (sem zeros).** $x^2+2x+5$: Δ = 4 − 20 = −16 < 0. Não há zeros reais. Como a > 0, a parábola está sempre acima do eixo, e f(x) > 0 para todo o x.\n\n**Exemplo 4 (problema).** Uma loja vende x telemóveis por dia e o lucro (em milhares de Kz) é L(x) = −2x² + 24x. Quantos deve vender para o lucro ser máximo?\n\nx_v = −24 ÷ (2·(−2)) = 6. O lucro máximo é L(6) = −72 + 144 = 72 mil Kz.",
  guided_exercise="Resolve connosco: **um agricultor tem 60 m de rede para vedar uma horta retangular encostada a um muro (só precisa de vedar três lados). Qual a maior área possível?**\n\n1) Sejam x os dois lados perpendiculares ao muro. Quanto sobra para o lado paralelo? 60 − 2x.\n\n2) Qual é a área? A(x) = x(60 − 2x) = −2x² + 60x.\n\n3) A parábola abre para cima ou para baixo? Para baixo, porque a = −2: tem máximo.\n\n4) Vértice: x = −60 ÷ (2·(−2)) = 15.\n\n5) Área máxima: A(15) = 15·30 = 450 m². Lados: 15 m, 15 m e 30 m.",
  independent_exercise=INDEP,
  challenge="**Um preço para o lucro máximo.** Uma papelaria vende cadernos a p Kz cada e vende (400 − p) cadernos por dia. Cada caderno custou 100 Kz à papelaria. Que preço dá o maior lucro diário?\n\nPista: o lucro é (p − 100)(400 − p). Desenvolve e procura o vértice, ou lembra-te que o vértice fica no meio dos dois zeros: o lucro é zero quando p = 100 e quando p = 400.",
  assessment="Consideras a competência dominada quando consegues: (1) dizer, só pelo sinal de a, se há máximo ou mínimo; (2) calcular Δ e interpretar o número de zeros; (3) resolver ax² + bx + c = 0 com a fórmula resolvente; (4) encontrar o vértice e o valor máximo ou mínimo; (5) traduzir um problema de máximo ou mínimo (área, altura, lucro) numa função quadrática e resolvê-lo."),
  exercises=ex)

# ================= 3. Sistemas =================
C = "sistemas.lineares"
ex = []
x,y = solve2(1,1,10,1,-1,4)
ex.append(num(1, C, "Resolve o sistema $x+y=10$ e $x-y=4$. Qual é o valor de x?", x, "Soma as duas equações: 2x = 14, logo x = 7 (e y = 3).", ["Soma membro a membro: 2x = 14.", "x = 7.", "Depois y = 10 − 7 = 3."]))
x,y = solve2(2,1,11,1,1,7)
ex.append(num(1, C, "Resolve o sistema $2x+y=11$ e $x+y=7$. Qual é o valor de y?", y, "Subtrai as equações: x = 4; depois y = 7 − 4 = 3.", ["(2x + y) − (x + y) = 11 − 7 dá x = 4.", "y = 7 − 4 = 3."]))
x,y = solve2(3,2,16,1,-1,2)
ex.append(num(2, C, "Resolve $3x+2y=16$ e $x-y=2$. Qual é o valor de x?", x, "De x − y = 2 tira-se x = y + 2. Substituindo: 3(y + 2) + 2y = 16, logo 5y = 10, y = 2 e x = 4.", ["x = y + 2.", "3(y + 2) + 2y = 16 → 5y + 6 = 16.", "y = 2 e x = 4."]))
x,y = solve2(5,2,19,1,-2,-1)
ex.append(num(2, C, "Resolve $5x+2y=19$ e $x-2y=-1$. Qual é o valor de x?", x, "Somando as equações o termo em y desaparece: 6x = 18, logo x = 3 (e y = 2).", ["Soma: 6x = 18.", "x = 3.", "5·3 + 2y = 19 dá y = 2."]))
x,y = solve2(2,3,12,4,-1,10)
ex.append(num(3, C, "Resolve $2x+3y=12$ e $4x-y=10$. Qual é o valor de x?", x, "Da segunda, y = 4x − 10. Na primeira: 2x + 12x − 30 = 12, logo 14x = 42 e x = 3 (y = 2).", ["y = 4x − 10.", "2x + 3(4x − 10) = 12 → 14x = 42.", "x = 3."]))
# preços: adulto 300, criança 200
adulto, crianca = solve2(2,3,1200,1,3,900)
assert (adulto, crianca) == (300, 200)
ex.append(num(2, C, "Num cinema, 2 bilhetes de adulto e 3 de criança custam 1 200 Kz, e 1 bilhete de adulto e 3 de criança custam 900 Kz. Quanto custa um bilhete de criança, em Kz?", crianca, "Subtrai as equações: um adulto custa 300 Kz. Depois 300 + 3c = 900 dá c = 200.", ["Subtrai: (2a + 3c) − (a + 3c) = 1200 − 900, logo a = 300.", "300 + 3c = 900.", "c = 200 Kz."]))
# idades: p + f = 50; p = 4f
p, f_ = solve2(1,1,50,1,-4,0); assert (p, f_) == (40, 10)
ex.append(num(2, C, "A soma das idades de um pai e do filho é 50 anos e o pai tem o quádruplo da idade do filho. Que idade tem o filho?", f_, "p + f = 50 e p = 4f dão 5f = 50, logo f = 10 (o pai tem 40).", ["p = 4f.", "4f + f = 50.", "f = 10."]))
# galinhas e coelhos
coel, gal = solve2(4,2,56,1,1,20); assert (coel, gal) == (8, 12)
ex.append(num(3, C, "Num quintal há galinhas e coelhos: 20 cabeças e 56 patas no total. Quantos coelhos há?", coel, "Seja c o número de coelhos e g o de galinhas: c + g = 20 e 4c + 2g = 56. Multiplicando a primeira por 2: 2c + 2g = 40; subtraindo, 2c = 16 e c = 8.", ["c + g = 20 e 4c + 2g = 56.", "Subtrai 2·(c + g) = 40: 2c = 16.", "c = 8."]))
# notas de 500 e 1000
n500, n1000 = solve2(1,1,14,500,1000,9500); assert (n500, n1000) == (9, 5)
ex.append(num(3, C, "Uma pessoa tem 14 notas, umas de 500 Kz e outras de 1 000 Kz, no valor total de 9 500 Kz. Quantas notas de 1 000 Kz tem?", n1000, "a + b = 14 e 500a + 1000b = 9500, ou seja, a + 2b = 19. Subtraindo a primeira: b = 5 (e a = 9).", ["a + b = 14.", "500a + 1000b = 9500 → a + 2b = 19.", "Subtrai: b = 5."]))
assert 2*2+3 == 7 and 2*2-3 == 1
ex.append(tf(1, C, "O par $(2,3)$ é solução do sistema $x+y=5$ e $2x-y=1$.", True, "Substituindo: 2 + 3 = 5 ✓ e 2·2 − 3 = 1 ✓. Satisfaz as duas equações.", ["1.ª: 2 + 3 = 5.", "2.ª: 4 − 3 = 1.", "Ambas verificam-se."]))
ex.append(mc(2, C, "O sistema $x+y=3$ e $x+y=5$ é…", ["Impossível (sem solução)", "Possível e determinado (uma solução)", "Possível e indeterminado (infinitas soluções)", "Tem a solução (1, 2)"], 0,
    "A mesma soma x + y não pode valer 3 e 5 ao mesmo tempo, por isso não há solução. As retas são paralelas.", ["Subtrai as equações: 0 = −2.", "É impossível, logo o sistema não tem solução."]))
ex.append(mc(3, C, "Resolveste um sistema e chegaste a $0=0$. O que concluis?", ["O sistema tem infinitas soluções", "O sistema não tem solução", "O sistema tem solução única x = 0", "Erraste: deve dar sempre um número"], 0,
    "Chegar a uma igualdade sempre verdadeira (0 = 0) significa que as duas equações dizem o mesmo: as retas coincidem e há infinitas soluções.", ["0 = 0 é verdadeiro para qualquer x.", "As equações são equivalentes: infinitas soluções."]))

sis = dict(subject="sistemas-de-equacoes", topic_title="Sistemas de equações do 1.º grau", topic_slug="sistemas-lineares-2x2", lesson_title="Sistemas de duas equações: substituição e adição", lesson_slug="sistemas-lineares-substituicao-adicao",
  summary="Resolve sistemas de duas equações com duas incógnitas por substituição e por adição, e usa-os em problemas do dia a dia.", minutes=30,
  blocks=dict(
  introduction="No cinema, dois adultos e três crianças pagam 1 200 Kz; um adulto e três crianças pagam 900 Kz. Quanto custa cada bilhete? Aqui há **duas coisas que não sabes** (o preço do adulto e o da criança) e **duas informações** que as ligam. Com uma só informação não dava para descobrir; com duas, dá.\n\nIsso é um **sistema de equações**. Aparece nas compras, nas idades, nas misturas, nas notas de dinheiro de uma carteira, na quantidade de galinhas e coelhos de um quintal. Nesta aula vais aprender dois métodos simples, substituição e adição, e a perceber quando um sistema não tem solução ou tem infinitas.",
  intuition="Cada equação como $x+y=10$ é uma reta: todos os pares (x, y) que a verificam. Resolver o sistema é encontrar o ponto onde as duas retas se **cruzam**, o único par que satisfaz as duas ao mesmo tempo.\n\nHá dois caminhos principais. Na **substituição** tiras uma incógnita de uma equação (por exemplo, y = 4x − 10) e substituis na outra, ficando com uma equação só com x. Na **adição** (ou eliminação) somas ou subtrais as equações de modo a que uma incógnita desapareça: em x + y = 10 e x − y = 4, somando fica 2x = 14.\n\nSe as retas forem **paralelas** (x + y = 3 e x + y = 5) não há solução: o sistema é **impossível**. Se forem a **mesma reta**, há infinitas soluções: **possível e indeterminado**. O caso normal, com um só ponto, é o **possível e determinado**.\n\n**Erros comuns:** (1) achar só o valor de x e esquecer o y; (2) errar o sinal ao subtrair equações (subtrai todos os termos, não só um); (3) não fazer a prova: substitui o par nas duas equações originais, não só numa.",
  definition="Um **sistema de duas equações lineares com duas incógnitas** é um conjunto de duas equações da forma $ax+by=c$. Uma **solução** é um par (x, y) que verifica as duas equações. O sistema diz-se **possível e determinado** se tem exatamente uma solução, **possível e indeterminado** se tem infinitas, e **impossível** se não tem nenhuma. Dois sistemas são **equivalentes** se têm as mesmas soluções; multiplicar uma equação por um número diferente de zero, ou somar uma equação à outra, dá um sistema equivalente.",
  formulas="$$\\begin{cases}a_1x+b_1y=c_1\\\\ a_2x+b_2y=c_2\\end{cases}\;\\Rightarrow\; x=\\frac{c_1b_2-c_2b_1}{a_1b_2-a_2b_1},\\quad y=\\frac{a_1c_2-a_2c_1}{a_1b_2-a_2b_1}$$\n\nO denominador $a_1b_2-a_2b_1$ é o **determinante**. Se for zero, o sistema é impossível ou indeterminado.\n\nNa prática, usa a **substituição** quando uma incógnita já está sozinha (ou com coeficiente 1) e a **adição** quando os coeficientes de uma incógnita são iguais ou simétricos. Mnemónica: **\"elimina uma, acha a outra, volta atrás e prova\"**.",
  worked_example="**Exemplo 1 (adição).** $x+y=10$ e $x-y=4$.\n\nSomando: 2x = 14, logo x = 7. Depois y = 10 − 7 = 3. Prova: 7 + 3 = 10 e 7 − 3 = 4 ✓.\n\n**Exemplo 2 (substituição).** $y=2x$ e $x+y=12$.\n\nSubstitui y: x + 2x = 12, logo x = 4 e y = 8. Prova: 4 + 8 = 12 ✓.\n\n**Exemplo 3 (multiplicar antes).** $2x+3y=13$ e $x+y=5$.\n\nMultiplica a segunda por 2: 2x + 2y = 10. Subtrai da primeira: y = 3. Então x = 2. Prova: 4 + 9 = 13 ✓.\n\n**Exemplo 4 (problema).** Numa banca, 3 pães e 2 sumos custam 1 100 Kz e 2 pães e 1 sumo custam 650 Kz. Preço de cada?\n\n3p + 2s = 1100 e 2p + s = 650. Da segunda, s = 650 − 2p. Substituindo: 3p + 1300 − 4p = 1100, logo p = 200 Kz e s = 250 Kz. Prova: 600 + 500 = 1100 ✓.",
  guided_exercise="Resolve connosco: **numa carteira há 12 notas, umas de 500 Kz e outras de 1 000 Kz, num total de 8 000 Kz. Quantas são de cada?**\n\n1) Define as incógnitas: a = notas de 500 e b = notas de 1 000.\n\n2) Primeira equação (número de notas): a + b = 12.\n\n3) Segunda equação (valor): 500a + 1000b = 8000, que dividida por 500 dá a + 2b = 16.\n\n4) Subtrai a primeira da segunda: b = 4.\n\n5) Então a = 8. Prova: 8·500 + 4·1000 = 4000 + 4000 = 8000 ✓. Resposta: 8 notas de 500 Kz e 4 de 1 000 Kz.",
  independent_exercise=INDEP,
  challenge="**O número misterioso.** Um número de dois algarismos tem soma dos algarismos igual a 11. Se trocares a ordem dos algarismos, o número aumenta 27 unidades. Qual é o número?\n\nPista: se as dezenas são d e as unidades u, o número é 10d + u e o invertido é 10u + d. Escreve as duas equações e resolve o sistema.",
  assessment="Consideras a competência dominada quando consegues: (1) resolver sistemas pelos dois métodos, escolhendo o mais cómodo; (2) fazer sempre a prova nas duas equações; (3) reconhecer um sistema impossível ou indeterminado; (4) traduzir um problema com duas incógnitas (preços, idades, notas, animais) num sistema e interpretar a solução com unidades."),
  exercises=ex)

for i, d in enumerate([afim, quad, sis], start=1):
    write(3, i, d)
    print(d["lesson_slug"], len(d["exercises"]), "ok")

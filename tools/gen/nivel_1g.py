"""Nível 1 — Tema 8 (Potências: 37–39) e Tema 9 (Raízes: 40–42)."""
from common import *
import math

# ===== 37. Potenciação: base, expoente, inteiros, expoente 0 e 1, base 10 =====
C = 'potencias.conceito'; ex = []
for a, n in [(3, 4), (5, 3), (2, 9), (6, 3), (9, 2), (4, 5)]:
    ex.append(num(1 if a ** n < 100 else 2, C, f"Calcula ${a}^{n}$.", a ** n, f"${a}^{n}$ = {a} multiplicado {n} vezes = {a**n}.", [f"{' × '.join([str(a)]*n)}.", f"= {a**n}."]))
for a, n in [(-2, 4), (-3, 3), (-5, 2), (-1, 99), (-10, 3)]:
    ex.append(num(2, C, f"Calcula $({a})^{{{n}}}$.", a ** n, f"Expoente {'par' if n%2==0 else 'ímpar'} com base negativa: resultado {'positivo' if a**n>0 else 'negativo'}: {a**n}.", ["Conta os fatores negativos.", f"= {a**n}."]))
ex.append(num(2, C, "Calcula $-4^2$ (o sinal fica fora da potência).", -16, "Primeiro $4^2=16$, depois o sinal: −16.", ["4² = 16.", "Sinal fora."]))
ex.append(num(2, C, "Calcula $7^0+7^1$.", 8, "$7^0=1$ e $7^1=7$: soma 8.", ["a⁰ = 1.", "a¹ = a."]))
ex.append(num(2, C, "Quantos zeros tem $10^{9}$ (mil milhões)?", 9, "$10^9$ tem 9 zeros.", ["O expoente é o nº de zeros."]))
ex.append(num(3, C, "Escreve 4 500 000 como $45\\times10^{n}$. Qual é n?", 5, "4 500 000 = 45 × 100 000 = 45 × 10⁵.", ["100 000 = 10⁵."]))
ex.append(num(3, C, "Um boato é enviado a 3 pessoas, e cada uma envia a outras 3, e assim por diante. Quantas pessoas recebem na 5.ª ronda?", 3 ** 5, "$3^5=243$.", ["Na ronda n recebem 3ⁿ."]))
ex.append(tf(1, C, "$2^3=6$.", False, "$2^3=2\\times2\\times2=8$. Não é $2\\times3$.", ["Multiplica a base por si mesma."]))
ex.append(tf(2, C, "$(-3)^2=-9$.", False, "$(-3)^2=(-3)\\times(-3)=9$.", ["Sinais iguais → positivo."]))
ex.append(tf(2, C, "$5^0=1$.", True, "Qualquer número diferente de 0 elevado a 0 é 1.", ["a⁰ = 1."]))
ex.append(mc(2, C, "Qual é a diferença entre $(-2)^4$ e $-2^4$?", ["$(-2)^4=16$ e $-2^4=-16$", "Ambos dão 16", "Ambos dão −16", "$(-2)^4=-16$ e $-2^4=16$"], 0, "Com parênteses a base é −2: (−2)(−2)(−2)(−2)=16. Sem parênteses, o sinal fica fora: −(2⁴)=−16.", ["Quem é a base?"]))
A = lesson('potencias', 'Conceito de potenciação', 'conceito-potenciacao', 'Potenciação: base, expoente, inteiros, expoentes 0 e 1 e potências de 10', 'potenciacao-conceito-base-expoente-inteiros',
 'Compreende a potenciação, calcula potências de naturais e inteiros, os casos de expoente 0 e 1 e as potências de base 10.', 25,
 "**Objetivos:** compreender base e expoente, calcular potências de naturais e inteiros (incluindo base negativa), conhecer os casos $a^0$ e $a^1$ e usar potências de 10. **Pré-requisitos:** multiplicação, números inteiros e regra de sinais.\n\nUma notícia espalha-se: cada pessoa conta a outras 3, e cada uma destas a outras 3. Depois de 5 rondas, $3\\times3\\times3\\times3\\times3=243$ pessoas ouviram-na. Em vez de escrever o 3 cinco vezes, escreve-se $3^5$. A **potenciação** é a forma curta de multiplicar um número por si próprio várias vezes.",
 "Em $a^n$, $a$ é a **base** (o fator repetido) e $n$ é o **expoente** (quantas vezes se repete). $a^n=a\\times a\\times\\cdots\\times a$ ($n$ fatores). Lê-se «$a$ elevado a $n$»; $a^2$ é «ao quadrado» e $a^3$ «ao cubo». **Cuidado:** $2^3=8$, não $2\\times3=6$.\n\n**Casos especiais:** $a^1=a$ e $a^0=1$ (se $a\\ne0$). A razão do $a^0=1$: $\\frac{a^3}{a^3}=1$ e, pela regra do quociente, $a^{3-3}=a^0$.\n\n**Base negativa:** o sinal depende da paridade do expoente. **Expoente par** → resultado positivo: $(-2)^4=16$. **Expoente ímpar** → negativo: $(-2)^3=-8$. Atenção aos parênteses: $(-2)^4=16$ mas $-2^4=-16$ (o sinal menos fica fora; a base é 2).\n\n**Potências de 10:** $10^n$ é o 1 seguido de $n$ zeros ($10^3=1\\,000$). Servem para escrever números grandes: $4\\,500\\,000=45\\times10^5=4{,}5\\times10^6$ (notação científica). Por $10^{-n}$ entende-se $\\frac{1}{10^n}$ (pequenos números).\n\nO expoente cresce depressa: $2^{10}=1\\,024$ e $2^{20}$ já passa de um milhão.\n\n**Erros comuns:** multiplicar base por expoente; achar que $a^0=0$; esquecer os parênteses com base negativa.",
 "Para $n\\ge2$, $a^n$ é o produto de $n$ fatores iguais a $a$. Define-se $a^1=a$ e $a^0=1$ ($a\\neq0$). O **sinal** de $a^n$ com $a<0$ é positivo se $n$ é par e negativo se $n$ é ímpar.",
 "$$a^n=\\underbrace{a\\times\\cdots\\times a}_{n}\\qquad a^1=a\\qquad a^0=1\\ (a\\ne0)$$\n\n$$(-a)^{\\text{par}}>0,\\quad(-a)^{\\text{ímpar}}<0\\qquad10^n=1\\underbrace{0\\ldots0}_{n}$$",
 "**Exemplo 1.** $3^4=3\\times3\\times3\\times3=81$.\n\n**Exemplo 2 (base negativa).** $(-2)^5=-32$ e $(-2)^4=16$.\n\n**Exemplo 3 (sinal fora).** $-4^2=-(4\\times4)=-16$, enquanto $(-4)^2=16$.\n\n**Exemplo 4 (casos especiais).** $7^0=1$ e $7^1=7$.\n\n**Exemplo 5 (base 10).** $10^6=1\\,000\\,000$ e $4\\,500\\,000=45\\times10^5$.\n\n**Aplicação.** Um boato enviado a 3 pessoas em cada ronda chega a $3^5=243$ pessoas na 5.ª ronda.",
 "Resolve connosco: **calcula $(-3)^3+(-3)^2$.**\n\n1) $(-3)^2=9$ (dois fatores negativos).\n\n2) $(-3)^3=(-3)^2\\times(-3)=9\\times(-3)=-27$.\n\n3) Soma: $-27+9=-18$.\n\n4) Verifica os sinais: expoente ímpar → negativo; expoente par → positivo ✓.",
 "**Desafio.** Uma folha de papel é dobrada ao meio repetidamente. Com a espessura de 0,1 mm, qual seria a altura depois de 10 dobras? E de 20? Usa $2^n$ e compara com a altura de um prédio.",
 "Consideras a competência dominada quando consegues: (1) distinguir base e expoente; (2) calcular potências de naturais e inteiros; (3) aplicar $a^0=1$ e $a^1=a$; (4) tratar bem o sinal e os parênteses; (5) escrever números grandes com potências de 10.", ex)
write(1, 37, A)

# ===== 38. Propriedades da potenciação =====
C = 'potencias.propriedades'; ex = []
for a, m, n in [(2, 3, 4), (3, 2, 5), (5, 4, 2), (10, 3, 3)]:
    ex.append(num(2, C, f"Calcula ${a}^{m}\\times{a}^{n}$.", a ** (m + n), f"Mesma base: somam-se os expoentes: ${a}^{{{m+n}}}={a**(m+n)}$.", [f"{m} + {n} = {m+n}.", f"{a}^{m+n} = {a**(m+n)}."]))
for a, m, n in [(2, 8, 3), (3, 7, 4), (10, 9, 6)]:
    ex.append(num(2, C, f"Calcula ${a}^{m}\\div{a}^{n}$.", a ** (m - n), f"Mesma base: subtraem-se os expoentes: ${a}^{{{m-n}}}={a**(m-n)}$.", [f"{m} − {n} = {m-n}.", f"= {a**(m-n)}."]))
for a, m, n in [(2, 3, 2), (3, 2, 2), (5, 2, 2)]:
    ex.append(num(3, C, f"Calcula $({a}^{m})^{n}$.", a ** (m * n), f"Potência de potência: multiplicam-se os expoentes: ${a}^{{{m*n}}}={a**(m*n)}$.", [f"{m} × {n} = {m*n}.", f"= {a**(m*n)}."]))
ex.append(num(2, C, "Calcula $(2\\times3)^2$ usando a potência de um produto.", 36, "$(2\\times3)^2=2^2\\times3^2=4\\times9=36$.", ["Distribui o expoente."]))
ex.append(num(3, C, "Calcula $\\left(\\dfrac{6}{3}\\right)^4$.", 16, "$(6/3)^4=2^4=16$ (ou $6^4\\div3^4=1296\\div81=16$).", ["6 ÷ 3 = 2."]))
ex.append(num(3, C, "Se $2^x\\times2^5=2^{11}$, quanto vale x?", 6, "x + 5 = 11, logo x = 6.", ["Soma os expoentes."]))
ex.append(num(3, C, "Calcula $\\dfrac{2^5\\times2^4}{2^6}$.", 2 ** 3, "$2^{5+4-6}=2^3=8$.", ["9 − 6 = 3."]))
ex.append(tf(2, C, "$a^m\\times a^n=a^{m\\times n}$.", False, "Na multiplicação de potências de mesma base somam-se os expoentes: $a^{m+n}$.", ["Soma, não produto."]))
ex.append(tf(2, C, "$(a\\times b)^n=a^n\\times b^n$.", True, "A potência de um produto é o produto das potências.", ["Distributiva em produtos."]))
ex.append(tf(2, C, "$(a+b)^2=a^2+b^2$.", False, "$(a+b)^2=a^2+2ab+b^2$. A potência não se distribui pela soma. Ex.: $(2+3)^2=25\\neq13$.", ["Testa com números."]))
ex.append(mc(2, C, "Qual é o resultado de $(3^2)^3$?", ["$3^6$", "$3^5$", "$3^8$", "$9^5$"], 0, "Multiplicam-se os expoentes: $2\\times3=6$.", ["Potência de potência."]))
A = lesson('potencias', 'Propriedades da potenciação', 'propriedades-potenciacao', 'Propriedades da potenciação: produto, quociente, potência de potência, produto e quociente', 'potenciacao-propriedades',
 'Aplica as propriedades do produto, do quociente, da potência de potência e da potência de produto e de quociente.', 30,
 "**Objetivos:** demonstrar e aplicar as propriedades da potenciação com a mesma base, e as de potência de potência, produto e quociente. **Pré-requisitos:** conceito de potência e regras de sinais.\n\nCalcular $2^{10}\\times2^{15}$ escrevendo todos os fatores seria um absurdo. Mas as potências obedecem a regras simples que permitem simplificar contas enormes numa linha.",
 "**Produto de potências com a mesma base:** $a^m\\times a^n=a^{m+n}$. Porquê? $2^3\\times2^4=(2\\times2\\times2)\\times(2\\times2\\times2\\times2)=2^7$: contam-se os fatores no total.\n\n**Quociente de potências com a mesma base:** $a^m\\div a^n=a^{m-n}$ ($a\\neq0$). Ex.: $\\frac{2^8}{2^3}=2^5$ (cortam-se 3 fatores).\n\n**Potência de potência:** $(a^m)^n=a^{m\\times n}$. Ex.: $(2^3)^2=2^3\\times2^3=2^6$.\n\n**Potência de um produto:** $(a\\times b)^n=a^n\\times b^n$. **Potência de um quociente:** $\\left(\\frac{a}{b}\\right)^n=\\frac{a^n}{b^n}$ ($b\\ne0$).\n\n**Atenção:** estas regras **não** valem para somas: $(a+b)^n\\neq a^n+b^n$. Por exemplo $(2+3)^2=25$ mas $2^2+3^2=13$. Também só se somam expoentes se as **bases forem iguais**: $2^3\\times3^2$ não se simplifica assim.\n\nConsequência: $a^{-n}=\\frac{1}{a^n}$ (pois $a^0\\div a^n=a^{-n}$).\n\n**Erros comuns:** multiplicar os expoentes no produto de potências; somar bases; aplicar o expoente à soma.",
 "As **propriedades da potenciação** são identidades válidas para $a,b\\neq0$ e $m,n$ inteiros: produto e quociente de potências de mesma base, potência de potência, potência de produto e de quociente.",
 "$$a^m\\times a^n=a^{m+n}\\qquad\\frac{a^m}{a^n}=a^{m-n}\\qquad(a^m)^n=a^{mn}$$\n\n$$(ab)^n=a^nb^n\\qquad\\left(\\frac{a}{b}\\right)^n=\\frac{a^n}{b^n}\\qquad a^{-n}=\\frac{1}{a^n}$$",
 "**Exemplo 1 (produto).** $2^3\\times2^4=2^7=128$.\n\n**Exemplo 2 (quociente).** $3^7\\div3^4=3^3=27$.\n\n**Exemplo 3 (potência de potência).** $(2^3)^2=2^6=64$.\n\n**Exemplo 4 (de produto).** $(2\\times5)^3=2^3\\times5^3=8\\times125=1\\,000$.\n\n**Exemplo 5 (de quociente).** $\\left(\\frac{6}{3}\\right)^4=\\frac{6^4}{3^4}=\\frac{1\\,296}{81}=16$.\n\n**Aplicação.** $\\dfrac{2^5\\times2^4}{2^6}=2^{5+4-6}=2^3=8$.",
 "Resolve connosco: **simplifica $\\dfrac{3^5\\times3^2}{3^4}$ e calcula.**\n\n1) Numerador: $3^5\\times3^2=3^{5+2}=3^7$.\n\n2) Quociente: $\\frac{3^7}{3^4}=3^{7-4}=3^3$.\n\n3) $3^3=27$.\n\n4) Prova: $243\\times9=2\\,187$ e $2\\,187\\div81=27$ ✓.",
 "**Desafio.** Descobre o erro em «$(2+3)^2=2^2+3^2=13$». Desenvolve $(2+3)^2$ e compara com $2^2+2\\times2\\times3+3^2$. Que termo estava em falta?",
 "Consideras a competência dominada quando consegues: (1) somar expoentes no produto e subtraí-los no quociente (mesma base); (2) multiplicar expoentes na potência de potência; (3) distribuir o expoente por produtos e quocientes; (4) evitar aplicá-lo a somas.", ex)
write(1, 38, A)

# ===== 39. Expressões com potências e aplicações =====
C = 'potencias.expressoes'; ex = []
E = [("2^3+3^2", 8 + 9), ("5^2-2^4", 25 - 16), ("(2+3)^2-4\\times2", 25 - 8), ("3\\times2^3-10", 24 - 10), ("(-2)^3+(-3)^2", -8 + 9), ("2^4\\div2^2+3^0", 4 + 1), ("(10-4)^2\\div3^2", 36 // 9), ("2\\times(3^2-5)^2", 2 * 16)]
for k, (s, v) in enumerate(E):
    ex.append(num(2 if k < 5 else 3, C, f"Calcula ${s}$.", v, f"Respeitando a ordem (parênteses → potências → ×,÷ → +,−): ${s}={v}$.", ["Parênteses.", "Potências.", "Restantes operações."]))
ex.append(num(3, C, "Um capital de 1 000 Kz duplica todos os anos. Quanto terá ao fim de 6 anos, em Kz?", 1000 * 2 ** 6, "1 000 × 2⁶ = 64 000 Kz.", ["Fator 2 por ano.", "2⁶ = 64."]))
ex.append(num(3, C, "Uma bactéria divide-se em 2 a cada hora. Partindo de 5 bactérias, quantas há ao fim de 8 horas?", 5 * 2 ** 8, "5 × 2⁸ = 5 × 256 = 1 280.", ["2⁸ = 256."]))
ex.append(num(3, C, "Um quadrado tem lado 12 m. Qual é a sua área, em m²?", 144, "Área = 12² = 144 m².", ["Lado ao quadrado."]))
ex.append(num(3, C, "Um cubo tem aresta 5 cm. Qual é o seu volume, em cm³?", 125, "Volume = 5³ = 125 cm³.", ["Aresta ao cubo."]))
ex.append(tf(2, C, "$2+3\\times4^2=98$.", False, "Primeiro 4² = 16, depois 3 × 16 = 48 e 2 + 48 = 50.", ["Potência, produto, soma."]))
ex.append(mc(2, C, "Qual é o valor de $3^2\\times2^3$?", ["72", "36", "216", "18"], 0, "9 × 8 = 72.", ["3² = 9; 2³ = 8."]))
A = lesson('potencias', 'Expressões com potências', 'expressoes-potencias-aplicacoes', 'Expressões numéricas com potências e aplicações práticas', 'potencias-expressoes-aplicacoes',
 'Resolve expressões com potências pela ordem correta e aplica-as a áreas, volumes e crescimentos.', 30,
 "**Objetivos:** calcular expressões numéricas com potências e usá-las em problemas de área, volume e crescimento exponencial. **Pré-requisitos:** potências, propriedades e ordem das operações.\n\nQuanto custa um terreno quadrado de 12 m de lado, a 3 000 Kz o m²? Primeiro calculas a área $12^2=144$ m². As potências aparecem em áreas, volumes, juros compostos e crescimento de populações.",
 "**Ordem das operações:** (1) parênteses, colchetes e chavetas (de dentro para fora); (2) **potências e raízes**; (3) multiplicações e divisões; (4) somas e subtrações. A potenciação tem prioridade sobre a multiplicação: $2+3\\times4^2=2+3\\times16=50$.\n\nCuidado com o sinal: $-3^2=-9$ e $(-3)^2=9$. Cuidado com a base: $2\\times3^2=2\\times9=18$, não $(2\\times3)^2=36$.\n\n**Aplicações:** **área** de um quadrado de lado $l$ é $l^2$; **volume** de um cubo de aresta $a$ é $a^3$; o **crescimento exponencial** (que duplica, triplica...) dá $V_0\\times f^n$: 1 000 Kz que duplicam todos os anos valem $1\\,000\\times2^6=64\\,000$ ao fim de 6 anos.\n\nPotências de 10 para medidas: $1\\text{ km}=10^3\\text{ m}$; $1\\text{ m}^2=10^4\\text{ cm}^2$; $1\\text{ m}^3=10^6\\text{ cm}^3$.\n\n**Erros comuns:** calcular antes a multiplicação do que a potência; esquecer parênteses; confundir $a^2$ com $2a$ (por exemplo, $5^2=25$, não 10).",
 "Uma **expressão com potências** é uma expressão numérica em que aparecem potências. O **crescimento exponencial** é aquele em que uma grandeza é multiplicada por um mesmo fator em intervalos iguais: $V_n=V_0\\times f^n$.",
 "Ordem: agrupamentos → potências/raízes → $\\times,\\div$ → $+,-$.\n\n$$A_{\\square}=l^2\\qquad V_{\\text{cubo}}=a^3\\qquad V_n=V_0\\times f^n$$",
 "**Exemplo 1.** $2^3+3^2=8+9=17$.\n\n**Exemplo 2.** $(2+3)^2-4\\times2=25-8=17$.\n\n**Exemplo 3.** $3\\times2^3-10=3\\times8-10=14$.\n\n**Exemplo 4.** $(-2)^3+(-3)^2=-8+9=1$.\n\n**Exemplo 5.** $2\\times(3^2-5)^2=2\\times4^2=32$.\n\n**Aplicação.** 1 000 Kz que duplicam por ano: $1\\,000\\times2^6=64\\,000$ Kz em 6 anos. Um cubo de aresta 5 cm tem volume $5^3=125$ cm³.",
 "Resolve connosco: **uma cultura de 5 bactérias duplica a cada hora. Quantas há ao fim de 8 horas?**\n\n1) Fator por hora: 2. Em 8 horas, $2^8=256$.\n\n2) $5\\times256=1\\,280$.\n\n3) Confere o início: ao fim de 1 h são 10 ($5\\times2^1$) ✓.",
 "**Desafio.** Se $2^{10}=1\\,024$, usa as propriedades para calcular $2^{20}$ e $2^{30}$ aproximadamente. Quantas vezes é maior que 1 milhão? E que ordem de grandeza tem $2^{40}$?",
 "Consideras a competência dominada quando consegues: (1) respeitar a prioridade das potências; (2) tratar sinais e parênteses; (3) usar potências em área, volume e crescimento; (4) interpretar o resultado no contexto.", ex)
write(1, 39, A)

# ======================= TEMA 9 — RAÍZES =======================
# ===== 40. Radiciação: conceito, raiz quadrada e cúbica, exatas e não exatas, estimativa =====
C = 'raizes.conceito'; ex = []
for n in [49, 81, 121, 225, 400]:
    r = math.isqrt(n); assert r * r == n
    ex.append(num(1 if n <= 100 else 2, C, f"Calcula $\\sqrt{{{n}}}$.", r, f"${r}^2={n}$, logo $\\sqrt{{{n}}}={r}$.", [f"{r} × {r} = {n}."]))
for n in [8, 27, 125, 1000]:
    r = round(n ** (1 / 3)); assert r ** 3 == n
    ex.append(num(2, C, f"Calcula $\\sqrt[3]{{{n}}}$.", r, f"${r}^3={n}$, logo $\\sqrt[3]{{{n}}}={r}$.", [f"{r}³ = {n}."]))
ex.append(num(2, C, "Entre que dois inteiros consecutivos está $\\sqrt{40}$? Indica o menor.", 6, "$6^2=36<40<49=7^2$: entre 6 e 7.", ["36 < 40 < 49."]))
ex.append(num(3, C, "Qual é o inteiro mais próximo de $\\sqrt{50}$?", 7, "$\\sqrt{50}\\approx7{,}07$, o mais próximo é 7.", ["49 está muito perto de 50."]))
ex.append(num(2, C, "Qual é o índice da raiz cúbica?", 3, "Na raiz cúbica o índice é 3. Na quadrada é 2 (não se escreve).", ["Pequeno número sobre o radical."]))
ex.append(num(3, C, "Um quadrado tem 144 cm² de área. Quanto mede o lado, em cm?", 12, "Lado = $\\sqrt{144}=12$.", ["12 × 12 = 144."]))
ex.append(num(3, C, "Um cubo tem 64 cm³ de volume. Quanto mede a aresta, em cm?", 4, "Aresta = $\\sqrt[3]{64}=4$.", ["4³ = 64."]))
ex.append(tf(1, C, "$\\sqrt{16}=4$.", True, "$4\\times4=16$.", ["4² = 16."]))
ex.append(tf(2, C, "$\\sqrt{2}$ é uma raiz exata.", False, "Não há número inteiro (nem decimal exato) cujo quadrado seja 2: $\\sqrt{2}\\approx1{,}414$.", ["1² = 1 < 2 < 4 = 2²."]))
ex.append(tf(2, C, "A raiz quadrada de um número negativo existe nos números reais.", False, "Nenhum número real ao quadrado dá um resultado negativo.", ["x² ≥ 0."]))
ex.append(mc(2, C, "Qual é a relação entre potência e raiz?", ["$\\sqrt{a}=b\\iff b^2=a$ (com $b\\ge0$)", "$\\sqrt{a}=a\\div2$", "$\\sqrt{a}=a^2$", "$\\sqrt{a}=2a$"], 0, "A raiz é a operação inversa da potência.", ["Inversa do quadrado."]))
A = lesson('raizes', 'Conceito de radiciação', 'conceito-radiciacao', 'Radiciação: raiz quadrada e cúbica, índice e radicando, raízes exatas e estimativa', 'radiciacao-conceito-quadrada-cubica',
 'Compreende a radiciação como operação inversa da potenciação, calcula raízes quadradas e cúbicas exatas e estima as não exatas.', 30,
 "**Objetivos:** compreender a radiciação, os termos (radicando, índice, radical), calcular raízes quadradas e cúbicas exatas e estimar as não exatas. **Pré-requisitos:** potenciação e quadrados perfeitos.\n\nUm terreno quadrado tem 144 m² de área. Quanto mede o lado? Procuras o número que multiplicado por si próprio dá 144: é 12. Este caminho inverso do quadrado chama-se **raiz quadrada**. E se tens um depósito cúbico de 64 litros? A aresta é o número que ao cubo dá 64: 4. É a **raiz cúbica**.",
 "A radiciação é a operação **inversa** da potenciação. $\\sqrt[n]{a}=b$ quando $b^n=a$. Em $\\sqrt[n]{a}$: $a$ é o **radicando**, $n$ o **índice** e $\\sqrt{\\ \\ }$ o **radical**. Se o índice é 2 não se escreve: $\\sqrt{16}=4$. Raiz cúbica: $\\sqrt[3]{27}=3$.\n\n**Quadrados perfeitos:** 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225… Têm raiz quadrada inteira. **Cubos perfeitos:** 1, 8, 27, 64, 125, 216, 343, 512, 729, 1 000.\n\nUma raiz é **exata** quando é um número inteiro (ou racional); caso contrário, é **não exata** (irracional) e só se pode aproximar: $\\sqrt{2}\\approx1{,}414$.\n\n**Estimativa:** para $\\sqrt{40}$, vê entre que quadrados perfeitos está: $36<40<49$, logo $6<\\sqrt{40}<7$; como 40 está mais perto de 36, é cerca de 6,3.\n\n**Raiz de números negativos:** a raiz quadrada de um número negativo **não existe** nos reais (nenhum número ao quadrado dá negativo). Mas a raiz cúbica existe: $\\sqrt[3]{-8}=-2$, porque $(-2)^3=-8$.\n\n**Erros comuns:** achar que $\\sqrt{16}=8$ (confunde com metade); dizer $\\sqrt{a+b}=\\sqrt a+\\sqrt b$; ignorar que $\\sqrt{a}$ é sempre não negativa.",
 "A **raiz de índice $n$** de $a$, $\\sqrt[n]{a}$, é o número $b$ tal que $b^n=a$ (com $b\\ge0$ se $n$ é par). Chama-se **radicando** a $a$, **índice** a $n$. Uma raiz é **exata** quando $b$ é inteiro. Um **quadrado perfeito** é um natural de raiz quadrada natural.",
 "$$\\sqrt[n]{a}=b\\iff b^n=a\\qquad\\sqrt{a}=\\sqrt[2]{a}$$\n\n$$\\sqrt[n]{a^n}=a\\ (a\\ge0)\\qquad\\left(\\sqrt[n]{a}\\right)^n=a$$\n\nQuadrados: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144. Cubos: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1 000.",
 "**Exemplo 1.** $\\sqrt{49}=7$, porque $7^2=49$.\n\n**Exemplo 2.** $\\sqrt[3]{125}=5$, porque $5^3=125$.\n\n**Exemplo 3 (negativo).** $\\sqrt[3]{-27}=-3$, porque $(-3)^3=-27$; mas $\\sqrt{-27}$ não existe nos reais.\n\n**Exemplo 4 (estimar).** $\\sqrt{40}$: $6^2=36$ e $7^2=49$, logo $6<\\sqrt{40}<7$ (cerca de 6,3).\n\n**Exemplo 5 (não exata).** $\\sqrt{2}\\approx1{,}414$.\n\n**Aplicação.** Um terreno quadrado de 144 m² tem lado $\\sqrt{144}=12$ m; um depósito cúbico de 64 L tem aresta $\\sqrt[3]{64}=4$ dm.",
 "Resolve connosco: **calcula $\\sqrt{169}$ e $\\sqrt[3]{216}$ e estima $\\sqrt{75}$.**\n\n1) $13\\times13=169$, logo $\\sqrt{169}=13$.\n\n2) $6\\times6\\times6=216$, logo $\\sqrt[3]{216}=6$.\n\n3) $8^2=64<75<81=9^2$: $\\sqrt{75}$ está entre 8 e 9 (mais perto de 9: cerca de 8,7).\n\n4) Confirma: $8{,}7^2=75{,}69$ ✓.",
 "**Desafio.** Descobre um número natural que seja ao mesmo tempo quadrado perfeito e cubo perfeito (além de 1). Dica: pensa em $n^6$. Quantos há abaixo de 5 000?",
 "Consideras a competência dominada quando consegues: (1) explicar a raiz como inversa da potência; (2) calcular raízes quadradas e cúbicas exatas; (3) estimar raízes não exatas; (4) distinguir radicando, índice e radical.", ex)
write(1, 40, A)

# ===== 41. Propriedades dos radicais e simplificação =====
C = 'raizes.propriedades'; ex = []
def simp(n):
    out, rest = 1, n
    p = 2
    while p * p <= rest:
        while rest % (p * p) == 0: rest //= p * p; out *= p
        p += 1
    return out, rest
for n in [12, 18, 50, 72, 98, 200]:
    a, b = simp(n)
    ex.append(num(2 if n < 100 else 3, C, f"Simplifica $\\sqrt{{{n}}}=a\\sqrt{{b}}$ com $b$ o menor possível. Qual é o valor de $a$?", a, f"{n} = {a*a} × {b}, logo $\\sqrt{{{n}}}={a}\\sqrt{{{b}}}$ e $a={a}$.", [f"{n} = {a*a} × {b}.", f"√{a*a} = {a}."]))
for x, y in [(4, 9), (25, 4), (36, 49)]:
    ex.append(num(2, C, f"Calcula $\\sqrt{{{x}\\times{y}}}$.", math.isqrt(x * y), f"$\\sqrt{{{x}\\times{y}}}=\\sqrt{{{x}}}\\times\\sqrt{{{y}}}={math.isqrt(x)}\\times{math.isqrt(y)}={math.isqrt(x*y)}$.", ["Raiz de cada fator."]))
ex.append(num(2, C, "Calcula $\\sqrt{\\dfrac{81}{9}}$.", 3, "$\\sqrt{81}\\div\\sqrt{9}=9\\div3=3$.", ["Raiz de cada termo."]))
ex.append(num(3, C, "Calcula $3\\sqrt{2}+5\\sqrt{2}$ e indica o coeficiente de $\\sqrt{2}$.", 8, "Radicais semelhantes somam-se: $(3+5)\\sqrt{2}=8\\sqrt{2}$.", ["Mesmo radical."]))
ex.append(num(3, C, "Calcula $\\sqrt{2}\\times\\sqrt{8}$.", 4, "$\\sqrt{2\\times8}=\\sqrt{16}=4$.", ["Junta os radicandos."]))
ex.append(num(3, C, "Calcula $\\sqrt{12}+\\sqrt{27}$ e indica o coeficiente de $\\sqrt{3}$.", 5, "$\\sqrt{12}=2\\sqrt3$ e $\\sqrt{27}=3\\sqrt3$; soma $5\\sqrt3$.", ["Simplifica primeiro."]))
ex.append(tf(2, C, "$\\sqrt{9+16}=\\sqrt{9}+\\sqrt{16}$.", False, "$\\sqrt{25}=5$ mas $3+4=7$. A raiz não se distribui pela soma.", ["Testa."]))
ex.append(tf(2, C, "$\\sqrt{50}=5\\sqrt{2}$.", True, "$50=25\\times2$, logo $\\sqrt{50}=5\\sqrt{2}$.", ["25 × 2."]))
ex.append(tf(3, C, "$\\sqrt{2}+\\sqrt{3}=\\sqrt{5}$.", False, "$\\sqrt2+\\sqrt3\\approx3{,}15$ e $\\sqrt5\\approx2{,}24$.", ["Aproxima."]))
ex.append(mc(2, C, "Qual é a forma simplificada de $\\sqrt{72}$?", ["$6\\sqrt{2}$", "$2\\sqrt{18}$", "$3\\sqrt{8}$", "$8\\sqrt{3}$"], 0, "72 = 36 × 2, logo 6√2. As outras ainda se simplificam ou estão erradas.", ["Maior quadrado que divide 72."]))
A = lesson('raizes', 'Propriedades dos radicais', 'propriedades-radicais', 'Propriedades dos radicais, simplificação e operações com radicais', 'raizes-propriedades-simplificacao-operacoes',
 'Aplica as propriedades dos radicais, simplifica raízes e opera com radicais semelhantes.', 30,
 "**Objetivos:** aplicar a raiz de um produto e de um quociente, simplificar radicais e somar e multiplicar radicais. **Pré-requisitos:** raízes exatas, decomposição em fatores primos, quadrados perfeitos.\n\nComo se calcula $\\sqrt{72}$ sem calculadora? Não é exato, mas podes escrevê-lo de forma mais simples: $\\sqrt{72}=6\\sqrt{2}$. Isto torna os cálculos com raízes muito mais fáceis e é usado em geometria e física.",
 "**Raiz de um produto:** $\\sqrt{a\\times b}=\\sqrt{a}\\times\\sqrt{b}$ ($a,b\\ge0$). **Raiz de um quociente:** $\\sqrt{\\frac{a}{b}}=\\frac{\\sqrt a}{\\sqrt b}$ ($b>0$). Valem também com índices $n$.\n\n**Simplificar um radical:** procura o maior quadrado perfeito que divide o radicando e tira-o para fora. $\\sqrt{72}=\\sqrt{36\\times2}=6\\sqrt{2}$. Com decomposição: $72=2^3\\times3^2$; os pares saem: $2^2\\to2$, $3^2\\to3$; fica $2\\times3\\times\\sqrt{2}=6\\sqrt2$.\n\n**Somar e subtrair:** só se somam radicais **semelhantes** (mesmo radical): $3\\sqrt{2}+5\\sqrt{2}=8\\sqrt{2}$. Muitas vezes é preciso simplificar primeiro: $\\sqrt{12}+\\sqrt{27}=2\\sqrt3+3\\sqrt3=5\\sqrt3$.\n\n**Multiplicar e dividir:** $\\sqrt{2}\\times\\sqrt{8}=\\sqrt{16}=4$; $a\\sqrt{b}\\times c\\sqrt{d}=ac\\sqrt{bd}$.\n\n**Não existe regra para a soma:** $\\sqrt{a+b}\\neq\\sqrt a+\\sqrt b$ e $\\sqrt2+\\sqrt3\\neq\\sqrt5$.\n\n**Erros comuns:** somar radicandos; tirar para fora números que não são quadrados perfeitos; esquecer que o que sai multiplica o que fica.",
 "Dois **radicais são semelhantes** se têm o mesmo índice e o mesmo radicando. **Simplificar** um radical $\\sqrt{a}$ é escrevê-lo como $k\\sqrt{m}$ com $m$ sem fatores quadrados.",
 "$$\\sqrt{ab}=\\sqrt a\\sqrt b\\qquad\\sqrt{\\frac ab}=\\frac{\\sqrt a}{\\sqrt b}\\qquad\\sqrt{k^2m}=k\\sqrt m$$\n\n$$a\\sqrt m\\pm b\\sqrt m=(a\\pm b)\\sqrt m\\qquad a\\sqrt m\\times b\\sqrt n=ab\\sqrt{mn}$$",
 "**Exemplo 1 (produto).** $\\sqrt{4\\times9}=\\sqrt4\\times\\sqrt9=2\\times3=6$.\n\n**Exemplo 2 (simplificar).** $\\sqrt{50}=\\sqrt{25\\times2}=5\\sqrt{2}$.\n\n**Exemplo 3 (outra).** $\\sqrt{72}=\\sqrt{36\\times2}=6\\sqrt{2}$.\n\n**Exemplo 4 (soma).** $\\sqrt{12}+\\sqrt{27}=2\\sqrt3+3\\sqrt3=5\\sqrt3$.\n\n**Exemplo 5 (multiplicação).** $\\sqrt2\\times\\sqrt8=\\sqrt{16}=4$.\n\n**Aplicação.** A diagonal de um quadrado de lado 6 m é $6\\sqrt2\\approx8{,}49$ m.",
 "Resolve connosco: **simplifica $\\sqrt{98}-\\sqrt{50}+\\sqrt{8}$.**\n\n1) $\\sqrt{98}=\\sqrt{49\\times2}=7\\sqrt2$.\n\n2) $\\sqrt{50}=5\\sqrt2$ e $\\sqrt{8}=2\\sqrt2$.\n\n3) $7\\sqrt2-5\\sqrt2+2\\sqrt2=4\\sqrt2$.\n\n4) Aproximação: $\\sqrt{98}\\approx9{,}90$; $\\sqrt{50}\\approx7{,}07$; $\\sqrt8\\approx2{,}83$; soma $5{,}66\\approx4\\sqrt2$ ✓.",
 "**Desafio.** O lado de um quadrado mede $\\sqrt{12}$ cm. Escreve o lado simplificado e calcula a área e o perímetro exatos. Porque a área é um número inteiro e o perímetro não?",
 "Consideras a competência dominada quando consegues: (1) usar a raiz de produto e de quociente; (2) simplificar radicais; (3) somar radicais semelhantes após simplificar; (4) multiplicar radicais.", ex)
write(1, 41, A)

# ===== 42. Expressões com raízes e problemas =====
C = 'raizes.expressoes'; ex = []
E = [("\\sqrt{9}+\\sqrt{16}", 7), ("\\sqrt{25}\\times\\sqrt{4}-3", 10 - 3), ("\\sqrt{100}\\div5+2^3", 2 + 8), ("\\sqrt{9+16}", 5), ("\\sqrt[3]{27}+\\sqrt{49}", 3 + 7), ("(\\sqrt{36}-\\sqrt{25})^2", 1), ("\\sqrt{144}\\div\\sqrt{9}", 4), ("2\\sqrt{81}-\\sqrt[3]{8}\\times3", 18 - 6)]
for k, (s, v) in enumerate(E):
    ex.append(num(2 if k < 5 else 3, C, f"Calcula ${s}$.", v, f"Calcula as raízes e depois as restantes operações: ${s}={v}$.", ["Raízes.", "Resto da expressão."]))
ex.append(num(3, C, "Um quadrado tem 81 m² de área. Qual é o perímetro, em m?", 36, "Lado = √81 = 9; perímetro 4 × 9 = 36 m.", ["Raiz da área."]))
ex.append(num(3, C, "Um triângulo retângulo tem catetos 6 e 8. Qual é a hipotenusa? (Pitágoras: $h=\\sqrt{6^2+8^2}$.)", 10, "$\\sqrt{36+64}=\\sqrt{100}=10$.", ["36 + 64 = 100."]))
ex.append(num(3, C, "Um cubo tem 125 cm³ de volume. Qual é a área de uma face, em cm²?", 25, "Aresta = ∛125 = 5; face 5² = 25 cm².", ["Aresta primeiro."]))
ex.append(num(3, C, "A diagonal $d$ de um quadrado de lado $l$ obtém-se por $d^2=2l^2$. Se $l=5$, qual é $d^2$?", 50, "d² = 2 × 25 = 50 (logo d = √50 = 5√2 ≈ 7,07).", ["l² = 25."]))
ex.append(tf(2, C, "$\\sqrt{(-5)^2}=5$.", True, "$(-5)^2=25$ e $\\sqrt{25}=5$ (a raiz é não negativa).", ["25 → 5."]))
ex.append(tf(2, C, "$\\sqrt{16}=\\pm4$.", False, "$\\sqrt{16}$ designa apenas a raiz não negativa, 4. A equação $x^2=16$ tem soluções ±4.", ["Raiz é sempre ≥ 0."]))
ex.append(mc(2, C, "Qual é o valor de $\\sqrt{3^2+4^2}$?", ["5", "7", "25", "12"], 0, "$\\sqrt{9+16}=\\sqrt{25}=5$.", ["Soma antes de tirar a raiz."]))
A = lesson('raizes', 'Expressões com raízes', 'expressoes-raizes-problemas', 'Expressões numéricas com raízes e problemas de aplicação', 'raizes-expressoes-problemas',
 'Resolve expressões com raízes e aplica-as a áreas, volumes e ao teorema de Pitágoras.', 30,
 "**Objetivos:** calcular expressões numéricas com raízes e usar raízes em problemas de geometria e medidas. **Pré-requisitos:** raízes, potências e ordem das operações.\n\nAs raízes aparecem em quase todos os problemas de geometria: o lado de um quadrado a partir da área, a aresta de um cubo a partir do volume, a distância em linha reta entre dois pontos (teorema de Pitágoras).",
 "**Ordem das operações:** (1) parênteses; (2) potências e raízes; (3) $\\times$ e $\\div$; (4) $+$ e $-$. O radical funciona como um «parêntese»: a expressão sob a raiz calcula-se primeiro. $\\sqrt{9+16}=\\sqrt{25}=5$, mas $\\sqrt9+\\sqrt{16}=7$.\n\n**Geometria:** o **lado de um quadrado** de área $A$ é $\\sqrt{A}$; a **aresta de um cubo** de volume $V$ é $\\sqrt[3]{V}$. O **teorema de Pitágoras** diz que num triângulo retângulo de catetos $a$, $b$ e hipotenusa $h$: $h^2=a^2+b^2$, logo $h=\\sqrt{a^2+b^2}$. Para catetos 6 e 8, $h=\\sqrt{100}=10$.\n\n**Diagonal do quadrado:** $d=l\\sqrt2$ (por Pitágoras com dois lados iguais). Para $l=5$, $d=5\\sqrt2\\approx7{,}07$.\n\n**Sinal:** $\\sqrt{a}$ é sempre **não negativa**. Por isso $\\sqrt{(-5)^2}=\\sqrt{25}=5$. Já a equação $x^2=16$ tem duas soluções, $x=\\pm4$.\n\n**Resolução de problemas:** extrai os dados, escolhe a fórmula, calcula a raiz exata ou aproximada e responde com a unidade.\n\n**Erros comuns:** distribuir a raiz pela soma; esquecer de tirar a raiz no fim em Pitágoras ($h^2$ não é $h$); dizer $\\sqrt{16}=\\pm4$.",
 "O **teorema de Pitágoras** estabelece que num triângulo retângulo o quadrado da hipotenusa é igual à soma dos quadrados dos catetos. Uma **expressão com raízes** é uma expressão numérica com radicais, calculada pela ordem das operações.",
 "$$h=\\sqrt{a^2+b^2}\\qquad l=\\sqrt{A}\\qquad a=\\sqrt[3]{V}\\qquad d=l\\sqrt2$$\n\nOrdem: agrupamentos → potências e raízes → $\\times,\\div$ → $+,-$.",
 "**Exemplo 1.** $\\sqrt9+\\sqrt{16}=3+4=7$.\n\n**Exemplo 2.** $\\sqrt{9+16}=\\sqrt{25}=5$ (muda o resultado).\n\n**Exemplo 3.** $\\sqrt{100}\\div5+2^3=10\\div5+8=10$.\n\n**Exemplo 4 (Pitágoras).** Catetos 6 e 8: $h=\\sqrt{36+64}=10$.\n\n**Exemplo 5 (cubo).** Volume 125 cm³: aresta $\\sqrt[3]{125}=5$ cm e face $5^2=25$ cm².\n\n**Aplicação.** Uma escada de 10 m encosta numa parede, com o pé a 6 m da base. Altura que alcança: $\\sqrt{10^2-6^2}=\\sqrt{64}=8$ m.",
 "Resolve connosco: **um terreno retangular mede 24 m por 7 m. Qual é a diagonal?**\n\n1) Pitágoras: $d=\\sqrt{24^2+7^2}$.\n\n2) $24^2=576$ e $7^2=49$: soma 625.\n\n3) $d=\\sqrt{625}=25$ m.\n\n4) Verifica: $25^2=625$ ✓.",
 "**Desafio.** Quantos metros de rede são precisos para um percurso que vai de uma ponta de um campo de 40 m × 30 m à ponta oposta, em linha reta? E quanto se poupa em relação a ir pelos dois lados?",
 "Consideras a competência dominada quando consegues: (1) calcular expressões com raízes pela ordem correta; (2) usar o teorema de Pitágoras; (3) achar lado, aresta e diagonal; (4) não distribuir a raiz pela soma.", ex)
write(1, 42, A)
print('P/R ok')

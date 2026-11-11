"""Nível 2 — Módulo 5 (continuação): Equações do 2.º grau (aulas 19–21)."""
from n2h import *
SUB = 'equacoes'
def chk(f, x): assert f(F(x)) == 0, (f, x)

# ---------- E6: incompletas ----------
C = 'equacoes.segundo_incompletas'; ex = []
ex += [num(1, C, "Qual é a solução positiva de $x^2-49=0$?", 7, "x² = 49 → x = ±7; a positiva é 7.", ["x² = 49."]),
       num(1, C, "Qual é a solução positiva de $3x^2=27$?", 3, "x² = 9 → x = ±3.", ["Divide por 3."]),
       num(1, C, "Qual é a solução diferente de 0 de $x^2+4x=0$?", -4, "x(x + 4) = 0 → x = 0 ou x = −4.", ["Põe x em evidência."])]
ex += [num(2, C, "Qual é a solução positiva de $2x^2-50=0$?", 5, "x² = 25 → x = ±5.", ["Divide por 2."]),
       num(2, C, "Qual é a solução diferente de 0 de $x^2-9x=0$?", 9, "x(x − 9) = 0 → x = 9.", ["Evidência: x."]),
       num(2, C, "Qual é a solução diferente de 0 de $5x^2=20x$?", 4, "5x² − 20x = 0 → 5x(x − 4) = 0 → x = 4.", ["Passa tudo para um lado.", "Evidência: 5x."]),
       num(2, C, "Resolve $\\dfrac{x^2}{4}=9$ e indica a solução positiva.", 6, "x² = 36 → x = ±6.", ["Multiplica por 4."])]
ex += [num(3, C, "Qual é a soma das soluções de $x^2-16=0$?", 0, "As soluções são 4 e −4; soma 0.", ["x = ±4."]),
       num(3, C, "Um quadrado tem 169 cm² de área. Qual é o lado, em cm?", 13, "l² = 169 → l = 13 (só vale a solução positiva).", ["Lado positivo."]),
       tf(2, C, "A equação $x^2+9=0$ não tem soluções reais.", True, "x² = −9 e nenhum número real ao quadrado é negativo.", ["x² ≥ 0."]),
       mc(3, C, "Para resolver $x^2-7x=0$ o método mais rápido é:", ["Pôr $x$ em evidência: $x(x-7)=0$", "Aplicar só a raiz quadrada: $x=\\sqrt7$", "Dividir por $x$ (perdendo a solução 0)", "Somar 7 aos dois membros"], 0, "Produto nulo: x = 0 ou x = 7. Dividir por x perderia a solução x = 0.", ["Lei do anulamento do produto."])]
for f,x in [(lambda x:x*x-49,7),(lambda x:x*x+4*x,-4),(lambda x:x*x-9*x,9),(lambda x:5*x*x-20*x,4)]: chk(f,x)
A = std(SUB, 'Equações do 2.º grau', 'equacoes-2-grau', 'Equações do 2.º grau incompletas', 'equacoes-2-grau-incompletas',
 'Resolve equações do 2.º grau incompletas por raiz quadrada e por evidência.', 30,
 'reconhecer equações do 2.º grau, resolver as incompletas ($ax^2+c=0$ e $ax^2+bx=0$) e usar a lei do anulamento do produto.', 'equações do 1.º grau, fatores e raízes quadradas.',
 'Uma equação do 2.º grau aparece quando a incógnita surge ao quadrado: por exemplo, ao procurar o lado de um quadrado a partir da área.',
 "Uma **equação do 2.º grau** tem a forma $ax^2+bx+c=0$ com $a\\ne0$. É **completa** se $b\\ne0$ e $c\\ne0$ e **incompleta** se $b=0$ ou $c=0$.\n\n**Caso $b=0$: $ax^2+c=0$.** Isola $x^2$: $x^2=-\\frac{c}{a}$. Se $-\\frac{c}{a}>0$ há duas soluções simétricas $x=\\pm\\sqrt{-\\frac{c}{a}}$; se for $0$ há uma ($x=0$); se for negativo **não há soluções reais**. Exemplo: $x^2-49=0\\Rightarrow x=\\pm7$. $x^2+9=0$ é impossível.\n\n**Caso $c=0$: $ax^2+bx=0$.** Põe $x$ em evidência: $x(ax+b)=0$. Pela **lei do anulamento do produto** (um produto é zero se algum fator é zero): $x=0$ ou $ax+b=0$, ou seja, $x=-\\frac{b}{a}$. Exemplo: $x^2+4x=0\\Rightarrow x(x+4)=0\\Rightarrow x=0$ ou $x=-4$.\n\n**Caso $b=c=0$:** $ax^2=0\\Rightarrow x=0$ (solução dupla).\n\n**Aviso:** nunca dividas os dois membros por $x$: perdes a solução $x=0$. Em $5x^2=20x$, passa tudo para um lado e usa evidência: $5x(x-4)=0$.\n\n**Contexto geométrico:** se a área de um quadrado é 169 cm², $l^2=169$, $l=13$ cm. Só a solução **positiva** serve como medida.\n\n**Verificação:** substitui cada solução na equação original.\n\n**Erros comuns:** dizer $x^2=49\\Rightarrow x=7$ (esquecer $-7$); dividir por $x$; aceitar a solução negativa num comprimento.",
 'Equação do 2.º grau: $ax^2+bx+c=0$, $a\\neq0$. **Incompleta** se $b=0$ ou $c=0$. **Lei do anulamento do produto:** $A\\cdot B=0\\iff A=0$ ou $B=0$.',
 '$$ax^2+c=0\\Rightarrow x=\\pm\\sqrt{-\\tfrac{c}{a}}\\ \\ (-\\tfrac{c}{a}\\ge0)\\qquad ax^2+bx=0\\Rightarrow x=0\\ \\text{ou}\\ x=-\\tfrac{b}{a}$$',
 ['$x^2-49=0$: $x^2=49$, $x=\\pm7$.', '$3x^2=27$: $x^2=9$, $x=\\pm3$.', '$x^2+4x=0$: $x(x+4)=0$, $x=0$ ou $x=-4$.',
  '$5x^2=20x$: $5x(x-4)=0$, $x=0$ ou $x=4$.', '$x^2+9=0$: sem soluções reais.', 'Quadrado de 169 cm²: $l=\\sqrt{169}=13$ cm.'],
 "Resolve connosco: **$2x^2-18=0$.**\n\n1) Isola $x^2$: $2x^2=18$, logo $x^2=9$.\n\n2) Raiz: $x=3$ ou $x=-3$.\n\n3) Verifica: $2\\cdot9-18=0$ ✓ para ambas.\n\n4) Se fosse o lado de um quadrado, só serviria $x=3$.",
 '**Desafio.** Um retângulo tem um lado o triplo do outro e 108 cm² de área. Escreve a equação $3x^2=108$, resolve e diz as dimensões. Porque só uma solução serve?',
 ['reconhecer completa e incompleta', 'resolver ax²+c=0 e discutir o número de soluções', 'resolver ax²+bx=0 por evidência', 'não perder a solução x=0', 'escolher soluções com sentido geométrico'], ex)
write(2, 19, A)

# ---------- E7: completas: discriminante e fórmula resolvente ----------
C = 'equacoes.resolvente'; ex = []
def delta(a,b,c): return b*b-4*a*c
ex += [num(1, C, "Calcula o discriminante de $x^2-5x+6=0$.", delta(1,-5,6), "Δ = (−5)² − 4·1·6 = 25 − 24 = 1.", ["Δ = b² − 4ac."]),
       num(1, C, "Calcula o discriminante de $x^2+2x-8=0$.", delta(1,2,-8), "Δ = 4 + 32 = 36.", ["a=1, b=2, c=−8."]),
       num(1, C, "Quantas soluções reais tem $x^2+x+1=0$? (Calcula Δ.)", 0, "Δ = 1 − 4 = −3 < 0: nenhuma solução real.", ["Δ < 0."])]
ex += [num(2, C, "Qual é a maior solução de $x^2-5x+6=0$?", 3, "x = (5 ± 1)/2 → 3 ou 2.", ["Δ = 1."]),
       num(2, C, "Qual é a menor solução de $x^2+2x-8=0$?", -4, "x = (−2 ± 6)/2 → 2 ou −4.", ["Δ = 36."]),
       num(2, C, "Qual é a solução única de $x^2-6x+9=0$?", 3, "Δ = 36 − 36 = 0; x = 6/2 = 3 (solução dupla).", ["Δ = 0."]),
       num(2, C, "Qual é a maior solução de $x^2-10x+21=0$?", 7, "Δ = 100 − 84 = 16; x = (10 ± 4)/2 → 7 ou 3.", ["Δ = 16."])]
ex += [num(3, C, "Qual é a maior solução de $2x^2-7x+3=0$?", 3, "Δ = 49 − 24 = 25; x = (7 ± 5)/4 → 3 ou 1/2.", ["a=2, b=−7, c=3.", "Δ = 25."]),
       num(3, C, "Qual é a maior solução de $3x^2-2x-1=0$?", 1, "Δ = 4 + 12 = 16; x = (2 ± 4)/6 → 1 ou −1/3.", ["Δ = 16."]),
       tf(2, C, "Se $\\Delta>0$ a equação tem duas soluções reais distintas.", True, "Δ > 0: duas soluções; Δ = 0: uma (dupla); Δ < 0: nenhuma real.", ["Sinal de Δ."]),
       mc(3, C, "Qual é a fórmula resolvente da equação $ax^2+bx+c=0$?", ["$x=\\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}$", "$x=\\dfrac{b\\pm\\sqrt{b^2-4ac}}{2a}$", "$x=\\dfrac{-b\\pm\\sqrt{b^2+4ac}}{2a}$", "$x=\\dfrac{-b\\pm\\sqrt{b^2-4ac}}{a}$"], 0, "É a fórmula resolvente, com −b e 2a no denominador.", ["Cuidado com os sinais."])]
for f,x in [(lambda x:x*x-5*x+6,3),(lambda x:x*x+2*x-8,-4),(lambda x:x*x-10*x+21,7),(lambda x:2*x*x-7*x+3,3),(lambda x:3*x*x-2*x-1,1)]: chk(f,x)
A = std(SUB, 'Equações do 2.º grau', 'equacoes-2-grau', 'Equações do 2.º grau completas: discriminante e fórmula resolvente', 'equacoes-2-grau-completas-resolvente',
 'Resolve equações completas do 2.º grau com o discriminante e a fórmula resolvente.', 35,
 'calcular o discriminante, discutir o número de soluções e aplicar a fórmula resolvente.', 'equações incompletas do 2.º grau, raízes quadradas e regra dos sinais.',
 'Quando a equação tem $x^2$, $x$ e termo independente, a evidência já não chega. A fórmula resolvente resolve todas as equações do 2.º grau.',
 "Para $ax^2+bx+c=0$ ($a\\ne0$):\n\n**1) Escreve na forma geral** e identifica $a$, $b$ e $c$ **com sinais**.\n\n**2) Calcula o discriminante** $\\Delta=b^2-4ac$.\n\n**3) Discute:**\n- $\\Delta>0$: **duas** soluções reais distintas;\n- $\\Delta=0$: **uma** solução (dupla);\n- $\\Delta<0$: **nenhuma** solução real.\n\n**4) Fórmula resolvente:** $x=\\dfrac{-b\\pm\\sqrt{\\Delta}}{2a}$.\n\nExemplo: $x^2-5x+6=0$. $a=1$, $b=-5$, $c=6$. $\\Delta=25-24=1$. $x=\\frac{5\\pm1}{2}$, logo $x=3$ ou $x=2$.\n\nExemplo com $a\\neq1$: $2x^2-7x+3=0$. $\\Delta=49-24=25$. $x=\\frac{7\\pm5}{4}$: $x=3$ ou $x=\\frac{1}{2}$.\n\nExemplo com $\\Delta=0$: $x^2-6x+9=0$. $\\Delta=0$, $x=\\frac{6}{2}=3$.\n\nExemplo com $\\Delta<0$: $x^2+x+1=0$. $\\Delta=-3$: sem soluções reais.\n\n**Verificação:** substitui as soluções, ou usa soma e produto das raízes (próxima aula).\n\n**Cuidados:** $-b$ com $b$ negativo fica positivo; $b^2$ é sempre positivo (por exemplo $(-5)^2=25$); o denominador é $2a$ (dois vezes $a$, não só $a$); a raiz tem **todo** o $\\Delta$.\n\n**Erros comuns:** esquecer o sinal de $b$; calcular $-b^2$ em vez de $(-b)^2$; dividir só por $a$; esquecer-se de escrever na forma geral antes.",
 'O **discriminante** é $\\Delta=b^2-4ac$. A **fórmula resolvente** dá $x=\\dfrac{-b\\pm\\sqrt{\\Delta}}{2a}$, válida quando $\\Delta\\ge0$.',
 '$$\\Delta=b^2-4ac\\qquad x=\\frac{-b\\pm\\sqrt{\\Delta}}{2a}\\qquad\\Delta>0:\\ 2\\text{ sol.};\\ \\Delta=0:\\ 1\\text{ sol.};\\ \\Delta<0:\\ \\text{nenhuma}$$',
 ['$x^2-5x+6=0$: $\\Delta=1$; $x=\\frac{5\\pm1}{2}$: $3$ e $2$.', '$x^2+2x-8=0$: $\\Delta=36$; $x=\\frac{-2\\pm6}{2}$: $2$ e $-4$.',
  '$2x^2-7x+3=0$: $\\Delta=25$; $x=\\frac{7\\pm5}{4}$: $3$ e $\\frac{1}{2}$.', '$x^2-6x+9=0$: $\\Delta=0$; $x=3$.',
  '$x^2+x+1=0$: $\\Delta=-3<0$: sem soluções reais.', '$3x^2-2x-1=0$: $\\Delta=16$; $x=\\frac{2\\pm4}{6}$: $1$ e $-\\frac{1}{3}$.'],
 "Resolve connosco: **$x^2-10x+21=0$.**\n\n1) $a=1$, $b=-10$, $c=21$.\n\n2) $\\Delta=(-10)^2-4\\cdot1\\cdot21=100-84=16$.\n\n3) $x=\\frac{10\\pm4}{2}$: $x=7$ ou $x=3$.\n\n4) Verifica: $49-70+21=0$ ✓ e $9-30+21=0$ ✓.",
 '**Desafio.** Para que valores de $k$ a equação $x^2-4x+k=0$ tem duas soluções? Uma? Nenhuma? (Impõe condições a $\\Delta=16-4k$.)',
 ['escrever na forma geral e identificar a, b, c', 'calcular o discriminante', 'discutir o número de soluções', 'aplicar a fórmula resolvente', 'verificar as soluções'], ex)
write(2, 20, A)

# ---------- E8: soma e produto das raízes ----------
C = 'equacoes.soma_produto'; ex = []
ex += [num(1, C, "Qual é a soma das raízes de $x^2-7x+10=0$?", 7, "S = −b/a = 7.", ["S = −b/a."]),
       num(1, C, "Qual é o produto das raízes de $x^2-7x+10=0$?", 10, "P = c/a = 10.", ["P = c/a."]),
       num(1, C, "As raízes são 3 e 5. Qual é a soma?", 8, "3 + 5 = 8.", ["Soma."])]
ex += [num(2, C, "Qual é o produto das raízes de $2x^2-6x+4=0$?", 2, "P = c/a = 4/2 = 2.", ["a = 2, c = 4."]),
       num(2, C, "Uma raiz de $x^2-5x+k=0$ é 2. Quanto vale $k$?", 6, "4 − 10 + k = 0 → k = 6 (a outra raiz é 3).", ["Substitui x = 2."]),
       num(2, C, "Dois números têm soma 12 e produto 35. Qual é o maior?", 7, "São raízes de x² − 12x + 35 = 0: 5 e 7.", ["S = 12, P = 35.", "Procura dois números."]),
       num(2, C, "Uma raiz de $x^2-9x+20=0$ é 4. Qual é a outra?", 5, "Soma 9 → a outra é 9 − 4 = 5.", ["Usa a soma."])]
ex += [num(3, C, "Um retângulo tem perímetro 30 m e área 56 m². Qual é o maior lado, em m?", 8, "Semiperímetro 15 e área 56: lados raízes de x² − 15x + 56 = 0 → 7 e 8.", ["Soma 15, produto 56."]),
       num(3, C, "Constrói a equação $x^2+bx+c=0$ com raízes $-2$ e $6$. Quanto vale $c$?", -12, "P = (−2)(6) = −12; S = 4 → x² − 4x − 12 = 0. c = −12.", ["P = c."]),
       tf(2, C, "Na equação $ax^2+bx+c=0$ ($a\\ne0$, $\\Delta\\ge0$) a soma das raízes é $-\\frac{b}{a}$.", True, "É a relação de Vieta: S = −b/a e P = c/a.", ["Relações de Vieta."]),
       mc(3, C, "A equação com raízes 4 e −1 é:", ["$x^2-3x-4=0$", "$x^2+3x-4=0$", "$x^2-3x+4=0$", "$x^2+3x+4=0$"], 0, "S = 3, P = −4: x² − Sx + P = x² − 3x − 4.", ["x² − Sx + P = 0."])]
for f,x in [(lambda x:x*x-5*x+6,2),(lambda x:x*x-9*x+20,4)]: chk(f,x)
A = std(SUB, 'Equações do 2.º grau', 'equacoes-2-grau', 'Relação entre os coeficientes e as raízes: soma e produto', 'equacoes-2-grau-soma-produto-raizes',
 'Usa a soma e o produto das raízes para resolver, verificar e construir equações do 2.º grau.', 30,
 'relacionar coeficientes e raízes, usar soma e produto para verificar soluções e construir equações do 2.º grau.', 'fórmula resolvente e equações do 2.º grau.',
 'Se souberes que dois números têm soma 12 e produto 35, descobres-os sem fórmula nenhuma: pensas em 5 e 7. Esta ideia tem uma forma geral muito poderosa.',
 "Se $x_1$ e $x_2$ são as raízes de $ax^2+bx+c=0$ ($a\\ne0$, $\\Delta\\ge0$), então:\n\n$$S=x_1+x_2=-\\frac{b}{a}\\qquad P=x_1\\times x_2=\\frac{c}{a}$$\n\nSão as **relações de Vieta** (ou entre coeficientes e raízes). Porquê? Se as raízes são $x_1$ e $x_2$, a equação (com $a=1$) escreve-se $(x-x_1)(x-x_2)=0$, ou seja, $x^2-(x_1+x_2)x+x_1x_2=0$.\n\n**Verificar soluções:** em $x^2-5x+6=0$, as raízes 2 e 3 têm soma 5 e produto 6 ✓.\n\n**Encontrar a outra raiz:** se sabes uma raiz, usa a soma ou o produto. Em $x^2-9x+20=0$ com raiz 4, a outra é $9-4=5$.\n\n**Construir uma equação** a partir das raízes: $x^2-Sx+P=0$. Raízes $4$ e $-1$: $S=3$, $P=-4$, equação $x^2-3x-4=0$.\n\n**Resolver por «pensar em dois números»:** se $a=1$, procura dois números de soma $-b$ e produto $c$. Em $x^2-12x+35=0$: soma 12, produto 35, logo 5 e 7.\n\n**Problemas:** perímetro 30 m e área 56 m². Semiperímetro $=15$ é a soma dos lados e 56 é o produto: lados 7 e 8.\n\n**Sinais úteis:** se $P>0$ as raízes têm o mesmo sinal; se $P<0$ têm sinais contrários.\n\n**Erros comuns:** trocar o sinal da soma ($S=\\frac{b}{a}$ ✗); aplicar a relações quando $\\Delta<0$; esquecer de dividir por $a$.",
 'As **relações de Vieta**: $x_1+x_2=-\\frac{b}{a}$ e $x_1x_2=\\frac{c}{a}$. A equação com raízes $x_1$ e $x_2$ é $x^2-Sx+P=0$.',
 '$$S=-\\frac{b}{a}\\qquad P=\\frac{c}{a}\\qquad x^2-Sx+P=0$$\n\n$a,b,c$: coeficientes ($a\\ne0$); $S$: soma das raízes; $P$: produto das raízes.',
 ['$x^2-7x+10=0$: $S=7$, $P=10$; raízes 2 e 5.', '$2x^2-6x+4=0$: $S=3$, $P=2$; raízes 1 e 2.',
  'Raiz 2 em $x^2-5x+k=0$: $4-10+k=0$, $k=6$ (outra raiz: 3).', 'Soma 12 e produto 35: raízes de $x^2-12x+35=0$, 5 e 7.',
  'Raízes 4 e $-1$: $S=3$, $P=-4$; $x^2-3x-4=0$.', 'Retângulo de perímetro 30 e área 56: lados 7 e 8.'],
 "Resolve connosco: **uma raiz de $x^2-9x+20=0$ é 4. Qual é a outra e confirma com o produto?**\n\n1) $S=9$, logo a outra raiz é $9-4=5$.\n\n2) Confirma com o produto: $P=\\frac{20}{1}=20$ e $4\\times5=20$ ✓.\n\n3) Equação reconstruída: $x^2-9x+20=0$ ✓.",
 '**Desafio.** Sem resolver, calcula $x_1^2+x_2^2$ para as raízes de $x^2-5x+6=0$ usando $x_1^2+x_2^2=S^2-2P$. Confirma com as raízes 2 e 3.',
 ['calcular soma e produto a partir dos coeficientes', 'encontrar a outra raiz', 'construir a equação a partir das raízes', 'resolver «dois números» por soma e produto', 'aplicar a problemas com retângulos'], ex)
write(2, 21, A)
print('M5b ok')

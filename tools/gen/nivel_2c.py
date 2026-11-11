"""Nível 2 — Módulo 5: Equações (aulas novas 14–20)."""
from n2h import *
SUB = 'equacoes'

def chk(f, x):  # confirma que x anula f
    assert f(F(x)) == 0, (f, x)

# ---------- E1: igualdade, equação, princípios de equivalência ----------
C = 'equacoes.conceito'; ex = []
ex += [tf(1, C, "A igualdade $3x+2=11$ é uma equação com incógnita $x$.", True, "Uma equação é uma igualdade com pelo menos uma incógnita.", ["Há um x desconhecido."]),
       num(1, C, "Qual é a solução de $x+9=21$?", 12, "Subtrai 9 aos dois membros: x = 21 − 9 = 12.", ["Operação inversa da soma."]),
       num(1, C, "Qual é a solução de $5x=45$?", 9, "Divide os dois membros por 5: x = 9.", ["Operação inversa do produto."])]
ex += [tf(2, C, "O número 4 é solução da equação $2x-3=5$.", True, "2·4 − 3 = 5 ✓.", ["Substitui x por 4."]),
       tf(2, C, "As equações $x+3=7$ e $2x=8$ são equivalentes.", True, "Ambas têm como única solução x = 4.", ["Resolve as duas."]),
       num(2, C, "Resolve $3x-7=14$.", 7, "3x = 21, logo x = 7. Verificação: 3·7 − 7 = 14 ✓.", ["Soma 7: 3x = 21.", "Divide por 3."]),
       num(2, C, "Resolve $4x+6=2x+18$.", 6, "4x − 2x = 18 − 6 → 2x = 12 → x = 6. Verificação: 30 = 30 ✓.", ["Passa os x para a esquerda.", "Resolve."])]
ex += [num(3, C, "Resolve $9x-4=5x+20$.", 6, "9x − 5x = 20 + 4 → 4x = 24 → x = 6. Verificação: 50 = 50 ✓.", ["Agrupa os termos com x.", "x = 6."]),
       num(3, C, "Resolve $10-3x=x-6$.", 4, "10 + 6 = x + 3x → 16 = 4x → x = 4. Verificação: −2 = −2 ✓.", ["Passa 3x para a direita e 6 para a esquerda."]),
       mc(2, C, "O princípio da adição diz que, numa equação, podemos:", ["somar ou subtrair o mesmo número aos dois membros", "somar números só ao primeiro membro", "dividir por zero", "trocar o sinal de um só membro"], 0, "Somar ou subtrair o mesmo valor aos dois membros mantém a igualdade.", ["Mesmo número, nos dois lados."]),
       tf(3, C, "Dividir os dois membros de uma equação por $x$ é sempre permitido.", False, "Se x = 0 seria dividir por zero, e podes perder soluções. Só dividimos por números diferentes de zero.", ["x pode ser 0."])]
for f, x in [(lambda x: 3*x-7-14, 7), (lambda x: 4*x+6-(2*x+18), 6), (lambda x: 9*x-4-(5*x+20), 6), (lambda x: 10-3*x-(x-6), 4)]: chk(f, x)
A = std(SUB, 'Conceitos', 'conceitos-equacoes', 'Igualdades, equações e princípios de equivalência', 'equacoes-conceito-principios-equivalencia',
 'Compreende o que é uma equação, os seus membros e solução, e usa os princípios de equivalência.', 25,
 'distinguir igualdade e equação, identificar incógnita, membros e solução e aplicar os princípios de equivalência.', 'operações com inteiros e racionais.',
 'Uma balança em equilíbrio é a melhor imagem de uma equação: o que fazes de um lado tens de fazer do outro para manter o equilíbrio.',
 "Uma **igualdade** liga duas expressões com o sinal $=$: $2+3=5$ (verdadeira) ou $2+3=6$ (falsa). Uma **equação** é uma igualdade com pelo menos uma **incógnita** (valor desconhecido, normalmente $x$). Em $3x+2=11$, $3x+2$ é o **1.º membro** e $11$ é o **2.º membro**. A **solução** (ou raiz) é o valor que torna a igualdade verdadeira: $x=3$, porque $3\\times3+2=11$.\n\n**Resolver** uma equação é encontrar todas as suas soluções. Para verificar, substituímos a solução na equação original.\n\n**Equações equivalentes** têm as mesmas soluções: $x+3=7$ e $2x=8$ têm ambas $x=4$.\n\n**Princípio da adição:** somar (ou subtrair) o mesmo número aos dois membros dá uma equação equivalente. É por isso que «passamos» termos para o outro lado trocando o sinal: $x+9=21\\Rightarrow x=21-9$.\n\n**Princípio da multiplicação:** multiplicar (ou dividir) os dois membros pelo mesmo número **diferente de zero** dá uma equação equivalente. $5x=45\\Rightarrow x=9$.\n\n**Estratégia:** (1) juntar os termos com $x$ de um lado e os números do outro; (2) simplificar; (3) dividir pelo coeficiente de $x$; (4) verificar.\n\nExemplo: $4x+6=2x+18\\Rightarrow4x-2x=18-6\\Rightarrow2x=12\\Rightarrow x=6$. Verificação: $4\\times6+6=30$ e $2\\times6+18=30$ ✓.\n\n**Tipos de resultado:** pode haver **uma solução** (normal), **nenhuma** (equação impossível, como $x+1=x+2$) ou **infinitas** (equação possível indeterminada, como $x+1=x+1$).\n\n**Erros comuns:** mudar o sinal só de um termo; fazer uma operação num só membro; dividir por $x$; não verificar.",
 'Uma **equação** é uma igualdade com incógnita. **Solução** é o valor da incógnita que a verifica. Duas equações são **equivalentes** se têm as mesmas soluções.',
 '$$a=b\\iff a+c=b+c\\qquad a=b\\iff ac=bc\\ (c\\neq0)$$\n\nEquação do 1.º grau: $ax+b=0\\Rightarrow x=-\\dfrac{b}{a}$ ($a\\ne0$).',
 ['$x+9=21$: $x=21-9=12$.', '$5x=45$: $x=45\\div5=9$.', '$3x-7=14$: $3x=21$, $x=7$ (verificação: $21-7=14$ ✓).',
  '$4x+6=2x+18$: $2x=12$, $x=6$.', '$9x-4=5x+20$: $4x=24$, $x=6$.', '$10-3x=x-6$: $16=4x$, $x=4$.'],
 "Resolve connosco: **$7x-5=3x+11$.**\n\n1) Passa os termos com $x$ para a esquerda e os números para a direita: $7x-3x=11+5$.\n\n2) Simplifica: $4x=16$.\n\n3) Divide por 4: $x=4$.\n\n4) Verifica: $7\\times4-5=23$ e $3\\times4+11=23$ ✓.",
 '**Desafio.** Cria uma equação com solução $x=5$ que tenha $x$ nos dois membros. Depois cria uma sem solução e outra com infinitas soluções e explica porquê.',
 ['distinguir igualdade e equação', 'nomear membros, incógnita e solução', 'aplicar os dois princípios de equivalência', 'verificar soluções', 'reconhecer equações impossíveis e indeterminadas'], ex)
write(2, 14, A)

# ---------- E2: parênteses ----------
C = 'equacoes.parenteses'; ex = []
def lin(p1,q1,p2,q2): return F(q2-q1, p1-p2)
ex += [num(1, C, "Resolve $2(x+3)=14$.", 4, "2x + 6 = 14 → 2x = 8 → x = 4.", ["Propriedade distributiva.", "x = 4."]),
       num(1, C, "Resolve $3(x-2)=15$.", 7, "3x − 6 = 15 → 3x = 21 → x = 7.", ["Distribui o 3."]),
       num(1, C, "Resolve $5(x+1)=30$.", 5, "5x + 5 = 30 → x = 5.", ["Distribui."])]
ex += [num(2, C, "Resolve $2(x+4)=x+15$.", 7, "2x + 8 = x + 15 → x = 7. Verificação: 22 = 22 ✓.", ["Distribui o 2.", "Agrupa x."]),
       num(2, C, "Resolve $3(2x-1)=2(x+5)$.", F(13,4), "6x − 3 = 2x + 10 → 4x = 13 → x = 13/4. Verificação: 3(13/2 − 1) = 33/2 e 2(13/4 + 5) = 33/2 ✓.", ["Distribui os dois lados.", "4x = 13."], ["3,25"]),
       num(2, C, "Resolve $4-(x-3)=2x-5$.", 4, "4 − x + 3 = 2x − 5 → 12 = 3x → x = 4 (o sinal − troca os sinais dentro do parêntese).", ["−(x − 3) = −x + 3.", "7 − x = 2x − 5."]),
       num(2, C, "Resolve $5x-2(x-3)=18$.", 4, "5x − 2x + 6 = 18 → 3x = 12 → x = 4.", ["−2(x − 3) = −2x + 6."])]
ex += [num(3, C, "Resolve $2[x-(3-x)]=10$.", 4, "Dentro: x − 3 + x = 2x − 3; 2(2x − 3) = 4x − 6 = 10 → x = 4.", ["Resolve primeiro o parêntese interior.", "4x − 6 = 10."]),
       num(3, C, "Resolve $3(x+2)-2(x-1)=4(x-2)-3$.", F(19,3), "3x + 6 − 2x + 2 = 4x − 8 − 3 → x + 8 = 4x − 11 → 19 = 3x → x = 19/3.", ["Distribui tudo.", "Agrupa."], ["6,33"]),
       tf(2, C, "$-(x-5)$ é igual a $-x-5$.", False, "O sinal − troca os dois sinais: −(x − 5) = −x + 5.", ["Distribui o −1."]),
       mc(3, C, "Qual é o primeiro passo para resolver $3(x+2)=x-4$?", ["Aplicar a propriedade distributiva: $3x+6=x-4$", "Dividir os dois membros por 3 sem distribuir os termos", "Somar 2 a x", "Cortar os parênteses"], 0, "Distribuímos o 3 por todos os termos do parêntese: 3x + 6.", ["Elimina primeiro os parênteses."])]
for f,x in [(lambda x:2*(x+4)-(x+15),7),(lambda x:3*(2*x-1)-2*(x+5),F(13,4)),(lambda x:4-(x-3)-(2*x-5),4),(lambda x:5*x-2*(x-3)-18,4),(lambda x:2*(x-(3-x))-10,4),(lambda x:3*(x+2)-2*(x-1)-(4*(x-2)-3),F(19,3))]: chk(f,x)
A = std(SUB, 'Equações do 1.º grau', 'equacoes-1-grau', 'Equações do 1.º grau com parênteses', 'equacoes-1-grau-parenteses',
 'Resolve equações do 1.º grau com parênteses, aplicando a propriedade distributiva e a regra dos sinais.', 30,
 'eliminar parênteses (distributiva e regra dos sinais) e resolver equações do 1.º grau com parênteses.', 'equações simples, regra dos sinais e distributiva.',
 'Quando há parênteses, a primeira ideia é sempre a mesma: eliminá-los com cuidado, principalmente quando há um sinal menos à frente.',
 "**Propriedade distributiva:** $a(b+c)=ab+ac$ e $a(b-c)=ab-ac$. Cada termo dentro do parêntese é multiplicado por $a$.\n\n**Sinal menos à frente:** $-(b+c)=-b-c$ e $-(b-c)=-b+c$. Equivale a multiplicar por $-1$: **todos** os sinais trocam. Este é o erro mais frequente.\n\n**Parênteses encaixados:** resolve de dentro para fora. $2[x-(3-x)]$: primeiro $x-(3-x)=x-3+x=2x-3$; depois $2(2x-3)=4x-6$.\n\n**Método:** (1) elimina os parênteses; (2) reduz os termos semelhantes em cada membro; (3) agrupa os termos com $x$ de um lado e os números do outro; (4) divide pelo coeficiente de $x$; (5) verifica na equação original.\n\nExemplo: $3(2x-1)=2(x+5)$. Eliminar: $6x-3=2x+10$. Agrupar: $6x-2x=10+3$. Simplificar: $4x=13$. Logo $x=\\frac{13}{4}$.\n\n**Resultado fracionário:** pode acontecer e é normal. Verifica substituindo.\n\n**Erros comuns:** esquecer de multiplicar o segundo termo do parêntese ($2(x+4)=2x+4$ ✗); trocar o sinal de um só termo depois de um menos; passar termos sem trocar o sinal.",
 '**Propriedade distributiva** da multiplicação em relação à adição e à subtração, e **regra de eliminação de parênteses** precedidos de $-$.',
 '$$a(b\\pm c)=ab\\pm ac\\qquad-(b+c)=-b-c\\qquad-(b-c)=-b+c$$\n\n$a,b,c$ são números (ou expressões). O sinal $-$ antes do parêntese multiplica cada termo por $-1$. Depois de eliminar parênteses, resolve como equação do 1.º grau: agrupa, reduz e divide pelo coeficiente de $x$.',
 ['$2(x+3)=14$: $2x+6=14$, $2x=8$, $x=4$.', '$2(x+4)=x+15$: $2x+8=x+15$, $x=7$.',
  '$3(2x-1)=2(x+5)$: $6x-3=2x+10$, $4x=13$, $x=\\frac{13}{4}$.', '$4-(x-3)=2x-5$: $7-x=2x-5$, $12=3x$, $x=4$.',
  '$5x-2(x-3)=18$: $3x+6=18$, $x=4$.', '$2[x-(3-x)]=10$: $2(2x-3)=10$, $4x-6=10$, $x=4$.'],
 "Resolve connosco: **$3(x+2)-2(x-1)=4(x-2)-3$.**\n\n1) Distribui: $3x+6-2x+2=4x-8-3$.\n\n2) Reduz: $x+8=4x-11$.\n\n3) Agrupa: $8+11=4x-x$, logo $19=3x$.\n\n4) $x=\\frac{19}{3}$. Verifica: lado esquerdo $3\\cdot\\frac{25}{3}-2\\cdot\\frac{16}{3}=25-\\frac{32}{3}=\\frac{43}{3}$ e lado direito $4\\cdot\\frac{13}{3}-3=\\frac{43}{3}$ ✓.",
 '**Desafio.** Resolve $2(x-3)-3(2x+1)=-4(x+2)+5$. O que acontece? Explica o resultado (impossível ou indeterminada?).',
 ['aplicar a distributiva corretamente', 'trocar todos os sinais depois de um menos', 'resolver parênteses encaixados', 'agrupar e reduzir termos semelhantes', 'verificar a solução'], ex)
write(2, 15, A)

# ---------- E3: frações e denominadores ----------
C = 'equacoes.fracoes'; ex = []
ex += [num(1, C, "Resolve $\\dfrac{x}{3}=5$.", 15, "Multiplica os dois membros por 3: x = 15.", ["Operação inversa de dividir por 3."]),
       num(1, C, "Resolve $\\dfrac{x}{2}+1=6$.", 10, "x/2 = 5 → x = 10.", ["Subtrai 1.", "Multiplica por 2."]),
       num(1, C, "Resolve $\\dfrac{2x}{5}=4$.", 10, "2x = 20 → x = 10.", ["Multiplica por 5."])]
ex += [num(2, C, "Resolve $\\dfrac{x}{2}+\\dfrac{x}{3}=10$.", 12, "mmc(2, 3) = 6: 3x + 2x = 60 → 5x = 60 → x = 12.", ["Multiplica tudo por 6.", "5x = 60."]),
       num(2, C, "Resolve $\\dfrac{x+1}{2}=\\dfrac{x-1}{3}+1$.", 1, "Multiplica por 6: 3(x+1) = 2(x−1) + 6 → 3x + 3 = 2x + 4 → x = 1.", ["mmc = 6.", "Distribui."]),
       num(2, C, "Resolve $\\dfrac{3x}{4}-2=\\dfrac{x}{2}+1$.", 12, "Multiplica por 4: 3x − 8 = 2x + 4 → x = 12.", ["mmc = 4.", "x = 12."]),
       num(2, C, "Resolve $\\dfrac{x}{4}=\\dfrac{x+3}{6}$.", 6, "Produto cruzado: 6x = 4(x + 3) → 2x = 12 → x = 6.", ["Ou multiplica por 12."])]
ex += [num(3, C, "Resolve $\\dfrac{2x-1}{3}-\\dfrac{x+2}{4}=1$.", F(22,5), "Multiplica por 12: 4(2x−1) − 3(x+2) = 12 → 8x − 4 − 3x − 6 = 12 → 5x = 22 → x = 22/5.", ["mmc = 12.", "Cuidado com o − antes do parêntese."], ["4,4"]),
       num(3, C, "Resolve $x-\\dfrac{x-2}{3}=\\dfrac{x}{2}+1$.", 6, "Multiplica por 6: 6x − 2(x−2) = 3x + 6 → 4x + 4 = 3x + 6 → x = 2... verifica: lado esq. 2 − 0 = 2; lado dir. 1 + 1 = 2 ✓.", ["mmc = 6.", "Distribui o −2."]) if False else
       num(3, C, "Resolve $x-\\dfrac{x-2}{3}=\\dfrac{x}{2}+1$.", 2, "Multiplica por 6: 6x − 2(x−2) = 3x + 6 → 4x + 4 = 3x + 6 → x = 2. Verificação: 2 − 0 = 2 e 1 + 1 = 2 ✓.", ["mmc = 6.", "Distribui o −2."]),
       tf(2, C, "Para eliminar denominadores, multiplicamos todos os termos da equação (dos dois membros) pelo mmc dos denominadores.", True, "Multiplicar os dois membros pelo mesmo número ≠ 0 mantém a equação equivalente, e fazemo-lo a todos os termos.", ["Todos os termos."]),
       mc(3, C, "Numa equação com denominadores 2, 3 e 4, por que número é mais prático multiplicar tudo?", ["12", "24", "9", "6"], 0, "mmc(2, 3, 4) = 12.", ["Menor múltiplo comum."])]
for f,x in [(lambda x:x/2+x/3-10,12),(lambda x:(x+1)/2-((x-1)/3+1),1),(lambda x:3*x/4-2-(x/2+1),12),(lambda x:x/4-(x+3)/6,6),(lambda x:(2*x-1)/3-(x+2)/4-1,F(22,5)),(lambda x:x-(x-2)/3-(x/2+1),2)]: chk(f,x)
A = std(SUB, 'Equações do 1.º grau', 'equacoes-1-grau', 'Equações com frações e denominadores', 'equacoes-fracoes-denominadores',
 'Resolve equações com denominadores eliminando-os com o mmc.', 30,
 'eliminar denominadores com o mmc, resolver equações com frações e verificar as soluções.', 'frações, mmc, equações com parênteses.',
 'Equações com frações assustam muita gente, mas há um truque simples: multiplicar tudo pelo mmc dos denominadores faz os denominadores desaparecerem.',
 "**Ideia central:** multiplicar os **dois membros** (todos os termos) pelo **mmc dos denominadores**. O resultado é uma equação equivalente sem denominadores.\n\nExemplo: $\\frac{x}{2}+\\frac{x}{3}=10$. mmc$(2,3)=6$. Multiplicamos tudo por 6: $3x+2x=60$, logo $5x=60$ e $x=12$.\n\n**Passos:** (1) calcula o mmc; (2) multiplica **cada termo** pelo mmc (incluindo os inteiros); (3) simplifica; (4) elimina parênteses; (5) agrupa e resolve; (6) verifica.\n\n**Atenção com numeradores com vários termos:** $\\frac{x+1}{2}$ torna-se $3(x+1)$ depois de multiplicar por 6 (mmc de 2 e 3), pois $\\frac{6}{2}=3$. Mantém o parêntese!\n\n**Sinal menos antes de uma fração:** $-\\frac{x+2}{4}$ torna-se $-3(x+2)$ (multiplicando por 12) e depois $-3x-6$. Troca todos os sinais.\n\n**Produto cruzado:** se a equação é só uma fração igual a outra, $\\frac{x}{4}=\\frac{x+3}{6}$, usamos $6x=4(x+3)$.\n\n**Verificação:** substitui a solução e calcula os dois membros com frações.\n\n**Erros comuns:** multiplicar só alguns termos pelo mmc; esquecer o termo sem fração; não manter o parêntese no numerador.",
 '**Eliminação de denominadores:** multiplicar todos os termos pelo mmc dos denominadores dá uma equação equivalente, desde que o mmc ≠ 0.',
 '$$\\frac{A}{d_1}+\\frac{B}{d_2}=C\\ \\Longrightarrow\\ \\frac{m}{d_1}A+\\frac{m}{d_2}B=mC,\\qquad m=\\text{mmc}(d_1,d_2)$$',
 ['$\\frac{x}{3}=5$: $x=15$.', '$\\frac{x}{2}+\\frac{x}{3}=10$: $\\times6$: $3x+2x=60$, $x=12$.',
  '$\\frac{x+1}{2}=\\frac{x-1}{3}+1$: $\\times6$: $3x+3=2x-2+6$, $x=1$.', '$\\frac{3x}{4}-2=\\frac{x}{2}+1$: $\\times4$: $3x-8=2x+4$, $x=12$.',
  '$\\frac{x}{4}=\\frac{x+3}{6}$: $6x=4x+12$, $x=6$.', '$\\frac{2x-1}{3}-\\frac{x+2}{4}=1$: $\\times12$: $8x-4-3x-6=12$, $x=\\frac{22}{5}$.'],
 "Resolve connosco: **$\\frac{x-1}{2}-\\frac{x}{3}=\\frac{1}{6}$.**\n\n1) mmc$(2,3,6)=6$.\n\n2) $3(x-1)-2x=1$.\n\n3) $3x-3-2x=1$, logo $x-3=1$.\n\n4) $x=4$. Verifica: $\\frac{3}{2}-\\frac{4}{3}=\\frac{9-8}{6}=\\frac{1}{6}$ ✓.",
 '**Desafio.** Resolve $\\frac{x}{2}-\\frac{x}{3}=\\frac{x}{6}$. O que notas no resultado? Explica porquê.',
 ['calcular o mmc dos denominadores', 'multiplicar todos os termos pelo mmc', 'manter parênteses nos numeradores', 'tratar sinais antes de frações', 'verificar com frações'], ex)
write(2, 16, A)

# ---------- E4: equações literais ----------
C = 'equacoes.literais'; ex = []
ex += [num(1, C, "Da fórmula $v=\\dfrac{d}{t}$, isola $d$: $d=v\\,t$. Calcula $d$ quando $v=80$ e $t=3$.", 240, "d = 80 × 3 = 240.", ["Multiplica os dois membros por t."]),
       num(1, C, "Da fórmula $P=2(a+b)$ (perímetro do retângulo), calcula $b$ se $P=30$ e $a=9$.", 6, "P/2 = a + b → 15 = 9 + b → b = 6.", ["Divide por 2.", "Subtrai a."]),
       num(1, C, "Na fórmula $A=b\\times h$, calcula $h$ quando $A=48$ e $b=6$.", 8, "h = A/b = 8.", ["Divide por b."])]
ex += [num(2, C, "Da fórmula $A=\\dfrac{b\\,h}{2}$, calcula $h$ para $A=30$ e $b=10$.", 6, "2A = bh → h = 60 ÷ 10 = 6.", ["Multiplica por 2.", "Divide por b."]),
       num(2, C, "Da fórmula $F=\\dfrac{9}{5}C+32$, calcula $C$ para $F=95$.", 35, "F − 32 = 63 = 9C/5 → C = 63 × 5 ÷ 9 = 35.", ["Subtrai 32.", "Multiplica por 5/9."]),
       num(2, C, "Resolve em ordem a $x$ a equação $ax+b=c$ e calcula $x$ com $a=3$, $b=5$, $c=26$.", 7, "x = (c − b)/a = 21/3 = 7.", ["Isola x."]),
       num(2, C, "Da fórmula do perímetro da circunferência $P=2\\pi r$, determina $r$ para $P=62{,}8$ (usa $\\pi=3{,}14$).", 10, "r = P/(2π) = 62,8 ÷ 6,28 = 10.", ["2π = 6,28.", "Divide."]),
       num(3, C, "Da fórmula $S=\\dfrac{n(a_1+a_n)}{2}$ (soma de n termos de uma sequência), calcula $a_n$ para $S=120$, $n=10$ e $a_1=3$.", 21, "2S/n = a₁ + aₙ → 24 = 3 + aₙ → aₙ = 21.", ["Multiplica por 2 e divide por n."])]
ex += [num(3, C, "De $\\dfrac{1}{R}=\\dfrac{1}{R_1}+\\dfrac{1}{R_2}$, calcula $R$ para $R_1=6$ e $R_2=3$.", 2, "1/R = 1/6 + 1/3 = 1/2 → R = 2.", ["mmc 6."]),
       num(3, C, "Da fórmula $s=s_0+vt$, calcula $t$ para $s=150$, $s_0=30$ e $v=20$.", 6, "t = (s − s₀)/v = 120 ÷ 20 = 6.", ["Isola t."]),
       tf(2, C, "Resolver a fórmula $A=\\frac{bh}{2}$ em ordem a $b$ dá $b=\\frac{2A}{h}$ (com $h\\ne0$).", True, "Multiplica por 2 e divide por h.", ["Isola b."]),
       mc(3, C, "Resolvendo $y=mx+k$ em ordem a $x$ ($m\\ne0$) obtém-se:", ["$x=\\dfrac{y-k}{m}$", "$x=\\dfrac{y+k}{m}$", "$x=m(y-k)$", "$x=\\dfrac{m}{y-k}$"], 0, "Subtrai k aos dois membros e divide por m.", ["Operações inversas."])]
A = std(SUB, 'Equações literais', 'equacoes-literais', 'Equações literais e fórmulas', 'equacoes-literais-formulas',
 'Isola uma variável numa fórmula e calcula valores por substituição.', 25,
 'resolver equações literais (em ordem a uma letra), isolar variáveis em fórmulas e substituir valores.', 'equações do 1.º grau e fórmulas elementares.',
 'Em ciência e na vida usamos fórmulas: velocidade, área, temperatura. Muitas vezes queremos a fórmula «virada» de outra maneira. Isso é resolver uma equação literal.',
 "Uma **equação literal** tem **letras** com valor genérico (parâmetros) além da incógnita. **Resolver em ordem a $x$** é isolar $x$ num membro, tratando as outras letras como se fossem números.\n\nExemplo: de $v=\\frac{d}{t}$ queremos $d$. Multiplicamos os dois membros por $t$ ($t\\ne0$): $d=v\\,t$. Queremos $t$? $t=\\frac{d}{v}$ ($v\\ne0$).\n\n**Método:** usa as **operações inversas**, pela ordem inversa das operações da fórmula. Em $F=\\frac{9}{5}C+32$: primeiro subtrai 32, depois multiplica por $\\frac{5}{9}$: $C=\\frac{5}{9}(F-32)$.\n\n**Fórmulas úteis:**\n\n- Perímetro do retângulo: $P=2(a+b)$ ⇒ $b=\\frac{P}{2}-a$.\n- Área do triângulo: $A=\\frac{bh}{2}$ ⇒ $h=\\frac{2A}{b}$.\n- Posição: $s=s_0+vt$ ⇒ $t=\\frac{s-s_0}{v}$.\n- Circunferência: $P=2\\pi r$ ⇒ $r=\\frac{P}{2\\pi}$.\n\n**Cuidado:** só divides por uma letra se ela for diferente de zero. Escreve essa **condição**.\n\n**Substituição:** depois de isolar, substitui as letras conhecidas e calcula. Ou substitui primeiro e resolve a equação numérica: o resultado é o mesmo.\n\n**Erros comuns:** isolar sem respeitar a ordem das operações; esquecer de dividir **todos** os termos; ignorar as condições (divisão por zero).",
 'Uma **equação literal** é uma equação com letras além da incógnita; **resolver em ordem a $x$** é isolar $x$ usando os princípios de equivalência.',
 '$$d=vt\\quad t=\\frac{d}{v}\\quad b=\\frac{2A}{h}\\quad C=\\frac{5}{9}(F-32)\\quad x=\\frac{c-b}{a}\\ (ax+b=c,\\ a\\neq0)$$',
 ['De $v=\\frac{d}{t}$: $d=vt$; com $v=80$ e $t=3$: $d=240$.', 'De $P=2(a+b)$: $b=\\frac{P}{2}-a$; com $P=30$, $a=9$: $b=6$.',
  'De $A=\\frac{bh}{2}$: $h=\\frac{2A}{b}$; com $A=30$ e $b=10$: $h=6$.', 'De $F=\\frac{9}{5}C+32$: $C=\\frac{5}{9}(F-32)$; com $F=95$: $C=35$.',
  'De $ax+b=c$: $x=\\frac{c-b}{a}$; com $a=3,b=5,c=26$: $x=7$.', 'De $s=s_0+vt$: $t=\\frac{s-s_0}{v}$; com $s=150$, $s_0=30$, $v=20$: $t=6$.'],
 "Resolve connosco: **resolve $S=\\frac{n(a+l)}{2}$ em ordem a $l$ e calcula $l$ para $S=120$, $n=10$, $a=3$.**\n\n1) Multiplica por 2: $2S=n(a+l)$.\n\n2) Divide por $n$ ($n\\ne0$): $\\frac{2S}{n}=a+l$.\n\n3) Subtrai $a$: $l=\\frac{2S}{n}-a$.\n\n4) Substitui: $l=\\frac{240}{10}-3=21$ ✓.",
 '**Desafio.** Da fórmula da energia $E=\\frac{1}{2}mv^2$, isola $m$ e isola $v^2$. Calcula $m$ para $E=400$ e $v=4$. Escreve as condições para as divisões.',
 ['isolar uma variável numa fórmula', 'respeitar a ordem inversa das operações', 'escrever condições de existência', 'substituir valores e calcular', 'verificar o resultado'], ex)
write(2, 17, A)

# ---------- E5: problemas que conduzem a equações ----------
C = 'equacoes.problemas'; ex = []
ex += [num(1, C, "O triplo de um número, mais 5, é igual a 26. Qual é o número?", 7, "3x + 5 = 26 → x = 7.", ["Traduz: 3x + 5 = 26."]),
       num(1, C, "A soma de dois números consecutivos é 41. Qual é o menor?", 20, "x + (x+1) = 41 → 2x = 40 → x = 20.", ["Consecutivos: x e x + 1."]),
       num(1, C, "Um caderno custa o dobro de uma caneta. Juntos custam 900 Kz. Quanto custa a caneta, em Kz?", 300, "x + 2x = 900 → x = 300.", ["Caneta x, caderno 2x."])]
ex += [num(2, C, "Ana tem o triplo da idade do filho e a diferença das idades é 24 anos. Quantos anos tem o filho?", 12, "3x − x = 24 → x = 12.", ["Filho x; Ana 3x."]),
       num(2, C, "O perímetro de um retângulo é 52 cm e o comprimento excede a largura em 6 cm. Qual é a largura, em cm?", 10, "2(x + x + 6) = 52 → 4x + 12 = 52 → x = 10.", ["Largura x; comprimento x + 6."]),
       num(2, C, "Um táxi cobra 500 Kz de bandeirada mais 150 Kz por km. Quantos km se percorreram se a corrida custou 2 750 Kz?", 15, "500 + 150x = 2 750 → x = 15.", ["500 + 150x."]),
       num(2, C, "Num mercado, comprei 3 kg de feijão e 2 kg de arroz por 5 100 Kz. O arroz custa 900 Kz/kg. Quanto custa 1 kg de feijão, em Kz?", 1100, "3x + 1 800 = 5 100 → 3x = 3 300 → x = 1 100.", ["2 × 900 = 1 800."])]
ex += [num(3, C, "Dois irmãos têm juntos 66 000 Kz. Se o mais velho der 6 000 Kz ao mais novo, ficam com o mesmo valor. Quanto tem o mais velho, em Kz?", 39000, "x − 6 000 = (66 000 − x) + 6 000 → 2x = 78 000 → x = 39 000.", ["Mais velho x; mais novo 66 000 − x.", "Equilíbrio depois da transferência."]),
       num(3, C, "Dois comboios partem ao mesmo tempo de cidades distantes 360 km, um contra o outro, a 70 km/h e 50 km/h. Ao fim de quantas horas se cruzam?", 3, "70t + 50t = 360 → 120t = 360 → t = 3 h.", ["Distâncias somam 360."]),
       num(3, C, "Mistura-se água e sumo concentrado; o concentrado é 1/5 da mistura total. Em 12 L de mistura, quantos litros de água há?", F(48,5), "Concentrado = 12/5 = 2,4 L; água = 12 − 2,4 = 9,6 L.", ["Concentrado 12 ÷ 5."]) if False else
       num(3, C, "Pensei num número; adicionei-lhe 8, multipliquei o resultado por 3 e subtraí 10, obtendo 47. Qual era o número?", 11, "3(x + 8) − 10 = 47 → 3x + 24 = 57 → x = 11.", ["Inverte as operações.", "47 + 10 = 57."]),
       tf(2, C, "Em «a soma de três números consecutivos é 72», o menor é 23.", True, "x + (x+1) + (x+2) = 72 → 3x = 69 → x = 23.", ["3x + 3 = 72."]),
       mc(2, C, "Qual é a equação do problema «o dobro de um número menos 7 é igual ao número mais 5»?", ["$2x-7=x+5$", "$2(x-7)=x+5$", "$2x-7=5x$", "$x-7=2x+5$"], 0, "Dobro de x: 2x; menos 7: 2x − 7; igual a x + 5.", ["Traduz frase a frase."])]
for f,x in [(lambda x:3*x+5-26,7),(lambda x:500+150*x-2750,15),(lambda x:3*(x+8)-10-47,11)]: chk(f,x)
A = std(SUB, 'Problemas com equações', 'equacoes-problemas', 'Problemas que conduzem a equações do 1.º grau', 'equacoes-problemas-1-grau',
 'Traduz problemas em equações, resolve-as e interpreta a solução no contexto.', 35,
 'traduzir problemas para a linguagem algébrica, resolver a equação e interpretar e verificar a solução no contexto.', 'equações do 1.º grau (parênteses e frações).',
 'A maior utilidade das equações é resolver problemas. O difícil não é resolver a equação, é montá-la bem. Esta aula ensina a traduzir palavras em símbolos.',
 "**Método em 6 passos:**\n\n1) **Ler** o problema até ao fim e perceber o que se pede.\n\n2) **Escolher a incógnita** e escrever o seu significado com a unidade: «$x$ = idade do filho, em anos».\n\n3) **Exprimir** as outras grandezas em função de $x$.\n\n4) **Escrever a equação** traduzindo a frase que dá a igualdade.\n\n5) **Resolver** a equação.\n\n6) **Interpretar e verificar:** a solução tem sentido (por exemplo, idade positiva)? Satisfaz o enunciado original?\n\n**Dicionário de tradução:**\n\n- «o dobro de $x$»: $2x$; «o triplo»: $3x$; «a metade»: $\\frac{x}{2}$.\n- «$x$ mais 5»: $x+5$; «5 a mais que $x$»: $x+5$; «5 a menos que $x$»: $x-5$.\n- «números consecutivos»: $x$, $x+1$, $x+2$; «pares consecutivos»: $x$, $x+2$.\n- «a soma é 41»: $x+(41-x)$ ou duas letras com $=41$.\n- «excede em 6»: $x+6$.\n\n**Exemplo:** táxi com bandeirada de 500 Kz e 150 Kz por km. Corrida de 2 750 Kz: $500+150x=2\\,750$, $x=15$ km.\n\n**Exemplo com movimento:** dois comboios que se aproximam: as distâncias somam. $70t+50t=360$, $t=3$ h.\n\n**Exemplo de «pensei num número»:** resolve por operações inversas ou com equação: $3(x+8)-10=47$.\n\n**Verificação final:** substitui a solução no **enunciado** (não só na equação): se a equação estiver mal montada, o enunciado denuncia o erro.\n\n**Erros comuns:** escolher mal a incógnita; traduzir «5 a menos que $x$» como $5-x$; esquecer de responder com a unidade.",
 '**Resolver um problema por equação**: escolher incógnita, traduzir em equação, resolver, interpretar e verificar no enunciado.',
 '$$\\text{dobro: }2x\\quad\\text{consecutivos: }x,\\,x+1\\quad\\text{distância}=\\text{velocidade}\\times\\text{tempo}\\quad\\text{custo}=\\text{fixo}+\\text{unitário}\\times n$$',
 ['O triplo de um número mais 5 é 26: $3x+5=26$, $x=7$.', 'Dois números consecutivos com soma 41: $2x+1=41$, $x=20$.',
  'Caderno = 2 × caneta; juntos 900 Kz: $3x=900$, caneta 300 Kz.', 'Perímetro 52 cm, comprimento = largura + 6: $4x+12=52$, $x=10$ cm.',
  'Táxi: $500+150x=2\\,750$, $x=15$ km.', 'Comboios que se cruzam: $70t+50t=360$, $t=3$ h.'],
 "Resolve connosco: **dois irmãos têm 66 000 Kz juntos. Se o mais velho der 6 000 Kz ao mais novo, ficam com o mesmo. Quanto tem cada um?**\n\n1) $x$ = Kz do mais velho; o mais novo tem $66\\,000-x$.\n\n2) Depois da transferência: $x-6\\,000=(66\\,000-x)+6\\,000$.\n\n3) $2x=78\\,000$, $x=39\\,000$.\n\n4) O mais novo tem $27\\,000$. Verifica: $39\\,000-6\\,000=33\\,000=27\\,000+6\\,000$ ✓.",
 '**Desafio.** Um trabalhador ganha 4 500 Kz por dia e perde 1 000 Kz por cada dia que falta. Em 20 dias recebeu 70 000 Kz. Em quantos dias faltou? Monta a equação e verifica.',
 ['escolher e definir a incógnita', 'traduzir frases em expressões', 'montar e resolver a equação', 'interpretar a solução com unidades', 'verificar no enunciado'], ex)
write(2, 18, A)
print('M5a ok')

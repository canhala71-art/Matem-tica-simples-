from common import *
import math
from itertools import combinations

# ============ 4. Inequações do 1.º grau ============
C = "inequacoes.primeiro_grau"
ex = []
def minint(a, b, c):  # menor inteiro com ax+b>c, a>0
    x = F(c-b, a); m = math.floor(x)+1
    assert a*m+b > c and a*(m-1)+b <= c; return m
def maxint(a, b, c):  # maior inteiro com ax+b<c, a>0
    x = F(c-b, a); m = math.ceil(x)-1
    assert a*m+b < c and a*(m+1)+b >= c; return m
ex.append(num(1, C, "Qual é o menor inteiro x que verifica $x+4>9$?", minint(1,4,9), "x + 4 > 9 dá x > 5, e o menor inteiro maior que 5 é 6.", ["Subtrai 4: x > 5.", "O menor inteiro é 6."]))
ex.append(num(1, C, "Qual é o maior inteiro x que verifica $x-3<2$?", maxint(1,-3,2), "x − 3 < 2 dá x < 5, e o maior inteiro menor que 5 é 4.", ["Soma 3: x < 5.", "O maior inteiro é 4."]))
ex.append(num(2, C, "Qual é o menor inteiro x que verifica $3x-5>10$?", minint(3,-5,10), "3x > 15 dá x > 5, logo o menor inteiro é 6 (com x = 5 dá exatamente 10, que não é maior).", ["3x > 15.", "x > 5.", "Menor inteiro: 6."]))
ex.append(num(2, C, "Qual é o maior inteiro x que verifica $2x+7<20$?", maxint(2,7,20), "2x < 13 dá x < 6,5, logo o maior inteiro é 6.", ["2x < 13.", "x < 6,5.", "Maior inteiro: 6."]))
# multiplicar por negativo: -2x+8>2 -> x<3 -> maior inteiro 2
assert all((-2*x+8>2)==(x<3) for x in range(-5,10))
ex.append(num(3, C, "Qual é o maior inteiro x que verifica $-2x+8>2$?", 2, "−2x > −6. Ao dividir por −2 o sinal da desigualdade inverte-se: x < 3. O maior inteiro é 2.", ["−2x > 2 − 8 = −6.", "Dividir por número negativo inverte: x < 3.", "Maior inteiro: 2."]))
# quantos inteiros positivos verificam 4x-3<=21: x<=6
cnt = len([x for x in range(1,100) if 4*x-3 <= 21]); assert cnt == 6
ex.append(num(3, C, "Quantos inteiros positivos verificam $4x-3\\le 21$?", cnt, "4x ≤ 24 dá x ≤ 6; os inteiros positivos são 1, 2, 3, 4, 5 e 6.", ["4x ≤ 24.", "x ≤ 6.", "Inteiros positivos: 1 a 6, ou seja, 6 valores."]))
# problema: 1500 + 250 t >= 6000 -> t>=18
t = F(6000-1500, 250); assert t == 18
ex.append(num(2, C, "O João tem 1 500 Kz e poupa 250 Kz por dia. Ao fim de quantos dias, no mínimo, terá pelo menos 6 000 Kz?", t, "1500 + 250d ≥ 6000 dá 250d ≥ 4500 e d ≥ 18.", ["1500 + 250d ≥ 6000.", "250d ≥ 4500.", "d ≥ 18: no mínimo 18 dias."]))
# 3 recargas: cada 50 Kz + 20 por GB <= 700 -> GB max 32
g = maxint(1,0,1) if False else (700-50)//20; assert 50+20*g <= 700 < 50+20*(g+1) and g == 32
ex.append(num(3, C, "Um plano de dados cobra 50 Kz de taxa mais 20 Kz por GB. Com 700 Kz, quantos GB inteiros, no máximo, se podem comprar?", g, "50 + 20g ≤ 700 dá 20g ≤ 650 e g ≤ 32,5. O máximo inteiro é 32.", ["50 + 20g ≤ 700.", "20g ≤ 650.", "g ≤ 32,5: no máximo 32 GB."]))
ex.append(tf(1, C, "Se $x>3$, então $x=4$ é uma solução.", True, "4 é maior que 3, por isso verifica a desigualdade.", ["Compara 4 com 3.", "4 > 3."]))
ex.append(tf(2, C, "Ao multiplicar os dois lados de uma desigualdade por −1, o sentido mantém-se.", False, "Multiplicar (ou dividir) por um número negativo inverte o sentido: 2 < 5 mas −2 > −5.", ["Testa com 2 < 5.", "Multiplicando por −1: −2 > −5. O sentido inverteu."]))
ex.append(mc(2, C, "Qual é o conjunto solução de $2x-1\\ge 7$?", ["$x\\ge 4$", "$x\\le 4$", "$x\\ge 3$", "$x> 4$"], 0, "2x ≥ 8 dá x ≥ 4 (o 4 está incluído porque o sinal é ≥).", ["2x ≥ 8.", "x ≥ 4."]))
ex.append(mc(3, C, "Resolveste $-3x<12$ e escreveste $x<-4$. O que está errado?", ["Não se inverteu o sentido ao dividir por −3: o correto é x > −4", "Nada, está certo", "Devia ser x < 4", "Devia ser x > 4"], 0, "Dividindo por −3 inverte-se: x > −4.", ["−3x < 12.", "Divide por −3 e inverte: x > −4."]))
ineq = lesson("algebra", "Inequações do 1.º grau", "inequacoes-primeiro-grau", "Inequações do 1.º grau: resolver desigualdades", "inequacoes-primeiro-grau-resolver", "Resolve desigualdades com uma incógnita, interpreta o conjunto solução e usa-as em problemas de orçamento.", 25,
 "Tens 6 000 Kz e queres comprar cadernos de 450 Kz e uma caneta de 300 Kz. Quantos cadernos podes levar sem ultrapassar o dinheiro? Aqui não procuras um valor exato, mas **todos os valores possíveis**: uma **inequação**. Orçamentos, limites de dados, pesos máximos num transporte, notas mínimas para passar, tudo isto são desigualdades.\n\nNesta aula vais resolver inequações do 1.º grau com o mesmo método das equações, aprender a única regra nova (o que fazer com números negativos) e interpretar o resultado como um conjunto de valores.",
 "Uma inequação é uma equação com ≤, <, ≥ ou > no lugar do =. A balança continua a valer: **o que fazes a um lado fazes ao outro**. Somar ou subtrair o mesmo número não muda o sentido. Multiplicar ou dividir por um número **positivo** também não.\n\nA regra nova é esta: ao multiplicar ou dividir por um número **negativo**, o sentido **inverte-se**. Prova com números: 2 < 5 é verdade; multiplicando por −1 ficam −2 e −5, e agora −2 > −5. Os números trocaram de ordem na reta.\n\nA solução não é um número, é um conjunto, por exemplo x > 3, que inclui 3,1, 4, 100 e infinitos outros. O sinal ≥ ou ≤ inclui o extremo; < ou > não inclui.\n\n**Erros comuns:** (1) esquecer de inverter o sentido ao dividir por negativo; (2) incluir o extremo quando o sinal é estrito (com x > 5, o 5 não serve); (3) responder só com um valor quando se pede todos. Defesa: testa um número da solução e outro fora dela na inequação original.",
 "Uma **inequação do 1.º grau** com uma incógnita é uma desigualdade que se pode escrever na forma ax + b > c (ou <, ≥, ≤), com a ≠ 0. A **solução** é o conjunto dos números que a tornam verdadeira. Duas inequações são **equivalentes** se têm o mesmo conjunto solução. Princípios de equivalência: somar ou subtrair o mesmo número aos dois lados mantém o sentido; multiplicar ou dividir por um número positivo mantém o sentido; multiplicar ou dividir por um número negativo inverte o sentido.",
 "$$ax+b>c\;\\Longrightarrow\; x>\\frac{c-b}{a}\\quad(a>0)$$\n\n$$ax+b>c\;\\Longrightarrow\; x<\\frac{c-b}{a}\\quad(a<0)$$\n\nMnemónica: **\"negativo a dividir, sinal a virar\"**. Resposta em intervalo: x > 3 escreve-se $]3,+\\infty[$; x ≤ 2 escreve-se $]-\\infty,2]$.",
 "**Exemplo 1.** Resolve $x+5>9$. Subtrai 5: x > 4.\n\n**Exemplo 2.** Resolve $3x-2\\le 10$. Soma 2: 3x ≤ 12. Divide por 3: x ≤ 4.\n\n**Exemplo 3 (negativo).** Resolve $-2x+1<7$. Subtrai 1: −2x < 6. Divide por −2 e inverte: x > −3. Teste: x = 0 dá 1 < 7 ✓; x = −5 dá 11 < 7 ✗.\n\n**Exemplo 4 (problema).** Com 6 000 Kz, cada caderno custa 450 Kz e há uma caneta de 300 Kz. 450c + 300 ≤ 6000 dá 450c ≤ 5700 e c ≤ 12,67. No máximo 12 cadernos.",
 "Resolve connosco: **uma turma precisa de média mínima 10 para passar. Já tem 8 e 12 em dois testes. Que nota mínima precisa no 3.º teste?**\n\n1) A média é (8 + 12 + n) ÷ 3.\n\n2) Quer-se ≥ 10: (20 + n) ÷ 3 ≥ 10.\n\n3) Multiplica por 3 (positivo, sentido mantém): 20 + n ≥ 30.\n\n4) n ≥ 10.\n\n5) Resposta: pelo menos 10. Prova: (8 + 12 + 10) ÷ 3 = 10 ✓.",
 "**Qual é o maior preço?** Tens 5 000 Kz e queres comprar 4 camisolas iguais e ainda pagar 800 Kz de transporte. Qual é o preço máximo de cada camisola? E se os preços só puderem ser múltiplos de 50 Kz?\n\nPista: 4p + 800 ≤ 5000.",
 "Estarás pronto quando conseguires: (1) resolver ax + b > c com a positivo e negativo; (2) inverter o sentido quando necessário; (3) escrever a solução como x > k ou em intervalo; (4) traduzir um problema de limite (orçamento, nota mínima, dados) numa inequação; (5) testar a resposta com um valor dentro e outro fora da solução.", ex)

# ============ 5. Produtos notáveis ============
C = "algebra.produtos_notaveis"
ex = []
ex.append(num(1, C, "Calcula $(x+3)^2$ para $x=5$ usando o quadrado da soma. Qual é o resultado?", (5+3)**2, "(x + 3)² = x² + 6x + 9 = 25 + 30 + 9 = 64, que é igual a 8².", ["x² + 6x + 9 com x = 5.", "25 + 30 + 9 = 64."]))
ex.append(num(1, C, "Calcula $103^2$ pensando em $(100+3)^2$.", 103**2, "(100 + 3)² = 10000 + 600 + 9 = 10609.", ["100² = 10000.", "2·100·3 = 600.", "3² = 9. Soma: 10609."]))
ex.append(num(1, C, "Calcula $99^2$ pensando em $(100-1)^2$.", 99**2, "(100 − 1)² = 10000 − 200 + 1 = 9801.", ["10000 − 200 + 1 = 9801."]))
ex.append(num(2, C, "Calcula $51\\times 49$ pensando em $(50+1)(50-1)$.", 51*49, "A diferença de quadrados dá 50² − 1² = 2500 − 1 = 2499.", ["(a + b)(a − b) = a² − b².", "2500 − 1 = 2499."]))
# coeficiente do termo em x de (2x+5)^2 = 20
assert (2*2*5) == 20
ex.append(num(2, C, "Desenvolve $(2x+5)^2$. Qual é o coeficiente do termo em x?", 20, "(2x + 5)² = 4x² + 20x + 25. O termo do meio é 2·2x·5 = 20x.", ["a = 2x, b = 5.", "2ab = 2·2x·5 = 20x."]))
# (x-4)^2 com x=10 -> 36
ex.append(num(2, C, "Calcula $x^2-8x+16$ para $x=10$ (repara que é $(x-4)^2$).", (10-4)**2, "x² − 8x + 16 = (x − 4)² = 6² = 36. Confirma: 100 − 80 + 16 = 36.", ["Reconhece o quadrado da diferença.", "(10 − 4)² = 36."]))
# x^2 - 49 para x=10 -> 51 ; (x-7)(x+7)
ex.append(num(2, C, "Calcula $x^2-49$ para $x=10$, fatorizando como $(x-7)(x+7)$.", (10-7)*(10+7), "(10 − 7)(10 + 7) = 3·17 = 51.", ["x² − 49 = (x − 7)(x + 7).", "3·17 = 51."]))
# se x+y=10 e xy=21 então x^2+y^2 = 58
s,p = 10,21; assert s*s-2*p == 58
ex.append(num(3, C, "Se $x+y=10$ e $xy=21$, quanto vale $x^2+y^2$?", s*s-2*p, "(x + y)² = x² + 2xy + y², logo x² + y² = 100 − 42 = 58.", ["(x + y)² = 100.", "2xy = 42.", "x² + y² = 100 − 42 = 58."]))
# a^2-b^2 com a-b=3, a+b=11 -> 33 
ex.append(num(3, C, "Sabendo que $a-b=3$ e $a+b=11$, calcula $a^2-b^2$.", 3*11, "a² − b² = (a − b)(a + b) = 3·11 = 33.", ["Usa a diferença de quadrados.", "3·11 = 33."]))
# 1001^2 - 999^2 = 2*2000 = 4000
assert 1001**2-999**2 == 4000
ex.append(num(3, C, "Calcula $1001^2-999^2$ sem calculadora.", 1001**2-999**2, "(1001 − 999)(1001 + 999) = 2·2000 = 4000.", ["Diferença de quadrados.", "2·2000 = 4000."]))
ex.append(tf(1, C, "$(a+b)^2=a^2+b^2$.", False, "Falta o termo do meio 2ab. Exemplo: (1 + 2)² = 9, mas 1² + 2² = 5.", ["Testa com a = 1, b = 2.", "9 ≠ 5."]))
ex.append(mc(2, C, "Qual é o desenvolvimento correto de $(x-3)^2$?", ["$x^2-6x+9$", "$x^2-9$", "$x^2+9$", "$x^2-6x-9$"], 0, "(a − b)² = a² − 2ab + b², com a = x e b = 3: x² − 6x + 9.", ["a² = x².", "−2ab = −6x.", "b² = 9."]))
pn = lesson("polinomios", "Produtos notáveis", "produtos-notaveis", "Produtos notáveis: quadrados e diferença de quadrados", "produtos-notaveis-quadrados-diferenca", "Desenvolve e fatoriza expressões com os três produtos notáveis e usa-os para calcular de cabeça.", 25,
 "Quanto é 103 vezes 103? Sem calculadora parece custoso, mas se pensares 103 = 100 + 3, a conta fica fácil. E 51 vezes 49? É quase 50 vezes 50. Há uns atalhos algébricos que os matemáticos descobriram há séculos e que poupam muito trabalho: os **produtos notáveis**.\n\nNesta aula vais aprender três fórmulas (quadrado da soma, quadrado da diferença e diferença de quadrados), perceber de onde vêm e usá-las para calcular depressa e para fatorizar expressões nos exames.",
 "Porque é que (a + b)² não é a² + b²? Desenha um quadrado de lado a + b. Divide-o: um quadrado de área a², outro de área b² e **dois retângulos** de área ab cada. A área total é a² + 2ab + b². O termo do meio 2ab são esses dois retângulos que muita gente esquece.\n\nPara (a − b)² a ideia é a mesma, mas o termo do meio é negativo: a² − 2ab + b².\n\nA diferença de quadrados vem de (a + b)(a − b): multiplicando, +ab e −ab cancelam-se e sobra a² − b². Por isso 51·49 = (50 + 1)(50 − 1) = 2500 − 1.\n\n**Erros comuns:** (1) escrever (a + b)² = a² + b²; (2) esquecer o 2 no termo do meio; (3) em (a − b)² pôr o sinal do último termo negativo (b² é sempre positivo). Defesa: testa com números pequenos, a = 1 e b = 2.",
 "Os **produtos notáveis** são igualdades algébricas que se verificam para quaisquer números reais a e b: (a + b)² = a² + 2ab + b² (quadrado da soma), (a − b)² = a² − 2ab + b² (quadrado da diferença) e (a + b)(a − b) = a² − b² (diferença de quadrados). Lidas da direita para a esquerda, servem para **fatorizar**: um trinómio quadrado perfeito a² ± 2ab + b² escreve-se (a ± b)² e a² − b² escreve-se (a + b)(a − b).",
 "$$(a+b)^2=a^2+2ab+b^2$$\n\n$$(a-b)^2=a^2-2ab+b^2$$\n\n$$(a+b)(a-b)=a^2-b^2$$\n\nMnemónica: **\"quadrado do primeiro, duas vezes o primeiro pelo segundo, quadrado do segundo\"**.",
 "**Exemplo 1.** Desenvolve $(x+4)^2$: x² + 8x + 16.\n\n**Exemplo 2.** Fatoriza $x^2-10x+25$: é (x − 5)², porque 2·5 = 10 e 5² = 25.\n\n**Exemplo 3.** Fatoriza $9x^2-16$: é (3x)² − 4², logo (3x + 4)(3x − 4).\n\n**Exemplo 4 (cálculo mental).** 98² = (100 − 2)² = 10000 − 400 + 4 = 9604. E 47·53 = (50 − 3)(50 + 3) = 2500 − 9 = 2491.",
 "Resolve connosco: **calcula 202² sem calculadora.**\n\n1) Como escrever 202 de forma fácil? 200 + 2.\n\n2) Qual é a fórmula? (a + b)² = a² + 2ab + b².\n\n3) a² = 200² = 40 000.\n\n4) 2ab = 2·200·2 = 800.\n\n5) b² = 4.\n\n6) Soma: 40 000 + 800 + 4 = 40 804.",
 "**O quadrado perfeito escondido.** Para que valor de k a expressão $x^2+12x+k$ é o quadrado de uma soma? E se fosse $x^2-12x+k$?\n\nPista: compara com a² + 2ab + b² e descobre b a partir de 2b = 12.",
 "Consideras a competência dominada quando consegues: (1) desenvolver os três produtos notáveis sem erro no termo do meio; (2) reconhecer um quadrado perfeito e fatorizá-lo; (3) fatorizar uma diferença de quadrados; (4) usar os produtos notáveis para calcular de cabeça; (5) usar x + y e xy para calcular x² + y².", ex)

# ============ 6. Estatística ============
C = "estatistica.medidas"
ex = []
from statistics import median
def media(l): return F(sum(l), len(l))
d1 = [12, 15, 15, 18, 20]
ex.append(num(1, C, "Calcula a média das notas $12, 15, 15, 18, 20$.", media(d1), "(12 + 15 + 15 + 18 + 20) ÷ 5 = 80 ÷ 5 = 16.", ["Soma: 80.", "Divide por 5: 16."]))
d2 = [8, 3, 9, 5, 12]
ex.append(num(1, C, "Calcula a mediana de $8, 3, 9, 5, 12$.", F(median(d2)), "Ordena: 3, 5, 8, 9, 12. O valor do meio é 8.", ["Ordena os dados.", "O 3.º dos 5 valores é 8."]))
d3 = [2, 4, 4, 5, 4, 7, 2]
from collections import Counter
mo = Counter(d3).most_common(1)[0][0]; assert mo == 4
ex.append(num(1, C, "Qual é a moda de $2, 4, 4, 5, 4, 7, 2$?", mo, "A moda é o valor mais frequente: o 4 aparece três vezes.", ["Conta as repetições.", "4 aparece 3 vezes."]))
d4 = [10, 12, 14, 16]
ex.append(num(2, C, "Calcula a mediana de $10, 12, 14, 16$ (quatro valores).", F(median(d4)), "Com número par de valores, a mediana é a média dos dois do meio: (12 + 14) ÷ 2 = 13.", ["Dois valores centrais: 12 e 14.", "Média: 13."]))
ex.append(num(2, C, "Qual é a amplitude (maior valor menos menor valor) de $7, 15, 3, 22, 9$?", 22-3, "22 − 3 = 19.", ["Maior: 22.", "Menor: 3.", "19."]))
# média 5 notas = 14; 4 notas somam 52; falta nota 18
assert 14*5-52 == 18
ex.append(num(3, C, "A média de 5 notas é 14. Quatro delas somam 52. Qual é a quinta nota?", 14*5-52, "A soma das 5 notas é 14·5 = 70; a quinta é 70 − 52 = 18.", ["Soma total: 14·5 = 70.", "70 − 52 = 18."]))
# média ponderada: 3 alunos com 10, 2 com 15 -> (30+30)/5=12
ex.append(num(3, C, "Numa turma, 3 alunos têm nota 10 e 2 alunos têm nota 15. Qual é a média da turma?", F(3*10+2*15, 5), "(3·10 + 2·15) ÷ 5 = 60 ÷ 5 = 12.", ["Soma ponderada: 30 + 30 = 60.", "60 ÷ 5 = 12."]))
# acrescentar um valor muda a média: média de 4,6,8 =6 ; adicionando 12 -> 30/4=7.5
ex.append(num(3, C, "A média de $4, 6, 8$ é 6. Qual é a nova média se juntares o valor 12?", media([4,6,8,12]), "A nova soma é 30 e há 4 valores: 30 ÷ 4 = 7,5.", ["Nova soma: 18 + 12 = 30.", "30 ÷ 4 = 7,5."]), ) if False else None
ex.append(num(3, C, "A média de $4, 6, 8$ é 6. Qual é a nova média se juntares o valor 12?", media([4,6,8,12]), "A nova soma é 30 e há 4 valores: 30 ÷ 4 = 15/2.", ["Nova soma: 18 + 12 = 30.", "30 ÷ 4 = 7,5 (ou 15/2)."], accepted=["7,5"]))
ex.append(num(2, C, "Cinco vendedores faturaram em mil Kz: $40, 55, 40, 70, 45$. Qual é a média?", media([40,55,40,70,45]), "(40 + 55 + 40 + 70 + 45) ÷ 5 = 250 ÷ 5 = 50.", ["Soma: 250.", "250 ÷ 5 = 50."]))
ex.append(tf(2, C, "A mediana de um conjunto de dados pode ser um valor que não pertence ao conjunto.", True, "Com número par de dados faz-se a média dos dois centrais, que pode não ser nenhum dos dados (ex.: 10, 12, 14, 16 tem mediana 13).", ["Pensa em 10, 12, 14, 16.", "A mediana é 13, que não está na lista."]))
ex.append(mc(2, C, "Num bairro quase todos ganham pouco, mas um vizinho ganha uma fortuna. Que medida representa melhor o rendimento típico?", ["A mediana", "A média", "A amplitude", "O maior valor"], 0, "A média é arrastada por valores extremos; a mediana não.", ["Valores extremos distorcem a média.", "A mediana é resistente a eles."]))
est = lesson("estatistica", "Estatística descritiva", "estatistica-descritiva", "Média, mediana e moda: resumir dados", "estatistica-media-mediana-moda", "Calcula e interpreta média, mediana, moda e amplitude, e percebe quando usar cada uma.", 25,
 "Numa turma de 30 alunos, como resumir as notas num só número? E num bairro, qual é o salário típico? A estatística dá-nos medidas que resumem muitos dados numa ideia: a **média**, a **mediana** e a **moda**. São usadas nas notícias, nos exames, nos preços do mercado e nos resultados do futebol.\n\nNesta aula vais calcular as três medidas, medir a dispersão com a amplitude e, sobretudo, perceber qual escolher em cada situação.",
 "A **média** é o valor que cada um teria se tudo fosse repartido por igual: somas tudo e divides pelo número de dados. A **mediana** é o valor do meio quando os dados estão ordenados: metade fica abaixo e metade acima. A **moda** é o valor que mais se repete.\n\nImagina cinco amigos com 100, 100, 110, 120 e 1 000 Kz. A média é 286, mas ninguém tem perto disso! A mediana é 110 e descreve melhor o grupo. Por isso, quando há valores extremos, a mediana é mais honesta que a média. A moda é a única que serve para dados que não são números (cor favorita, marca de telemóvel).\n\nA **amplitude** (maior menos menor) mostra o quão espalhados estão os dados.\n\n**Erros comuns:** (1) calcular a mediana sem ordenar primeiro; (2) com número par de dados, escolher um dos dois centrais em vez da média deles; (3) dividir pela quantidade errada ao calcular a média.",
 "Dado um conjunto de n valores, a **média aritmética** é a soma dos valores dividida por n. A **mediana** é o valor central dos dados ordenados (se n é ímpar) ou a média dos dois valores centrais (se n é par). A **moda** é o valor com maior frequência; pode haver mais de uma ou nenhuma. A **amplitude** é a diferença entre o maior e o menor valor.",
 "$$\\bar{x}=\\frac{x_1+x_2+\\dots+x_n}{n}$$\n\n$$\\text{média ponderada}=\\frac{x_1f_1+x_2f_2+\\dots}{f_1+f_2+\\dots}$$\n\n$$\\text{amplitude}=x_{\\max}-x_{\\min}$$\n\nMnemónica: **\"média reparte, mediana divide ao meio, moda é a mais popular\"**.",
 "**Exemplo 1.** Notas 12, 15, 15, 18, 20. Média = 80 ÷ 5 = 16. Mediana = 15 (o 3.º). Moda = 15. Amplitude = 8.\n\n**Exemplo 2 (par).** 10, 12, 14, 16: mediana = (12 + 14) ÷ 2 = 13.\n\n**Exemplo 3 (extremo).** Salários em mil Kz: 80, 90, 90, 100, 640. Média = 200, mediana = 90. A mediana representa melhor o típico.\n\n**Exemplo 4 (nota que falta).** Média de 4 testes é 12 e queres média 13 com 5 testes. Soma necessária: 65. Já tens 48, falta 17. Como 17 não passa de 20, é possível lá chegar.",
 "Resolve connosco: **os golos de uma equipa em 6 jogos foram 2, 0, 3, 1, 3, 1. Calcula média, mediana e moda.**\n\n1) Soma: 2 + 0 + 3 + 1 + 3 + 1 = 10. Média: 10 ÷ 6 = 5/3.\n\n2) Ordena: 0, 1, 1, 2, 3, 3.\n\n3) Mediana: média dos dois do meio, (1 + 2) ÷ 2 = 1,5.\n\n4) Moda: 1 e 3 aparecem duas vezes cada; há duas modas.\n\n5) Interpretação: a equipa marca cerca de 1,7 golos por jogo.",
 "**O erro da média.** Uma turma de 10 alunos tem média 12. Entra um aluno novo e a média passa a 13. Que nota teve o aluno novo?\n\nPista: compara a soma antes (10·12) com a soma depois (11·13).",
 "Estarás pronto quando conseguires: (1) calcular média, mediana, moda e amplitude; (2) ordenar os dados antes da mediana; (3) tratar número par e ímpar de dados; (4) usar média ponderada; (5) escolher a medida mais adequada e justificar.", ex)

# ============ 7. Probabilidade ============
C = "probabilidade.classica"
ex = []
ex.append(num(1, C, "Lança-se um dado equilibrado de 6 faces. Qual é a probabilidade de sair um número par? (fração)", F(3,6), "Há 3 casos favoráveis (2, 4, 6) em 6 possíveis: 3/6 = 1/2.", ["Favoráveis: 2, 4, 6.", "3/6 = 1/2."]))
ex.append(num(1, C, "Lança-se um dado. Qual é a probabilidade de sair 5? (fração)", F(1,6), "1 caso favorável em 6 possíveis.", ["1 favorável.", "6 possíveis: 1/6."]))
ex.append(num(1, C, "Num saco há 3 bolas vermelhas e 7 azuis. Qual é a probabilidade de tirar uma vermelha? (fração)", F(3,10), "3 favoráveis em 10 possíveis: 3/10.", ["Total: 10.", "Favoráveis: 3."]))
ex.append(num(2, C, "Lançam-se duas moedas. Qual é a probabilidade de saírem duas caras? (fração)", F(1,4), "Há 4 resultados igualmente possíveis (CC, CK, KC, KK) e só 1 é CC: 1/4.", ["Lista os 4 resultados.", "1 favorável: 1/4."]))
two = [(a,b) for a in range(1,7) for b in range(1,7)]
fav = len([1 for a,b in two if a+b == 7]); assert fav == 6
ex.append(num(2, C, "Lançam-se dois dados. Qual é a probabilidade de a soma ser 7? (fração)", F(fav,36), "Há 36 pares possíveis e 6 somam 7 ((1,6), (2,5), (3,4), (4,3), (5,2), (6,1)): 6/36 = 1/6.", ["Total: 6·6 = 36.", "Favoráveis: 6.", "6/36 = 1/6."]))
fav = len([1 for a,b in two if a+b >= 10]); assert fav == 6
ex.append(num(3, C, "Lançam-se dois dados. Qual é a probabilidade de a soma ser pelo menos 10? (fração)", F(fav,36), "Somas 10, 11 e 12: 3 + 2 + 1 = 6 casos em 36, ou seja, 1/6.", ["Soma 10: (4,6), (5,5), (6,4).", "Soma 11: 2 casos. Soma 12: 1 caso.", "6/36 = 1/6."]))
# complementar: P(nao 6) = 5/6
ex.append(num(2, C, "A probabilidade de chover amanhã é $\\frac{2}{5}$. Qual é a probabilidade de NÃO chover? (fração)", 1-F(2,5), "Acontecimentos complementares: 1 − 2/5 = 3/5.", ["P(não chover) = 1 − P(chover).", "1 − 2/5 = 3/5."]))
# 2 bolas sem reposição: 4 vermelhas, 6 azuis, 2 vermelhas seguidas: 4/10*3/9 = 2/15
p = F(4,10)*F(3,9); assert p == F(2,15)
ex.append(num(3, C, "Numa caixa há 4 bolas vermelhas e 6 azuis. Tiram-se duas bolas, uma a seguir à outra, sem repor. Qual é a probabilidade de ambas serem vermelhas? (fração)", p, "Primeira: 4/10. Segunda (restam 3 vermelhas em 9): 3/9. Produto: 12/90 = 2/15.", ["P(1.ª vermelha) = 4/10.", "P(2.ª vermelha | 1.ª vermelha) = 3/9.", "4/10 · 3/9 = 2/15."]))
# turma: 12 rapazes 18 raparigas; probabilidade escolher rapariga 3/5
ex.append(num(2, C, "Numa turma há 12 rapazes e 18 raparigas. Escolhe-se um aluno ao acaso. Qual é a probabilidade de ser uma rapariga? (fração irredutível)", F(18,30), "18 favoráveis em 30: 18/30 = 3/5.", ["Total: 30.", "18/30 = 3/5."]))
ex.append(tf(1, C, "A probabilidade de um acontecimento impossível é 0.", True, "Se nunca pode acontecer, não há casos favoráveis: 0/n = 0.", ["Impossível: 0 casos favoráveis.", "Probabilidade 0."]))
ex.append(tf(2, C, "Uma probabilidade pode ser igual a 1,5.", False, "Uma probabilidade está sempre entre 0 e 1 (ou 0% e 100%).", ["Favoráveis ≤ possíveis.", "Logo P ≤ 1."]))
ex.append(mc(2, C, "Uma moeda equilibrada saiu cara 5 vezes seguidas. Qual é a probabilidade de sair cara no 6.º lançamento?", ["1/2", "Menor que 1/2", "Maior que 1/2", "0"], 0, "Os lançamentos são independentes: a moeda não tem memória, por isso é sempre 1/2.", ["Lançamentos independentes.", "A probabilidade mantém-se 1/2."]))
prob = lesson("probabilidade", "Probabilidade", "probabilidade-classica", "Probabilidade: medir a sorte com frações", "probabilidade-classica-lei-de-laplace", "Calcula probabilidades com casos favoráveis e possíveis, usa o acontecimento complementar e o produto em extrações sucessivas.", 25,
 "Vais ao mercado e o vendedor diz: \"há 30% de hipótese de chover hoje\". Num jogo, tens de adivinhar se o dado sai par. Numa rifa de 100 bilhetes, tens 2 bilhetes: que hipótese tens de ganhar? A **probabilidade** é o número que mede o quão provável é um acontecimento.\n\nNesta aula vais aprender a calcular probabilidades contando casos, a usar o complementar (\"a probabilidade de não acontecer\") e a tratar duas extrações seguidas. É a base de seguros, jogos, previsões e estatística.",
 "Quando todos os resultados são igualmente possíveis, a probabilidade é **casos favoráveis ÷ casos possíveis**. No dado, o número par tem 3 casos favoráveis (2, 4, 6) em 6 possíveis: 3/6 = 1/2.\n\nA probabilidade é sempre um número entre 0 (impossível) e 1 (certo). A soma da probabilidade de um acontecimento com a do seu contrário é 1, por isso P(não A) = 1 − P(A). Isso poupa muito trabalho: \"pelo menos um 6 em 3 lançamentos\" é mais fácil de calcular como 1 − P(nenhum 6).\n\nEm duas extrações **sem reposição**, a segunda probabilidade muda, porque o saco ficou com menos bolas: multiplicas as probabilidades de cada passo.\n\n**Erros comuns:** (1) contar resultados não igualmente possíveis (com dois dados, (1,6) e (6,1) são dois casos diferentes); (2) pensar que a moeda \"tem memória\" depois de várias caras; (3) esquecer de atualizar o total quando não há reposição.",
 "Numa **experiência aleatória** com um número finito de resultados igualmente possíveis, a **probabilidade** de um acontecimento A é $P(A)=\\dfrac{\\text{número de casos favoráveis}}{\\text{número de casos possíveis}}$ (Lei de Laplace). Verifica-se $0\\le P(A)\\le 1$, $P(\\text{impossível})=0$, $P(\\text{certo})=1$ e $P(\\bar A)=1-P(A)$. Em extrações sucessivas, a probabilidade de uma sequência é o produto das probabilidades de cada etapa, condicionada ao que já aconteceu.",
 "$$P(A)=\\frac{n(A)}{n(\\Omega)}$$\n\n$$P(\\bar A)=1-P(A)$$\n\n$$P(A\\text{ e depois }B)=P(A)\\times P(B\\mid A)$$\n\nMnemónica: **\"favoráveis sobre possíveis, e quando for difícil, vai pelo contrário\"**.",
 "**Exemplo 1.** Dado: P(maior que 4) = 2/6 = 1/3 (resultados 5 e 6).\n\n**Exemplo 2.** Duas moedas: resultados CC, CK, KC, KK. P(uma cara e uma coroa) = 2/4 = 1/2.\n\n**Exemplo 3 (complementar).** P(pelo menos uma cara em 2 lançamentos) = 1 − P(duas coroas) = 1 − 1/4 = 3/4.\n\n**Exemplo 4 (sem reposição).** Saco com 3 vermelhas e 2 azuis; tiram-se duas bolas. P(duas vermelhas) = 3/5 · 2/4 = 6/20 = 3/10.",
 "Resolve connosco: **numa rifa há 50 bilhetes e tens 5. Qual é a probabilidade de ganhares o 1.º prémio? E de não ganhares?**\n\n1) Casos possíveis: 50.\n\n2) Casos favoráveis: 5.\n\n3) P(ganhar) = 5/50 = 1/10.\n\n4) P(não ganhar) = 1 − 1/10 = 9/10.\n\n5) Interpretação: em média, ganharias 1 vez em 10 rifas.",
 "**Os dois dados do Natal.** Lançam-se dois dados. Qual é a soma mais provável? Constrói a tabela 6×6 e conta quantas vezes aparece cada soma.\n\nPista: a soma 2 só aparece em (1,1), mas a soma 7 aparece em seis pares diferentes.",
 "Consideras a competência dominada quando consegues: (1) listar os casos possíveis e contar os favoráveis; (2) calcular probabilidades como frações irredutíveis; (3) usar o complementar; (4) calcular extrações sucessivas sem reposição; (5) explicar porque é que a moeda não tem memória.", ex)

# ============ 8. Trigonometria ============
C = "trigonometria.triangulo_retangulo"
ex = []
ex.append(num(1, C, "Num triângulo retângulo os catetos medem 3 e 4 e a hipotenusa mede 5. Qual é o seno do ângulo oposto ao cateto de medida 3? (fração)", F(3,5), "seno = cateto oposto ÷ hipotenusa = 3/5.", ["Oposto: 3.", "Hipotenusa: 5.", "3/5."]))
ex.append(num(1, C, "No mesmo triângulo (3, 4, 5), qual é o cosseno do ângulo oposto ao cateto de medida 3? (fração)", F(4,5), "cosseno = cateto adjacente ÷ hipotenusa = 4/5.", ["Adjacente: 4.", "Hipotenusa: 5.", "4/5."]))
ex.append(num(1, C, "No mesmo triângulo, qual é a tangente do ângulo oposto ao cateto 3? (fração)", F(3,4), "tangente = oposto ÷ adjacente = 3/4.", ["Oposto: 3.", "Adjacente: 4.", "3/4."]))
h = math.isqrt(5*5+12*12); assert h*h == 25+144 and h == 13
ex.append(num(2, C, "Um triângulo retângulo tem catetos 5 e 12. Quanto mede a hipotenusa?", h, "Teorema de Pitágoras: 5² + 12² = 25 + 144 = 169, logo h = 13.", ["h² = 25 + 144 = 169.", "h = 13."]))
ex.append(num(2, C, "Num triângulo retângulo a hipotenusa mede 13 e um cateto mede 5. Qual é o seno do ângulo oposto a esse cateto? (fração)", F(5,13), "sen = oposto ÷ hipotenusa = 5/13.", ["Oposto 5, hipotenusa 13.", "5/13."]))
assert math.isqrt(15*15-9*9)**2 == 15*15-9*9
ex.append(num(2, C, "Uma escada de 15 m encosta a uma parede e a base está a 9 m da parede. A que altura da parede chega a escada, em metros?", math.isqrt(15*15-9*9), "Pitágoras: altura² = 15² − 9² = 225 − 81 = 144, logo a altura é 12 m.", ["h² + 9² = 15².", "h² = 144.", "h = 12 m."]))
# sen 30 = 1/2: hipotenusa 20 -> oposto 10
ex.append(num(3, C, "Num triângulo retângulo com um ângulo de 30°, a hipotenusa mede 20 m. Quanto mede o cateto oposto a esse ângulo? (sen 30° = 1/2)", F(1,2)*20, "oposto = hipotenusa × sen 30° = 20 · 1/2 = 10 m.", ["sen = oposto/hipotenusa.", "oposto = 20 · 1/2 = 10."]))
# tg 45 = 1 : sombra 8 m, ângulo 45 -> altura 8
ex.append(num(3, C, "A sombra de um poste mede 8 m quando os raios do sol formam 45° com o chão (tg 45° = 1). Qual é a altura do poste, em metros?", 8*1, "altura = sombra × tg 45° = 8 · 1 = 8 m.", ["tg = altura/sombra.", "altura = 8 · 1 = 8 m."]))
# cos 60 = 1/2 : hipotenusa 18, adjacente 9
ex.append(num(3, C, "Uma rampa de 18 m de comprimento faz 60° com o chão. Qual é o comprimento da sua projeção horizontal, em metros? (cos 60° = 1/2)", F(1,2)*18, "adjacente = hipotenusa × cos 60° = 18 · 1/2 = 9 m.", ["cos = adjacente/hipotenusa.", "adjacente = 18 · 1/2 = 9 m."]))
ex.append(tf(2, C, "Num triângulo retângulo, a hipotenusa é o maior lado.", True, "É o lado oposto ao ângulo reto, e é sempre maior que cada cateto (Pitágoras: h² = a² + b²).", ["h² = a² + b² > a² e > b².", "Logo h é o maior lado."]))
ex.append(tf(2, C, "O seno de um ângulo agudo pode ser maior que 1.", False, "sen = oposto ÷ hipotenusa e o cateto é menor que a hipotenusa, por isso o seno está entre 0 e 1.", ["Cateto < hipotenusa.", "Razão menor que 1."]))
ex.append(mc(2, C, "Qual é a relação correta?", ["$\\sin^2\\alpha+\\cos^2\\alpha=1$", "$\\sin\\alpha+\\cos\\alpha=1$", "$\\tan\\alpha=\\cos\\alpha/\\sin\\alpha$", "$\\sin\\alpha=\\cos\\alpha$ para todo α"], 0, "É a relação fundamental da trigonometria, consequência do teorema de Pitágoras. A tangente é sen ÷ cos.", ["(oposto/h)² + (adjacente/h)² = (o² + a²)/h² = 1."]))
trig = lesson("trigonometria", "Trigonometria", "trigonometria-triangulo-retangulo", "Trigonometria no triângulo retângulo: seno, cosseno e tangente", "trigonometria-seno-cosseno-tangente", "Usa seno, cosseno, tangente e o teorema de Pitágoras para calcular lados e alturas em triângulos retângulos.", 30,
 "Como é que um topógrafo mede a altura de um prédio sem lá subir? Mede a distância à base e o ângulo até ao topo, e a **trigonometria** faz o resto. É assim que se calculam rampas, telhados, torres de telecomunicações, a inclinação de uma estrada ou a altura de uma árvore pela sombra.\n\nNesta aula vais aprender o teorema de Pitágoras e as razões trigonométricas seno, cosseno e tangente, e usá-los para resolver problemas com triângulos retângulos.",
 "Num triângulo retângulo, escolhe um ângulo agudo α. O lado maior, oposto ao ângulo reto, é a **hipotenusa**. Em relação a α, o **cateto oposto** é o que está \"à frente\" do ângulo e o **cateto adjacente** é o que lhe está encostado.\n\nA ideia genial é que, para o mesmo ângulo, a razão entre dois lados **não depende do tamanho do triângulo**: um triângulo pequeno e outro grande, ambos com 30°, têm sempre a mesma razão oposto ÷ hipotenusa. Essa razão chama-se **seno**. O **cosseno** é adjacente ÷ hipotenusa e a **tangente** é oposto ÷ adjacente.\n\nAssim, se souberes o ângulo e um lado, calculas os outros. Mnemónica útil: **SOH-CAH-TOA** (Seno = Oposto/Hipotenusa, Cosseno = Adjacente/Hipotenusa, Tangente = Oposto/Adjacente).\n\n**Erros comuns:** (1) trocar oposto com adjacente (depende do ângulo escolhido); (2) usar seno quando precisavas de tangente; (3) esquecer que a calculadora tem de estar em graus.",
 "Num triângulo retângulo, para um ângulo agudo α: $\\sin\\alpha=\\dfrac{\\text{cateto oposto}}{\\text{hipotenusa}}$, $\\cos\\alpha=\\dfrac{\\text{cateto adjacente}}{\\text{hipotenusa}}$, $\\tan\\alpha=\\dfrac{\\text{cateto oposto}}{\\text{cateto adjacente}}$. O **teorema de Pitágoras** afirma que a soma dos quadrados dos catetos é igual ao quadrado da hipotenusa. Os valores das razões dependem apenas do ângulo.",
 "$$a^2+b^2=c^2$$\n\n$$\\sin\\alpha=\\frac{o}{h},\\quad\\cos\\alpha=\\frac{a}{h},\\quad\\tan\\alpha=\\frac{o}{a}$$\n\n$$\\sin^2\\alpha+\\cos^2\\alpha=1,\\qquad \\tan\\alpha=\\frac{\\sin\\alpha}{\\cos\\alpha}$$\n\nÂngulos notáveis: sen 30° = 1/2, cos 60° = 1/2, tg 45° = 1.\n\nMnemónica: **SOH-CAH-TOA**.",
 "**Exemplo 1.** Catetos 6 e 8: hipotenusa = √(36 + 64) = 10. Para o ângulo oposto ao cateto 6: sen = 6/10 = 3/5, cos = 4/5, tg = 3/4.\n\n**Exemplo 2.** Triângulo com hipotenusa 10 e ângulo de 30°. O cateto oposto vale 10 · sen 30° = 5.\n\n**Exemplo 3 (altura).** A 20 m de um prédio, vês o topo com ângulo de 45°. tg 45° = 1 = altura ÷ 20, logo a altura é 20 m.\n\n**Exemplo 4 (escada).** Uma escada de 5 m, com a base a 3 m da parede, chega a √(25 − 9) = 4 m de altura.",
 "Resolve connosco: **uma rampa tem 10 m de comprimento e sobe 5 m. Qual é o seno do ângulo de inclinação?**\n\n1) A rampa é a hipotenusa: 10 m.\n\n2) A subida é o cateto oposto ao ângulo de inclinação: 5 m.\n\n3) sen α = 5/10 = 1/2.\n\n4) Que ângulo tem seno 1/2? 30°.\n\n5) Verifica: uma rampa que sobe metade do seu comprimento faz 30° com o chão.",
 "**A altura da torre.** Estás a 30 m da base de uma torre e vês o topo com um ângulo de 45°. Os teus olhos estão a 1,5 m do chão. Qual é a altura da torre?\n\nPista: o triângulo dá a altura acima dos teus olhos; depois soma a altura dos olhos.",
 "Estarás pronto quando conseguires: (1) usar Pitágoras para achar o terceiro lado; (2) identificar oposto, adjacente e hipotenusa em relação a um ângulo; (3) calcular sen, cos e tg como frações; (4) usar os ângulos notáveis para achar lados; (5) resolver problemas de alturas, rampas e escadas.", ex)

# ============ 9. Geometria analítica ============
C = "geometria_analitica.reta"
ex = []
def dist2(p,q): return (p[0]-q[0])**2+(p[1]-q[1])**2
ex.append(num(1, C, "Qual é a distância entre $A(1,2)$ e $B(4,6)$?", math.isqrt(dist2((1,2),(4,6))), "d = √((4 − 1)² + (6 − 2)²) = √(9 + 16) = 5.", ["Δx = 3, Δy = 4.", "√25 = 5."]))
ex.append(num(1, C, "Qual é a abcissa do ponto médio entre $A(2,3)$ e $B(8,7)$?", F(2+8,2), "xm = (2 + 8) ÷ 2 = 5.", ["(2 + 8)/2 = 5."]))
ex.append(num(1, C, "Qual é a ordenada do ponto médio entre $A(2,3)$ e $B(8,7)$?", F(3+7,2), "ym = (3 + 7) ÷ 2 = 5.", ["(3 + 7)/2 = 5."]))
ex.append(num(2, C, "Qual é o declive da reta que passa por $A(1,2)$ e $B(3,8)$?", F(8-2,3-1), "m = (8 − 2) ÷ (3 − 1) = 3.", ["Δy = 6.", "Δx = 2.", "m = 3."]))
ex.append(num(2, C, "A reta $y=2x+3$ passa pelo ponto $(4,k)$. Qual é o valor de k?", 2*4+3, "Substitui x = 4: y = 2·4 + 3 = 11.", ["k = 2·4 + 3.", "k = 11."]))
ex.append(num(2, C, "Qual é a distância entre $A(-2,1)$ e $B(4,9)$?", math.isqrt(dist2((-2,1),(4,9))), "d = √(6² + 8²) = √100 = 10.", ["Δx = 6, Δy = 8.", "√(36 + 64) = 10."]))
# reta por (1,5) e (4,11): y=2x+3 ; zero -3/2
ex.append(num(3, C, "Uma reta passa por $(1,5)$ e $(4,11)$. Em que ponto corta o eixo dos yy? (indica a ordenada)", 5-2*1, "Declive: (11 − 5) ÷ (4 − 1) = 2. A reta é y = 2x + b com 5 = 2 + b, logo b = 3.", ["Declive 2.", "5 = 2·1 + b.", "b = 3."]))
# ponto médio xm=(a+8)/2=5 -> a=2 ; dado M(5,2) e A(1,1) -> B(9,3)
ex.append(num(3, C, "O ponto médio de $AB$ é $M(5,2)$ e $A=(1,1)$. Qual é a abcissa de B?", 2*5-1, "(1 + xB) ÷ 2 = 5 dá xB = 9.", ["(1 + xB)/2 = 5.", "xB = 10 − 1 = 9."]))
# paralelas: y=3x+1 e reta por (0,5) paralela: declive 3 -> y(2)=11
ex.append(num(3, C, "Uma reta é paralela a $y=3x+1$ e passa pelo ponto $(0,5)$. Qual é a ordenada do seu ponto com abcissa 2?", 3*2+5, "Retas paralelas têm o mesmo declive: y = 3x + 5, e para x = 2 vem y = 11.", ["Declive 3.", "y = 3x + 5.", "x = 2 dá 11."]))
ex.append(num(2, C, "Qual é o declive da reta $4x+2y=10$?", -2, "Isola y: 2y = −4x + 10, logo y = −2x + 5 e o declive é −2.", ["2y = −4x + 10.", "y = −2x + 5."]))
ex.append(tf(1, C, "A reta horizontal $y=4$ tem declive 0.", True, "Em y = 4, y não varia quando x varia: declive 0.", ["Δy = 0.", "Declive 0."]))
ex.append(mc(2, C, "Duas retas com o mesmo declive e ordenadas na origem diferentes são…", ["Paralelas", "Perpendiculares", "Coincidentes", "Concorrentes num só ponto"], 0, "O mesmo declive significa a mesma inclinação, e ordenadas diferentes significam que não coincidem: são paralelas.", ["Mesmo declive: mesma inclinação.", "Não coincidem, logo paralelas."]))
ga = lesson("geometria-analitica", "Geometria analítica", "geometria-analitica-reta", "Geometria analítica: distância, ponto médio e equação da reta", "geometria-analitica-distancia-reta", "Calcula distâncias, pontos médios e declives no plano cartesiano e escreve a equação reduzida da reta.", 30,
 "Quando abres o mapa no telemóvel, a tua posição é um ponto com duas coordenadas. A distância até casa, o ponto a meio caminho entre dois lugares, a inclinação de uma rua, tudo se pode calcular com números. Isto é a **geometria analítica**: descrever figuras com coordenadas e resolvê-las com álgebra.\n\nNesta aula vais usar o plano cartesiano para calcular a distância entre dois pontos, o ponto médio e o declive, e escrever a equação de uma reta.",
 "No plano cartesiano, cada ponto tem uma abcissa (x) e uma ordenada (y). Para a **distância** entre dois pontos, desenha um triângulo retângulo cujos catetos são as diferenças das coordenadas: Δx e Δy. A distância é a hipotenusa, e basta usar Pitágoras: $d=\\sqrt{(\\Delta x)^2+(\\Delta y)^2}$.\n\nO **ponto médio** fica a meio caminho: a abcissa é a média das abcissas e a ordenada é a média das ordenadas.\n\nO **declive** de uma reta mede a inclinação: quanto y sobe por cada unidade que x anda. A equação reduzida é y = mx + b, onde m é o declive e b a ordenada na origem. Retas **paralelas** têm o mesmo declive.\n\n**Erros comuns:** (1) esquecer de fazer a raiz quadrada na distância; (2) trocar a ordem das coordenadas (em (x, y) vem primeiro x); (3) dividir Δx por Δy no declive em vez de Δy por Δx.",
 "Dados $A(x_1,y_1)$ e $B(x_2,y_2)$, a **distância** é $d(A,B)=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$ e o **ponto médio** é $M\\left(\\frac{x_1+x_2}{2},\\frac{y_1+y_2}{2}\\right)$. O **declive** da reta AB (com x₁ ≠ x₂) é $m=\\frac{y_2-y_1}{x_2-x_1}$. A **equação reduzida** de uma reta não vertical é y = mx + b.",
 "$$d=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$$\n\n$$M=\\left(\\frac{x_1+x_2}{2},\\frac{y_1+y_2}{2}\\right)$$\n\n$$m=\\frac{y_2-y_1}{x_2-x_1},\\qquad y-y_1=m(x-x_1)$$\n\nParalelas: mesmo declive. Perpendiculares: $m_1\\cdot m_2=-1$.",
 "**Exemplo 1.** A(0, 0) e B(6, 8): d = √(36 + 64) = 10. Ponto médio: (3, 4).\n\n**Exemplo 2.** Reta por (1, 3) e (3, 7): m = 4 ÷ 2 = 2. Então y = 2x + b e 3 = 2 + b, logo b = 1: y = 2x + 1.\n\n**Exemplo 3.** A reta y = −x + 4 corta o eixo dos xx quando y = 0, isto é, x = 4. Corta o eixo dos yy em y = 4.\n\n**Exemplo 4 (perpendicular).** A reta y = 2x + 1 tem declive 2; uma perpendicular tem declive −1/2.",
 "Resolve connosco: **dois bairros estão nos pontos A(2, 3) e B(10, 9) de um mapa em km. Qual é a distância entre eles e onde fica o ponto médio?**\n\n1) Δx = 10 − 2 = 8 e Δy = 9 − 3 = 6.\n\n2) d = √(64 + 36) = √100 = 10 km.\n\n3) Ponto médio: x = (2 + 10) ÷ 2 = 6 e y = (3 + 9) ÷ 2 = 6.\n\n4) Resposta: 10 km, ponto médio (6, 6).",
 "**O triângulo isósceles.** Os pontos A(0, 0), B(4, 0) e C(2, 5) formam um triângulo. Mostra que AC e BC têm o mesmo comprimento. Que tipo de triângulo é?\n\nPista: calcula as duas distâncias com a fórmula.",
 "Consideras a competência dominada quando consegues: (1) calcular a distância entre dois pontos; (2) calcular o ponto médio; (3) calcular o declive por dois pontos; (4) escrever e interpretar y = mx + b; (5) reconhecer retas paralelas e perpendiculares pelo declive.", ex)

for i, d in enumerate([ineq, pn, est, prob, trig, ga], start=4):
    write(3, i, d); print(d["lesson_slug"], len(d["exercises"]))

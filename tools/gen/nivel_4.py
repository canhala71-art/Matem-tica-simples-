from common import *
import math

# ===== 4.1 Sucessões e padrões =====
C = "raciocinio.sucessoes"
ex = []
an = lambda a1, r, n: a1 + (n-1)*r
gn = lambda a1, q, n: a1 * q**(n-1)
ex.append(num(1, C, "Qual é o próximo termo da sucessão $3, 7, 11, 15, \\dots$?", an(3,4,5), "A diferença entre termos consecutivos é 4: 15 + 4 = 19.", ["Diferença: 7 − 3 = 4.", "15 + 4 = 19."]))
ex.append(num(1, C, "Qual é o próximo termo de $2, 6, 18, 54, \\dots$?", gn(2,3,5), "Cada termo é o triplo do anterior: 54 · 3 = 162.", ["Razão: 6 ÷ 2 = 3.", "54 · 3 = 162."]))
ex.append(num(2, C, "Numa progressão aritmética com primeiro termo 5 e razão 3, qual é o termo de ordem 10?", an(5,3,10), "a₁₀ = 5 + 9·3 = 32.", ["a_n = a₁ + (n − 1)r.", "5 + 9·3 = 32."]))
ex.append(num(2, C, "Numa progressão geométrica com primeiro termo 2 e razão 2, qual é o termo de ordem 8?", gn(2,2,8), "a₈ = 2 · 2⁷ = 256.", ["a_n = a₁ · q^(n−1).", "2 · 128 = 256."]))
s = sum(an(1,1,n) for n in range(1,101)); assert s == 5050
ex.append(num(2, C, "Calcula a soma $1+2+3+\\dots+100$.", s, "S = n(a₁ + aₙ) ÷ 2 = 100·101 ÷ 2 = 5050.", ["n = 100, a₁ = 1, a₁₀₀ = 100.", "100·101/2 = 5050."]))
# quantos termos tem 7, 12, ..., 112 : (112-7)/5+1 = 22
n = (112-7)//5+1; assert an(7,5,n) == 112 and n == 22
ex.append(num(3, C, "Quantos termos tem a progressão aritmética $7, 12, 17, \\dots, 112$?", n, "112 = 7 + (n − 1)·5 dá n − 1 = 21 e n = 22.", ["112 − 7 = 105.", "105 ÷ 5 = 21.", "n = 22."]))
# soma 7..112 = 22*(7+112)/2 = 1309
ss = n*(7+112)//2; assert ss == sum(range(7,113,5)) == 1309
ex.append(num(3, C, "Calcula a soma dos termos de $7, 12, 17, \\dots, 112$.", ss, "S = 22·(7 + 112) ÷ 2 = 22·119 ÷ 2 = 1309.", ["22 termos.", "S = 22·119/2 = 1309."]))
# poupança: 500 no 1º mês, +200 por mês, total em 12 meses
tot = sum(an(500,200,k) for k in range(1,13)); assert tot == 19200
ex.append(num(3, C, "A Ana poupa 500 Kz no 1.º mês e, em cada mês seguinte, mais 200 Kz do que no anterior. Quanto terá poupado ao fim de 12 meses, em Kz?", tot, "No mês 12 poupa 500 + 11·200 = 2700. S = 12·(500 + 2700) ÷ 2 = 19200.", ["a₁₂ = 500 + 11·200 = 2700.", "S = 12·3200/2 = 19200."]))
# bactérias duplicam: 5 -> após 6 duplicações 320
ex.append(num(2, C, "Uma colónia tem 5 bactérias e o número duplica a cada hora. Quantas há ao fim de 6 horas?", 5*2**6, "5 · 2⁶ = 5 · 64 = 320.", ["Duplicar 6 vezes: × 2⁶.", "5 · 64 = 320."]))
ex.append(num(2, C, "Qual é o próximo termo de $1, 1, 2, 3, 5, 8, \\dots$ (cada termo é a soma dos dois anteriores)?", 13, "5 + 8 = 13.", ["É a sucessão de Fibonacci.", "5 + 8 = 13."]))
ex.append(tf(2, C, "A sucessão $2, 4, 8, 16, \\dots$ é uma progressão aritmética.", False, "A diferença não é constante (2, 4, 8). É geométrica, com razão 2.", ["Diferenças: 2, 4, 8.", "Razões: 2, 2, 2: geométrica."]))
ex.append(mc(2, C, "Qual é o termo geral da sucessão $5, 8, 11, 14, \\dots$?", ["$3n+2$", "$3n+5$", "$5n+3$", "$n+4$"], 0, "É aritmética com a₁ = 5 e r = 3: aₙ = 5 + (n − 1)·3 = 3n + 2.", ["a_n = 5 + 3(n − 1).", "= 3n + 2. Teste: n = 1 dá 5."]))
suc = lesson("problemas-de-raciocinio", "Sucessões e padrões", "sucessoes-e-padroes", "Sucessões, progressões aritméticas e geométricas", "sucessoes-progressoes-aritmeticas-geometricas", "Descobre padrões, usa o termo geral e calcula somas em progressões aritméticas e geométricas.", 30,
 "Poupar 500 Kz no primeiro mês e mais 200 Kz em cada mês seguinte; uma colónia de bactérias que duplica de hora a hora; os lugares numa bancada de estádio, que aumentam fila a fila. Todas estas situações têm um padrão. Nos exames pedem muitas vezes: \"qual é o próximo termo?\" ou \"quanto soma tudo?\".\n\nNesta aula vais aprender a distinguir progressões **aritméticas** (soma-se sempre o mesmo) de **geométricas** (multiplica-se sempre pelo mesmo), a escrever o termo geral e a calcular somas sem somar termo a termo.",
 "Numa progressão aritmética, a diferença entre termos consecutivos é constante, a **razão** r: 3, 7, 11, 15 tem r = 4. Para chegar ao 10.º termo dás 9 saltos de 4 a partir do primeiro: a₁₀ = 3 + 9·4. Daí o termo geral aₙ = a₁ + (n − 1)r: o \"n − 1\" são os saltos.\n\nNuma progressão geométrica o que é constante é o **quociente**: 2, 6, 18, 54 tem q = 3, e aₙ = a₁ · qⁿ⁻¹. O crescimento é muito mais rápido, por isso as bactérias e os juros compostos são geométricos.\n\nA soma 1 + 2 + … + 100 tem um truque célebre: emparelha o primeiro com o último (1 + 100), o segundo com o penúltimo (2 + 99)… Há 50 pares, todos com soma 101: 5050. Esse é o argumento da fórmula S = n(a₁ + aₙ) ÷ 2.\n\n**Erros comuns:** (1) usar n em vez de n − 1 no termo geral; (2) confundir aritmética com geométrica (testa diferenças e razões); (3) na soma, esquecer de dividir por 2.",
 "Uma **progressão aritmética** (PA) é uma sucessão em que cada termo, a partir do segundo, se obtém do anterior somando uma constante r (a **razão**). O termo geral é $a_n=a_1+(n-1)r$ e a soma dos n primeiros termos é $S_n=\\frac{n(a_1+a_n)}{2}$. Uma **progressão geométrica** (PG) é uma sucessão em que cada termo se obtém do anterior multiplicando por uma constante q (a **razão**). O termo geral é $a_n=a_1q^{n-1}$ e, se q ≠ 1, $S_n=a_1\\frac{q^n-1}{q-1}$.",
 "$$a_n=a_1+(n-1)r,\\qquad S_n=\\frac{n(a_1+a_n)}{2}\\quad(\\text{PA})$$\n\n$$a_n=a_1q^{n-1},\\qquad S_n=a_1\\,\\frac{q^n-1}{q-1}\\quad(\\text{PG})$$\n\nTeste: PA se as **diferenças** são iguais; PG se os **quocientes** são iguais.",
 "**Exemplo 1 (PA).** 4, 9, 14, …: r = 5. a₂₀ = 4 + 19·5 = 99.\n\n**Exemplo 2 (soma PA).** Soma dos 20 primeiros termos: 20·(4 + 99) ÷ 2 = 1030.\n\n**Exemplo 3 (PG).** 3, 6, 12, …: q = 2. a₇ = 3·2⁶ = 192. Soma dos 7 primeiros: 3·(2⁷ − 1) ÷ (2 − 1) = 381.\n\n**Exemplo 4 (problema).** Num auditório, a 1.ª fila tem 12 lugares e cada fila seguinte tem mais 2. Com 15 filas: a₁₅ = 12 + 14·2 = 40 lugares na última. Total: 15·(12 + 40) ÷ 2 = 390 lugares.",
 "Resolve connosco: **um taxista faz 20 corridas no 1.º dia e, por dia, mais 3 do que no dia anterior. Quantas corridas faz em 10 dias?**\n\n1) É PA com a₁ = 20 e r = 3.\n\n2) Corridas no 10.º dia: 20 + 9·3 = 47.\n\n3) Total: S₁₀ = 10·(20 + 47) ÷ 2 = 335.\n\n4) Resposta: 335 corridas. Verifica a ordem de grandeza: média entre 20 e 47 é 33,5, vezes 10 dá 335 ✓.",
 "**Dobrar o arroz.** Uma lenda conta que um sábio pediu 1 grão na 1.ª casa de um tabuleiro de xadrez, 2 na 2.ª, 4 na 3.ª, e assim sucessivamente a duplicar. Quantos grãos pediu na 10.ª casa? E no total das 10 primeiras casas?\n\nPista: é PG com q = 2; usa a fórmula da soma e vê a diferença para a 64.ª casa.",
 "Estarás pronto quando conseguires: (1) classificar uma sucessão como PA ou PG; (2) escrever o termo geral; (3) calcular termos de ordem qualquer; (4) calcular somas sem somar tudo; (5) modelar poupanças, crescimentos e filas de lugares com progressões.", ex)

# ===== 4.2 Problemas de idades, trabalho e misturas =====
C = "raciocinio.problemas"
ex = []
# idades: pai 3x filho agora; daqui 10 anos pai = 2 filho + 5? Use: daqui a 6 anos pai tem o dobro: p=3f, p+6=2(f+6) -> 3f+6=2f+12 -> f=6
f = 6; assert 3*f+6 == 2*(f+6)
ex.append(num(2, C, "Hoje o pai tem o triplo da idade do filho. Daqui a 6 anos terá o dobro. Que idade tem o filho hoje?", f, "Seja f a idade do filho: 3f + 6 = 2(f + 6), logo f = 6.", ["Pai hoje: 3f; daqui a 6 anos: 3f + 6 e f + 6.", "3f + 6 = 2f + 12.", "f = 6."]))
# trabalho: A faz em 6 dias, B em 12 -> juntos 4
t = 1/(F(1,6)+F(1,12)); assert t == 4
ex.append(num(2, C, "O Pedro pinta uma parede em 6 horas e o Paulo pinta a mesma em 12 horas. Quanto tempo demoram juntos, em horas?", F(1)/(F(1,6)+F(1,12)), "Em 1 hora fazem 1/6 + 1/12 = 3/12 = 1/4 da parede; logo demoram 4 horas.", ["Ritmos: 1/6 e 1/12 por hora.", "Juntos: 1/4 por hora.", "Tempo: 4 horas."]))
# misturas: 20 L a 30% + x L a 60% = mistura a 40%: 0.3*20+0.6x=0.4(20+x) -> 6+0.6x=8+0.4x -> x=10
x = F(2*10,2); assert F(3,10)*20 + F(6,10)*x == F(4,10)*(20+x)
ex.append(num(3, C, "Misturam-se 20 litros de uma solução a 30% de sal com x litros de outra a 60%, para obter uma mistura a 40%. Quanto vale x, em litros?", x, "Sal: 0,3·20 + 0,6x = 0,4(20 + x), isto é, 6 + 0,6x = 8 + 0,4x, logo x = 10.", ["Quantidade de sal antes = depois.", "6 + 0,6x = 8 + 0,4x.", "0,2x = 2, x = 10."]))
# distância/velocidade: dois carros, 60 e 90 km/h, saem de pontos a 300 km em sentidos opostos: encontro 2h
t = F(300, 60+90); assert t == 2
ex.append(num(2, C, "Dois carros partem ao mesmo tempo de duas cidades a 300 km de distância, um contra o outro, a 60 km/h e 90 km/h. Ao fim de quantas horas se cruzam?", t, "A distância diminui 60 + 90 = 150 km por hora: 300 ÷ 150 = 2 horas.", ["Velocidade de aproximação: 150 km/h.", "300 ÷ 150 = 2."]))
# média velocidade: ida 60, volta 40 -> 48
v = F(2*60*40, 60+40); assert v == 48
ex.append(num(3, C, "Um autocarro vai de A a B a 60 km/h e volta a 40 km/h. Qual é a velocidade média de todo o percurso, em km/h?", v, "Com d km em cada sentido: tempo total d/60 + d/40 = d/24; distância 2d; média 2d ÷ (d/24) = 48 km/h (não é 50).", ["Escolhe d = 120 km: ida 2 h, volta 3 h.", "Total 240 km em 5 h.", "240 ÷ 5 = 48 km/h."]))
# troco/ percentagens combinadas: preço 8000 com 10% desconto e depois +5% IVA
p = F(8000)*F(90,100)*F(105,100); assert p == 7560
ex.append(num(2, C, "Um telemóvel custa 8 000 Kz. Faz-se um desconto de 10% e depois acrescentam-se 5% de imposto sobre o novo preço. Quanto se paga, em Kz?", p, "Desconto: 8000 · 0,9 = 7200. Imposto: 7200 · 1,05 = 7560.", ["8000 · 0,90 = 7200.", "7200 · 1,05 = 7560."]))
# torneira: enche em 6h, ralo esvazia em 12h: juntos enchem em 12h
t = 1/(F(1,6)-F(1,12)); assert t == 12
ex.append(num(3, C, "Uma torneira enche um tanque em 6 horas e um ralo esvazia-o em 12 horas. Com ambos abertos, em quantas horas se enche o tanque vazio?", t, "Por hora, enche 1/6 e esvazia 1/12: sobra 1/12 por hora, logo 12 horas.", ["1/6 − 1/12 = 1/12.", "Tempo: 12 horas."]))
# três irmãos dividem 1200 na razão 1:2:3 -> maior 600
ex.append(num(2, C, "Três irmãos dividem 1 200 Kz na razão 1 : 2 : 3. Quanto recebe o que fica com a maior parte?", F(1200,6)*3, "Total de partes: 6; cada parte é 200 Kz; a maior é 3 · 200 = 600 Kz.", ["1 + 2 + 3 = 6 partes.", "1200 ÷ 6 = 200.", "3 · 200 = 600."]))
# idades somam: soma de 3 consecutivos 78 -> 25,26,27: menor 25
ex.append(num(1, C, "A soma de três números inteiros consecutivos é 78. Qual é o menor?", 25, "n + (n + 1) + (n + 2) = 78 dá 3n + 3 = 78, n = 25.", ["3n + 3 = 78.", "n = 25."]))
ex.append(tf(2, C, "Se uma torneira enche um tanque em 3 h e outra, igual, também em 3 h, juntas enchem-no em 6 h.", False, "Juntas fazem o dobro do trabalho por hora, por isso demoram metade do tempo: 1,5 h.", ["Ritmo de cada uma: 1/3 por hora.", "Juntas: 2/3 por hora, ou seja, 1,5 h."]))
ex.append(mc(3, C, "Um preço sobe 20% e depois desce 20%. O preço final, comparado com o inicial, é…", ["5% … menor", "igual", "4% menor", "4% maior"], 2, "Fica 1,2 × 0,8 = 0,96 do preço inicial: 4% menor.", ["Sobe: × 1,2.", "Desce: × 0,8.", "1,2 · 0,8 = 0,96."]))
# fix option label
ex[-1]["options"][0]["label"] = "5% menor"
prb = lesson("problemas-de-raciocinio", "Problemas de raciocínio", "problemas-idades-trabalho-misturas", "Problemas clássicos: idades, trabalho, misturas e velocidades", "problemas-idades-trabalho-misturas-velocidades", "Resolve os problemas típicos de exame com um método único: escolher a incógnita, traduzir em equação e verificar.", 30,
 "Há problemas que aparecem em todos os exames: idades de pais e filhos, duas torneiras a encher um tanque, dois carros que se cruzam, misturas de soluções. À primeira vista parecem todos diferentes, mas todos se resolvem com o mesmo método: **escolher a incógnita, traduzir o texto em equação, resolver e verificar**.\n\nNesta aula vais treinar os cinco tipos mais comuns, com os truques que poupam tempo, como pensar em \"quanto faz por hora\" nos problemas de trabalho.",
 "O grande segredo é traduzir. Cada frase do problema vira uma igualdade: \"o triplo da idade\" é 3f; \"daqui a 6 anos\" soma 6 a **todas** as idades; \"misturam-se\" significa que a quantidade total de soluto antes e depois é a mesma.\n\nNos problemas de **trabalho**, pensa em ritmos: se o Pedro faz a parede em 6 h, faz 1/6 por hora; o Paulo faz 1/12. Juntos fazem 1/6 + 1/12 = 1/4 por hora, logo demoram 4 horas. Soma-se o que fazem **por hora**, nunca os tempos.\n\nNos de **velocidades**, quando dois corpos se aproximam as velocidades somam-se; quando um persegue outro, subtraem-se. E a velocidade média de ida e volta com velocidades diferentes **não** é a média das velocidades: é a distância total a dividir pelo tempo total.\n\n**Erros comuns:** (1) somar tempos em vez de ritmos; (2) esquecer de somar os anos a todas as idades; (3) calcular percentagens sucessivas somando-as (+20% e −20% não dá zero).",
 "Um **problema de equações** resolve-se em quatro passos: 1) definir a incógnita com unidade; 2) traduzir as condições do texto em equações; 3) resolver; 4) verificar no enunciado e responder com a unidade. Num problema de **trabalho**, se uma tarefa leva t horas a um agente, o seu ritmo é 1/t por hora e os ritmos somam-se. Numa **mistura**, a quantidade de substância pura conserva-se: soma das partes = parte do todo. Em **percentagens sucessivas**, multiplicam-se os fatores (1 + p).",
 "$$\\text{trabalho em conjunto: } \\frac1T=\\frac1{t_1}+\\frac1{t_2}$$\n\n$$\\text{velocidade média}=\\frac{\\text{distância total}}{\\text{tempo total}}$$\n\n$$\\text{mistura: } c_1V_1+c_2V_2=c_f(V_1+V_2)$$\n\n$$\\text{percentagens sucessivas: } P_f=P_i(1+p_1)(1+p_2)$$",
 "**Exemplo 1 (idades).** A Rita tem 4 anos mais do que a irmã e juntas somam 30. Se a irmã tem x, a Rita tem x + 4 e 2x + 4 = 30, logo x = 13 (a Rita tem 17).\n\n**Exemplo 2 (trabalho).** Duas máquinas imprimem um lote em 3 h e 6 h. Juntas: 1/3 + 1/6 = 1/2 por hora, logo 2 horas.\n\n**Exemplo 3 (velocidade).** Dois ciclistas partem do mesmo sítio em sentidos opostos a 12 e 18 km/h. Após 2 h estão a (12 + 18)·2 = 60 km.\n\n**Exemplo 4 (percentagens).** Um preço sobe 10% e depois mais 10%: 1,1 · 1,1 = 1,21, ou seja, sobe 21%, não 20%.",
 "Resolve connosco: **a mãe tem hoje 36 anos e o filho 6. Daqui a quantos anos a idade da mãe será o triplo da do filho?**\n\n1) Seja x o número de anos. Mãe: 36 + x; filho: 6 + x.\n\n2) Condição: 36 + x = 3(6 + x).\n\n3) Desenvolve: 36 + x = 18 + 3x.\n\n4) 18 = 2x, logo x = 9.\n\n5) Verifica: mãe 45, filho 15, e 45 = 3 · 15 ✓.",
 "**Duas torneiras e um ralo.** Uma torneira enche um depósito em 4 horas, outra em 6 horas, e um ralo esvazia-o em 12 horas. Com tudo aberto, quanto tempo leva a encher o depósito vazio?\n\nPista: 1/4 + 1/6 − 1/12 por hora.",
 "Consideras a competência dominada quando consegues: (1) traduzir frases em equações; (2) resolver problemas de idades, trabalho, velocidades e misturas; (3) somar ritmos em vez de tempos; (4) calcular velocidades médias e percentagens sucessivas corretamente; (5) verificar sempre a resposta no enunciado.", ex)

# ===== 4.3 Percentagens, descontos e juros =====
C = "exames.percentagens"
ex = []
ex.append(num(1, C, "Calcula 15% de 2 000 Kz.", F(15,100)*2000, "0,15 · 2000 = 300.", ["15% = 0,15.", "0,15 · 2000 = 300."]))
ex.append(num(1, C, "Um artigo de 5 000 Kz tem 20% de desconto. Quanto se paga, em Kz?", 5000*F(80,100), "Paga-se 80% do preço: 0,8 · 5000 = 4000.", ["100% − 20% = 80%.", "0,8 · 5000 = 4000."]))
ex.append(num(2, C, "Depois de um aumento de 25%, um salário passou a ser 50 000 Kz. Qual era o salário antes, em Kz?", F(50000)/F(125,100), "novo = antigo · 1,25, logo antigo = 50000 ÷ 1,25 = 40000.", ["50000 = x · 1,25.", "x = 40000."]))
ex.append(num(2, C, "Um preço passou de 8 000 para 9 200 Kz. De quantos por cento foi o aumento?", F(9200-8000,8000)*100, "Aumento: 1200. 1200 ÷ 8000 = 0,15, ou seja, 15%.", ["Aumento = 9200 − 8000 = 1200.", "1200/8000 = 0,15 → 15%."]))
# juros simples: 10000 a 5% ao ano 3 anos = 1500
ex.append(num(2, C, "Em juros simples, qual é o juro de 10 000 Kz a 5% ao ano durante 3 anos, em Kz?", 10000*F(5,100)*3, "J = C · i · t = 10000 · 0,05 · 3 = 1500.", ["J = C·i·t.", "10000 · 0,05 · 3 = 1500."]))
# juros compostos: 10000 a 10% 2 anos -> 12100
mont = 10000*F(11,10)**2; assert mont == 12100
ex.append(num(3, C, "Em juros compostos, qual é o montante de 10 000 Kz a 10% ao ano ao fim de 2 anos, em Kz?", mont, "M = C(1 + i)ⁿ = 10000 · 1,1² = 12100.", ["1,1² = 1,21.", "10000 · 1,21 = 12100."]))
# desconto sucessivo 20% e 10% -> 28% total: 1-0.72
dtot = 100*(1 - F(80,100)*F(90,100)); assert dtot == 28
ex.append(num(3, C, "Dois descontos sucessivos de 20% e de 10% equivalem a um desconto único de quantos por cento?", dtot, "0,8 · 0,9 = 0,72, logo paga-se 72% e o desconto único é 28%.", ["Fatores: 0,8 e 0,9.", "0,72 → desconto de 28%."]))
# lucro: comprou a 6000 vendeu a 7500 lucro % sobre custo = 25
ex.append(num(2, C, "Uma pessoa comprou um produto por 6 000 Kz e vendeu-o por 7 500 Kz. De quantos por cento foi o lucro sobre o custo?", F(1500,6000)*100, "Lucro: 1500. 1500 ÷ 6000 = 0,25, isto é, 25%.", ["Lucro = 7500 − 6000 = 1500.", "1500/6000 = 25%."]))
# mistura percentual: turma 40 alunos, 60% raparigas -> 24; saem 4 raparigas -> 20/36 = 5/9
ex.append(num(3, C, "Numa turma de 40 alunos, 60% são raparigas. Se 4 raparigas saírem da turma, que fração (irredutível) da turma passam a ser raparigas?", F(24-4, 40-4), "Raparigas: 24. Depois: 20 em 36 alunos = 5/9.", ["0,6 · 40 = 24.", "24 − 4 = 20 raparigas; 40 − 4 = 36 alunos.", "20/36 = 5/9."]))
# percentagem de percentagem: 50% de 40% = 20
ex.append(num(2, C, "Quanto é 50% de 40% de 600?", F(1,2)*F(40,100)*600, "0,5 · 0,4 · 600 = 120.", ["0,4 · 600 = 240.", "0,5 · 240 = 120."]))
ex.append(tf(2, C, "Um aumento de 50% seguido de uma descida de 50% devolve o preço inicial.", False, "1,5 · 0,5 = 0,75: o preço final é 75% do inicial.", ["Fatores: 1,5 e 0,5.", "Produto: 0,75."]))
ex.append(mc(2, C, "Um produto custa 1 000 Kz e sobe 30%. O novo preço é…", ["1 300 Kz", "1 030 Kz", "1 130 Kz", "1 003 Kz"], 0, "1000 · 1,30 = 1300 Kz.", ["30% de 1000 = 300.", "1000 + 300 = 1300."]))
pct = lesson("exames-de-admissao", "Percentagens de exame", "percentagens-descontos-juros", "Percentagens, descontos e juros nos exames", "percentagens-descontos-juros-exame", "Resolve percentagens, aumentos e descontos sucessivos, lucro e juros simples e compostos.", 30,
 "Numa loja anunciam \"30% de desconto\". No banco, falam de juros de 5% ao ano. Na fatura aparece o imposto. As **percentagens** estão em todo o lado e são das matérias que mais caem nos exames de admissão, porque medem se sabes raciocinar com números do dia a dia.\n\nNesta aula vais aprender o método dos **fatores** (1 + p), que resolve aumentos, descontos, sucessivos, lucros e juros com a mesma ideia.",
 "Dizer \"25%\" é dizer \"25 em cada 100\", ou seja, 0,25. Para saber quanto é 25% de 800 multiplicas 800 por 0,25. Para **aumentar** 25% multiplicas por 1,25 (o 1 é o preço original e 0,25 o aumento). Para **descontar** 25% multiplicas por 0,75.\n\nO fator torna tudo mecânico. Dois aumentos sucessivos de 10% não dão 20%, dão 1,1 · 1,1 = 1,21, ou seja, 21%, porque o segundo aumento incide sobre um preço já maior. Um aumento de 50% seguido de um desconto de 50% dá 1,5 · 0,5 = 0,75: perdes 25%.\n\nPara descobrir o valor **antes** de um aumento, divide pelo fator: se depois de +25% o preço é 50 000, o inicial é 50 000 ÷ 1,25 = 40 000.\n\n**Erros comuns:** (1) somar percentagens sucessivas; (2) calcular a variação sobre o valor errado (a percentagem é sempre sobre o valor inicial); (3) confundir lucro sobre o custo com lucro sobre o preço de venda.",
 "A **percentagem** p% é a razão p/100. Aplicar um **aumento** de p% a um valor V dá $V\\left(1+\\frac p{100}\\right)$; um **desconto** de p% dá $V\\left(1-\\frac p{100}\\right)$. A **variação percentual** é $\\frac{V_f-V_i}{V_i}\\times100\\%$. Em **juros simples**, o juro é $J=C\\,i\\,t$. Em **juros compostos**, o montante é $M=C(1+i)^t$, porque cada período rende sobre o capital já acrescido de juros.",
 "$$V_f=V_i(1\\pm p)\\qquad \\text{variação}=\\frac{V_f-V_i}{V_i}$$\n\n$$J=C\\cdot i\\cdot t\\qquad M=C(1+i)^t$$\n\n$$\\text{sucessivos: } F=F_1\\cdot F_2\\cdots$$\n\nMnemónica: **\"aumenta com 1 mais p, desconta com 1 menos p, e multiplica os fatores\"**.",
 "**Exemplo 1.** 18% de 3 500 = 0,18 · 3500 = 630.\n\n**Exemplo 2.** Um preço de 12 000 Kz sobe 15%: 12000 · 1,15 = 13 800 Kz.\n\n**Exemplo 3 (sucessivos).** Desconto de 10% e depois mais 10%: 0,9 · 0,9 = 0,81, ou seja, 19% de desconto total.\n\n**Exemplo 4 (juros).** 20 000 Kz a 4% ao ano durante 2 anos. Simples: 20000 · 0,04 · 2 = 1 600. Compostos: 20000 · 1,04² = 21 632, ou seja, 1 632 de juro.",
 "Resolve connosco: **uma loja compra um frigorífico por 60 000 Kz e quer um lucro de 30% sobre o custo, mais 5% de imposto no preço final. Qual é o preço de venda?**\n\n1) Preço com lucro: 60 000 · 1,30 = 78 000.\n\n2) Com imposto: 78 000 · 1,05 = 81 900.\n\n3) Resposta: 81 900 Kz.\n\n4) Verifica: o aumento total é 1,30 · 1,05 = 1,365, ou seja, 36,5%, e não 35%.",
 "**O desconto que engana.** Uma loja anuncia \"50% + 20% de desconto\". Será 70% de desconto? Calcula o desconto único e conta a diferença em kwanzas num artigo de 10 000 Kz.\n\nPista: fatores 0,5 e 0,8.",
 "Estarás pronto quando conseguires: (1) converter percentagens em fatores; (2) calcular aumentos, descontos e variações; (3) encadear percentagens sucessivas; (4) recuperar o valor inicial; (5) distinguir juros simples de compostos e calcular o lucro.", ex)

for i, d in enumerate([suc, prb, pct], start=1):
    write(4, i, d); print(d["lesson_slug"], len(d["exercises"]))

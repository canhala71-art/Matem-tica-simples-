"""Nível 2 — Módulo 4: Regra de três (aulas novas 10–13)."""
from n2h import *
SUB = 'regra-de-tres'

# ---------- RT1: identificar grandezas e montar tabela ----------
C = 'regra3.identificar'; ex = []
ex += [tf(1, C, "Para decidir se uma regra de três é direta ou inversa, perguntamos o que acontece a uma grandeza quando a outra aumenta.", True, "Se aumentam juntas na mesma proporção é direta; se uma aumenta e a outra diminui é inversa.", ["Direta: aumentam juntas. Inversa: uma sobe, outra desce."]),
       mc(1, C, "Qual das situações é de regra de três direta?", ["Mais litros de gasolina, mais Kz a pagar", "Mais pedreiros, menos dias de obra", "Maior velocidade, menos tempo de viagem", "Mais torneiras abertas, menos tempo para encher"], 0, "Preço e quantidade aumentam juntos. As outras três são inversas.", ["Qual aumenta junto?"]),
       num(1, C, "5 cadernos custam 1 250 Kz. Quanto custa 1 caderno (valor unitário), em Kz?", F(1250,5), "1 250 ÷ 5 = 250 Kz.", ["Divide o preço pela quantidade."])]
ex += [num(2, C, "Direta: 4 kg de arroz custam 3 200 Kz. Quanto custam 7 kg, em Kz?", F(3200*7,4), "Tabela: 4 kg → 3 200; 7 kg → x. x = 3 200 × 7 ÷ 4 = 5 600 Kz.", ["Setas no mesmo sentido.", "x = 5 600."]),
       num(2, C, "Direta: um carro faz 90 km com 6 L. Quantos litros gasta em 240 km?", F(6*240,90), "x = 6 × 240 ÷ 90 = 16 L.", ["90 km → 6 L; 240 km → x."]),
       num(2, C, "Direta: 3 pacotes de bolachas têm 36 bolachas. Quantas bolachas há em 8 pacotes?", F(36*8,3), "x = 36 × 8 ÷ 3 = 96.", ["Cada pacote: 12."]),
       num(2, C, "Direta: 15 m de tecido custam 22 500 Kz. Que comprimento se compra com 9 000 Kz, em m?", F(15*9000,22500), "x = 15 × 9 000 ÷ 22 500 = 6 m.", ["22 500 → 15; 9 000 → x."])]
ex += [num(3, C, "Direta: uma máquina produz 840 peças em 7 horas. Em quantas horas produz 1 560 peças? (Responde em horas, com decimais se necessário.)", F(7*1560,840), "x = 7 × 1 560 ÷ 840 = 13 h.", ["840 peças → 7 h.", "1 560 peças → x."]),
       num(3, C, "Direta: com 12 L de tinta pintam-se 90 m². Quantos litros de tinta são precisos para pintar 150 m²?", F(12*150,90), "x = 12 × 150 ÷ 90 = 20 L.", ["90 m² → 12 L.", "150 m² → x."]),
       tf(2, C, "Na regra de três direta, se a primeira grandeza triplica, a segunda também triplica.", True, "É isso que significa serem diretamente proporcionais: a razão é constante.", ["y/x constante."]),
       mc(3, C, "Numa regra de três direta com os dados «a → b» e «c → x», o valor de x é:", ["$\\frac{b\\times c}{a}$", "$\\frac{a\\times b}{c}$", "$\\frac{a\\times c}{b}$", "$a+b-c$"], 0, "De a/b = c/x tira-se x = b·c/a.", ["Produto cruzado."])]
A = std(SUB, 'Regra de três simples', 'regra-tres-simples', 'Regra de três: grandezas, tabelas e montagem da proporção', 'regra-tres-grandezas-tabelas-montagem',
 'Identifica as grandezas, organiza os dados em tabela e monta a proporção da regra de três.', 25,
 'identificar grandezas envolvidas, organizar os dados em tabela, decidir se a relação é direta ou inversa e montar a proporção.', 'razão, proporção e grandezas proporcionais.',
 'Se 4 kg de arroz custam 3 200 Kz, quanto custam 7 kg? Este tipo de pergunta aparece todos os dias no mercado. A **regra de três** é o método que permite resolvê-la com segurança.',
 "A **regra de três** serve para descobrir um valor desconhecido a partir de três valores conhecidos, quando duas grandezas são proporcionais.\n\n**Passo 1 — Identificar as grandezas.** No exemplo: quantidade de arroz (kg) e preço (Kz).\n\n**Passo 2 — Organizar numa tabela**, alinhando valores da mesma grandeza na mesma coluna e com as mesmas unidades:\n\n$$\\begin{array}{c|c}\\text{kg}&\\text{Kz}\\\\\\hline 4&3\\,200\\\\7&x\\end{array}$$\n\n**Passo 3 — Decidir a relação.** Se compro mais kg, pago mais Kz: as grandezas aumentam juntas, logo são **diretamente proporcionais**.\n\n**Passo 4 — Montar a proporção** e resolver pelo produto cruzado: $\\frac{4}{7}=\\frac{3\\,200}{x}$ → $4x=7\\times3\\,200$ → $x=5\\,600$ Kz.\n\n**Passo 5 — Verificar.** 1 kg custa $3\\,200\\div4=800$ Kz; 7 kg custam $7\\times800=5\\,600$ ✓. A resposta é razoável: 7 kg é mais de 4 kg, logo o preço é maior que 3 200 Kz.\n\n**Truque do valor unitário:** reduzir primeiro à unidade (1 kg) e depois multiplicar é outra forma de resolver, muito útil mentalmente.\n\n**Cuidados:** mesmas unidades em cada coluna; verificar sempre se faz sentido; não assumir direta sem pensar (veja a regra de três inversa na próxima aula).\n\n**Erros comuns:** pôr valores de grandezas diferentes na mesma coluna; montar a proporção ao contrário; esquecer a verificação.",
 'A **regra de três simples** relaciona duas grandezas proporcionais. Na **direta**, $\\frac{a}{b}=\\frac{c}{x}$ (setas no mesmo sentido): $x=\\frac{b\\,c}{a}$.',
 '$$\\begin{array}{c|c}A&B\\\\\\hline a&b\\\\c&x\\end{array}\\qquad\\text{direta: }\\ x=\\frac{b\\times c}{a}$$\n\n$a$ e $c$: valores da 1.ª grandeza; $b$: valor da 2.ª correspondente a $a$; $x$: valor procurado ($a\\ne0$).',
 ['4 kg custam 3 200 Kz; 7 kg: $x=\\frac{3\\,200\\times7}{4}=5\\,600$ Kz.',
  'Um carro faz 90 km com 6 L; em 240 km: $x=\\frac{6\\times240}{90}=16$ L.',
  '15 m de tecido custam 22 500 Kz; com 9 000 Kz: $x=\\frac{15\\times9\\,000}{22\\,500}=6$ m.',
  '12 L de tinta pintam 90 m²; para 150 m²: $x=\\frac{12\\times150}{90}=20$ L.',
  'Valor unitário: 5 cadernos custam 1 250 Kz; 1 caderno: 250 Kz; 8 cadernos: 2 000 Kz.',
  'Verificação por estimativa: 840 peças em 7 h; 1 560 peças é cerca do dobro, logo cerca do dobro das horas (13 h ✓).'],
 "Resolve connosco: **uma máquina produz 840 peças em 7 horas. Quantas horas precisa para 1 560 peças?**\n\n1) Tabela: 840 peças ↔ 7 h; 1 560 peças ↔ $x$.\n\n2) Mais peças, mais horas: direta.\n\n3) $x=\\frac{7\\times1\\,560}{840}=13$ h.\n\n4) Verifica: 840 ÷ 7 = 120 peças/h; $1\\,560\\div120=13$ ✓.",
 '**Desafio.** Um gerador gasta 18 L de gasóleo em 5 horas. Quanto gasta num dia inteiro de funcionamento (24 h)? E quantas horas funciona com 100 L? Resolve por regra de três e pelo valor unitário.',
 ['identificar as duas grandezas e organizar a tabela', 'decidir se a relação é direta', 'montar e resolver a proporção', 'verificar o resultado', 'usar o valor unitário como alternativa'], ex)
write(2, 10, A)

# ---------- RT2: regra de três inversa ----------
C = 'regra3.inversa'; ex = []
ex += [num(1, C, "Inversa: 6 operários fazem um muro em 10 dias. Quantos dias demoram 12 operários?", F(6*10,12), "6 × 10 = 12 × x → x = 5 dias.", ["Produto constante: 60.", "x = 60 ÷ 12."]),
       num(1, C, "Inversa: um carro a 60 km/h demora 4 h. A que velocidade demora 3 h?", F(60*4,3), "60 × 4 = 3 × v → v = 80 km/h.", ["Distância constante: 240 km."]),
       tf(1, C, "Na regra de três inversa, se uma grandeza duplica a outra reduz-se a metade.", True, "O produto fica constante.", ["x·y = k."])]
ex += [num(2, C, "Inversa: 8 torneiras enchem um tanque em 15 minutos. Quantas torneiras iguais são precisas para encher em 10 minutos?", F(8*15,10), "8 × 15 = n × 10 → n = 12.", ["Produto 120."]),
       num(2, C, "Inversa: um grupo de 20 pessoas consome uma reserva de comida em 18 dias. Em quantos dias consumiriam 30 pessoas?", F(20*18,30), "20 × 18 = 30 × x → x = 12 dias.", ["360 pessoas-dia."]),
       num(2, C, "Inversa: com 5 máquinas, uma tarefa demora 12 horas. Com 4 máquinas quantas horas demora?", F(5*12,4), "5 × 12 = 4 × x → x = 15 h.", ["Produto 60."]),
       num(2, C, "Inversa: uma viagem a 80 km/h demora 3,5 h. A que velocidade demora 4 h?", F(80*7,2)/4, "80 × 3,5 = 280 km; v = 280 ÷ 4 = 70 km/h.", ["Distância constante: 280 km."])]
ex += [num(3, C, "Inversa: 12 pedreiros constroem uma casa em 45 dias. Depois de 15 dias de trabalho saem 6 pedreiros. Em quantos dias, a contar da saída, terminam os restantes? (Pensa na parte que falta.)", F(30*12,6), "Restam 30 dias com 12 pedreiros = 360 pessoas-dia; com 6: 360 ÷ 6 = 60 dias.", ["Parte que falta: 30 dias × 12 pedreiros.", "360 ÷ 6 = 60."]),
       num(3, C, "Inversa: um poço enche um depósito com 4 bombas em 9 horas. Com 6 bombas quantas horas poupa?", 9 - F(4*9,6), "Com 6 bombas: 36 ÷ 6 = 6 h; poupa 9 − 6 = 3 h.", ["4 × 9 = 36.", "9 − 6."]),
       mc(2, C, "Qual é a forma correta de montar uma regra de três inversa «a → b» e «c → x»?", ["$a\\times b=c\\times x$", "$\\frac{a}{b}=\\frac{c}{x}$", "$a+b=c+x$", "$a\\times c=b\\times x$"], 0, "Inversa: produtos iguais, $ab=cx$, logo $x=\\frac{ab}{c}$.", ["Produto constante."]),
       tf(3, C, "Se 6 operários demoram 10 dias, então 12 operários demoram 20 dias.", False, "Mais operários, menos dias: 6 × 10 = 12 × x → x = 5 dias, e não 20.", ["Inversa."])]
A = std(SUB, 'Regra de três simples', 'regra-tres-simples', 'Regra de três simples inversa', 'regra-tres-simples-inversa',
 'Reconhece grandezas inversamente proporcionais e resolve problemas com a regra de três inversa.', 25,
 'reconhecer grandezas inversamente proporcionais e resolver problemas pela regra de três inversa.', 'regra de três direta e proporcionalidade inversa.',
 'Seis operários fazem um muro em 10 dias. E se forem doze? Não vai demorar 20 dias, mas **menos**. Esta é uma situação de regra de três **inversa**.',
 "Na regra de três **inversa**, as grandezas variam em sentidos opostos: quando uma **aumenta**, a outra **diminui**, na mesma proporção. O que fica constante é o **produto**.\n\nExemplos típicos: número de trabalhadores e dias de obra; velocidade e tempo (distância fixa); número de torneiras e tempo para encher; número de pessoas e dias que dura uma reserva de comida.\n\n**Como montar:** com a tabela $\\begin{array}{c|c}A&B\\\\\\hline a&b\\\\c&x\\end{array}$ numa relação inversa, $a\\times b=c\\times x$, portanto $x=\\frac{a\\times b}{c}$.\n\n**Passo a passo:** (1) identifica as grandezas; (2) organiza a tabela; (3) pergunta «se uma aumenta, a outra aumenta ou diminui?»; (4) se diminui, a relação é inversa e os **produtos são iguais**; (5) resolve e (6) verifica se o resultado faz sentido: com **mais** operários, **menos** dias.\n\n**Pensar com o «trabalho total»:** 6 operários × 10 dias = 60 «operários-dia». Qualquer combinação com produto 60 serve: 12 operários × 5 dias, 4 operários × 15 dias, 3 operários × 20 dias.\n\n**Mudanças a meio do trabalho:** calcula o trabalho que falta (em pessoas-dia) e divide pelo novo número de pessoas.\n\n**Erros comuns:** aplicar a direta por reflexo; verificar o resultado pelo sentido esquecendo-se de que deve ser menor/maior conforme o caso.",
 'Na **regra de três simples inversa**: $a\\times b=c\\times x$, logo $x=\\dfrac{a\\times b}{c}$ ($c\\ne0$). O produto das duas grandezas é constante.',
 '$$\\begin{array}{c|c}A&B\\\\\\hline a&b\\\\c&x\\end{array}\\qquad\\text{inversa: }\\ a\\,b=c\\,x\\iff x=\\frac{a\\times b}{c}$$',
 ['6 operários, 10 dias; 12 operários: $x=\\frac{6\\times10}{12}=5$ dias.',
  'Carro a 60 km/h demora 4 h; para 3 h: $v=\\frac{60\\times4}{3}=80$ km/h.',
  '8 torneiras enchem em 15 min; para 10 min: $n=\\frac{8\\times15}{10}=12$ torneiras.',
  '20 pessoas, comida para 18 dias; com 30 pessoas: $x=\\frac{20\\times18}{30}=12$ dias.',
  '5 máquinas, 12 h; com 4: $x=\\frac{5\\times12}{4}=15$ h.',
  'Mudança a meio: 12 pedreiros, 45 dias; após 15 dias faltam 30 dias × 12 = 360 pessoas-dia; com 6: $360\\div6=60$ dias.'],
 "Resolve connosco: **um autocarro demora 5 horas a 72 km/h. Quanto tempo demora a 90 km/h?**\n\n1) Mais velocidade, menos tempo: inversa.\n\n2) $72\\times5=90\\times t$.\n\n3) $t=\\frac{360}{90}=4$ h.\n\n4) Verifica: $90\\times4=360=72\\times5$ ✓ (e 4 h < 5 h).",
 '**Desafio.** Uma reserva de água dura 20 dias para 15 pessoas. Passados 8 dias chegam mais 9 pessoas. Quantos dias dura a água que sobra para as 24 pessoas?',
 ['reconhecer quando a relação é inversa', 'montar a igualdade dos produtos', 'resolver e verificar o sentido do resultado', 'usar o conceito de trabalho total', 'resolver problemas com mudanças a meio'], ex)
write(2, 11, A)

# ---------- RT3: regra de três composta ----------
C = 'regra3.composta'; ex = []
ex += [num(1, C, "10 operários fazem 20 m de muro em 5 dias. Quantos metros fazem 10 operários em 10 dias?", 40, "O tempo duplica e os operários ficam iguais: o muro duplica: 40 m.", ["Mesmo nº de operários, o dobro dos dias."]),
       num(1, C, "Uma torneira gasta 12 L em 3 minutos. Quantos litros gasta em 9 minutos?", 36, "Direta: 12 × 9 ÷ 3 = 36 L.", ["Triplo do tempo, triplo da água."]),
       tf(1, C, "A regra de três composta envolve mais de duas grandezas.", True, "Por isso se chama composta.", ["Três ou mais grandezas."])]
def comp(op1, d1, m1, op2, d2):  # direta em operários e dias para metros
    return F(m1*op2*d2, op1*d1)
ex += [num(2, C, "6 pedreiros constroem 30 m de parede em 5 dias. Quantos metros constroem 9 pedreiros em 4 dias?", comp(6,5,30,9,4), "Metros ∝ pedreiros × dias: 30 × 9 × 4 ÷ (6 × 5) = 36 m.", ["Mais pedreiros, mais metros; menos dias, menos metros.", "x = 1080 ÷ 30."]),
       num(2, C, "4 máquinas produzem 480 peças em 6 horas. Quantas peças produzem 6 máquinas em 8 horas?", comp(4,6,480,6,8), "480 × 6 × 8 ÷ (4 × 6) = 960 peças.", ["Ambas diretas."]),
       num(2, C, "3 camiões transportam 90 toneladas em 2 viagens. Quantas toneladas transportam 5 camiões em 3 viagens?", comp(3,2,90,5,3), "90 × 5 × 3 ÷ (3 × 2) = 225 t.", ["Ambas diretas."]),
       num(2, C, "5 trabalhadores, trabalhando 8 horas por dia, acabam uma obra em 12 dias. Quantos dias demoram 6 trabalhadores a trabalhar 10 horas por dia?", F(12*5*8,6*10), "Trabalho total: 5 × 8 × 12 = 480 homem-hora; com 6 × 10 = 60 por dia: 480 ÷ 60 = 8 dias.", ["Trabalhadores e horas: inversas com os dias.", "480 ÷ 60 = 8."])]
ex += [num(3, C, "20 operários, a trabalhar 6 horas por dia, constroem 300 m de estrada em 15 dias. Quantos metros constroem 30 operários a trabalhar 8 horas por dia durante 10 dias?", F(300*30*8*10,20*6*15), "Metros ∝ operários × horas × dias: 300 × (30·8·10) ÷ (20·6·15) = 400 m.", ["Compara cada grandeza com os metros: todas diretas.", "x = 400."]),
       num(3, C, "Um depósito é enchido por 3 torneiras iguais em 4 horas, a debitar 20 L/min cada. Quantas horas demoram 6 torneiras a debitar 10 L/min cada?", F(3*4*20,6*10), "Volume = n × débito × tempo: 3·20·4 = 240 unid.; com 6·10 = 60: 240 ÷ 60 = 4 h.", ["Volume constante.", "x = 4."]),
       tf(3, C, "Numa regra de três composta, cada grandeza deve ser comparada com a grandeza onde está o x, uma de cada vez.", True, "Cada razão é direta ou inversa em relação à grandeza do x, e o x calcula-se multiplicando as razões.", ["Compara par a par."]),
       mc(2, C, "Para 8 pessoas a trabalhar 6 h/dia fazem um trabalho em 10 dias. Com 12 pessoas e 8 h/dia, o número de dias:", ["Diminui (mais pessoas e mais horas)", "Aumenta", "Fica igual", "Não se pode saber"], 0, "Mais pessoas e mais horas por dia: o trabalho acaba mais cedo.", ["Inversas com os dias."])]
A = std(SUB, 'Regra de três composta', 'regra-tres-composta', 'Regra de três composta', 'regra-tres-composta',
 'Resolve problemas com três ou mais grandezas pela regra de três composta.', 35,
 'resolver problemas com três ou mais grandezas pela regra de três composta, comparando cada grandeza com a do valor desconhecido.', 'regra de três simples, direta e inversa.',
 'Uma obra depende de vários fatores ao mesmo tempo: número de pedreiros, horas por dia e dias de trabalho. A regra de três **composta** permite lidar com todos de forma organizada.',
 "A **regra de três composta** relaciona **três ou mais** grandezas. O método é sempre o mesmo:\n\n**1) Tabela.** Coloca em linhas os valores conhecidos e a incógnita $x$.\n\n**2) Compara cada grandeza com a do $x$**, mantendo as outras fixas, e decide: direta ou inversa?\n\n**3) Escreve as razões.** Para uma grandeza **direta** com a do $x$, a razão mantém-se na mesma ordem; para **inversa**, inverte-se.\n\n**4) Resolve:** $\\frac{x}{\\text{valor conhecido}}=\\text{razão}_1\\times\\text{razão}_2\\times\\cdots$.\n\nExemplo: 6 pedreiros constroem 30 m de parede em 5 dias. Quantos metros constroem 9 pedreiros em 4 dias? Metros crescem com pedreiros (direta) e com dias (direta):\n\n$$\\frac{x}{30}=\\frac{9}{6}\\times\\frac{4}{5}\\Rightarrow x=30\\times\\frac{36}{30}=36\\text{ m}$$\n\n**Outro exemplo, com inversa:** 5 trabalhadores, 8 h/dia, acabam em 12 dias. Com 6 trabalhadores e 10 h/dia, quantos dias? Mais trabalhadores e mais horas dão **menos** dias (inversas com os dias):\n\n$$\\frac{x}{12}=\\frac{5}{6}\\times\\frac{8}{10}\\Rightarrow x=12\\times\\frac{40}{60}=8\\text{ dias}$$\n\n**Atalho útil:** pensa no «trabalho total», por exemplo trabalhadores × horas × dias = 480 homem-hora. Qualquer combinação com o mesmo produto faz o mesmo trabalho.\n\n**Verificação:** estima o sentido do resultado (deve ser maior ou menor?) e confere por outra via.\n\n**Erros comuns:** comparar duas grandezas ao mesmo tempo (sem manter as outras fixas); trocar direta por inversa; esquecer de inverter a razão.",
 'A **regra de três composta** resolve $x$ multiplicando as razões de cada grandeza com a do $x$: diretas na mesma ordem e inversas invertidas.',
 '$$\\frac{x}{v}=r_1\\times r_2\\times\\cdots\\times r_n$$\n\n$v$: valor conhecido da mesma grandeza do $x$; $r_i$: razão de cada outra grandeza (direta: $\\frac{\\text{novo}}{\\text{inicial}}$; inversa: $\\frac{\\text{inicial}}{\\text{novo}}$).',
 ['6 pedreiros, 30 m, 5 dias → 9 pedreiros, 4 dias: $x=30\\times\\frac{9}{6}\\times\\frac{4}{5}=36$ m.',
  '4 máquinas, 480 peças, 6 h → 6 máquinas, 8 h: $x=480\\times\\frac{6}{4}\\times\\frac{8}{6}=960$ peças.',
  '3 camiões, 90 t, 2 viagens → 5 camiões, 3 viagens: $x=90\\times\\frac{5}{3}\\times\\frac{3}{2}=225$ t.',
  '5 trabalhadores, 8 h/dia, 12 dias → 6 trabalhadores, 10 h/dia: $x=12\\times\\frac{5}{6}\\times\\frac{8}{10}=8$ dias.',
  '20 operários, 6 h, 15 dias, 300 m → 30 operários, 8 h, 10 dias: $x=300\\times\\frac{30}{20}\\times\\frac{8}{6}\\times\\frac{10}{15}=400$ m.',
  'Trabalho total: $5\\times8\\times12=480$ homem-hora; com $6\\times10=60$ homem-hora por dia: $480\\div60=8$ dias.'],
 "Resolve connosco: **12 operários, a trabalhar 8 horas por dia, constroem uma casa em 30 dias. Quantos dias demoram 16 operários a trabalhar 6 horas por dia?**\n\n1) Mais operários → menos dias (inversa). Menos horas por dia → mais dias (inversa).\n\n2) $\\frac{x}{30}=\\frac{12}{16}\\times\\frac{8}{6}$.\n\n3) $x=30\\times\\frac{96}{96}=30$ dias.\n\n4) Verifica com o trabalho total: $12\\times8\\times30=2\\,880$ e $16\\times6\\times30=2\\,880$ ✓.",
 '**Desafio.** Uma fábrica com 15 máquinas produz 3 000 garrafas em 8 horas. Quantas máquinas são precisas para produzir 4 500 garrafas em 6 horas? Resolve por regra de três composta e confirma com «garrafas por máquina por hora».',
 ['organizar os dados numa tabela de várias grandezas', 'comparar cada grandeza com a do x', 'decidir direta ou inversa e inverter razões', 'resolver e verificar com o trabalho total', 'interpretar o resultado'], ex)
write(2, 12, A)

# ---------- RT4: problemas com contexto angolano ----------
C = 'regra3.problemas'; ex = []
ex += [num(1, C, "Num candongueiro, 4 passageiros pagam 2 400 Kz no total pelo mesmo trajeto (preço igual para todos). Quanto pagam 7 passageiros, em Kz?", F(2400*7,4), "Preço por pessoa: 600 Kz; 7 × 600 = 4 200 Kz.", ["2 400 ÷ 4 = 600."]),
       num(1, C, "Um litro de óleo custa 1 800 Kz. Quanto custam 2,5 L, em Kz?", F(1800*5,2), "1 800 × 2,5 = 4 500 Kz.", ["Direta."]),
       num(1, C, "Um tanque gasta 30 L de água por dia. Quantos litros gasta em 14 dias?", 30*14, "30 × 14 = 420 L.", ["Direta."])]
ex += [num(2, C, "Um salário de 180 000 Kz por mês. Quanto se ganha em 5 meses, em Kz?", 180000*5, "Direta: 180 000 × 5 = 900 000 Kz.", ["Mês → Kz."]),
       num(2, C, "Um trabalhador ganha 12 000 Kz por 3 dias de trabalho. Quanto ganha em 22 dias, em Kz?", F(12000*22,3), "x = 12 000 × 22 ÷ 3 = 88 000 Kz.", ["12 000 ÷ 3 = 4 000 por dia."]),
       num(2, C, "6 pedreiros constroem um muro em 12 dias. Para acabar em 8 dias, quantos pedreiros são precisos?", F(6*12,8), "Inversa: 6 × 12 = 8 × n → n = 9.", ["Produto 72."]),
       num(2, C, "Numa obra, 50 sacos de cimento chegam para 400 m² de reboco. Quantos sacos para 640 m²?", F(50*640,400), "Direta: 50 × 640 ÷ 400 = 80 sacos.", ["50 sacos → 400 m²."])]
ex += [num(3, C, "O consumo de eletricidade de uma casa foi 240 kWh em 30 dias. Quantos kWh se esperam em 45 dias, com o mesmo ritmo?", F(240*45,30), "Direta: 240 × 45 ÷ 30 = 360 kWh.", ["8 kWh por dia."]),
       num(3, C, "Uma mercearia compra 40 kg de farinha por 28 000 Kz e vende-os com 25% de lucro sobre o custo. Qual é o preço de venda total, em Kz?", 28000*F(125,100), "28 000 × 1,25 = 35 000 Kz.", ["Lucro 25% de 28 000 = 7 000.", "28 000 + 7 000."]),
       num(3, C, "4 pessoas com 1 800 L de água têm reserva para 15 dias. Quantos dias dura a água para 6 pessoas?", F(4*15,6), "Inversa: 4 × 15 = 6 × x → x = 10 dias.", ["Produto 60."]),
       mc(2, C, "Para saber se um problema é de regra de três inversa, devemos perguntar:", ["Se uma grandeza aumenta, a outra diminui?", "Se os números são inteiros?", "Se há três valores?", "Se há Kz no problema?"], 0, "Inversa: uma sobe e a outra desce.", ["Direção da variação."])]
A = std(SUB, 'Problemas de regra de três', 'regra-tres-problemas', 'Problemas de regra de três da vida real (Angola)', 'regra-tres-problemas-vida-real-angola',
 'Aplica a regra de três em compras, salários, transportes, construção, água e energia, com verificação.', 30,
 'resolver problemas contextualizados com regra de três (simples e composta), verificar resultados e justificar o raciocínio.', 'regra de três direta, inversa e composta.',
 'Preços no mercado, salários, candongueiros, obras, água, eletricidade: a regra de três está em todo o lado. Esta aula é de treino com situações da vida em Angola.',
 "**Método em 5 passos** para qualquer problema:\n\n1) **Ler e sublinhar** os dados e o que se pede; escreve as unidades.\n\n2) **Tabela** com as grandezas e o $x$.\n\n3) **Direta ou inversa?** Testa com um caso simples (se o dobro de pedreiros, o tempo duplica ou reduz-se a metade?).\n\n4) **Montar e resolver** (produto cruzado para direta; produtos iguais para inversa).\n\n5) **Verificar:** (a) o resultado tem sentido (maior ou menor do que devia ser)? (b) as unidades estão certas? (c) outra via dá o mesmo?\n\n**Situações típicas:**\n\n**Compras e vendas:** preço proporcional à quantidade (direta). Preço por unidade ajuda a comparar.\n\n**Salários:** pagamento proporcional aos dias ou horas trabalhadas (direta).\n\n**Transportes:** distância e combustível (direta); velocidade e tempo (inversa).\n\n**Construção civil:** número de pedreiros e dias (inversa); cimento e área (direta); homens × horas × dias (composta).\n\n**Água e energia:** consumo proporcional ao tempo (direta); número de pessoas e dias que a reserva dura (inversa).\n\n**Percentagens e lucro:** com 25% de lucro sobre o custo, preço de venda = custo × 1,25.\n\n**Dica de segurança:** quando os números são grandes, estima primeiro (arredonda) para detetar um erro grosseiro.\n\n**Erros comuns:** ler mal o enunciado e trocar as colunas; direta por inversa; ignorar a verificação final.",
 'Em problemas de regra de três: **direta** $\\to x=\\frac{b\\,c}{a}$; **inversa** $\\to x=\\frac{a\\,b}{c}$; **composta** $\\to$ produto das razões.',
 '$$\\text{direta: }\\frac{x}{b}=\\frac{c}{a}\\qquad\\text{inversa: }\\frac{x}{b}=\\frac{a}{c}\\qquad\\text{lucro: }V=C\\left(1+\\frac{p}{100}\\right)$$\n\n$C$: custo; $V$: preço de venda; $p$: percentagem de lucro.',
 ['Candongueiro: 4 passageiros pagam 2 400 Kz; 7 passageiros: $\\frac{2\\,400\\times7}{4}=4\\,200$ Kz.',
  'Salário: 12 000 Kz por 3 dias; 22 dias: $\\frac{12\\,000\\times22}{3}=88\\,000$ Kz.',
  'Obra: 6 pedreiros em 12 dias; para 8 dias: $n=\\frac{6\\times12}{8}=9$ pedreiros.',
  'Construção: 50 sacos para 400 m²; para 640 m²: $\\frac{50\\times640}{400}=80$ sacos.',
  'Eletricidade: 240 kWh em 30 dias; 45 dias: $\\frac{240\\times45}{30}=360$ kWh.',
  'Água: 4 pessoas, 15 dias; 6 pessoas: $\\frac{4\\times15}{6}=10$ dias.'],
 "Resolve connosco: **uma obra tem 8 trabalhadores e demora 20 dias. Ao fim de 5 dias contratam-se mais 4 trabalhadores. Em quantos dias acaba a obra, contando desde o início?**\n\n1) Trabalho total: $8\\times20=160$ trabalhador-dia.\n\n2) Feitos: $8\\times5=40$; faltam $160-40=120$.\n\n3) Com 12 trabalhadores: $120\\div12=10$ dias.\n\n4) Total: $5+10=15$ dias. Verifica: $40+12\\times10=160$ ✓.",
 '**Desafio.** O gasóleo de um gerador custa 450 Kz/L e o gerador gasta 3 L por hora. Uma loja precisa dele 6 horas por dia, 26 dias por mês. Quanto gasta por mês? E se o preço subir 10%?',
 ['seguir o método dos 5 passos', 'distinguir direta, inversa e composta', 'resolver problemas de compras, salários e obras', 'verificar com estimativa e outra via', 'justificar a resposta com unidades'], ex)
write(2, 13, A)
print('M4 ok')

from common import *

# ============ 1. Equações do 1.º grau ============
def lin(a, b, c, d=0, e=0):
    """a*x + b = c*x + d  ->  x"""
    x = F(d - b, a - c); assert a*x + b == c*x + d; return x

C = "equacoes.primeiro_grau"
ex = []
for a, b, c_, d_ in [(1, 9, 0, 21), (1, -7, 0, 13)]:
    x = lin(a, b, c_, d_)
    ex.append(num(1, C, f"Resolve a equação ${'x' if a==1 else str(a)+'x'}{'+' if b>0 else '-'}{abs(b)}={d_}$.", x,
        f"Passa o {b if b>0 else b} para o outro lado com a operação inversa: x = {d_} {'-' if b>0 else '+'} {abs(b)} = {T(x)}.",
        [f"Operação inversa de {'somar' if b>0 else 'subtrair'} {abs(b)}: {'subtrair' if b>0 else 'somar'} {abs(b)} aos dois lados.", f"x = {T(x)}."]))
ex.append(num(1, C, "Resolve $4x=36$.", lin(4,0,0,36), "Divide os dois lados por 4: x = 36 ÷ 4 = 9.", ["Para desfazer \"×4\", divide por 4.", "x = 9."]))
for a, b, d_ in [(3, 5, 26), (5, -8, 17)]:
    x = lin(a, b, 0, d_)
    ex.append(num(2, C, f"Resolve ${a}x{'+' if b>0 else '-'}{abs(b)}={d_}$.", x,
        f"Primeiro {'subtrai' if b>0 else 'soma'} {abs(b)} aos dois lados e depois divide por {a}: x = {T(x)}.",
        [f"{a}x = {d_} {'-' if b>0 else '+'} {abs(b)} = {a*x}", f"x = {a*x} ÷ {a} = {T(x)}"]))
x = lin(2, 7, 1, 15)
ex.append(num(2, C, "Resolve $2x+7=x+15$.", x, "Junta os x do mesmo lado: 2x − x = 15 − 7, logo x = 8.",
    ["Passa x para a esquerda (subtrai x aos dois lados): x + 7 = 15.", "Subtrai 7: x = 8."]))
x = lin(7, -4, 3, 20)
ex.append(num(3, C, "Resolve $7x-4=3x+20$.", x, "7x − 3x = 20 + 4, ou seja, 4x = 24 e x = 6.",
    ["Agrupa os termos com x à esquerda e os números à direita: 7x − 3x = 20 + 4.", "4x = 24.", "x = 24 ÷ 4 = 6."]))
# 3(x-2) = 2x+5 -> 3x-6 = 2x+5
x = lin(3, -6, 2, 5)
ex.append(num(3, C, "Resolve $3(x-2)=2x+5$.", x, "Aplica a propriedade distributiva: 3x − 6 = 2x + 5, logo x = 11.",
    ["Distribui o 3: 3x − 6 = 2x + 5.", "3x − 2x = 5 + 6.", "x = 11."]))
# problema: 3 caixas + 500 transporte = 3500
x = lin(3, 500, 0, 3500)
ex.append(num(2, C, "A Dona Ana pagou 3 caixas de tomate iguais e mais 500 Kz de transporte. Gastou 3 500 Kz no total. Quanto custa cada caixa, em Kz?", x,
    "3x + 500 = 3 500, então 3x = 3 000 e x = 1 000.", ["Escolhe a incógnita: x = preço de uma caixa.", "Equação: 3x + 500 = 3500.", "3x = 3000, logo x = 1000 Kz."]))
x = lin(1, 2000, 0, 0) if False else F(6500-2000, 750)
assert x == 6
ex.append(num(3, C, "O Paulo tem 2 000 Kz e poupa 750 Kz por semana. Ao fim de quantas semanas terá 6 500 Kz?", x,
    "2000 + 750s = 6500, logo 750s = 4500 e s = 6.", ["Equação: 2000 + 750·s = 6500.", "750·s = 4500.", "s = 4500 ÷ 750 = 6 semanas."]))
ex.append(tf(1, C, "A solução de $2x+3=11$ é $x=4$.", 2*4+3 == 11, "Substituindo: 2·4 + 3 = 11. Está certo.", ["Substitui x por 4.", "2·4 + 3 = 11 ✓."]))
ex.append(mc(2, C, "Na resolução de $5x-10=20$, um aluno escreveu $5x=10$. Qual foi o erro?",
    ["Subtraiu 10 em vez de somar 10 aos dois lados", "Dividiu por 5 cedo demais", "Trocou o sinal do 20", "Não houve erro"], 0,
    "Para desfazer \"−10\" soma-se 10 aos dois lados: 5x = 30 e x = 6.", ["A operação inversa de −10 é +10.", "5x = 20 + 10 = 30.", "x = 6."]))
assert lin(5, -10, 0, 20) == 6

write(2, 1, {
 "subject": "equacoes", "topic_title": "Equações do 1.º grau", "topic_slug": "equacoes-primeiro-grau",
 "lesson_title": "Equações do 1.º grau: descobrir o valor escondido", "lesson_slug": "equacoes-primeiro-grau",
 "summary": "Resolve equações com uma incógnita usando a ideia da balança e as operações inversas.", "minutes": 25,
 "blocks": {
  "introduction": "Na praça, a Dona Ana comprou 3 caixas de tomate iguais e ainda pagou 500 Kz de transporte. No fim, gastou 3 500 Kz. Quanto custou cada caixa? Repara: não sabemos o preço da caixa, mas sabemos como tudo se liga. Esse valor escondido chama-se **incógnita** e costumamos chamar-lhe x.\n\nNesta aula vais aprender a transformar uma história como esta numa equação e a resolvê-la em poucos passos. No fim, vais conseguir resolver equações do 1.º grau, mesmo com x dos dois lados, e confirmar sozinho se a resposta está certa.",
  "intuition": "Imagina uma balança de dois pratos em equilíbrio. Num prato está \"3x + 500\" e no outro \"3 500\". A regra de ouro: **tudo o que fazes a um prato tens de fazer ao outro**, senão a balança desequilibra. Se tiras 500 de um lado, tiras 500 do outro. Se dividires um prato em 3 partes iguais, tens de dividir o outro também.\n\nResolver uma equação é isto: ir desfazendo, pela ordem contrária, as operações que foram feitas ao x, até ele ficar sozinho. A \"operação inversa\" de somar é subtrair, a de multiplicar é dividir (e vice-versa). Em 3x + 500 = 3 500 primeiro desfazemos o +500 (subtraímos 500 aos dois lados) e depois o ×3 (dividimos por 3).\n\nQuando há x dos dois lados, por exemplo 5x + 2 = 2x + 17, o objetivo é o mesmo: juntar os x num prato e os números no outro.\n\n**Erros comuns:** (1) fazer a operação só de um lado da igualdade; (2) trocar o sinal ao \"passar\" um termo (se está a somar 500, ao passar fica −500); (3) dividir só o termo do x e esquecer o outro lado. Defesa simples: no fim, **substitui o valor encontrado na equação original**; se os dois lados derem o mesmo número, acertaste.",
  "definition": "Uma **equação do 1.º grau com uma incógnita** é uma igualdade que pode ser escrita na forma $ax+b=c$ (ou $ax+b=cx+d$), em que a incógnita x aparece com expoente 1. A **solução** é o número que, colocado no lugar de x, torna a igualdade verdadeira. Duas equações são **equivalentes** quando têm a mesma solução; somar, subtrair, multiplicar ou dividir os dois lados pelo mesmo número (diferente de zero) dá sempre uma equação equivalente.",
  "formulas": "$$ax+b=c \;\\Longrightarrow\; x=\\frac{c-b}{a}\\quad (a\\neq 0)$$\n\n$$ax+b=cx+d \;\\Longrightarrow\; (a-c)\\,x=d-b \;\\Longrightarrow\; x=\\frac{d-b}{a-c}$$\n\nMnemónica: **\"termos com x para um lado, números para o outro, depois divide\"**. Prova real: substitui o resultado na equação inicial.",
  "worked_example": "**Exemplo 1.** Resolve $x+7=15$.\n\nO x está a somar 7. Desfazemos subtraindo 7 aos dois lados: $x=15-7=8$. Prova: 8 + 7 = 15 ✓.\n\n**Exemplo 2.** Resolve $3x-4=11$.\n\n**Passo 1.** Soma 4 aos dois lados: $3x=15$.\n\n**Passo 2.** Divide por 3: $x=5$. Prova: 3·5 − 4 = 11 ✓.\n\n**Exemplo 3.** Resolve $5x+2=2x+17$.\n\n**Passo 1.** Subtrai 2x aos dois lados: $3x+2=17$.\n\n**Passo 2.** Subtrai 2: $3x=15$.\n\n**Passo 3.** Divide por 3: $x=5$. Prova: 5·5 + 2 = 27 e 2·5 + 17 = 27 ✓.\n\n**Exemplo 4 (problema).** Um táxi cobra 400 Kz de bandeirada mais 150 Kz por quilómetro. Uma corrida custou 1 600 Kz. Quantos quilómetros foram?\n\nEquação: $400+150x=1600$. Subtrai 400: $150x=1200$. Divide por 150: $x=8$. Foram 8 km.",
  "guided_exercise": "Vamos resolver juntos: **o Paulo tem 2 000 Kz e poupa 750 Kz por semana. Quando terá 6 500 Kz?**\n\n1) Qual é a incógnita? O número de semanas, s.\n\n2) Que equação traduz a história? $2000+750s=6500$.\n\n3) Que operação desfazemos primeiro? O +2000: subtrai 2000 aos dois lados e fica $750s=4500$.\n\n4) E depois? Divide por 750: $s=6$.\n\n5) Prova: 2000 + 750·6 = 2000 + 4500 = 6500 ✓. Resposta: ao fim de 6 semanas.",
  "independent_exercise": INDEP,
  "challenge": "**Adivinha o número.** Pensei num número, multipliquei-o por 4 e subtraí 6. O resultado é igual ao dobro do número somado com 8. Qual é o número?\n\nPista: se o número é x, o dobro do número somado com 8 escreve-se $2(x+4)$ ou $2x+8$. Constrói a equação e resolve-a. Confirma depois com a prova real!",
  "assessment": "Consideras esta competência dominada quando consegues: (1) resolver $ax+b=c$ sem errar sinais; (2) resolver equações com x dos dois lados; (3) traduzir um problema simples numa equação e interpretar o resultado com a unidade certa; (4) fazer a prova real. Acertar de forma consistente em exercícios fáceis, médios e difíceis é o que conta, e não a rapidez."
 },
 "exercises": ex})
print("equacoes ok", len(ex))

# ============ 2. Regra de três simples ============
def direta(a, b, c):  # a -> b ; c -> ?
    return F(b) * F(c) / F(a)
def inversa(a, b, c):  # a -> b ; c -> ?   (a*b = c*?)
    return F(a) * F(b) / F(c)

C = "regra_de_tres.simples"
assert direta(5, 4500, 8) == 7200 and inversa(6, 10, 15) == 4
ex = []
for a, b, c_ in [(2, 600, 5), (4, 1000, 10)]:
    r = direta(a, b, c_)
    ex.append(num(1, C, f"{a} pães custam {b} Kz. Quanto custam {c_} pães (ao mesmo preço)?", r,
        f"É diretamente proporcional: preço de 1 pão = {b} ÷ {a} = {T(F(b,a))} Kz; {c_} pães = {T(r)} Kz.",
        [f"Preço de 1 pão: {b} ÷ {a} = {T(F(b,a))}.", f"{c_} pães: {c_} × {T(F(b,a))} = {T(r)} Kz."]))
r = direta(5, 4500, 8)
ex.append(num(2, C, "5 kg de arroz custam 4 500 Kz. Quanto custam 8 kg?", r,
    "Quantidade e preço aumentam juntos (diretamente proporcionais): 4500 ÷ 5 = 900 por kg; 900 × 8 = 7 200.",
    ["Monta a tabela: 5 kg → 4500; 8 kg → x.", "Multiplica em cruz: 5·x = 8·4500.", "x = 36000 ÷ 5 = 7200 Kz."]))
r = direta(3, 45, 7)
ex.append(num(2, C, "Um carro gasta 3 litros de gasolina em 45 km. Quantos quilómetros faz com 7 litros?", r,
    "Quanto mais litros, mais quilómetros: 45 ÷ 3 = 15 km por litro; 15 × 7 = 105 km.", ["15 km por litro.", "7 × 15 = 105 km."]))
r = inversa(6, 10, 15)
ex.append(num(2, C, "6 pedreiros constroem um muro em 10 dias. Quantos dias demorariam 15 pedreiros, ao mesmo ritmo?", r,
    "Mais pedreiros, menos dias (grandezas inversamente proporcionais): 6 × 10 = 60 \"pedreiros-dia\"; 60 ÷ 15 = 4 dias.",
    ["O trabalho total é fixo: 6 × 10 = 60.", "Com 15 pedreiros: 60 ÷ 15 = 4 dias."]))
r = inversa(60, 4, 80)
ex.append(num(3, C, "A 60 km/h uma viagem demora 4 horas. A 80 km/h, quantas horas demora?", r,
    "Velocidade e tempo são inversamente proporcionais: 60 × 4 = 240 km; 240 ÷ 80 = 3 horas.", ["Distância = 60 × 4 = 240 km.", "Tempo = 240 ÷ 80 = 3 h."]))
r = inversa(4, 12, 6)
ex.append(num(3, C, "4 torneiras iguais enchem um tanque em 12 horas. Em quantas horas o encheriam 6 torneiras?", r,
    "Mais torneiras, menos tempo: 4 × 12 = 48; 48 ÷ 6 = 8 horas.", ["Produto constante: 48.", "48 ÷ 6 = 8 h."]))
r = direta(12, 18000, 20)
ex.append(num(3, C, "12 cadernos custam 18 000 Kz. Qual o preço de 20 cadernos?", r,
    "18 000 ÷ 12 = 1 500 por caderno; 1 500 × 20 = 30 000 Kz.", ["Preço de 1 caderno: 1500 Kz.", "20 × 1500 = 30000 Kz."]))
ex.append(mc(2, C, "Em qual destas situações usas regra de três INVERSA?",
    ["Mais camiões a descarregar, menos horas para acabar", "Mais kg de peixe, mais Kz a pagar", "Mais litros de água, mais tempo a encher", "Mais metros de tecido, mais preço"], 0,
    "Quando uma grandeza aumenta e a outra diminui (mantendo o trabalho/total fixo), é inversa.", ["Pergunta-te: se uma sobe, a outra sobe ou desce?", "Aqui, mais camiões → menos horas → inversa."]))
ex.append(tf(1, C, "Se 3 laranjas custam 150 Kz, então 6 laranjas custam 300 Kz.", direta(3,150,6) == 300, "6 é o dobro de 3, logo o preço também dobra: 300 Kz.", ["6 = 2 × 3.", "2 × 150 = 300."]))
ex.append(num(2, C, "Uma receita para 4 pessoas leva 600 g de farinha. Quantos gramas são precisos para 10 pessoas?", direta(4, 600, 10),
    "600 ÷ 4 = 150 g por pessoa; 150 × 10 = 1 500 g.", ["150 g por pessoa.", "10 × 150 = 1500 g."]))

write(2, 2, {
 "subject": "regra-de-tres", "topic_title": "Regra de três simples", "topic_slug": "regra-de-tres-simples",
 "lesson_title": "Regra de três simples: direta e inversa", "lesson_slug": "regra-de-tres-simples",
 "summary": "Resolve problemas de proporcionalidade, quer as grandezas subam juntas, quer uma suba e a outra desça.", "minutes": 25,
 "blocks": {
  "introduction": "No mercado, 5 kg de arroz custam 4 500 Kz. E se precisares de 8 kg, quanto vais pagar? Ou: seis pedreiros acabam um muro em 10 dias; se chamares mais nove pedreiros, em quantos dias ficará pronto? Estas perguntas aparecem todos os dias, em compras, obras, viagens e cozinha.\n\nA **regra de três simples** é a ferramenta para as resolver: conhecendo três valores, descobre-se o quarto. No fim desta aula vais saber decidir se o problema é de proporcionalidade **direta** ou **inversa** e resolvê-lo com segurança.",
  "intuition": "O segredo está numa pergunta que deves fazer sempre antes de contar: **se uma grandeza aumenta, a outra aumenta ou diminui?**\n\nSe aumentam juntas (mais arroz, mais dinheiro), a relação é **direta**. Uma maneira fácil de pensar é voltar à unidade: 4 500 ÷ 5 = 900 Kz por quilo; para 8 quilos, 8 × 900 = 7 200 Kz.\n\nSe uma sobe e a outra desce (mais pedreiros, menos dias), a relação é **inversa**. Aqui o que fica fixo é o trabalho total: 6 pedreiros × 10 dias = 60 \"dias de pedreiro\". Com 15 pedreiros, 60 ÷ 15 = 4 dias.\n\n**Erros comuns:** (1) aplicar sempre a regra direta sem pensar; (2) trocar a ordem dos valores na tabela; (3) esquecer-se de escrever a unidade na resposta. Antes de fechar, faz um teste de bom senso: com mais pedreiros o muro ficou pronto mais depressa? Então 4 dias faz sentido.",
  "definition": "Duas grandezas são **diretamente proporcionais** quando, ao multiplicar uma por um número, a outra fica multiplicada pelo mesmo número (o quociente entre elas é constante). São **inversamente proporcionais** quando, ao multiplicar uma por um número, a outra fica dividida por esse número (o produto entre elas é constante). A **regra de três simples** resolve problemas com duas grandezas proporcionais, em que três valores são conhecidos.",
  "formulas": "**Direta** (a ↔ b, c ↔ x):  $$\\frac{a}{c}=\\frac{b}{x}\;\\Longrightarrow\; x=\\frac{b\\cdot c}{a}$$\n\n**Inversa** (a ↔ b, c ↔ x):  $$a\\cdot b=c\\cdot x\;\\Longrightarrow\; x=\\frac{a\\cdot b}{c}$$\n\nTruque da unidade: na direta, descobre o valor de **1**; na inversa, descobre o **total** (produto) e divide.",
  "worked_example": "**Exemplo 1 (direta).** 5 kg de arroz custam 4 500 Kz. Quanto custam 8 kg?\n\n**Passo 1.** Mais quilos, mais dinheiro: direta.\n\n**Passo 2.** Cálculo: $x=\\dfrac{4500\\cdot 8}{5}=7200$ Kz.\n\n**Exemplo 2 (direta).** Um carro faz 45 km com 3 litros. Com 7 litros faz $\\dfrac{45\\cdot 7}{3}=105$ km.\n\n**Exemplo 3 (inversa).** 6 pedreiros fazem o muro em 10 dias. Com 15 pedreiros: mais pessoas, menos dias, inversa. $x=\\dfrac{6\\cdot 10}{15}=4$ dias.\n\n**Exemplo 4 (inversa, com armadilha).** A 60 km/h uma viagem demora 4 h. A 80 km/h? Maior velocidade, menor tempo: $x=\\dfrac{60\\cdot 4}{80}=3$ h. Se tivesses usado a regra direta, terias obtido 5,33 h, um tempo maior com mais velocidade, que não faz sentido.",
  "guided_exercise": "Resolve connosco: **uma receita para 4 pessoas leva 600 g de farinha. Quanta farinha para 10 pessoas?**\n\n1) Mais pessoas, mais farinha ou menos? Mais. Logo, é direta.\n\n2) Quanto vai cada pessoa? 600 ÷ 4 = 150 g.\n\n3) Para 10 pessoas? 10 × 150 = 1 500 g.\n\n4) Teste de bom senso: 10 pessoas é mais do dobro de 4, e 1 500 g é mais do dobro de 600 g. Faz sentido.",
  "independent_exercise": INDEP,
  "challenge": "**Desafio da obra.** 8 trabalhadores fazem uma obra em 15 dias, mas ao fim de 5 dias saem 4 trabalhadores. Em quantos dias, no total, ficará concluída a obra?\n\nPista: depois de 5 dias, que parte do trabalho já foi feita? Quantos \"dias de trabalhador\" faltam, e com quantos trabalhadores?",
  "assessment": "Estarás pronto quando conseguires: (1) decidir corretamente entre proporcionalidade direta e inversa e justificar com uma frase; (2) montar a regra de três sem trocar valores; (3) calcular com números inteiros e com problemas em Kz; (4) fazer o teste de bom senso ao resultado."
 },
 "exercises": ex})
print("regra de 3 ok", len(ex))

# ============ 3. Razão e proporção ============
C = "razao_proporcao.base"
ex = []
ex.append(num(1, C, "Numa turma há 12 raparigas e 18 rapazes. Qual é a razão entre raparigas e rapazes, na forma de fração irredutível?", F(12, 18),
    "12/18 simplifica-se dividindo por 6: 2/3.", ["Escreve 12/18.", "m.d.c.(12, 18) = 6.", "12÷6 = 2 e 18÷6 = 3, logo 2/3."]))
ex.append(num(1, C, "Calcula x na proporção $\\frac{3}{4}=\\frac{x}{20}$.", F(3*20, 4),
    "Produto dos meios = produto dos extremos: 4x = 3·20 = 60, logo x = 15.", ["4·x = 3·20.", "x = 60 ÷ 4 = 15."]))
ex.append(num(2, C, "Calcula x na proporção $\\frac{5}{x}=\\frac{15}{27}$.", F(5*27, 15),
    "15x = 5·27 = 135, logo x = 9.", ["15·x = 5·27 = 135.", "x = 135 ÷ 15 = 9."]))
ex.append(num(2, C, "Um mapa tem escala 1 : 500 000. Dois lugares estão a 4 cm no mapa. A que distância real estão, em km?", F(4*500000, 100000),
    "4 cm × 500 000 = 2 000 000 cm = 20 km (100 000 cm = 1 km).", ["Distância real em cm: 4 × 500000 = 2000000.", "1 km = 100000 cm, logo 2000000 ÷ 100000 = 20 km."]))
ex.append(num(2, C, "Num mapa de escala 1 : 200 000, a distância entre duas cidades mede 9 cm. Quantos km são na realidade?", F(9*200000, 100000),
    "9 × 200 000 = 1 800 000 cm = 18 km.", ["9 × 200000 = 1800000 cm.", "÷ 100000 = 18 km."]))
ex.append(num(2, C, "Para fazer 3 litros de sumo usam-se 2 litros de polpa e 1 litro de água. A razão polpa : água é 2 : 1. Quantos litros de polpa são precisos para 12 litros de sumo (mesma razão)?", F(12*2, 3),
    "Cada 3 litros de sumo levam 2 de polpa: 12 ÷ 3 = 4 grupos; 4 × 2 = 8 litros.", ["12 ÷ 3 = 4 grupos.", "4 × 2 = 8 litros."]))
ex.append(num(3, C, "Dividir 840 Kz entre dois irmãos na razão 3 : 4. Quanto recebe o irmão que recebe a parte maior?", F(840, 7) * 4,
    "3 + 4 = 7 partes; cada parte vale 840 ÷ 7 = 120 Kz; a parte maior são 4 × 120 = 480 Kz.", ["Total de partes: 3 + 4 = 7.", "1 parte = 840 ÷ 7 = 120.", "Parte maior: 4 × 120 = 480 Kz."]))
ex.append(num(3, C, "A idade de um pai está para a do filho como 7 está para 2. Se o filho tem 10 anos, que idade tem o pai?", F(7*10, 2),
    "Proporção 7/2 = x/10: 2x = 70 e x = 35 anos.", ["7/2 = x/10.", "2x = 70.", "x = 35."]))
ex.append(mc(2, C, "Qual destas razões é equivalente a 6 : 9?", ["2 : 3", "3 : 2", "6 : 3", "9 : 6"], 0, "Divide os dois termos por 3: 6:9 = 2:3.", ["m.d.c.(6, 9) = 3.", "6÷3 = 2 e 9÷3 = 3."]))
ex.append(tf(1, C, "As frações $\\frac{4}{6}$ e $\\frac{10}{15}$ formam uma proporção.", F(4,6) == F(10,15), "Ambas valem 2/3 (ou: 4·15 = 6·10 = 60).", ["Simplifica: 4/6 = 2/3.", "10/15 = 2/3.", "São iguais, logo formam proporção."]))
assert F(840,7)*4 == 480 and F(12*2,3) == 8

write(2, 3, {
 "subject": "razao-e-proporcao", "topic_title": "Razão e proporção", "topic_slug": "razao-e-proporcao",
 "lesson_title": "Razão, proporção e escalas", "lesson_slug": "razao-proporcao-escalas",
 "summary": "Compara quantidades com razões, resolve proporções e lê escalas de mapas.", "minutes": 25,
 "blocks": {
  "introduction": "Para fazer um bom sumo de maracujá, a Dona Rosa mistura sempre 2 copos de polpa por 1 de água, quer faça um jarro pequeno, quer faça um balde para a festa. Está a manter uma **razão**. Quando o mapa diz que 1 cm representa 5 km, está a usar uma **escala**, que também é uma razão. Mestres de obras, cozinheiros, engenheiros e até quem lê o Google Maps usam estas ideias sem reparar.\n\nNesta aula vais aprender a comparar quantidades, a completar proporções e a ler escalas para descobrir distâncias reais.",
  "intuition": "Uma **razão** compara duas quantidades dividindo uma pela outra. Numa turma com 12 raparigas e 18 rapazes, a razão raparigas : rapazes é 12 : 18, que se simplifica para 2 : 3. Lê-se: \"por cada 2 raparigas há 3 rapazes\". Simplificar uma razão é como simplificar uma fração: divide-se os dois termos pelo mesmo número.\n\nUma **proporção** é a igualdade de duas razões, por exemplo $\\frac{3}{4}=\\frac{15}{20}$. Há uma regra prática poderosa: **o produto dos meios é igual ao produto dos extremos** (3·20 = 4·15 = 60). É por ela que descobrimos o termo em falta numa proporção.\n\nNas **escalas**, 1 : 500 000 significa que 1 cm no mapa corresponde a 500 000 cm na realidade, ou seja, 5 km.\n\n**Erros comuns:** (1) inverter a ordem da razão (raparigas : rapazes não é igual a rapazes : raparigas); (2) misturar unidades (cm com km) sem converter; (3) esquecer de simplificar no fim.",
  "definition": "A **razão** entre dois números a e b (b ≠ 0) é o quociente $\\frac{a}{b}$ (ou a : b). Uma **proporção** é uma igualdade entre duas razões: $\\frac{a}{b}=\\frac{c}{d}$. Nela, a e d são os **extremos** e b e c os **meios**. Propriedade fundamental: $a\\cdot d=b\\cdot c$. A **escala** de um mapa é a razão entre a distância no desenho e a distância real, expressas na mesma unidade.",
  "formulas": "$$\\frac{a}{b}=\\frac{c}{d}\;\\Longleftrightarrow\; a\\cdot d=b\\cdot c$$\n\n$$x=\\frac{b\\cdot c}{a}\\ \\text{ em }\\ \\frac{a}{b}=\\frac{x}{c}\\ \\ (\\text{ou seja, multiplica em cruz e divide})$$\n\nEscala 1 : E, distância real = distância no mapa × E.\n\nDivisão em partes proporcionais (razão m : n, total T): cada parte vale $\\dfrac{T}{m+n}$.",
  "worked_example": "**Exemplo 1.** Simplifica a razão 12 : 18.\n\nm.d.c.(12, 18) = 6, logo 12 : 18 = 2 : 3.\n\n**Exemplo 2.** Calcula x em $\\frac{3}{4}=\\frac{x}{20}$.\n\nMultiplica em cruz: $4x=3\\cdot 20=60$, logo $x=15$.\n\n**Exemplo 3 (escala).** No mapa, a distância Luanda–Catete mede 6 cm e a escala é 1 : 500 000. Distância real: 6 × 500 000 = 3 000 000 cm = 30 km (porque 100 000 cm = 1 km).\n\n**Exemplo 4 (partilha).** Dividir 840 Kz entre dois irmãos na razão 3 : 4.\n\nTotal de partes: 3 + 4 = 7. Cada parte vale 840 ÷ 7 = 120 Kz. Um recebe 3 × 120 = 360 Kz e o outro 4 × 120 = 480 Kz. Confirma: 360 + 480 = 840 ✓.",
  "guided_exercise": "Vamos juntos: **num mapa de escala 1 : 200 000, duas cidades estão a 9 cm. Qual é a distância real?**\n\n1) O que significa 1 : 200 000? Cada 1 cm no mapa são 200 000 cm no terreno.\n\n2) Multiplica: 9 × 200 000 = 1 800 000 cm.\n\n3) Converte para km: 1 km = 100 000 cm, logo 1 800 000 ÷ 100 000 = 18 km.\n\n4) Resposta: 18 km. Para ti: como ficaria se a escala fosse 1 : 100 000?",
  "independent_exercise": INDEP,
  "challenge": "**Desafio da tinta.** Uma tinta cinzenta faz-se misturando tinta branca e preta na razão 5 : 2. Para obter 14 litros de tinta cinzenta, quantos litros de cada cor são necessários? E se quiseres que a mistura fique mais escura, a razão branca : preta deve aumentar ou diminuir?\n\nPista: quantas partes tem a mistura toda?",
  "assessment": "Consideras a competência dominada quando consegues: (1) simplificar razões; (2) completar proporções com o produto em cruz; (3) usar a escala de um mapa nos dois sentidos (do mapa para a realidade e vice-versa); (4) dividir uma quantidade em partes proporcionais. Mostra-o com acertos em níveis de dificuldade diferentes."
 },
 "exercises": ex})
print("razao ok", len(ex))

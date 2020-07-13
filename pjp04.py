from random import randint, uniform, shuffle, choice

Dados_vendas = []
Lista_codigos = []

print("\n\n             ********************************              ") 
print("             ** Gerador de dados de vendas **              ")
print("             ********************************          \n\n")

mes = int(input("\n Digite o mês: "))
while mes <= 0 or mes > 12:
	mes = int(input(" Digite o mês (meses válidos): "))

ano = int(input(" Digite o ano desejado: "))
while ano < 2016 or ano > 2020:
	ano = int(input(" Digite o ano desejado (o ano deve ser no mínimo 2016 e não deve ultrapassar 2020): "))

QtdeVendasDia = int(input(" Digite a quantidade diária de lançamentos de vendas: "))
while QtdeVendasDia <= 0:
	QtdeVendasDia = int(input(" Digite a quantidade diária de lançamentos de vendas (maior que zero): "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
	qtde_dias_mes = 31
	qtde_vendas_geradas = QtdeVendasDia * qtde_dias_mes
elif mes == 2:
	qtde_dias_mes = 28
	qtde_vendas_geradas = QtdeVendasDia * qtde_dias_mes
else:
	qtde_dias_mes = 30
	qtde_vendas_geradas = QtdeVendasDia * qtde_dias_mes

	
arq = open("PRODUTOS.txt", "r")
s = arq.readline()
dia = 1
i = 0

while i < qtde_vendas_geradas and dia <= qtde_dias_mes:	
	j = 0
	while j < QtdeVendasDia: 	
		if s == '':
			arq.seek(0)
			s = arq.readline()
											
		s = s.rstrip()
		t = s.split(";")
		cod_produto = int(t[0])
		control_estoq = t[1]
		qtde_estoq_inicio = float(t[2])
		custo_unit = float(t[3])
		margem_lucro = float(t[4])		
					
		if control_estoq == 'P':
			QtdeVendida = uniform(1, qtde_estoq_inicio)
		elif control_estoq == 'U':
			QtdeVendida = randint(1, qtde_estoq_inicio)
										
		preco_venda = float(custo_unit) + (float(custo_unit) * float(margem_lucro) / 100)
		
		Lista_codigos.append(((int(cod_produto), QtdeVendida,  float(preco_venda))))
			
		Dados_vendas.append([ano, mes, dia, int(cod_produto), QtdeVendida, preco_venda])	
		s = arq.readline()
		j = j + 1		
	dia = dia + 1
	i = i + 1								
arq.close()

shuffle(Lista_codigos)

i = 0
while i < len(Dados_vendas):
	Dados_vendas[i][3] = Lista_codigos[i][0]
	Dados_vendas[i][4] = Lista_codigos[i][1]
	Dados_vendas[i][5] = Lista_codigos[i][2]
	i = i + 1
	
j = 0	
while j < len(Dados_vendas):
	Dados_vendas[j][5] = Dados_vendas[j][5] - (Dados_vendas[j][5] * (35 / 100))
	j = j + 6

i = 0
while i < len(Dados_vendas):
	Dados_vendas[i][5] = Dados_vendas[i][5] - (Dados_vendas[i][5] * (35 / 100))
	i = i + 15

arq = open("Dados_de_vendas.txt", "w")
for dados in Dados_vendas:
	if dados[1] == 1  or dados[1] == 2 or dados[1] == 3 or dados[1] == 4 or dados[1] == 5 or dados[1] == 6 or dados[1] == 7 or dados[1] == 8 or dados[1] == 9 and dados[2] == 1 or dados[2] == 2 or dados[2] == 3 or dados[2] == 4 or dados[2] == 5 or dados[2] == 6 or dados[2] == 7 or dados[2] == 8 or dados[2] == 9:
		arq.write("{};{:0>2};{:0>2};{};{:.3f};{:.2f};\n".format(dados[0], dados[1],
											dados[2], dados[3], dados[4],
											dados[5]))
											
	elif dados[1] == 1  or dados[1] == 2 or dados[1] == 3 or dados[1] == 4 or dados[1] == 5 or dados[1] == 6 or dados[1] == 7 or dados[1] == 8 or dados[1] == 9:
		arq.write("{};{:0>2};{};{};{:.3f};{:.2f};\n".format(dados[0], dados[1],
											dados[2], dados[3], dados[4],
											dados[5]))
		
	elif dados[2] == 1 or dados[2] == 2 or dados[2] == 3 or dados[2] == 4 or dados[2] == 5 or dados[2] == 6 or dados[2] == 7 or dados[2] == 8 or dados[2] == 9: 
		arq.write("{};{};{:0>2};{};{:.3f};{:.2f};\n".format(dados[0], dados[1],
											dados[2], dados[3], dados[4],
											dados[5]))	
	else:
		arq.write("{};{};{};{};{:.3f};{:.2f};\n".format(dados[0], dados[1],
											dados[2], dados[3], dados[4],
											dados[5]))												
arq.close()

print("\n\n Dados de vendas gerados com sucesso!")
print("\n Fim do programa.")

	



	

	



		
		
	
	











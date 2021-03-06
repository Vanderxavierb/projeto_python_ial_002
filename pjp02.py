# Função de leituro arquivo texto.
# Lê o arquivo texto e faz as devidas alterações
# qtde * valorUnitárioProduto ---> cada multiplicacão é 
# Armazenada na Lista_somatorios.
# A Lista_dados armazena todos os dados, contidos em cada linha do 
# arquivo, em tuplas.
def LeituraDeArquivo(Lista_dados, Lista_somatorios):
	arq = open("VENDAS.txt", "r")
	s = arq.readline() #--->           # Lê primeiro uma linha, e só
	while s != '':                     # depois lê a outra. 													
		s = s.rstrip()				   # Essa técnica facilita a
		L = s.split(";")               # modificação de cada linha lida.
		L[0] = int(L[0])
		L[1] = int(L[1])
		L[2] = float(L[2])  
		
		somatorio = 0 
		somatorio = somatorio + L[1] * L[2] 
		Lista_somatorios.append(somatorio)
		Lista_dados.append(tuple(L))
		s = arq.readline()
	return Lista_dados, Lista_somatorios
	arq.close()
	
# Função que retira o caractere(;) do último item da lista dados e 
#acrescenta um ponto final.
def RetiraCaractereNoItemFinal(Lista_dados):
	i = 0
	while i < len(Lista_dados):
		if i == len(Lista_dados) - 1:
			codigo = Lista_dados[i][0]
			print(str(codigo).rstrip() + ".")
		else:
			print(Lista_dados[i][0], end = ";")
		i = i + 1

# Código principal			
Somatorios = []
dados = []
LeituraDeArquivo(dados, Somatorios)

print("\nAqui estão os códigos(produtos) presentes na lista de dados\n")
RetiraCaractereNoItemFinal(dados)

codigo = int(input("\nDigite o código(inteiro): "))
while codigo != 0:	
	if codigo < 10000 or codigo > 21000:
		print("{} Código inválido (deve ser entre 10000 e 21000)"
			.format(codigo))
	else:
		i = 0
		flag = -1  
		while i < len(dados):
			if codigo == dados[i][0]:    # dados[i] [0] --> localiza
				flag = i
				break					 # somente os códigos de cada
			i = i + 1                    # tupla, lembrando que as tu-
			                             # estão dentro da lista dados.
		if flag < 0:
			print("{} código não está presente na lista dados"
				.format(codigo))
		else:
			print("Total vendido do produto {} = R$ {:.2f}"
				.format(codigo, Somatorios[flag]))
	codigo = int(input("\nDigite o código(inteiro): "))
	
	# Logo acima foi usado um mecanismo de conseguir migrar o indice 
	#(flag = i) para o resto do código. A justificativa do racícionio
	# é a seguinte: pensando nos indices das tuplas (lista dados), que
	# mostram somente os códigios (dados[1] [0]; dados [2] [0]...)
	# podemos usar o mesmo index com os da lista Somatorios, pois
	# o dados[1] [0] é o código e o Somatorios[1] é a 
	# qtde * valorUnitárioProduro desse código.
	# Essa lógica é válida para todos os próximos códigos, pois
	# os index das listas dados e somatorios estão sincronizados,
	# dessa forma, obtemos sempre os valores desejados.
	
print("\n\nFim do programa")
	

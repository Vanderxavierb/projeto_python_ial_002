def AsciiArtr():
	print("\n\n                  ********************                     ") 
	print("                  ** GERANDO SENHAS **                     ")
	print("                  ********************                     ")
	
def Introducao():
	print("\n ***************************************************************")
	print(" ***************************************************************")
	print(" ***************************************************************")
	print(" **                                                           **")     
	print(" **         GERADOR          DE           SENHAS              **") 
	print(" **                                                           **")
	print(" ***************************************************************")
	print(" ***************************************************************")
	print(" ***************************************************************\n\n")

	print("                ********************************               ")                                         
	print("                ** TIPOS DE SENHAS A DECLARAR **               ")
	print("                ********************************               \n\n")     
	print(" a. Numérica – conterá apenas algarismos                                  \n")
	print(" b. Alfabética – conterá apenas letras maiúsculas e minúsculas;           \n")
	print(" c. Alfanumérica 1 – conterá letras maiúsculas e algarismos;              \n")
	print(" d. Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos;  \n")
	print(" e. Geral – conterá letras maiúsculas, minúsculas,                        ")
	print("    algarismos e os caracteres ASCII [33, 46] e [58, 64]                  \n\n")

	print(" •Tipo: que é um caractere que deverá ser ‘a’, ‘b’, ‘c’, ‘d’, ‘e’ e definirá o tipo de senha gerada")
	print(" •Tam: que é o tamanho da senha, um número inteiro\n\n")

def Gera_lista_Maiusculas(Lista_Maiusculas):
	letras_maisculas = []
	for item in Lista_Maiusculas:
		item = chr(item)
		letras_maisculas.append(item)
	return letras_maisculas
	
def Gera_lista_caracteres_especiais(Lista_caracteres_especiais):
	caracteres_especiais = []
	for item in Lista_caracteres_especiais:
		item = chr(item)
		caracteres_especiais.append(item)
	return caracteres_especiais

def Gera_lista_Maiusculas_minusculas(Lista_Maiusculas_minusculas):
	letras_maisculas_minusculas = []
	for item in Lista_Maiusculas_minusculas:
		item = chr(item)
		letras_maisculas_minusculas.append(item)
	return letras_maisculas_minusculas

def tipos_caracteres(tipo_senha):
	# algarismos
	algarismos = [0 , 1, 2, 3, 4, 5, 6, 7, 8, 9] 

	# maiúsculas e minusculas
	Maiusculas_minusculas = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 
							76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 
							87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 
							103, 104, 105, 106, 107, 108, 109, 110, 111, 
							112, 113, 114,115, 116, 117, 118, 119, 120, 
							121, 122] 
							
	 # letras maiúsculas
	Maiusculas = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 
				  78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]   

	# caracteres especiais
	caracteres_especiais = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 
							44, 45, 46, 58, 59, 60, 61, 62, 63, 64]  
	
	if tipo_senha == 'a':
		return algarismos
		
	elif tipo_senha == 'b':
		letras_maisculas_minusculas = Gera_lista_Maiusculas_minusculas(Maiusculas_minusculas)
		return letras_maisculas_minusculas
		
	elif tipo_senha == 'c':
		letras_maisculas = Gera_lista_Maiusculas(Maiusculas)
		
		Alfa_01 = algarismos + algarismos + letras_maisculas
		random.shuffle(Alfa_01)
		return Alfa_01
	
	elif tipo_senha == 'd':
		letras_maisculas_minusculas = Gera_lista_Maiusculas_minusculas(Maiusculas_minusculas)
		
		Alfa_02 = algarismos + algarismos + letras_maisculas_minusculas
		random.shuffle(Alfa_02)
		return Alfa_02
	
	elif tipo_senha == 'e':
		letras_maisculas_minusculas = Gera_lista_Maiusculas_minusculas(Maiusculas_minusculas)
		lista_caracteres_especiais = Gera_lista_caracteres_especiais(caracteres_especiais)

		Senhas_Gerais =  algarismos + algarismos + letras_maisculas_minusculas + lista_caracteres_especiais
		random.shuffle(Senhas_Gerais)
		return Senhas_Gerais
		
def Input_tamanho_senha():
	numero = int(input(" Defina o tamanho da senha: "))
	while numero <= 0:
		numero = int(input(" Defina o tamanho da senha (Maior que zero): "))
	return numero

def Input_tipo_senha():
	Tipo = input(" Defina o tipo de senha: ")	
	while Tipo != 'a' and Tipo != 'b' and Tipo != 'c' and  Tipo!= 'd' and  Tipo != 'e':
		Tipo = input(" Defina o tipo de senha (‘a’, ‘b’, ‘c’, ‘d’, ‘e’): ")
	return Tipo	
	
def ReTornaMatricula():
	MaTr = []
	arq = open("MATR.txt", "r")
	s = arq.readline()
	while s != '':
		s = s.rstrip()
		MaTr.append(int(s))
		s = arq.readline()
	return MaTr
	arq.close()	
	
def ReTornaAcumulaSenha(Lista_Senhas, AcumulaSenha, Tamanho_senha):
	arq = open("MATR.txt", "r")
	s = arq.readline()
	while s != '':
		s = s.rstrip()
		AcumulaSenha.append(random.choices(Lista_Senhas, k = Tamanho_senha))
		s = arq.readline()
	return AcumulaSenha
	arq.close()
	
def GravaArq(numero, Tipo):
	MaTriculas = ReTornaMatricula()
	Conjunto_de_Senha = GeraSenha(Tipo, numero)
	AsciiArtr()
	arq = open("SENHAS.txt", "w")
	for matricula in MaTriculas:
		arq.write("{};{};\n".format(matricula, 
			''.join(map(str, random.choices(Conjunto_de_Senha, k = numero)))))	
	arq.close()		
	
def Gera_campos_de_senhas(AcumulaSenhas):
	Campo_de_senhas = []
	for lista in AcumulaSenhas:
		for item in lista:
			Campo_de_senhas.append(item)			
	return Campo_de_senhas		
	
def GeraSenha(Tipo, Tam):
	AcumuladorDeSenhas = []
	MaTriculas = []
	
	# Numérica – conterá apenas algarismos;	
	if Tipo == 'a':
		Algarismos = tipos_caracteres(Tipo)	
		ReTornaAcumulaSenha(Algarismos, AcumuladorDeSenhas, Tam)			
		Senha = Senha = Gera_campos_de_senhas(AcumuladorDeSenhas)	
		return Senha
	
	# Alfabética – conterá apenas letras maiúsculas e minúsculas;
	elif Tipo == 'b':
		alfabetica = tipos_caracteres(Tipo)
		ReTornaAcumulaSenha(alfabetica, AcumuladorDeSenhas, Tam)
		Senha = Gera_campos_de_senhas(AcumuladorDeSenhas)
		return Senha
	
	# Alfanumérica 1 – conterá letras maiúsculas e algarismos;	
	elif Tipo == 'c':	
		alfa01 = tipos_caracteres(Tipo)
		ReTornaAcumulaSenha(alfa01, AcumuladorDeSenhas, Tam)
		Senha = Senha = Gera_campos_de_senhas(AcumuladorDeSenhas)
		return Senha
	
	# Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos;
	elif Tipo == 'd':
		alfa02 = tipos_caracteres(Tipo)
		ReTornaAcumulaSenha(alfa02, AcumuladorDeSenhas, Tam)
		Senha = Senha = Gera_campos_de_senhas(AcumuladorDeSenhas)
		return Senha
		
	# Geral – conterá letras maiúsculas, minúsculas, algarismos e os caracteres ASCII [33, 46] e [58, 64]
	elif Tipo == 'e':
		Gerais = tipos_caracteres(Tipo)
		ReTornaAcumulaSenha(Gerais, AcumuladorDeSenhas, Tam)
		Senha = Senha = Gera_campos_de_senhas(AcumuladorDeSenhas)
		return Senha
					
import random

# Código principal
Introducao()
N = Input_tamanho_senha()
Tipo_senha = Input_tipo_senha()
GravaArq(N, Tipo_senha)
		
	
print("\n\n Senhas geradas com sucesso")
print("\n Fim do programa")
	

				








	
	

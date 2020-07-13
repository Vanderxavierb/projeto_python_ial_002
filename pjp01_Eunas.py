# Fatec São Paulo, Curso ADS Noturno, 1º / 2020.
# IAL 002: Projeto Programa nº4
# Entrega 13/07/2020
#
# 20100711 Eugenio Dalle Olle
# 20119491 Vitor Macedo de Medeiros
# 20118320 Vanderson Xavier Barbosa

#L
Saida = []
nomesize = 0

print("{:9} {:30} {:4} {:9}".format("", "", "Média".center(5), ""))
print("{:9} {:30} {:4} {:9}".format("Matrícula", "Nome do Aluno", "Final".center(5), " Situação"))

arq = open("ALUNOS.TXT", "r")
s = arq.readline()
while s!= "":
    s = s.strip() #Remove Carriage Return e Line Fedd
    t = s.split(";") #Separa a string pelo ponto e vírgula
    t[0] = int(t[0])    #Converte código do aluno para inteiro
    t[1] = float(t[1])  #Converte primeira nota para real
    t[2] = float(t[2])  #Converte segunda nota para real
    t[3] = float(t[3])  #Converte nota de trabalhos para real

    if len(t[4]) > nomesize:
        nomesize = len(t[4])

    media = (4*t[1] + 3*t[2] + 2*t[3])/10
    if media >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("{:9} {:30} {:4.1f} {} {:9}".format(t[0], t[4], media, " " , situacao))
    
    s = arq.readline()  #Lê a próxima linha

    

arq.close()    
print("\nFim do programa")












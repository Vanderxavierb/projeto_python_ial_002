Dados = []
arq = open("ALUNOS.txt", "r")
info = arq.readline()
print("\n") 
print("                                         Média")
print(" Matrícula " +
	" Nome do Aluno      " +
	"          Final " + 
	"    Situação")
                         
while info != '':
    info = info.rstrip()
    info = info.split(";")
    matricula = int(info[0])
    nota_P1 = float(info[1])
    nota_P2 = float(info[2])
    nota_MT = float(info[3])
    nome = info[4]
    Dados.append(tuple(info))
    
    MF = (4 * nota_P1 + 4 * nota_P2 + 2 * nota_MT) / 10
    if MF >= 5.9 and MF < 6.0:
	    MF = 6.0
	    
    MF_modificada = round(MF, 1)
    if MF_modificada >= 6.0:
	    situacao = 'Aprovado'		
	    print(f'{matricula:10}  {nome:27}  {MF_modificada:4}      {situacao}')
    else:
	    situacao = 'Reprovado'
	    print(f'{matricula:10}  {nome:27}  {MF_modificada:4}      {situacao}')
    info = arq.readline()
arq.close()


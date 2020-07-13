# Fatec São Paulo, Curso ADS Noturno, 1º / 2020.
# IAL 002: Projeto Programa nº4
# Entrega 13/07/2020
#
# 20100711 Eugenio Dalle Olle
# 20119491 Vitor Macedo de Medeiros
# 20118320 Vanderson Xavier Barbosa


from random import randint

arq = open("PRODUTOS.TXT", "r")
saida = open("VENDAS.TXT", "w")

#Entradas:
QtdeVendasDia = int(input("Digite o número de vendas diário: "))
while QtdeVendasDia <= 0:
  QtdeVendasDia = int(input("Número inválido.\nDigite o número de vendas diário: "))

mes = int(input("Digite o mês (1 a 12): "))
while mes < 1 or mes > 12:
  mes = int(input("Mês inválido.\nDigite o mês (1 a 12): "))

ano = int(input("Digite o ano (a partir de 2016): "))
while ano < 2016 or ano > 2020:
  ano = int(input("Ano inválido.\nDigite o ano (a partir de 2016): "))

#Número de dias do mês:
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
  dias = 31
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
  dias = 30
if mes == 2:
  dias = 28

tamlista = 15

#Gerador de vendas:
vendas = []
dia = 1
while dia <= dias:
  i = 0
  while i < QtdeVendasDia:
    v = randint(1, tamlista)
    print(v)
    k = 0
    s = "0"
    while k < v:
        s = arq.readline()


        print(s)
        k = k + 1
    s = s.rstrip()
    s = s.split(";")
    cod = int(s[0])
    tipo = s[1]
    custo = float(s[3])
    margem = float(s[4])
    

    if tipo == "U":
      quant = randint(1, 100)
      preco = (quant * custo) + ((quant * custo) * margem) /100

    if tipo == "P":
      quant = randint(1000, 100000)/1000
      preco = (quant * custo) + ((quant * custo) * margem) /100
      
    vendas.append((ano, mes, dia, cod, quant, preco))
    print(vendas)
    i = i + 1
  dia = dia + 1

arq.close()
saida.close()
print("\nFim do programa!")  

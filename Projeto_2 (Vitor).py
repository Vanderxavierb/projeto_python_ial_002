"""Função que carrega o arquivo VENDAS.txt"""         
def Upload_VENDAS():
    file = open("VENDAS.txt", "r")
    data = file.readline()
    sales = []
    while data != "":
        data = data.rstrip()
        s = data.split()
        sales.append(s)
        data = file.readline()
    file.close()
    return sales

"""Função que calcula o valor total das vendas registradas em VENDAS.txt"""
def Total_Sold():
    tSold = 0
    sales = Upload_VENDAS()
    sold = 0
    qty = 0
    PList = []
    SList = 0
    for i in sales:
        PList = i
        SList = PList[0]
        SList = SList.rstrip()
        SList = SList.split(";")
        sold = int(SList[1])
        qty = float(SList[2])
        tSold = tSold + (sold * qty)
        sold = 0
        qty = 0
    print("Total Geral Vendido: R${:.2f}".format(tSold))
    
"""Função que inicia o programa interagindo com o usuário."""
"""Aceita a pesquisa de código para demonstrar o total de vendas do produto referido."""
"""Encerra o programa quando se digita o valor "0" no código do produto."""
def Program_Init():
    Total_Sold()
    reference = 1
    while reference == 1:
        ProdCode = int(input("Digite o código do produto: "))
        if 10000 <= ProdCode <= 21000:
            sales = Upload_VENDAS()
            PList = []
            SList = 0
            ProdTSold = 0
            for i in sales:
                PList = i
                SList = PList[0]
                SList = SList.rstrip()
                SList = SList.split(";")
                PList = SList
                ProdCodeR = int(PList[0])
                if ProdCode == ProdCodeR:
                    ProdTSold = ProdTSold + (int(PList[1]) * float(PList[2]))                    
                else:
                    PList = []
            print("Total vendido do produto {} = R${:.2f}".format(ProdCode, ProdTSold))
        elif ProdCode == 0:
            break
        else:
            print("{} código inválido (Deve ser entre 10000 e 21000)".format(ProdCode))
            
Program_Init()
            
               

       



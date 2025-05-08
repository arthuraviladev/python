def criar_conta():
        print("    olá,esse é o banco avila")
        opcao = input("você gostaria de criar uma conta \n" )
        if opcao == "sim":
            informacoes_idade = int(input("digite sua idade").lower)
            informacoes_nome = input("digite seu nome")
            print(informacoes_nome,informacoes_idade)

        if opcao == "não":
            return
def sacar():
    if saldo < 0:
        return
    if saldo > 0:
        int(input("quanto que você quer sacar?")) 
def depositar():
    int(input("quento que você quer depositar"))
def conta():
    print("seu saldo é"),print(saldo)
saldo = 0

def banco():
    conta = criar_conta()
    if conta is None:
        return
    
banco()
while True:
        input("\n    menu principal banco avila")
        input("1- ")
        input("2-sacar")
        input("3-depositar")
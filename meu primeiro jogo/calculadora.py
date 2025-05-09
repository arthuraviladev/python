def soma(primeiro_numero,segundo_numero):
    resultado_soma = primeiro_numero + segundo_numero
    return resultado_soma

def subtraçao(pr_nu_ne,se_nu_ne):
    resultado_subtraçao = pr_nu_ne - se_nu_ne
    return resultado_subtraçao

def multiplicaçao(pr_nu_mul,se_nu_mul):
    resultado_da_multiplicaçao = pr_nu_mul * se_nu_mul
    return resultado_da_multiplicaçao

def divisao(pr_nu_di,se_nu_di):
    resultado_da_divisao = pr_nu_di / se_nu_di
    return resultado_da_divisao

def menu():
    while True:
        print("bem vindo a calculadora")
        valor_digitado = float(input("qual numero você quer usar : "))
        segundo_valor = float(input("qual o seu segundo numero : "))
        operaçao = input("você deseja realizar qual operação: +  -  *  /  ou você prefere 'sair'").lower()
        if operaçao == 'sair':
            print("encerrando o sistema")
            break
        elif (operaçao == "+" or operaçao == "soma"):
            resultado_soma = soma(valor_digitado,segundo_valor)
            print(f"seu resultado é {resultado_soma}")
        elif (operaçao == "subtraçao" or operaçao == "-"):
            resultado_subtraçao = subtraçao(valor_digitado,segundo_valor)
            print(f"seu resultado é {resultado_subtraçao}")
        elif (operaçao == "multiplicação" or operaçao == "*"):
            resultado_da_multiplicaçao = multiplicaçao(valor_digitado,segundo_valor)
            print(f"seu valor é {resultado_da_multiplicaçao}")
        elif (operaçao == "divisao" or operaçao == "/"):
            resultado_da_divisao = divisao(valor_digitado,segundo_valor)
            print(f"seu valor é {resultado_da_divisao}")
        else:
            print("essa operação nao pode ser calculada")

menu()





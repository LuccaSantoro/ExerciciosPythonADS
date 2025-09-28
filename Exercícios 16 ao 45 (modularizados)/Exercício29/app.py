print("Calcule o valor corrigido de um investimento na poupança ou renda fixa")

#modularização

def menu():
    while True:
        print("Menu de Escolha do Investimento")
        print("1. Poupança")
        print("2. Renda Fixa")

        escolha = input("Escolha uma opção:")
        if escolha in ("1", "2"):
            return escolha
        else:
            print("Opção inválida. Tente novamente.")

def investimento(valor_investido):
    escolha = menu()
    if escolha == "1":
        valor_corrigido = valor_investido * 1.03
    elif escolha == "2":
        valor_corrigido = valor_investido * 1.05
    else:
        return None
    return valor_corrigido

#declarar

valor_investido = float(input("Insira o valor a ser investido:"))


#inicio


valor_corrigido = investimento(valor_investido)

if valor_corrigido is not None:
    print(f"O valor corrigido do seu investimento é de R${valor_corrigido:.2f}")

#fim



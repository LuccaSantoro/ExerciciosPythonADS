#Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
print("Cálculo de rendimento de poupança ou renda fixa")

try:
    # 1. Recebe a entrada do valor do depósito
    valor_investido = float(input("Insira o valor do depósito (R$): "))
    if valor_investido < 0:
        raise ValueError("O valor do depósito não pode ser negativo.")
except ValueError:
    # 2. Tratativa de erro para entrada não-numérica ou negativa
    print("Entrada inválida. Por favor, insira um número positivo.")
    exit()

# 3. Recebe a escolha do tipo de investimento
print("\nEscolha o tipo de investimento:")
print("1 - Poupança (rende 1,3% ao mês)")
print("2 - Renda Fixa (rende 5% ao mês)")
escolha = input("Digite 1 ou 2: ")
if escolha not in ["1", "2"]:
    print("Escolha inválida. Por favor, digite 1 ou 2.")
    exit()
# --- Lógica do Investimento ---
valor_corrigido = None
if escolha == "1":
    # Poupança: 1,3% de correção (multiplica por 1.013)
    valor_corrigido = valor_investido * 1.013
elif escolha == "2":
    # Renda Fixa: 5% de correção (multiplica por 1.05)
    valor_corrigido = valor_investido * 1.05
# --- Fim da Lógica do Investimento ---

# Exibe o resultado, se o cálculo foi realizado
if valor_corrigido is not None:
    print(f"\nO valor corrigido do seu investimento é de R${valor_corrigido:.2f}")

#fim
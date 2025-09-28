# Calcule o valor corrigido de um investimento na poupança ou renda fixa

print("Cálculo do valor corrigido de um investimento na poupança ou renda fixa")

try:
    # 1. Recebe o valor a ser investido
    valor_investido = float(input("Insira o valor a ser investido: "))
except ValueError:
    print("Entrada inválida. Por favor, insira um valor numérico.")
    exit() # Encerra se a entrada for inválida

# Variável para armazenar a escolha do usuário
escolha = None

# --- Lógica do Menu (Substitui a função 'menu') ---
while True:
    print("\nMenu de Escolha do Investimento")
    print("1. Poupança (Correção de 3%)")
    print("2. Renda Fixa (Correção de 5%)")

    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha in ("1", "2"):
        break  # Sai do loop se a escolha for válida
    else:
        print("Opção inválida. Tente novamente.")
# --- Fim da Lógica do Menu ---

# --- Lógica do Investimento (Substitui a função 'investimento') ---
valor_corrigido = None

if escolha == "1":
    # Poupança: 3% de correção (multiplica por 1.03)
    valor_corrigido = valor_investido * 1.03
elif escolha == "2":
    # Renda Fixa: 5% de correção (multiplica por 1.05)
    valor_corrigido = valor_investido * 1.05
# --- Fim da Lógica do Investimento ---

# Exibe o resultado, se o cálculo foi realizado
if valor_corrigido is not None:
    print(f"\nO valor corrigido do seu investimento é de R${valor_corrigido:.2f}")
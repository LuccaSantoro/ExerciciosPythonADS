#Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.

print("Cálculo do novo salário com reajuste de 15%")

try:
    # 1. Recebe a entrada do valor do salário
    salario = float(input("Insira o valor do salário: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo do Novo Salário ---

novo_salario = salario * 1.15
print(f"O novo salário com reajuste de 15% é: {novo_salario:.2f}")

# --- Fim da Lógica de Cálculo ---

#fim

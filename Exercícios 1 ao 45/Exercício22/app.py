# Organize números inteiros em ordem decrescente (Conforme a lógica do código original)

print("Organize números inteiros em ordem decrescente")

try:
    # 1. Recebe a entrada do primeiro número
    valor1 = int(input("Insira o valor do primeiro número:"))
    
    # 2. Recebe a entrada do segundo número
    valor2 = int(input("Insira o valor do segundo número:"))
    
except ValueError:
    print("Entrada inválida. Por favor, insira números inteiros.")
    exit()

# --- Lógica de Impressão Ordenada (Substitui a função 'print_in_order') ---

# Verifica qual é o maior para imprimir primeiro
if valor1 > valor2:
    print(valor1)
    print(valor2)
else:
    # Se valor2 for maior ou igual a valor1
    print(valor2)
    print(valor1)
#Receba 2 valores reais. Calcule e mostre o maior deles
print("Verificação do maior valor entre dois números reais")

try:
    # 1. Recebe a entrada do primeiro número
    valor1 = float(input("Insira o valor do primeiro número: "))
    
    # 2. Recebe a entrada do segundo número
    valor2 = float(input("Insira o valor do segundo número: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Verificação do Maior Valor (Substitui a função 'verifica_maior') ---
if valor1 > valor2:
    print(f"O maior valor é: {valor1}")
elif valor2 > valor1:
    print(f"O maior valor é: {valor2}")
else:
    print("Os dois valores são iguais.")

# --- Fim da Lógica de Verificação ---

#fim
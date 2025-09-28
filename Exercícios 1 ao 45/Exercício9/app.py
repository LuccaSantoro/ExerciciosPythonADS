#Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.

print("Cálculo da soma dos quadrados de dois números inteiros")

try:
    # 1. Recebe a entrada do primeiro número
    valor1 = int(input("Insira o valor do primeiro número inteiro: "))
    
    # 2. Recebe a entrada do segundo número
    valor2 = int(input("Insira o valor do segundo número inteiro: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números inteiros.")
    exit()

# --- Lógica de Cálculo da Soma dos Quadrados (Substitui a função 'calcula_soma_quadrados') ---

soma_quadrados = valor1**2 + valor2**2
print(f"A soma dos quadrados de {valor1} e {valor2} é: {soma_quadrados}")

# --- Fim da Lógica de Cálculo ---

#fim
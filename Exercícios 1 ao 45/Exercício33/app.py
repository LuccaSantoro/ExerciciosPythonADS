# Receba um número N. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N. 

print("Cálculo da série 1 + 1/2 + 1/3 + ... + 1/N")

try:
    # 1. Recebe a entrada do usuário
    numero = int(input("Digite um número inteiro positivo: "))
    
    # 2. Validação da entrada (deve ser positivo)
    if numero <= 0:
        print("Número inválido. Por favor, digite um número inteiro positivo.")
        exit()
        
except ValueError:
    # 3. Tratativa de erro para entrada não-numérica
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()

# 4. Início do cálculo da série
total = 0.0

# Loop para somar cada termo (1/i) de 1 até N
for i in range(1, numero + 1):
    total += 1 / i

# 5. Exibe o resultado final
print(f"O resultado da série 1 + 1/2 + ... + 1/{numero} é: {total}")
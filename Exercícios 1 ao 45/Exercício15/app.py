#Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

print("Cálculo da hipotenusa de um triângulo retângulo")

try:
    # 1. Recebe a entrada do valor do primeiro cateto
    cateto1 = float(input("Insira o valor do primeiro cateto: "))
    
    # 2. Recebe a entrada do valor do segundo cateto
    cateto2 = float(input("Insira o valor do segundo cateto: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo da Hipotenusa ---

hipotenusa = (cateto1**2 + cateto2**2)**0.5
print(f"A hipotenusa do triângulo retângulo com catetos {cateto1} e {cateto2} é: {hipotenusa:.2f}")

# --- Fim da Lógica de Cálculo ---

#fim
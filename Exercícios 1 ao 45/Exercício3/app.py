#Receba a base e a altura de um triângulo. Calcule e mostre a sua área.
print("Cálculo da área de um triângulo")

try:
    # 1. Recebe a entrada do valor da base
    base = float(input("Insira o valor da base do triângulo: "))
    
    # 2. Recebe a entrada do valor da altura
    altura = float(input("Insira o valor da altura do triângulo: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()
# --- Lógica de Cálculo da Área ---

area = (base * altura) / 2
print(f"A área do triângulo é: {area:.2f}")

# --- Fim da Lógica de Cálculo ---

#fim
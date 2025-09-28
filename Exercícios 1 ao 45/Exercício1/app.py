#Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.

print("Cálculo da área de um quadrado")

try:

    # 1. Recebe a entrada do valor do lado
    lado = float(input("Insira o valor do lado do quadrado: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo da Área  ---

area = lado * lado
print(f"A área do quadrado é: {area:.2f}")

# --- Fim da Lógica de Cálculo ---

#fim
#Receba 2 números reais. Calcule e mostre a diferença desses valores.
print("Cálculo da diferença entre dois números reais")

try:
    # 1. Recebe a entrada do primeiro número
    valor1 = float(input("Insira o valor do primeiro número real: "))
    
    # 2. Recebe a entrada do segundo número
    valor2 = float(input("Insira o valor do segundo número real: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo da Diferença (Substitui a função 'calcula_diferenca') ---
if valor1 > valor2: 
    diferenca = valor1 - valor2
    print(f"A diferença entre {valor1} e {valor2} é: {diferenca}")
elif valor2 > valor1:
    diferenca = valor2 - valor1
    print(f"A diferença entre {valor2} e {valor1} é: {diferenca}")
else:
    print("Os dois valores são iguais. A diferença é 0.")
# --- Fim da Lógica de Cálculo ---

#fim
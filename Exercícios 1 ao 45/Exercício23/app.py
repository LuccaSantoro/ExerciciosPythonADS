# Organize quatro números em ordem crescente

print("Organize quatro números em ordem crescente")
print("Insira o primeiro, o segundo e o terceiro número em ordem crescente")

# --- Lógica de Entrada (Substitui a função 'get_input') ---
try:
    valor1 = float(input("Insira o valor do primeiro número:"))
    valor2 = float(input("Insira o valor do segundo número:"))
    valor3 = float(input("Insira o valor do terceiro número:"))
    valor4 = float(input("Insira o valor do quarto número:"))
except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Organização (Substitui as funções 'organize_numbers' e 'print_sorted') ---


if valor1 > valor2 and valor2 > valor3:
    # Coloca os valores em uma lista e ordena
    valores = [valor1, valor2, valor3, valor4]
    valores.sort()

    # Imprime os valores ordenados
    for v in valores:
        print(v)
        
    
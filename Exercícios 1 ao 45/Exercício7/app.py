#Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.

print("Cálculo do volume de um paralelepípedo")

try:
    # 1. Recebe a entrada do valor do comprimento
    comprimento = float(input("Insira o valor do comprimento: "))
    
    # 2. Recebe a entrada do valor da largura
    largura = float(input("Insira o valor da largura: "))
    
    # 3. Recebe a entrada do valor da altura
    altura = float(input("Insira o valor da altura: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo do Volume ---

volume = comprimento * largura * altura
print(f"O volume do paralelepípedo é: {volume:.2f}")

# --- Fim da Lógica de Cálculo ---

#fim

#Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo

print("Cálculo do terceiro ângulo de um triângulo")

try:
    # 1. Recebe a entrada do valor do primeiro ângulo
    angulo1 = float(input("Insira o valor do primeiro ângulo (em graus): "))
    
    # 2. Recebe a entrada do valor do segundo ângulo
    angulo2 = float(input("Insira o valor do segundo ângulo (em graus): "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo do Terceiro Ângulo ---
if angulo1 <= 0 or angulo2 <= 0 or (angulo1 + angulo2) >= 180:
    print("Os ângulos fornecidos não formam um triângulo válido.")
else:
    angulo3 = 180 - (angulo1 + angulo2)
    print(f"O valor do terceiro ângulo é: {angulo3} graus")

# --- Fim da Lógica de Cálculo ---

#fim

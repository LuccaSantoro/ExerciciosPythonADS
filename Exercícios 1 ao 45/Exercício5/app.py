#Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).
print("Cálculo das raízes reais de uma equação do 2º grau (AX² + BX + C = 0)")

try:
    # 1. Recebe a entrada do valor do coeficiente A
    coeficiente_a = float(input("Insira o valor do coeficiente A (não pode ser 0): "))
   
    # 2. Recebe a entrada do valor do coeficiente B
    coeficiente_b = float(input("Insira o valor do coeficiente B: "))
    
    # 3. Recebe a entrada do valor do coeficiente C
    coeficiente_c = float(input("Insira o valor do coeficiente C: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo das Raízes ---

delta = (coeficiente_b**2) - (4 * coeficiente_a * coeficiente_c)

raiz1 = (-coeficiente_b + delta**0.5) / (2 * coeficiente_a)
raiz2 = (-coeficiente_b - delta**0.5) / (2 * coeficiente_a)

print(f"As raízes reais da equação são: Raiz 1 = {raiz1:.2f}, Raiz 2 = {raiz2:.2f}")

# --- Fim da Lógica de Cálculo ---

#fim
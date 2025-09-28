#Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
print("Cálculo de raízes reais de uma equação do 2º grau (AX² + BX + C = 0)")

try:
    # 1. Recebe os coeficientes A, B e C
    coeficiente_a = float(input("Digite o coeficiente A (não pode ser 0): "))
    coeficiente_b = float(input("Digite o coeficiente B: "))
    coeficiente_c = float(input("Digite o coeficiente C: "))
    
    # 2. Verifica se A é zero (não é uma equação do 2º grau)
    if coeficiente_a == 0:
        print("O coeficiente A não pode ser zero em uma equação do 2º grau.")
        exit()
except ValueError:
    # 3. Trata erro se a entrada não for um número válido
    print("Entrada inválida. Por favor, insira números válidos para os coeficientes.")
    exit()
# 4. Calcula o discriminante (delta)
delta = (coeficiente_b**2) - (4 * coeficiente_a * coeficiente_c)

# 5. Verifica a existência de raízes reais com base no valor de delta
if delta < 0:
    print("Não existem raízes reais para esta equação.")
elif delta == 0:
    # 6. Uma raiz real (raiz dupla)
    raiz = -coeficiente_b / (2 * coeficiente_a)
    print(f"Existe uma raiz real (raiz dupla): {raiz}")
else:
    # 7. Duas raízes reais distintas
    raiz1 = (-coeficiente_b + delta**0.5) / (2 * coeficiente_a)
    raiz2 = (-coeficiente_b - delta**0.5) / (2 * coeficiente_a)
    print(f"Existem duas raízes reais distintas: {raiz1:.3f} e {raiz2:.2f}")

# Fim 
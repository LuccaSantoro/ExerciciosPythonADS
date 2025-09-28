#Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência.

print("Cálculo do comprimento de uma circunferência")

try:
    # 1. Recebe a entrada do valor do raio
    raio = float(input("Insira o valor do raio da circunferência: "))
except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    exit()
if raio < 0:
    print("O valor do raio não pode ser negativo.")
    exit()

# --- Lógica de Cálculo do Comprimento ---

comprimento = 2 * 3.14159 * raio
print(f"O comprimento da circunferência com raio {raio} é: {comprimento:.2f}")

# --- Fim da Lógica de Cálculo ---

#fim
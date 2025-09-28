#Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

print("Cálculo de duração do alimento")

try:
    # 1. Recebe a entrada do valor do alimento em quilos
    alimento_kg = float(input("Insira a quantidade de alimento (em kg): "))
    if alimento_kg < 0:
        raise ValueError("A quantidade de alimento não pode ser negativa.")
except ValueError:
    # 2. Tratativa de erro para entrada não-numérica ou negativa
    print("Entrada inválida. Por favor, insira um número positivo.")
    exit()
# --- Lógica de Cálculo da Duração do Alimento ---

dias_duracao = (alimento_kg * 1000) / 50  # Converte kg para g e divide por 50g/dia

print(f"\nO alimento durará por {dias_duracao:.0f} dias.")

# --- Fim da Lógica de Cálculo ---

#fim

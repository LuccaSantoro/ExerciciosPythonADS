# Descubra se o maior número é múltiplo do menor (Enunciado Original)

print("Descubra se o maior número é múltiplo do menor")

try:
    # 1. Recebe as entradas
    valor1 = float(input("Insira o primeiro número:"))
    valor2 = float(input("Insira o segundo número:"))
except ValueError:
    print("Entrada inválida. Por favor, insira números.")
    exit()

# --- Lógica de Verificação de Múltiplos ---

# Determina qual é o maior e o menor para realizar a verificação (Maior % Menor)
if valor1 >= valor2:
    dividendo = valor1
    divisor = valor2
else:
    dividendo = valor2
    divisor = valor1
    
# 1. Verifica divisão por zero
if divisor == 0:
    print("Não é possível dividir por zero.")
# 2. Verifica se o dividendo (o maior) é múltiplo do divisor (o menor)
# O cálculo é feito usando a função módulo (%)
elif dividendo % divisor == 0:
    print(f"O número {dividendo} é múltiplo de {divisor}")
else:
    print(f"O número {dividendo} não é múltiplo de {divisor}")
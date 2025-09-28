#Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

print("Troca de valores entre duas variáveis")

try:
    # 1. Recebe a entrada do valor de x
    valor_x = input("Insira o valor de x: ")
    
    # 2. Recebe a entrada do valor de y
    valor_y = input("Insira o valor de y: ")

except ValueError:
    print("Entrada inválida. Por favor, insira valores válidos.")
    exit()

# --- Lógica de Troca de Valores (Substitui a função 'troca_valores') ---

print(f"Antes da troca: x = {valor_x}, y = {valor_y}")
valor_x, valor_y = valor_y, valor_x
print(f"Depois da troca: x = {valor_x}, y = {valor_y}")

# --- Fim da Lógica de Troca ---

#fim

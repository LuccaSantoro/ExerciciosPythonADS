# Receba um número. Calcule e mostre os resultados da tabuada desse número.

print("Cálculo da tabuada de um número inteiro")

try: 
    # 1. Recebe a entrada do usuário
    valor = int(input("Insira o número inteiro: "))
    
    # 2. Validação: Checa se é positivo.
    # Nota: No seu código original, o tratamento de valor negativo estava presente,
    # mas o enunciado não proíbe números negativos. Mantendo a lógica original
    # que foi fornecida, apenas com o ajuste de 'return' para 'exit()'.
    if valor < 0:
        print("Número inválido. Por favor, insira um número inteiro positivo.")
        exit()
        
    # 3. Tratamento especial para o zero
    elif valor == 0:
        print("A tabuada do 0 é sempre 0.")
        exit()
        
except ValueError:
    # 4. Tratativa de erro para entrada não-numérica
    print("Entrada inválida. Por favor, insira um número inteiro.")
    exit()

# 5. Início do cálculo e exibição da tabuada
print(f"Tabuada do {valor}:")

# Loop para calcular de 1 até 10
for i in range(1, 11):
    resultado = valor * i
    print(f"{valor} x {i} = {resultado}")
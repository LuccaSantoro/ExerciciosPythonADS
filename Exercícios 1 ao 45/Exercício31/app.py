# Calcule o quadrado dos números entre 10 e 150

print("Calcule o quadrado dos números entre 10 e 150")

# Loop principal: continuará rodando até quebra, erro de entrada ou valor fora do intervalo
while True:
    try:
        # 1. Recebe a entrada do usuário
        valor = float(input("Insira o número: "))
        
    except ValueError:
        # 2. Tratativa de erro para entrada não-numérica e encerra
        print("Entrada inválida. Por favor, insira um número.")
        break # Sai do loop após erro de entrada
        
    # 3. Verifica se o valor está dentro do intervalo permitido (10 a 150)
    if valor >= 10 and valor <= 150:
        # 4. Calcula e exibe o quadrado
        valor_quadrado = valor ** 2
        print(f"O quadrado do número é {valor_quadrado:.2f}")
        
    else:
        # 5. Se estiver fora do intervalo, informa o usuário e encerra
        print("O valor inserido está fora do intervalo válido (10 a 150).")
        break # Sai do loop
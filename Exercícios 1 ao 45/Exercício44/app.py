# Cálculo de potência (base^expoente)

print("Cálculo de potência (base^expoente)")

try:
    # 1. Recebe e converte a base (float) e o expoente (int)
    base = float(input("Digite a base (número real): "))
    expoente = int(input("Digite o expoente (número inteiro): "))
    
    # 2. Calcula a potência diretamente (base ** expoente)
    resultado = base ** expoente
    
    # 3. Mostra o resultado
    print(f"O resultado de {base}^{expoente} é: {resultado}")

except ValueError:
    # 4. Trata erros de entrada (se o usuário digitar algo que não é número)
    print("Entrada inválida. Por favor, insira um número real para a base e um número inteiro para o expoente.")
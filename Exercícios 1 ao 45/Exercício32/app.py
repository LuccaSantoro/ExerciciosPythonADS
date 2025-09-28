# Código que calcula o fatorial de um número inteiro.

print("Calcule o fatorial de um número inteiro")

try:
    # 1. Obter o número do usuário
    valor = int(input("Insira o número:"))

    # 2. Verifica se o número é negativo
    if valor < 0:
        print("Não é possível calcular com esse valor")
    else:
        # --- Lógica de Fatorial (Substitui a função 'fatorial') ---
        
        # O fatorial de 0 é 1
        if valor == 0:
            valor_fatorial = 1
        else:
            # Variáveis para o cálculo
            valor_fatorial = 1
            fatorar = 1

            # Loop para multiplicar de 1 até o 'valor'
            while fatorar <= valor:
                valor_fatorial *= fatorar
                fatorar += 1
        
        # --- Fim da Lógica de Fatorial ---
        
        # 3. Exibe o resultado
        print(f"O fatorial do número {valor} é {valor_fatorial}")

except ValueError:
    # 4. Tratativa de erro para entrada não-numérica
    print("Entrada inválida. Por favor, insira um número inteiro.")
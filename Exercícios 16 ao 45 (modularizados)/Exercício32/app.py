# Código que calcula o fatorial de um número inteiro.

print("Calcule o fatorial de um número inteiro")

# Obter o número do usuário
try:
    valor = int(input("Insira o número:"))

    # Verifica se o número é negativo
    if valor < 0:
        print("Não é possível calcular com esse valor")
    else:
        # modularização
        def fatorial(n):
            if n == 0:
                return 1
            
            fatorar = 1
            resultado = 1

            while fatorar <= n:
                resultado *= fatorar
                fatorar += 1

            return resultado
        
        # inicio
        valor_fatorial = fatorial(valor)

        print(f"O fatorial do número {valor} é {valor_fatorial}")

except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")

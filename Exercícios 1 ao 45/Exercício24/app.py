# Saiba se um número inteiro é divisível por 2 ou por 3

print("Saiba se um número inteiro é divisível por 2 ou por 3")

try:
    # 1. Solicita ao usuário que digite um número inteiro
    numero = int(input("Digite um número inteiro: "))
    
    # 2. Inicia a lógica de verificação (Substitui a função 'verificar_divisibilidade')
    
    # Se o número for divisível por 2 e por 3
    if numero % 2 == 0 and numero % 3 == 0:
        resultado = "Divisível por 2 e por 3"
        
    # Se o número for divisível apenas por 2
    elif numero % 2 == 0:
        resultado = "Divisível por 2"
        
    # Se o número for divisível apenas por 3
    elif numero % 3 == 0:
        resultado = "Divisível por 3"
        
    # Se o número não for divisível nem por 2 nem por 3
    else:
        resultado = "Não é divisível por 2 nem por 3"
        
    # 3. Exibe o resultado para o usuário
    print(resultado)

except ValueError:
    # Tratativa de erro para entrada não-numérica
    print("Entrada inválida. Por favor, digite um número inteiro.")
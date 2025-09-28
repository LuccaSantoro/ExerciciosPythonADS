# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

print("Cálculo da somatória dos números ímpares entre dois valores inteiros")

try:
    # 1. Recebe os dois valores inteiros
    valor1 = int(input("Insira o primeiro número inteiro: "))
    valor2 = int(input("Insira o segundo número inteiro: "))
    
except ValueError:
    # 2. Trata erro se a entrada não for um número inteiro
    print("Entrada inválida. Por favor, insira números inteiros.")
    exit()

# 3. Verifica se os números são iguais
if valor1 == valor2:
    print("Os números são iguais. Por favor, insira dois números inteiros diferentes.")
else:
    # 4. Determina o intervalo correto (menor e maior)
    menor = min(valor1, valor2)
    maior = max(valor1, valor2)
    
    soma_impares = 0
    
    # 5. Itera por todos os números no intervalo (exclusivo)
    # Começa em 'menor + 1' e vai até 'maior - 1'
    for num in range(menor + 1, maior):
        
        # 6. Verifica se o número é ímpar
        if num % 2 != 0:
            # 7. Adiciona o número ímpar à soma
            soma_impares += num

    # 8. Exibe o resultado
    print(f"A somatória dos números ímpares entre {menor} e {maior} é: {soma_impares}")
# Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.

print("Verificação de números primos entre dois valores inteiros")

try:
    # Recebe os dois valores inteiros
    valor1 = int(input("Insira o primeiro número inteiro: "))
    valor2 = int(input("Insira o segundo número inteiro: "))
    
except ValueError:
    # Trata erro se a entrada não for um número inteiro
    print("Entrada inválida. Por favor, insira números inteiros.")
    exit()

# Verifica se os números são iguais
if valor1 == valor2:
    print("Os números são iguais. Por favor, insira dois números inteiros diferentes.")
else:
    # Determina o intervalo correto para iteração
    menor = min(valor1, valor2)
    maior = max(valor1, valor2)
    
    primos = []
    
    # Itera por todos os números no intervalo (exclusivo)
    for num in range(menor + 1, maior):
        
        # --- Lógica de Verificação de Primo (Substitui a função 'num_primo') ---
        eh_primo = True
        
        # 1. Trata números <= 1 (não são primos)
        if num <= 1:
            eh_primo = False
        else:
            # 2. Verifica divisores de 2 até a raiz quadrada do número (otimização)
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    eh_primo = False
                    break
        
        # --- Fim da Lógica de Verificação ---
        
        if eh_primo:
            primos.append(num)

    # Exibe o resultado
    if primos:
        print(f"Números primos entre {menor} e {maior}: {primos}")
    else:
        print(f"Não há números primos entre {menor} e {maior}.")
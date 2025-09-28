# Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

print("Verificação do maior e menor valor entre 100 números inteiros positivos")

# Inicialização das variáveis
maior = None
menor = None
count = 0  # Contador de números válidos lidos

# Loop principal para ler 100 números
while count < 100:
    try:
        # Recebe a entrada do usuário
        numero = int(input(f"Digite o {count + 1}º número inteiro positivo: "))
        
        # 1. Validação de valor positivo
        if numero < 0:
            print("Número inválido. Por favor, digite um número inteiro positivo.")
            continue
            
    except ValueError:
        # 2. Tratativa de erro para entrada não-numérica
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue
        
    # 3. Atualiza o maior valor
    # Se 'maior' ainda não foi definido (na primeira iteração) OU se o 'numero' atual for maior
    if maior is None or numero > maior:
        maior = numero
        
    # 4. Atualiza o menor valor
    # Se 'menor' ainda não foi definido (na primeira iteração) OU se o 'numero' atual for menor
    if menor is None or numero < menor:
        menor = numero
        
    # Incrementa o contador somente se a entrada foi válida e positiva
    count += 1

# Exibe os resultados
print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")
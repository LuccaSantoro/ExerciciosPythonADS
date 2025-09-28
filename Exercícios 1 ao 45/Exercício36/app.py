# Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

print("Cálculo da série 1 + 1/1! + 1/2! + ... + 1/N!")

try:
    # 1. Recebe a entrada do usuário
    numero = int(input("Digite um número inteiro positivo: "))
    
    # 2. Validação da entrada
    if numero < 0:
        print("Número inválido. Por favor, digite um número inteiro positivo.")
        exit()
        
except ValueError:
    # 3. Tratativa de erro para entrada não-numérica
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()

# Variáveis de controle
total = 0.0
fatorial_atual = 1  # Inicializa o fatorial de 0! (que é 1)

# Loop para calcular cada termo da série de 0 até N
for i in range(0, numero + 1):
    
    # --- Lógica de Fatorial (Cálculo Otimizado) ---
    # Para i=0, fatorial_atual é 1 (0!).
    # Para i > 1, o fatorial é calculado de forma incremental: i! = (i-1)! * i
    if i > 1:
        fatorial_atual *= i
    
    # Adiciona o termo 1/i! ao total
    total += 1 / fatorial_atual
    
    # Imprime o termo (opcional, para visualização da série)
    if i < numero:
        print(f"1/{i}!", end=" + ")
    else:
        print(f"1/{i}!")

# Exibe o resultado final
print(f"\nO resultado da série 1 + 1/1! + ... + 1/{numero}! é: {total}")
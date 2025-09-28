# Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

print("Cálculo da série de Fibonacci até o N'nésimo termo")

try:
    # 1. Recebe a entrada do usuário
    n = int(input("Digite um número inteiro positivo: "))
    
    # 2. Validação da entrada
    if n <= 0:
        print("Número inválido. Por favor, digite um número inteiro positivo.")
        # Encerra a execução após a mensagem de erro
        exit()
        
except ValueError:
    # 3. Tratativa de erro para entrada não-numérica
    print("Entrada inválida. Por favor, digite um número inteiro.")
    # Encerra a execução após a mensagem de erro
    exit()

# --- Lógica de Cálculo de Fibonacci (Substitui a função 'calcular_fibonacci') ---

fibonacci = []

if n == 1:
    fibonacci = [0]
elif n >= 2:
    # Inicializa a série com os dois primeiros termos
    fibonacci = [0, 1]
    
    # Gera os termos restantes
    for i in range(2, n):
        # O próximo termo é a soma dos dois termos anteriores
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)

# Exibe o resultado. (Se n<=0, 'fibonacci' é a lista vazia inicial)
print(f"A série de Fibonacci até o {n}º termo é: {fibonacci}")
# Cálculo da série 1 + 2/3 + 3/5 + ... + 50/99

# Definição do limite da série (o numerador vai até 50)
n = 50
total = 0.0

print("Cálculo da série 1 + 2/3 + 3/5 + ... + 50/99")

# Loop para calcular cada termo e somar ao total
for i in range(1, n + 1):
    # O numerador é 'i'
    numerador = i
    
    # O denominador segue o padrão 2*i - 1
    denominador = 2 * i - 1
    
    # Adiciona o termo (numerador/denominador) ao total
    total += numerador / denominador
    
    # Imprime o termo para visualização da série
    print(f"{numerador}/{denominador}", end=" + " if i < n else "\n")
    

# Exibe o resultado final
print(f"O resultado da série é: {total:.4f}")
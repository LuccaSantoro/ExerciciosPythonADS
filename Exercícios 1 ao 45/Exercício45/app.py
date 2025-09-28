# Cálculo da série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225

# Definição do limite da série
n = 15
total = 0.0

print("Cálculo da série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225")

# Loop para calcular cada termo e somar ao total
for i in range(1, n + 1):
    # O termo é i / i²
    termo = i / (i * i)
    
    # Se i for par, o termo deve ser negativo (subtração)
    if i % 2 == 0:
        termo = -termo
    
    # Adiciona o termo (positivo ou negativo) ao total
    total += termo
    
    # Imprime o termo para visualização da série (opcional)
    # Mostra o sinal de '+' entre os termos, exceto no último
    if i < n:
        # Verifica o sinal do próximo termo (i+1) para saber qual separador usar
        separador = " + "
        if (i + 1) % 2 == 0:
            separador = " " # Se o próximo for par, o sinal '-' será impresso antes dele
        
        print(f"{i}/{i*i}", end=separador)
    else:
        print(f"{i}/{i*i}") # Último termo
    

# Exibe o resultado final
print(f"O resultado da série é: {total:.4f}")
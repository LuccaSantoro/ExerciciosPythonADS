# Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 1 2 3 4 ... 64
# Qdte: 1 2 4 8 ... N

print("Cálculo da quantidade de grãos em um tabuleiro de xadrez")

# Variáveis de controle
total_graos = 0
graos_casa = 1  # Começa com 1 grão na primeira casa

# Loop para iterar pelas 64 casas do tabuleiro
for casa in range(1, 65):
    # Adiciona os grãos da casa atual ao total
    total_graos += graos_casa
    
    # Imprime o resultado da casa atual
    print(f"Casa {casa}: {graos_casa} grão(s)")
    
    # Dobra a quantidade de grãos para a próxima casa
    graos_casa *= 2

# Exibe o resultado final
print(f"\nTotal de grãos no tabuleiro: {total_graos}")
#Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
#Casa: 1 2 3 4 ... 64
#Qdte: 1 2 4 8 ... N

print("Cálculo da quantidade de grãos em um tabuleiro de xadrez")

def calcular_graos():
    total_graos = 0
    graos_casa = 1  # Começa com 1 grão na primeira casa

    for casa in range(1, 65):  # Casas de 1 a 64
        total_graos += graos_casa
        print(f"Casa {casa}: {graos_casa} grão(s)")
        graos_casa *= 2  # Dobra a quantidade de grãos para a próxima casa

    print(f"\nTotal de grãos no tabuleiro: {total_graos}")

if __name__ == "__main__":  
    calcular_graos()
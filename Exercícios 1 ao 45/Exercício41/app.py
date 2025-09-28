# Mostrando todas as possibilidades de 2 dados que somam 7

# Lista para armazenar os pares de dados
possibilidades = []

print("Mostrando todas as possibilidades de 2 dados que somam 7")

# Loop para o primeiro dado (valores de 1 a 6)
for dado1 in range(1, 7):
    # Loop para o segundo dado (valores de 1 a 6)
    for dado2 in range(1, 7):
        # Verifica se a soma dos dois dados é igual a 7
        if dado1 + dado2 == 7:
            # Adiciona o par de dados à lista de possibilidades
            possibilidades.append((dado1, dado2))
            
# Exibe o título
print("As combinações possíveis de dois dados que somam 7 são:")

# Itera sobre a lista e imprime cada combinação
for combo in possibilidades:
    print(f"Dado 1: {combo[0]}, Dado 2: {combo[1]}")
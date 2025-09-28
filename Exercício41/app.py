#Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.

print("Mostrando todas as possibilidades de 2 dados que somam 7")

def mostrar_possibilidades():
    possibilidades = []
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if dado1 + dado2 == 7:
                possibilidades.append((dado1, dado2))
    
    print("As combinações possíveis de dois dados que somam 7 são:")
    for combo in possibilidades:
        print(f"Dado 1: {combo[0]}, Dado 2: {combo[1]}")

if __name__ == "__main__":
    mostrar_possibilidades()
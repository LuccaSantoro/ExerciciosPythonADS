def obter_nota(bimestre):
    return float(input(f"Insira a nota do {bimestre}º bimestre:"))

def calcular_media(notas):
    return sum(notas) / len(notas)

def mostrar_resultado(media):
    print(f"A média do aluno é {media:.2f}")
    if media >= 6:
        print("APROVADO")
    elif media < 3:
        print("RETIDO")
    else:
        print("EXAME")

def main():
    print("Calcule a nota média de um aluno em 4 bimestres")
    notas = [obter_nota(i) for i in range(1, 5)]
    media = calcular_media(notas)
    mostrar_resultado(media)

if __name__ == "__main__":
    main()

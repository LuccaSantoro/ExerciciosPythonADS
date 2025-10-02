#Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

quilos = float(input("Digite a quantidade de alimento (kg): "))

gramas = quilos * 1000
dias = gramas / 50

print("O alimento vai durar", dias, "dias.")

#Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo

ang1 = float(input("Digite o valor do primeiro angulo: "))
ang2 = float(input("Digite o valor do segundo angulo: "))

ang3 = 180 - (ang1 + ang2)

print("O terceiro angulo e:", ang3)

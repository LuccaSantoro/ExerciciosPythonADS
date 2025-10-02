#Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

cateto1 = float(input("Digite o valor de um cateto: "))
cateto2 = float(input("Digite o valor do outro cateto: "))

soma_quadrados = (cateto1 * cateto1) + (cateto2 * cateto2)
hipotenusa = soma_quadrados ** 0.5

print("O valor da hipotenusa e:", hipotenusa)

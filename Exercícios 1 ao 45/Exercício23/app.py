# Organize quatro números em ordem crescente

#Declarar
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
n4 = float(input("Digite o quarto numero: "))
lista_numeros = []

#Início
lista_numeros = [n1, n2, n3, n4]
lista_numeros.sort()

print("Os numeros em ordem crescente sao:")
for numero in lista_numeros:
  print(numero)

#fim

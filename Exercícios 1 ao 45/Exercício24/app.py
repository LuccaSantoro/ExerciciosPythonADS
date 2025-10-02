# Saiba se um número inteiro é divisível por 2 ou por 3

#Declarar
numero = int(input("Digite um numero inteiro: "))

#Início
if (numero % 2 == 0) and (numero % 3 == 0):
  print("O numero e divisivel por 2 e por 3")
elif numero % 2 == 0:
  print("O numero e divisivel por 2")
elif numero % 3 == 0:
  print("O numero e divisivel por 3")
else:
  print("O numero nao e divisivel por 2 nem por 3")

#fim

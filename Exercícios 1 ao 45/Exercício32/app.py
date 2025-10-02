# Código que calcula o fatorial de um número inteiro.

#Declarar
num = int(input("Digite um numero: "))
fatorial = 1

#Início
if num < 0:
  print("Nao existe fatorial para numero negativo.")
elif num == 0:
  print("O fatorial de 0 e 1.")
else:
  for i in range(1, num + 1):
    fatorial = fatorial * i
  print("O fatorial de", num, "e", fatorial)

#fim

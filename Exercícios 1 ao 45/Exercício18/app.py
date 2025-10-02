#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

#Declarar
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
resultado = 0

#Início
if n1 > n2:
  resultado = n1 - n2
else:
  resultado = n2 - n1

print("A diferenca entre o maior e o menor e:", resultado)

#fim

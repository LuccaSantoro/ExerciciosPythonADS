# Receba um número N. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N. 

#Declarar
n = int(input("Digite um numero N: "))
soma = 0

#Início
for i in range(1, n + 1):
  soma = soma + (1/i)

print("O resultado da serie e:", soma)

#fim

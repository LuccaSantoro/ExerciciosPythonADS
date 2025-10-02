# Cálculo da série 1 + 2/3 + 3/5 + ... + 50/99

#Declarar
soma = 0.0
numerador = 0
denominador = 0

#Início
# O laço vai de 1 a 50
for i in range(1, 51):
  numerador = i
  denominador = (2 * i) - 1
  soma = soma + (numerador / denominador)

print("O resultado da serie e:", soma)

#fim

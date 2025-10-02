# Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

#Declarar
n = int(input("Digite um numero: "))
soma = 1.0 # Começa com 1, que é o primeiro termo da série (1/0!)
fatorial = 1

#Início
# Laço principal, para cada termo da série
for i in range(1, n + 1):
  
  # Laço interno para calcular o fatorial de 'i'
  fatorial = 1
  for j in range(1, i + 1):
    fatorial = fatorial * j
  
  # Soma o termo (1/fatorial) ao total
  soma = soma + (1 / fatorial)

print("O resultado da serie e:", soma)

#fim

# Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

#Declarar
n = int(input("Digite quantos termos da serie de Fibonacci voce quer: "))
anterior = 0
atual = 1
proximo = 0

#Início
print("Serie de Fibonacci:")

if n <= 0:
  print("Por favor, digite um numero positivo.")
elif n == 1:
  print(anterior)
else:
  print(anterior)
  print(atual)
  for i in range(2, n):
    proximo = anterior + atual
    print(proximo)
    anterior = atual
    atual = proximo

#fim

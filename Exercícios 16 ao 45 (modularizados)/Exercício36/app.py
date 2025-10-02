#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

#Declarar
n = 0
soma = 0.0

#procedimento
def Leitura():
  global n
  n = int(input("Digite um numero inteiro positivo: "))

#procedimento
def Calculo():
  global n, soma
  # A soma começa com 1.0 para representar o primeiro termo (1/0!)
  soma = 1.0
  
  # Laço principal da série (de 1 a N)
  for i in range(1, n + 1):
    fatorial = 1
    # Laço interno para calcular o fatorial de 'i'
    for j in range(1, i + 1):
      fatorial = fatorial * j
    
    # Adiciona o termo da série ao total
    soma = soma + (1 / fatorial)

#Início
Leitura()
Calculo()
print("O resultado da serie e:", soma)

#fim

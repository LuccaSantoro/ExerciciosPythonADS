#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

#Declarar
n = 0
soma_final = 0.0

#procedimento
def Leitura():
  global n
  n = int(input("Digite um numero inteiro positivo: "))

#procedimento
def Calculo():
  global n, soma_final
  for i in range(1, n + 1):
    soma_final = soma_final + (1/i)

#Início
Leitura()
Calculo()
print("O resultado da serie e:", soma_final)

#fim

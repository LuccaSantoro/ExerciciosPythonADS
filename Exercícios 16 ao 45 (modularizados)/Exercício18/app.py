# Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

#Declarar
num1 = 0
num2 = 0
diferenca = 0

#procedimento
def Leitura():
  global num1, num2
  num1 = int(input("Digite o primeiro numero: "))
  num2 = int(input("Digite o segundo numero: "))

#procedimento
def CalculaDiferenca():
  global num1, num2, diferenca
  if num1 > num2:
    diferenca = num1 - num2
  else:
    diferenca = num2 - num1

#Início
Leitura()
CalculaDiferenca()
print("A diferenca do maior para o menor e:", diferenca)

#fim

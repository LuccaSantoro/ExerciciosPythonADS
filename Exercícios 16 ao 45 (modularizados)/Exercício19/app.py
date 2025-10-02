# Receba 2 valores reais. Calcule e mostre o maior deles

#Declarar
num1 = 0.0
num2 = 0.0

#procedimento
def Leitura():
  global num1, num2
  num1 = float(input("Digite um numero: "))
  num2 = float(input("Digite outro numero: "))

#procedimento
def MostraMaior():
  global num1, num2
  if num1 > num2:
    print("O maior numero e:", num1)
  elif num2 > num1:
    print("O maior numero e:", num2)
  else:
    print("Os numeros sao iguais.")

#Início
Leitura()
MostraMaior()

#fim

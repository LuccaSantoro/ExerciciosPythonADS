#Receba 2 valores reais. Calcule e mostre o maior deles

#Declarar
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

#Início
if num1 > num2:
  print("O maior valor e:", num1)
elif num2 > num1:
  print("O maior valor e:", num2)
else:
  print("Os dois valores sao iguais.")

#fim

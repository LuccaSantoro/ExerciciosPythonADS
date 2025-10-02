#Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

#Declarar
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = 0
x1 = 0
x2 = 0

#Início
delta = (b*b) - (4*a*c)

if delta < 0:
  print("Nao ha raizes reais.")
elif delta == 0:
  x1 = (-b) / (2*a)
  print("Ha uma raiz real:", x1)
else:
  x1 = (-b + delta**0.5) / (2*a)
  x2 = (-b - delta**0.5) / (2*a)
  print("As raizes sao:", x1, "e", x2)

#fim

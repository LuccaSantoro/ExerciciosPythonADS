# Descubra se o maior número é múltiplo do menor (Enunciado Original)

#Declarar
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
maior = 0
menor = 0

#Início
if n1 > n2:
  maior = n1
  menor = n2
else:
  maior = n2
  menor = n1

if menor == 0:
  print("Nao se pode dividir por zero.")
elif maior % menor == 0:
  print(maior, "e multiplo de", menor)
else:
  print(maior, "nao e multiplo de", menor)

#fim

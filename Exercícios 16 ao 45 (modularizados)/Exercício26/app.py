#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo
do menor.

#Declarar
num1 = 0
num2 = 0

#procedimento
def Leitura():
  global num1, num2
  num1 = int(input("Digite o primeiro valor: "))
  num2 = int(input("Digite o segundo valor: "))

#procedimento
def Verifica():
  global num1, num2
  maior = 0
  menor = 0
  
  if num1 > num2:
    maior = num1
    menor = num2
  else:
    maior = num2
    menor = num1
  
  if menor == 0:
    print("Nao e possivel dividir por zero.")
  elif maior % menor == 0:
    print(maior, "e multiplo de", menor)
  else:
    print(maior, "nao e multiplo de", menor)

#Início
Leitura()
Verifica()

#fim

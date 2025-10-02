# Organize dois números inteiros em ordem decrescente

#Declarar
num1 = 0
num2 = 0

#procedimento
def Leitura():
  global num1, num2
  num1 = int(input("Digite o primeiro numero: "))
  num2 = int(input("Digite o segundo numero: "))

#procedimento
def Ordena():
  global num1, num2
  print("Os numeros em ordem decrescente sao:")
  if num1 > num2:
    print(num1)
    print(num2)
  else:
    print(num2)
    print(num1)

#Início
Leitura()
Ordena()

#fim

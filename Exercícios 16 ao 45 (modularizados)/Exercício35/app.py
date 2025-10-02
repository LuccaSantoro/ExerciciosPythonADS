#Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

#Declarar
num1 = 0
num2 = 0
soma = 0

#procedimento
def Leitura():
  global num1, num2
  num1 = int(input("Digite o primeiro numero: "))
  num2 = int(input("Digite o segundo numero: "))

#procedimento
def Calculo():
  global num1, num2, soma
  maior = 0
  menor = 0
  
  if num1 > num2:
    maior = num1
    menor = num2
  else:
    maior = num2
    menor = num1
  
  for i in range(menor + 1, maior):
    if i % 2 != 0:
      soma = soma + i

#Início
Leitura()
Calculo()
print("A soma dos impares entre os dois numeros e:", soma)

#fim

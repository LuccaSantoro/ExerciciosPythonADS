#Calcule e mostre o quadrado dos números entre 10 e 150.

#Declarar
numero = 0
quadrado = 0

#procedimento
def Leitura():
  global numero
  numero = float(input("Digite um numero: "))

#procedimento
def Calculo():
  global numero, quadrado
  if numero >= 10 and numero <= 150:
    quadrado = numero * numero
    print("O quadrado de", numero, "e:", quadrado)
  else:
    print("O numero esta fora do intervalo permitido (10 a 150).")

#Início
Leitura()
Calculo()

#fim

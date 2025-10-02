# Receba um número inteiro. Calcule e mostre o seu fatorial.

#Declarar
numero = 0
fatorial = 1

#procedimento
def Leitura():
  global numero
  numero = int(input("Digite um numero para o fatorial: "))

#procedimento
def Calculo():
  global numero, fatorial
  if numero < 0:
    print("Nao existe fatorial para numeros negativos.")
  elif numero == 0:
    print("O fatorial de 0 e 1.")
  else:
    for i in range(1, numero + 1):
      fatorial = fatorial * i
    print("O fatorial de", numero, "e:", fatorial)

#Início
Leitura()
Calculo()

#fim

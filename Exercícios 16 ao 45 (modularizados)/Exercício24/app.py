# Saiba se um número inteiro é divisível por 2 ou por 3

#Declarar
numero = 0

#procedimento
def Leitura():
  global numero
  numero = int(input("Digite um numero inteiro: "))

#procedimento
def Verifica():
  global numero
  if (numero % 2 == 0) and (numero % 3 == 0):
    print("O numero e divisivel por 2 e por 3.")
  elif numero % 2 == 0:
    print("O numero e divisivel apenas por 2.")
  elif numero % 3 == 0:
    print("O numero e divisivel apenas por 3.")
  else:
    print("O numero nao e divisivel nem por 2 nem por 3.")

#Início
Leitura()
Verifica()

#fim

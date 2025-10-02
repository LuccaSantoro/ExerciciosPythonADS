#Receba um número. Calcule e mostre os resultados da tabuada desse número.

#Declarar
numero = 0

#procedimento
def Leitura():
  global numero
  numero = int(input("Digite um numero para ver a sua tabuada: "))

#procedimento
def Tabuada():
  global numero
  resultado = 0
  print("--- Tabuada do", numero, "---")
  for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

#Início
Leitura()
Tabuada()

#fim

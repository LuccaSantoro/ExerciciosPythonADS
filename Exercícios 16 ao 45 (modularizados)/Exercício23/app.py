# Organize quatro números em ordem crescente

#Declarar
n1 = 0
n2 = 0
n3 = 0
n4 = 0
lista_final = []

#procedimento
def Leitura():
  global n1, n2, n3, n4
  n1 = float(input("Digite o 1º numero: "))
  n2 = float(input("Digite o 2º numero: "))
  n3 = float(input("Digite o 3º numero: "))
  n4 = float(input("Digite o 4º numero: "))

#procedimento
def Ordena():
  global n1, n2, n3, n4, lista_final
  # Coloca os numeros lidos em uma lista
  lista_numeros = [n1, n2, n3, n4]
  # Ordena a lista
  lista_numeros.sort()
  lista_final = lista_numeros

#Início
Leitura()
Ordena()
print("Os numeros em ordem crescente sao:", lista_final)

#fim

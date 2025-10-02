#Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

#Declarar
n_termos = 0

#procedimento
def Leitura():
  global n_termos
  n_termos = int(input("Digite o numero de termos da serie de Fibonacci: "))

#procedimento
def CalculaMostra():
  global n_termos
  anterior = 0
  atual = 1
  
  print("A serie de Fibonacci e:")
  
  if n_termos <= 0:
    print("O numero deve ser positivo.")
  elif n_termos == 1:
    print(anterior)
  else:
    print(anterior)
    print(atual)
    for i in range(2, n_termos):
      proximo = anterior + atual
      print(proximo)
      anterior = atual
      atual = proximo

#Início
Leitura()
CalculaMostra()

#fim

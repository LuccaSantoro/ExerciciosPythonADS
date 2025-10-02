#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

#Declarar
maior_valor = 0
menor_valor = 0

#procedimento
def Verifica():
  global maior_valor, menor_valor
  num = 0
  
  # Lê o primeiro número para ter um ponto de partida
  num = int(input("Digite o 1º numero: "))
  maior_valor = num
  menor_valor = num
  
  # Agora lê os 99 números restantes
  for i in range(99):
    num = int(input(f"Digite o {i+2}º numero: "))
    if num > maior_valor:
      maior_valor = num
    if num < menor_valor:
      menor_valor = num

#Início
Verifica()
print("O maior numero digitado foi:", maior_valor)
print("O menor numero digitado foi:", menor_valor)

#fim

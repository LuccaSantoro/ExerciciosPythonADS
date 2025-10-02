# Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

#Declarar
num = 0
maior = 0
menor = 0

#Início
# Lê o primeiro número para definir o maior e o menor iniciais
num = int(input("Digite o 1º numero: "))
maior = num
menor = num

# Faz um laço para ler os outros 99 números
for i in range(99):
  num = int(input(f"Digite o {i + 2}º numero: "))
  if num > maior:
    maior = num
  if num < menor:
    menor = num

print("O maior valor foi:", maior)
print("O menor valor foi:", menor)

#fim

# Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.

#Declarar
valor1 = int(input("Digite o primeiro numero: "))
valor2 = int(input("Digite o segundo numero: "))
maior = 0
menor = 0

#Início
if valor1 > valor2:
  maior = valor1
  menor = valor2
else:
  maior = valor2
  menor = valor1

print("Os numeros primos no intervalo sao:")

# Para cada número entre o menor e o maior...
for num in range(menor + 1, maior):
  eh_primo = True
  
  # ...verifica se ele é primo.
  if num < 2:
    eh_primo = False
  else:
    # Laço não otimizado: testa todos os divisores de 2 até num-1
    for i in range(2, num):
      if num % i == 0:
        eh_primo = False
        break
  
  if eh_primo == True:
    print(num)

#fim

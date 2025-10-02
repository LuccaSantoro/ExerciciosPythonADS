# Calcule o quadrado dos números entre 10 e 150

#Declarar
quadrado = 0

#Início
# O laço vai de 10 até 150 (o 151 não é incluído)
for numero in range(10, 151):
  quadrado = numero * numero
  print("O quadrado de", numero, "e", quadrado)

#fim

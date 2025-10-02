# Cálculo de potência (base^expoente)

#Declarar
base = float(input("Digite o numero base: "))
expoente = int(input("Digite o expoente (deve ser inteiro positivo): "))
resultado = 1

#Início
# Laço para multiplicar a base por ela mesma, 'expoente' vezes
for i in range(expoente):
  resultado = resultado * base

print("O resultado e:", resultado)

#fim

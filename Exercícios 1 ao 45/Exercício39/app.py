# Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 1 2 3 4 ... 64
# Qdte: 1 2 4 8 ... N

#Declarar
total = 0
graos = 0

#Início
# O laço vai de 0 a 63 (64 casas) para usar no expoente
for i in range(64):
  graos = 2**i
  total = total + graos

print("O total de graos no tabuleiro e:", total)

#fim

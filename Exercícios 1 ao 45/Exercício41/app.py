# Mostrando todas as possibilidades de 2 dados que somam 7

#Declarar
d1 = 0
d2 = 0

#Início
print("As combinacoes de dados que somam 7 sao:")
for d1 in range(1, 7):
  for d2 in range(1, 7):
    if d1 + d2 == 7:
      print(d1, "e", d2)

#fim

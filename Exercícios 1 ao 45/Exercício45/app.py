# Cálculo da série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225

#Declarar
soma = 0.0
termo = 0.0

#Início
# O laço vai de 1 a 15
for i in range(1, 16):
  termo = i / (i * i)
  
  # Se o contador 'i' for par, o termo deve ser subtraído
  if i % 2 == 0:
    soma = soma - termo
  # Se for ímpar, o termo deve ser somado
  else:
    soma = soma + termo

print("O resultado da serie e:", soma)

#fim

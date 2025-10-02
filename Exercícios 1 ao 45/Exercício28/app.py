# Calcule o novo preço de um produto

#Declarar
preco = float(input("Qual o preco atual do produto? "))
venda = int(input("Qual a venda mensal? "))
novo_preco = 0

#Início
if venda < 500 and preco < 30:
  novo_preco = preco * 1.10
  print("O novo preco sera:", novo_preco)
elif (venda >= 500 and venda < 1200) and (preco >= 30 and preco < 80):
  novo_preco = preco * 1.15
  print("O novo preco sera:", novo_preco)
elif venda >= 1200 and preco >= 80:
  novo_preco = preco * 0.95
  print("O novo preco sera:", novo_preco)
else:
  print("O preco se mantem o mesmo:", preco)

#fim

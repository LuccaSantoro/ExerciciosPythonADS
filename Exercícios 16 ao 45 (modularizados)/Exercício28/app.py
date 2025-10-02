# Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
# Venda Mensal Preço Atual Preço Novo
# < 500 < 30 + 10%
# >= 500 e < 1000 >= 30 e < 80 +15%
# >= 1000 >= 80 - 5%
# Obs.: para outras condições, preço novo será igual ao preço atual

#Declarar
preco_atual = 0
venda_mensal = 0

#procedimento
def Leitura():
  global preco_atual, venda_mensal
  preco_atual = float(input("Insira o valor atual do produto: "))
  venda_mensal = int(input("Insira a venda mensal do produto: "))

#procedimento
def CalculaReajuste():
  global preco_atual, venda_mensal
  novo_preco = 0
  
  if venda_mensal < 500 and preco_atual < 30:
    novo_preco = preco_atual * 1.1
    print("O novo preco e:", novo_preco)
  elif (venda_mensal >= 500 and venda_mensal < 1000) and (preco_atual >= 30 and preco_atual < 80):
    novo_preco = preco_atual * 1.15
    print("O novo preco e:", novo_preco)
  elif venda_mensal >= 1000 and preco_atual >= 80:
    novo_preco = preco_atual * 0.95
    print("O novo preco e:", novo_preco)
  else:
    print("O preco nao sofreu reajuste:", preco_atual)

#Início
Leitura()
CalculaReajuste()

#fim

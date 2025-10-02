# Calcule o valor corrigido de um investimento na poupança ou renda fixa

#Declarar
valor = float(input("Digite o valor do investimento: "))
tipo = ""

#Início
print("Escolha uma opcao:")
print("1 - Poupanca (3% de rendimento)")
print("2 - Renda Fixa (5% de rendimento)")
tipo = input("Digite 1 ou 2: ")

if tipo == "1":
  valor_novo = valor * 1.03
  print("O valor corrigido na poupanca e:", valor_novo)
elif tipo == "2":
  valor_novo = valor * 1.05
  print("O valor corrigido na renda fixa e:", valor_novo)
else:
  print("Opcao invalida.")

#fim

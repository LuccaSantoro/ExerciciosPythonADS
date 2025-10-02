# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

#Declarar
valor_investimento = 0
tipo_investimento = ""
valor_final = 0

#procedimento
def Leitura():
  global valor_investimento, tipo_investimento
  valor_investimento = float(input("Digite o valor do investimento: "))
  print("--- TIPO DE INVESTIMENTO ---")
  print("1 - Poupanca (3%)")
  print("2 - Renda Fixa (5%)")
  tipo_investimento = input("Digite 1 ou 2: ")

#procedimento
def Calculo():
  global valor_investimento, tipo_investimento, valor_final
  if tipo_investimento == "1":
    valor_final = valor_investimento * 1.03
    print("O valor corrigido na poupanca e:", valor_final)
  elif tipo_investimento == "2":
    valor_final = valor_investimento * 1.05
    print("O valor corrigido na renda fixa e:", valor_final)
  else:
    print("Opcao invalida.")

#Início
Leitura()
Calculo()

#fim

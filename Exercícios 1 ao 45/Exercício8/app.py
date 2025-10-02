#Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.

valor = float(input("Qual o valor do deposito? "))

rendimento = valor * 0.013
valor_final = valor + rendimento

print("O novo valor com rendimento e:", valor_final)


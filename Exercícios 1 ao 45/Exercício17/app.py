#Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

tempo = float(input("Qual o tempo de viagem (horas)? "))
velocidade = float(input("Qual a velocidade media (km/h)? "))

distancia = tempo * velocidade
litros = distancia / 12

print("Voce vai gastar", litros, "litros de combustivel.")

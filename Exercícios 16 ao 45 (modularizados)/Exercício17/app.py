# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

#Declarar
tempo_viagem = 0
vel_media = 0
distancia_final = 0
litros_gastos = 0

#procedimento
def Entrada():
  global tempo_viagem, vel_media
  tempo_viagem = float(input("Digite o tempo de percurso em horas: "))
  vel_media = float(input("Digite a velocidade media em km/h: "))

#procedimento
def Calculo():
  global tempo_viagem, vel_media, distancia_final, litros_gastos
  distancia_final = tempo_viagem * vel_media
  litros_gastos = distancia_final / 12

#Início
Entrada()
Calculo()
print("A distancia percorrida foi de", distancia_final, "km.")
print("A quantidade de litros gastos foi de", litros_gastos, "litros.")

#fim

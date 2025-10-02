#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de
duração (minutos). Calcule e mostre a velocidade média em km/h.

#Declarar
voltas = 0
circuito_m = 0
tempo_min = 0
velocidade_final = 0

#procedimento
def Leitura():
  global voltas, circuito_m, tempo_min
  voltas = int(input("Digite o numero de voltas: "))
  circuito_m = float(input("Digite a extensao do circuito em metros: "))
  tempo_min = int(input("Digite o tempo em minutos: "))

#procedimento
def Calculo():
  global voltas, circuito_m, tempo_min, velocidade_final
  distancia_km = (voltas * circuito_m) / 1000
  tempo_h = tempo_min / 60
  velocidade_final = distancia_km / tempo_h

#Início
Leitura()
Calculo()
print("A velocidade media foi de", velocidade_final, "km/h")

#fim

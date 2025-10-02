# Calcule a velocidade média(km/h) de um circuito

#Declarar
voltas = int(input("Digite a quantidade de voltas: "))
tamanho_m = float(input("Digite o tamanho do circuito em metros: "))
tempo_min = int(input("Digite o tempo total em minutos: "))
distancia_km = 0
tempo_h = 0
vel_media = 0

#Início
distancia_km = (voltas * tamanho_m) / 1000
tempo_h = tempo_min / 60

vel_media = distancia_km / tempo_h

print("A velocidade media foi de", vel_media, "km/h.")

#fim

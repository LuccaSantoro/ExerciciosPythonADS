print("Calcule a velocidade média(km/h) de um circuito")

#declarar

def percorrido_km():
    while True:
        try:
            voltas = float(input("Insira a quantidade de voltas:"))
            if voltas <= 0:
                print("A quantidade de voltas deve ser maior que zero.")
                continue
            tamanho_circuito = float(input("Insira o tamanho do circuito em metros:"))
            if tamanho_circuito <= 0:
                print("O tamanho do circuito deve ser maior que zero.")
                continue
            total_percorrido = voltas * (tamanho_circuito/1000)
            return total_percorrido
        except ValueError:
            print("Por favor, insira um número válido.")

def converter_horas():
    while True:
        try:
            minutos = int(input("Insira a duração do trajeto em minutos:"))
            if minutos <= 0:
                print("A duração deve ser maior que zero.")
                continue
            horas = minutos/60
            return horas
        except ValueError:
            print("Por favor, insira um número válido.")

#inicio

distancia = percorrido_km()
tempo = converter_horas()

velocidade_media = distancia/tempo

print(f"A velocidade média foi de {velocidade_media:.2f} km/h")

#fim

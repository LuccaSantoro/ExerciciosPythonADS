# Calcule a velocidade média(km/h) de um circuito

print("Calcule a velocidade média (km/h) de um circuito")

# --- Lógica de cálculo da Distância Total em Km ---
while True:
    try:
        # 1. Recebe e valida a quantidade de voltas
        voltas = float(input("Insira a quantidade de voltas: "))
        if voltas <= 0:
            print("A quantidade de voltas deve ser maior que zero.")
            continue
            
        # 2. Recebe e valida o tamanho do circuito em metros
        tamanho_circuito = float(input("Insira o tamanho do circuito em metros: "))
        if tamanho_circuito <= 0:
            print("O tamanho do circuito deve ser maior que zero.")
            continue
            
        # 3. Calcula o total percorrido em KM
        # (metros / 1000) * voltas
        distancia = voltas * (tamanho_circuito / 1000)
        break # Sai do loop se as entradas forem válidas
        
    except ValueError:
        print("Por favor, insira um número válido para voltas ou tamanho.")

# --- Lógica de cálculo do Tempo Total em Horas ---
while True:
    try:
        # 1. Recebe e valida a duração em minutos
        minutos = int(input("Insira a duração do trajeto em minutos: "))
        if minutos <= 0:
            print("A duração deve ser maior que zero.")
            continue
            
        # 2. Converte minutos para horas (minutos / 60)
        tempo = minutos / 60
        break # Sai do loop se a entrada for válida
        
    except ValueError:
        print("Por favor, insira um número válido para minutos.")

# --- Cálculo Final e Exibição ---

# Velocidade Média = Distância (Km) / Tempo (h)
velocidade_media = distancia / tempo

print(f"\nA velocidade média foi de {velocidade_media:.2f} km/h")
#Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

print("Calcule a quantidade de litros gastos em uma viagem")

# --- Lógica de Entrada (Substitui a função 'get_input') ---
try:
    tempo_percurso = float(input("Insira o tempo de percurso (em horas): "))
    velocidade_media = float(input("Insira a velocidade média (em km/h): "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo (Substitui a função 'calcula_litros') ---

# Distância = Tempo * Velocidade

distancia = tempo_percurso * velocidade_media
litros_gastos = distancia / 12  # Consumo de 12 km/l

print(f"Você gastará {litros_gastos:.2f} litros de combustível para percorrer {distancia:.2f} km.")

# --- Fim da Lógica de Cálculo ---

#fim
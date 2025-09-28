#Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5.

print("Cálculo de Conversão de Temperatura de Celsius para Fahrenheit")

try:
    # 1. Recebe a entrada do valor em Celsius
    celsius = float(input("Insira a temperatura em graus Celsius: "))

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit()

# --- Lógica de Cálculo da Conversão (Substitui a função 'converte_celsius_fahrenheit') ---

fahrenheit = (9 * celsius + 160) / 5
print(f"A temperatura de {celsius}°C em Fahrenheit é: {fahrenheit:.2f}°F")

# --- Fim da Lógica de Cálculo ---

#fim
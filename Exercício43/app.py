#Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

print("Cálculo do tempo necessário para Ana ser mais alta que Maria")

def calcular_tempo_necessario():
    altura_ana = 1.10  # Altura inicial de Ana em metros
    altura_maria = 1.50  # Altura inicial de Maria em metros
    crescimento_ana = 0.03  # Crescimento anual de Ana em metros
    crescimento_maria = 0.02  # Crescimento anual de Maria em metros
    anos = 0

    while altura_ana <= altura_maria:
        altura_ana += crescimento_ana
        altura_maria += crescimento_maria
        anos += 1

    print(f"Serão necessários {anos} anos para que Ana seja mais alta que Maria.")
    print(f"Altura final de Ana: {altura_ana:.2f} m")
    print(f"Altura final de Maria: {altura_maria:.2f} m")

if __name__ == "__main__":
    calcular_tempo_necessario()

# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

TAXA_CONSUMO = 12  # km/l

def obter_dados():
    """
    Solicita o tempo de percurso e a velocidade média ao usuário.
    Realiza a validação para garantir que são números.
    """
    print("Calcule a quantidade de litros gastos em uma viagem")
    while True:
        try:
            tempo_percurso = float(input("Insira o tempo de percurso (em horas): "))
            velocidade_media = float(input("Insira a velocidade média (em km/h): "))
            
            # Validação simples para evitar valores negativos ou zero no cálculo
            if tempo_percurso <= 0 or velocidade_media <= 0:
                print("O tempo e a velocidade devem ser maiores que zero.")
                continue
                
            return tempo_percurso, velocidade_media
        
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números.")

def calcular_litros(tempo_percurso, velocidade_media):
    """
    Calcula a distância percorrida e a quantidade de litros gastos.
    """
    # Distância = Tempo * Velocidade
    distancia = tempo_percurso * velocidade_media
    
    # Litros = Distância / Consumo (12 km/l)
    litros_gastos = distancia / TAXA_CONSUMO
    
    return litros_gastos, distancia

def main():
    """
    Função principal que coordena a execução do programa.
    """
    # 1. Obtém as entradas
    tempo, velocidade = obter_dados()
    
    # 2. Calcula os litros e a distância
    litros, distancia = calcular_litros(tempo, velocidade)
    
    # 3. Exibe o resultado
    print(f"Você gastará {litros:.2f} litros de combustível para percorrer {distancia:.2f} km.")

if __name__ == "__main__":
    main()
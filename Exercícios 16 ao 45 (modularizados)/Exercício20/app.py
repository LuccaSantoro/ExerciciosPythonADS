# Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

def obter_coeficientes():
    """
    Solicita os coeficientes A, B e C ao usuário com tratamento de erro.
    Garante que o coeficiente A não seja zero.
    """
    print("Cálculo de raízes reais de uma equação do 2º grau (AX² + BX + C = 0)")
    while True:
        try:
            # 1. Recebe os coeficientes A, B e C
            coeficiente_a = float(input("Digite o coeficiente A (não pode ser 0): "))
            coeficiente_b = float(input("Digite o coeficiente B: "))
            coeficiente_c = float(input("Digite o coeficiente C: "))
            
            # 2. Validação se A é zero
            if coeficiente_a == 0:
                print("O coeficiente A não pode ser zero em uma equação do 2º grau.")
                continue # Volta ao início do loop
            
            return coeficiente_a, coeficiente_b, coeficiente_c
        
        except ValueError:
            # 3. Trata erro se a entrada não for um número válido
            print("Entrada inválida. Por favor, insira números válidos para os coeficientes.")

def calcular_e_mostrar_raizes(a, b, c):
    """
    Calcula o delta, verifica a existência de raízes reais e as exibe.
    """
    # 4. Calcula o discriminante (delta = B² - 4AC)
    delta = (b**2) - (4 * a * c)

    # 5. Verifica a existência de raízes reais com base no valor de delta
    if delta < 0:
        print("Não existem raízes reais para esta equação.")
    elif delta == 0:
        # 6. Uma raiz real (raiz dupla)
        raiz = -b / (2 * a)
        print(f"Existe uma raiz real (raiz dupla): {raiz:.3f}")
    else:
        # 7. Duas raízes reais distintas
        # Usa delta**0.5 para calcular a raiz quadrada
        raiz1 = (-b + delta**0.5) / (2 * a)
        raiz2 = (-b - delta**0.5) / (2 * a)
        print(f"Existem duas raízes reais distintas: {raiz1:.3f} e {raiz2:.3f}")

def main():
    """
    Função principal que coordena a execução do programa.
    """
    # 1. Obtém os coeficientes A, B e C
    a, b, c = obter_coeficientes()
    
    # 2. Calcula e mostra as raízes
    calcular_e_mostrar_raizes(a, b, c)

if __name__ == "__main__":
    main()
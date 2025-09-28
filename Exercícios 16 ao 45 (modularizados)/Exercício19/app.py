# Receba 2 valores reais. Calcule e mostre o maior deles

def obter_valores():
    """
    Solicita dois números reais ao usuário com tratamento de erro.
    Retorna os dois valores como floats.
    """
    print("Verificação do maior valor entre dois números reais")
    while True:
        try:
            # 1. Recebe a entrada do primeiro número
            valor1 = float(input("Insira o valor do primeiro número: "))
            
            # 2. Recebe a entrada do segundo número
            valor2 = float(input("Insira o valor do segundo número: "))
            
            return valor1, valor2
        
        except ValueError:
            # Tratativa de erro para entrada não-numérica
            print("Entrada inválida. Por favor, insira apenas números.")

def verificar_e_mostrar_maior(valor1, valor2):
    """
    Compara os dois valores e exibe o maior, ou informa se são iguais.
    """
    # Lógica de Verificação do Maior Valor
    if valor1 > valor2:
        print(f"O maior valor é: {valor1}")
    elif valor2 > valor1:
        print(f"O maior valor é: {valor2}")
    else:
        print("Os dois valores são iguais.")

def main():
    """
    Função principal que coordena a execução do programa.
    """
    # 1. Obtém os valores
    val1, val2 = obter_valores()
    
    # 2. Verifica e mostra o maior valor
    verificar_e_mostrar_maior(val1, val2)

if __name__ == "__main__":
    main()
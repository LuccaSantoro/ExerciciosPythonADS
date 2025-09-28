# Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

def obter_valores():
    """
    Solicita dois números inteiros ao usuário com tratamento de erro.
    """
    print("Cálculo da diferença entre dois números inteiros")
    while True:
        try:
            # 1. Recebe a entrada do primeiro número
            valor1 = int(input("Insira o valor do primeiro número inteiro: "))
            
            # 2. Recebe a entrada do segundo número
            valor2 = int(input("Insira o valor do segundo número inteiro: "))
            
            return valor1, valor2
        
        except ValueError:
            # Tratativa de erro para entrada não-numérica
            print("Entrada inválida. Por favor, insira apenas números inteiros.")

def calcular_e_mostrar_diferenca(valor1, valor2):
    """
    Calcula a diferença entre o maior e o menor valor e exibe o resultado.
    """
    # Determina o maior e o menor
    if valor1 > valor2: 
        maior = valor1
        menor = valor2
    elif valor2 > valor1:
        maior = valor2
        menor = valor1
    else:
        # Se os valores são iguais
        print("Os dois valores são iguais. A diferença é 0.")
        return

    # Calcula a diferença
    diferenca = maior - menor
    
    # Exibe o resultado
    print(f"A diferença entre {maior} e {menor} é: {diferenca}")

def main():
    """
    Função principal que coordena a execução do programa.
    """
    # 1. Obtém os valores
    val1, val2 = obter_valores()
    
    # 2. Calcula e exibe a diferença
    calcular_e_mostrar_diferenca(val1, val2)

if __name__ == "__main__":
    main()
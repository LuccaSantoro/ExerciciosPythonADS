print("Cálculo da série 1 + 1/2 + 1/3 + ... + 1/N")
 
# modularização
def calcular_serie():
    """
    Função para calcular a soma da série harmônica até N.
    """
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        
        if numero <= 0:
            print("Número inválido. Por favor, digite um número inteiro positivo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
        
    total = 0.0
    for i in range(1, numero + 1):
        total += 1 / i

    print(f"O resultado da série 1 + 1/2 + ... + 1/{numero} é: {total}")
 
# inicio
if __name__ == "__main__":
    calcular_serie()

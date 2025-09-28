#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

print("Cálculo da série 1 + 1/1! + 1/2! + ... + 1/N!")

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

def calcular_serie():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        
        if numero < 0:
            print("Número inválido. Por favor, digite um número inteiro positivo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
    
    total = 0.0
    for i in range(0, numero + 1):
        total += 1 / calcular_fatorial(i)
    
    print(f"O resultado da série 1 + 1/1! + ... + 1/{numero}! é: {total}")

if __name__ == "__main__":
    calcular_serie()
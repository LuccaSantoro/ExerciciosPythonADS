#Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

print("Cálculo da série de Fibonacci até o N'nésimo termo")

def calcular_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci = [0, 1]
    for i in range(2, n):
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)
    
    return fibonacci

def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        
        if numero <= 0:
            print("Número inválido. Por favor, digite um número inteiro positivo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
    
    serie_fibonacci = calcular_fibonacci(numero)
    print(f"A série de Fibonacci até o {numero}º termo é: {serie_fibonacci}")

if __name__ == "__main__":
    main()
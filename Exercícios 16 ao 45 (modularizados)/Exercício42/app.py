#Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
print("Cálculo da série 1 + 2/3 + 3/5 + ... + 50/99")

def calcular_serie(n=50):
    total = 0.0
    for i in range(1, n + 1):
        numerador = i
        denominador = 2 * i - 1
        total += numerador / denominador
        print(f"{numerador}/{denominador}", end=" + " if i < n else "\n")
    
    print(f"O resultado da série é: {total:.4f}")

if __name__ == "__main__":
    calcular_serie()
    
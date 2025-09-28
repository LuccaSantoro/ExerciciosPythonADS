#Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225

print("Cálculo da série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225")

def calcular_serie(n=15):
    total = 0.0
    for i in range(1, n + 1):
        termo = i / (i * i)
        if i % 2 == 0:
            termo = -termo
        total += termo
        print(f"{'-' if i % 2 == 0 else ''}{i}/{i*i}", end=" + " if i < n else "\n")
    
    print(f"O resultado da série é: {total:.4f}")

if __name__ == "__main__":
    calcular_serie()

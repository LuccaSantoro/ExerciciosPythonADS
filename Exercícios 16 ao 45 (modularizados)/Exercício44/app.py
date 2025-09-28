#Receba o número da base e do expoente. Calcule e mostre o valor da potência.

print("Cálculo de potência (base^expoente)")

def calcular_potencia(base, expoente):
    return base ** expoente

def main():
    try:
        base = float(input("Digite a base (número real): "))
        expoente = int(input("Digite o expoente (número inteiro): "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número real para a base e um número inteiro para o expoente.")
        return
    
    resultado = calcular_potencia(base, expoente)
    print(f"O resultado de {base}^{expoente} é: {resultado}")

if __name__ == "__main__":
    main()

#Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
print("Cálculo da somatória dos números ímpares entre dois valores inteiros")

def somar_impares():
    try:
        valor1 = int(input("Insira o primeiro número inteiro: "))
        valor2 = int(input("Insira o segundo número inteiro: "))
        
        if valor1 == valor2:
            print("Os números são iguais. Por favor, insira dois números inteiros diferentes.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")
        return
    
    # Determina o intervalo correto
    menor = min(valor1, valor2)
    maior = max(valor1, valor2)
    
    soma_impares = 0
    for num in range(menor + 1, maior):
        if num % 2 != 0:
            soma_impares += num
    
    print(f"A somatória dos números ímpares entre {menor} e {maior} é: {soma_impares}")

if __name__ == "__main__":
    somar_impares()
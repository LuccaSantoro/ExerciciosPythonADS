#Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
print("Verificação de números primos entre dois valores inteiros")

def num_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def verificar_primos():
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
    
    primos = []
    for num in range(menor + 1, maior):
        if num_primo(num):
            primos.append(num)
    
    if primos:
        print(f"Números primos entre {menor} e {maior}: {primos}")
    else:
        print(f"Não há números primos entre {menor} e {maior}.")

if __name__ == "__main__":
    verificar_primos()
def is_multiple(a, b):
    if b == 0:
        return None  # Division by zero
    return a % b == 0

def check_multiples(valor1, valor2):
    if valor1 >= valor2:
        if valor2 == 0:
            print("Não é possível dividir por zero.")
        elif is_multiple(valor1, valor2):
            print(f"O número {valor1} é múltiplo de {valor2}")
        else:
            print(f"O número {valor1} não é múltiplo de {valor2}")
    else:
        if valor1 == 0:
            print("Não é possível dividir por zero.")
        elif is_multiple(valor2, valor1):
            print(f"O número {valor2} é múltiplo de {valor1}")
        else:
            print(f"O número {valor2} não é múltiplo de {valor1}")

def main():
    print("Descubra se o maior número é múltiplo do menor")
    valor1 = float(input("Insira o primeiro número:"))
    valor2 = float(input("Insira o segundo número:"))
    check_multiples(valor1, valor2)

if __name__ == "__main__":
    main()

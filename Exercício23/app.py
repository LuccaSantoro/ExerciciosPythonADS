def get_input():
    print("Organize quatro números em ordem crescente")
    print("Insira o primeiro, o segundo e o terceiro número em ordem crescente")
    valor1 = float(input("Insira o valor do primeiro número:"))
    valor2 = float(input("Insira o valor do segundo número:"))
    valor3 = float(input("Insira o valor do terceiro número:"))
    valor4 = float(input("Insira o valor do quarto número:"))
    return valor1, valor2, valor3, valor4

def print_sorted(valores):
    for v in valores:
        print(v)

def organize_numbers(valor1, valor2, valor3, valor4):
    if valor1 > valor2 > valor3:
        if valor4 >= valor1:
            print_sorted([valor4, valor1, valor2, valor3])
        elif valor4 <= valor3:
            print_sorted([valor1, valor2, valor3, valor4])
        elif valor1 > valor4 >= valor2:
            print_sorted([valor1, valor4, valor2, valor3])
        elif valor2 > valor4 >= valor3:
            print_sorted([valor1, valor2, valor4, valor3])
    else:
        print("Por favor, insira o primeiro, o segundo e o terceiro número em ordem crescente")

def main():
    valor1, valor2, valor3, valor4 = get_input()
    organize_numbers(valor1, valor2, valor3, valor4)

if __name__ == "__main__":
    main()

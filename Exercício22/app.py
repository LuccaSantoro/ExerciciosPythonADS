def get_integer(prompt):
    return int(input(prompt))

def print_in_order(a, b):
    if a > b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)

def main():
    print("Organize números inteiros em ordem crescente")
    valor1 = get_integer("Insira o valor do primeiro número:")
    valor2 = get_integer("Insira o valor do segundo número:")
    print_in_order(valor1, valor2)

if __name__ == "__main__":
    main()

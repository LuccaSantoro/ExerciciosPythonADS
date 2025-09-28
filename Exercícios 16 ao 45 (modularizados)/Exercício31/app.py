print("Calcule o quadrado dos números entre 10 e 150")

#declarar

def menu():
    try:
        valor = float(input("Insira o número: "))
        return valor
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return None

#inicio
    
valor = menu()

while valor is not None:
    if valor >= 10 and valor <= 150:
        valor_quadrado = valor ** 2
        print(f"O quadrado do número é {valor_quadrado:.2f}")
    else:
        print("O valor inserido está fora do intervalo válido (10 a 150).")
        break
    valor = menu()

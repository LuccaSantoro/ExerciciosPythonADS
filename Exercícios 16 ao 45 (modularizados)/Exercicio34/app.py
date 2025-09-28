#Receba um número. Calcule e mostre os resultados da tabuada desse número.

print("Cálculo da tabuada de um número inteiro")

def tabuada():
    try: 
        valor = int(input("Insira o número inteiro: "))
        if valor < 0:
            print("Número inválido. Por favor, insira um número inteiro positivo.")
            return
        elif valor == 0:
            print("A tabuada do 0 é sempre 0.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return
    
#inicio
    print(f"Tabuada do {valor}:")
    for i in range(1, 11):
        resultado = valor * i
        print(f"{valor} x {i} = {resultado}")

if __name__ == "__main__":
    tabuada()
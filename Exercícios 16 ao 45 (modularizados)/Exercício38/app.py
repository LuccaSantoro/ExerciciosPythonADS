#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.
print("Verificação do maior e menor valor entre 100 números inteiros positivos")

def verificar_maior_menor():
    maior = None
    menor = None
    count = 0
    
    while count < 100:
        try:
            numero = int(input(f"Digite o {count + 1}º número inteiro positivo: "))
            
            if numero < 0:
                print("Número inválido. Por favor, digite um número inteiro positivo.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue
        
        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero
        
        count += 1
    
    print(f"O maior valor digitado foi: {maior}")
    print(f"O menor valor digitado foi: {menor}")

if __name__ == "__main__":
    verificar_maior_menor()
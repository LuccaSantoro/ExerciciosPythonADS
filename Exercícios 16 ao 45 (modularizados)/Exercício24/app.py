# -*- coding: utf-8 -*-
# Função que verifica a divisibilidade de um número por 2 e/ou por 3
def verificar_divisibilidade(numero):
    # Se o número for divisível por 2 e por 3
    if numero % 2 == 0 and numero % 3 == 0:
        return "Divisível por 2 e por 3"
    # Se o número for divisível apenas por 2
    elif numero % 2 == 0:
        return "Divisível por 2"
    # Se o número for divisível apenas por 3
    elif numero % 3 == 0:
        return "Divisível por 3"
    # Se o número não for divisível nem por 2 nem por 3
    else:
        return "Não é divisível por 2 nem por 3"

# Função principal do programa
def main():
    # Exibe uma mensagem inicial ao usuário
    print("Saiba se um número inteiro é divisível por 2 ou por 3")
    # Solicita ao usuário que digite um número inteiro
    numero = int(input("Digite um número inteiro: "))
    # Chama a função para verificar a divisibilidade
    resultado = verificar_divisibilidade(numero)
    # Exibe o resultado para o usuário
    print(resultado)

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()

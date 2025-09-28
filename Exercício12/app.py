def calcular_idade(ano_nascimento, ano_referencia):
    return ano_referencia - ano_nascimento

def main():
    print('Calcule a sua idade em relação a hoje e a 17 anos')
    ano_nascimento = int(input('Insira o ano em que nasceu: '))
    ano_atual = 2025
    ano_17futuro = ano_atual + 17

    idade_atual = calcular_idade(ano_nascimento, ano_atual)
    idade_17futuro = calcular_idade(ano_nascimento, ano_17futuro)

    print(f'Sua idade atual é {idade_atual} e você terá {idade_17futuro} anos daqui 17 anos')

if __name__ == "__main__":
    main()

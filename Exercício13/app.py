def calcular_dias_comida(quant_kg, consumo_g=50):
    quant_g = quant_kg * 1000
    dias_comida = quant_g / consumo_g
    return dias_comida

def main():
    print('Calcule quanto tempo durará sua comida')
    quant_kg = float(input('Insira a quantidade do alimento em Quilogramas(Kg): '))
    dias = calcular_dias_comida(quant_kg)
    print(f'Sua comida durará por {dias:.2f} dias')

if __name__ == "__main__":
    main()

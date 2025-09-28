print("Calcule o novo preço de um produto")


#declarar

preço_atual = float(input("Insira o valor atual do produto:"))
venda_mensal = int(input("Insira a venda mensal do produto"))

def novo_preço():
    if venda_mensal < 500 and preço_atual < 30:
        reajuste = preço_atual * 1.1
    elif venda_mensal >= 500 and venda_mensal <1000 and preço_atual >= 30 and preço_atual <80:
        reajuste = preço_atual * 1.15
    elif venda_mensal >= 1000 and preço_atual >= 80:
        reajuste = preço_atual * 0.95
    elif preço_atual < 0 or venda_mensal <0:
        print("Valor inferior a 0, insira outro número")
        return None
    else:
        reajuste = preço_atual
    return reajuste

#inicio

reajuste = novo_preço()
if reajuste is not None:
    print(f"O novo valor do produto será de R${reajuste:.2f}")
print(f"O novo valor do produto será de R${reajuste:.2f}")

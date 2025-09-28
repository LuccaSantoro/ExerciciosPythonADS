# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

def obter_dados():
    """
    Solicita os dados necessários para o cálculo do salário ao usuário e
    realiza a validação de tipo e valor.
    """
    print("Cálculo do salário líquido com base nas horas trabalhadas, valor por hora, desconto e dependentes")
    while True:
        try:
            # 1. Recebe a entrada do usuário
            horas_trabalhadas = float(input("Insira a quantidade de horas trabalhadas: "))
            valor_por_hora = float(input("Insira o valor por hora trabalhada: "))
            percentual_desconto = float(input("Insira o percentual de desconto (em %): "))
            numero_dependentes = int(input("Insira o número de dependentes: "))
            
            # 2. Validação de valor (somente positivos)
            if horas_trabalhadas < 0 or valor_por_hora < 0 or percentual_desconto < 0 or numero_dependentes < 0:
                print("Entrada inválida. Por favor, insira valores positivos.")
                continue # Volta ao início do loop
            
            return horas_trabalhadas, valor_por_hora, percentual_desconto, numero_dependentes
        
        except ValueError:
            # 3. Tratativa de erro para entrada não-numérica
            print("Entrada inválida. Por favor, insira números válidos.")
            
def calcular_salario(horas_trabalhadas, valor_por_hora, percentual_desconto, numero_dependentes):
    """
    Calcula o salário líquido com base nos parâmetros fornecidos.
    """
    # Calcule o salário bruto (horas trabalhadas x valor por hora)
    salario_bruto = horas_trabalhadas * valor_por_hora
    
    # Calcule o desconto (Salário Bruto * Percentual)
    desconto = salario_bruto * (percentual_desconto / 100)
    
    # Calcule o salário líquido (Salário Bruto - Desconto + Acréscimo por Dependente)
    acrescimo_dependentes = numero_dependentes * 100
    salario_liquido = salario_bruto - desconto + acrescimo_dependentes
    
    return salario_liquido

def main():
    """
    Função principal que coordena a execução do programa.
    """
    # 1. Obtém as entradas do usuário com validação
    horas, valor, desconto_percentual, dependentes = obter_dados()
    
    # 2. Calcula o salário final
    salario_a_receber = calcular_salario(horas, valor, desconto_percentual, dependentes)
    
    # 3. Exibe o resultado
    print(f"\nO salário a receber é: R${salario_a_receber:.2f}")

if __name__ == "__main__":
    main()
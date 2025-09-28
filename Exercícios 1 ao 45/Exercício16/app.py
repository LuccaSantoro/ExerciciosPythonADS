#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

print("Cálculo do salário líquido com base nas horas trabalhadas, valor por hora, desconto e dependentes")

try:
    # 1. Recebe a entrada do usuário
    horas_trabalhadas = float(input("Insira a quantidade de horas trabalhadas: "))
    valor_por_hora = float(input("Insira o valor por hora trabalhada: "))
    percentual_desconto = float(input("Insira o percentual de desconto (em %): "))
    numero_dependentes = int(input("Insira o número de dependentes: "))
    
    # 2. Validação da entrada
    if horas_trabalhadas < 0 or valor_por_hora < 0 or percentual_desconto < 0 or numero_dependentes < 0:
        print("Entrada inválida. Por favor, insira valores positivos.")
        exit()
except ValueError:
    # 3. Tratativa de erro para entrada não-numérica
    print("Entrada inválida. Por favor, insira números válidos.")
    exit()
# --- Lógica de Cálculo do Salário (Substitui a função 'calcula_salario') ---

salario_bruto = horas_trabalhadas * valor_por_hora
desconto = salario_bruto * (percentual_desconto / 100)
salario_liquido = salario_bruto - desconto + (numero_dependentes * 100)

print(f"\nO salário a receber é: R${salario_liquido:.2f}")

# --- Fim da Lógica de Cálculo ---

#fim

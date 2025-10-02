#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

horas = float(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))
desconto_perc = float(input("Digite o percentual de desconto: "))
dependentes = int(input("Digite o numero de dependentes: "))

salario_bruto = horas * valor_hora
valor_desconto = salario_bruto * (desconto_perc / 100)
salario_liquido = salario_bruto - valor_desconto
bonus = dependentes * 100

salario_final = salario_liquido + bonus

print("O salario a receber e de:", salario_final)

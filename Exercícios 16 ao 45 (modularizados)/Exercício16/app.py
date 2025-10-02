# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

#Declarar
horas = 0
valor_hora = 0
p_desconto = 0
dependentes = 0
salario_final = 0

#procedimento
def Leitura():
  global horas, valor_hora, p_desconto, dependentes
  horas = float(input("Digite as horas trabalhadas: "))
  valor_hora = float(input("Digite o valor da hora: "))
  p_desconto = float(input("Digite o % de desconto: "))
  dependentes = int(input("Digite o n de dependentes: "))

#procedimento
def CalculaSalario():
  global horas, valor_hora, p_desconto, dependentes, salario_final
  salario_bruto = horas * valor_hora
  valor_desconto = salario_bruto * (p_desconto / 100)
  bonus = dependentes * 100
  salario_final = (salario_bruto - valor_desconto) + bonus

#Início
Leitura()
CalculaSalario()
print("O salario final a receber e:", salario_final)

#fim

# Calcule a nota média de um aluno em 4 bimestres

#Declarar
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))
media = 0

#Início
media = (n1 + n2 + n3 + n4) / 4

print("A media final e:", media)

if media >= 6:
  print("APROVADO")
elif media >= 3:
  print("EXAME")
else:
  print("RETIDO")

#fim

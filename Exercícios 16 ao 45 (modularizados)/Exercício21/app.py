# Calcule a nota média de um aluno em 4 bimestres

#Declarar
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0
media_final = 0.0

#procedimento
def Leitura():
  global nota1, nota2, nota3, nota4
  nota1 = float(input("Digite a nota do 1º bimestre: "))
  nota2 = float(input("Digite a nota do 2º bimestre: "))
  nota3 = float(input("Digite a nota do 3º bimestre: "))
  nota4 = float(input("Digite a nota do 4º bimestre: "))

#procedimento
def Calculo():
  global nota1, nota2, nota3, nota4, media_final
  media_final = (nota1 + nota2 + nota3 + nota4) / 4

#procedimento
def Resultado():
  global media_final
  print("A media final e:", media_final)
  if media_final >= 6.0:
    print("APROVADO")
  elif media_final >= 3.0:
    print("EXAME")
  else:
    print("RETIDO")

#Início
Leitura()
Calculo()
Resultado()

#fim

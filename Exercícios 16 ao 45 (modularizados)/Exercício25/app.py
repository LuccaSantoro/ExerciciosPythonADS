# Calcule a duração de um jogo

#Declarar
dia_i = 0
hora_i = 0
min_i = 0
dia_f = 0
hora_f = 0
min_f = 0
duracao_h = 0
duracao_m = 0

#procedimento
def Leitura():
  global dia_i, hora_i, min_i, dia_f, hora_f, min_f
  print("--- Início do Jogo ---")
  dia_i = int(input("Digite o dia inicial: "))
  hora_i = int(input("Digite a hora inicial: "))
  min_i = int(input("Digite o minuto inicial: "))
  print("--- Fim do Jogo ---")
  dia_f = int(input("Digite o dia final: "))
  hora_f = int(input("Digite a hora final: "))
  min_f = int(input("Digite o minuto final: "))

#procedimento
def CalculaDuracao():
  global dia_i, hora_i, min_i, dia_f, hora_f, min_f, duracao_h, duracao_m
  # Converte tudo para minutos para facilitar o cálculo
  total_minutos_inicio = (dia_i * 1440) + (hora_i * 60) + min_i
  total_minutos_fim = (dia_f * 1440) + (hora_f * 60) + min_f
  
  diferenca_minutos = total_minutos_fim - total_minutos_inicio
  
  # Converte a diferença de volta para horas e minutos
  duracao_h = diferenca_minutos // 60
  duracao_m = diferenca_minutos % 60

#Início
Leitura()
CalculaDuracao()
print("O jogo durou", duracao_h, "horas e", duracao_m, "minutos.")

#fim

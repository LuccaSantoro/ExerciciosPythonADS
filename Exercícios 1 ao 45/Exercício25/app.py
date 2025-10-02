# Calcule a duração de um jogo (menor que 24h)

#Declarar
hora_inicio = int(input("Digite a hora de inicio: "))
minuto_inicio = int(input("Digite o minuto de inicio: "))
hora_fim = int(input("Digite a hora de fim: "))
minuto_fim = int(input("Digite o minuto de fim: "))
duracao_horas = 0
duracao_minutos = 0

#Início
# Converte tudo para minutos
inicio_total_min = (hora_inicio * 60) + minuto_inicio
fim_total_min = (hora_fim * 60) + minuto_fim

# Verifica se o jogo acabou no mesmo dia ou no dia seguinte
if fim_total_min > inicio_total_min:
  duracao_total = fim_total_min - inicio_total_min
else:
  duracao_total = (24 * 60 - inicio_total_min) + fim_total_min

# Converte a duração de volta para horas e minutos
duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

print("O jogo durou", duracao_horas, "horas e", duracao_minutos, "minutos.")

#fim

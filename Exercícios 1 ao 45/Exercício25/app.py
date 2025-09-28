# Calcule a duração de um jogo (menor que 24h)

print("Calcule a duração de um jogo (permitindo diferença de dias)")

# --- Função de Entrada de Inteiros com Validação (Integrada) ---
def input_int_with_check(prompt, min_value, max_value, extra_check=None, error_msg=None):
    while True:
        try:
            value = int(input(prompt))
            
            # 1. Checa o intervalo básico (min_value e max_value)
            is_valid = min_value <= value <= max_value
            
            # 2. Checa a validação extra (se houver, ex: dia_fim >= dia_inicio)
            if is_valid and (extra_check is None or extra_check(value)):
                return value
            else:
                # Usa a mensagem de erro específica ou a padrão
                print(error_msg or f"Insira um valor válido ({min_value} a {max_value}).")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# --- Obter Tempo de Início ---
print("\n--- INÍCIO DO JOGO ---")
dia_inicio = input_int_with_check(
    "Insira o dia que o jogo começou (1 a 31): ", 1, 31
)
hora_inicio = input_int_with_check(
    "Insira a hora em que o jogo começou (0 a 23h): ", 0, 23
)
minuto_inicio = input_int_with_check(
    "Insira os minutos em que o jogo começou (0 a 59min): ", 0, 59
)

# --- Obter Tempo de Fim (com validação de dia) ---
print("\n--- FIM DO JOGO ---")
dia_fim = input_int_with_check(
    "Insira o dia que o jogo terminou (1 a 31): ", 1, 31,
    extra_check=lambda d: d >= dia_inicio,
    error_msg="O dia de término deve ser igual ou maior que o dia de início e um valor válido (1 a 31)."
)
hora_fim = input_int_with_check(
    "Insira a hora em que o jogo terminou (0 a 23h): ", 0, 23
)
minuto_fim = input_int_with_check(
    "Insira os minutos em que o jogo terminou (0 a 59min): ", 0, 59
)

# --- Lógica de Cálculo da Duração (Substitui a função 'calcular_duracao') ---

# Conversão total para minutos para simplificar o cálculo
# Tempo de Início (em minutos totais desde o início do mês/referência)
total_minutos_inicio = (dia_inicio * 24 * 60) + (hora_inicio * 60) + minuto_inicio

# Tempo de Fim (em minutos totais desde o início do mês/referência)
total_minutos_fim = (dia_fim * 24 * 60) + (hora_fim * 60) + minuto_fim

# Diferença total
diferenca_total_minutos = total_minutos_fim - total_minutos_inicio

# Calcula a duração em horas e minutos
duracao_hora = diferenca_total_minutos // 60
duracao_minuto = diferenca_total_minutos % 60

# --- Exibe o Resultado ---
print(f"\nO evento durou {duracao_hora} horas e {duracao_minuto} minutos.")
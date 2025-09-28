def get_int_input(prompt, min_value, max_value, extra_check=None, error_msg=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value and (extra_check is None or extra_check(value)):
                return value
            else:
                print(error_msg or f"Insira um valor válido ({min_value} a {max_value}).")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def get_start_time():
    dia_inicio = get_int_input(
        "Insira o dia que o jogo começou: ", 1, 31
    )
    hora_inicio = get_int_input(
        "Insira a hora em que o jogo começou (0 a 23h): ", 0, 23
    )
    minuto_inicio = get_int_input(
        "Insira os minutos em que o jogo começou (0 a 59min): ", 0, 59
    )
    return dia_inicio, hora_inicio, minuto_inicio

def get_end_time(dia_inicio):
    dia_fim = get_int_input(
        "Insira o dia que o jogo terminou: ", 1, 31,
        extra_check=lambda d: d >= dia_inicio,
        error_msg="O dia de término deve ser igual ou maior que o dia de início e um valor válido (1 a 31)."
    )
    hora_fim = get_int_input(
        "Insira a hora em que o jogo terminou (0 a 23h): ", 0, 23
    )
    minuto_fim = get_int_input(
        "Insira os minutos em que o jogo terminou (0 a 59min): ", 0, 59
    )
    return dia_fim, hora_fim, minuto_fim

def calcular_duracao(dia_inicio, hora_inicio, minuto_inicio, dia_fim, hora_fim, minuto_fim):
    if dia_fim == dia_inicio:
        duracao_hora = hora_fim - hora_inicio
        if minuto_fim >= minuto_inicio:
            duracao_minuto = minuto_fim - minuto_inicio
        else:
            duracao_minuto = (minuto_fim + 60) - minuto_inicio
            duracao_hora -= 1
    else:
        duracao_hora = (hora_fim + (24 * (dia_fim - dia_inicio))) - hora_inicio
        if minuto_fim >= minuto_inicio:
            duracao_minuto = minuto_fim - minuto_inicio
        else:
            duracao_minuto = (minuto_fim + 60) - minuto_inicio
            duracao_hora -= 1
    return duracao_hora, duracao_minuto

def main():
    print("Calcule a duração de um jogo (menor que 24h)")
    dia_inicio, hora_inicio, minuto_inicio = get_start_time()
    dia_fim, hora_fim, minuto_fim = get_end_time(dia_inicio)
    duracao_hora, duracao_minuto = calcular_duracao(
        dia_inicio, hora_inicio, minuto_inicio, dia_fim, hora_fim, minuto_fim
    )
    print(f"O evento durou {duracao_hora} horas e {duracao_minuto} minutos.")

if __name__ == "__main__":
    main()

#Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

print("Cálculo de Idade e Idade em 17 Anos")

try:
    # 1. Recebe a entrada do ano de nascimento
    ano_nascimento = int(input("Insira o ano de nascimento (ex: 1990): "))
    
    # 2. Recebe a entrada do ano atual
    ano_atual = int(input("Insira o ano atual (ex: 2024): "))
    
    if ano_nascimento > ano_atual:
        raise ValueError("O ano de nascimento não pode ser maior que o ano atual.")
    
except ValueError:
    # 3. Tratativa de erro para entrada não-numérica ou lógica inválida
    print("Entrada inválida. Por favor, insira anos válidos.")
    exit()

# --- Lógica de Cálculo da Idade (Substitui a função 'calcula_idade') ---

idade_atual = ano_atual - ano_nascimento
idade_17_anos = idade_atual + 17

print(f"\nSua idade atual é: {idade_atual} anos.")
print(f"Daqui a 17 anos, você terá: {idade_17_anos} anos.")

# --- Fim da Lógica de Cálculo ---

#fim
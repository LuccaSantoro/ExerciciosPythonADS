# Calcule a nota média de um aluno em 4 bimestres

print("Calcule a nota média de um aluno em 4 bimestres")

# Lista para armazenar as notas
notas = []
numero_de_bimestres = 4

try:
    # 1. Obter as notas dos 4 bimestres
    for i in range(1, numero_de_bimestres + 1):
        # A lógica de entrada de nota do 'obter_nota' é trazida para cá
        nota = float(input(f"Insira a nota do {i}º bimestre: "))
        notas.append(nota)
        
except ValueError:
    print("Entrada inválida. Por favor, insira valores numéricos para as notas.")
    exit()

# 2. Calcular a média (Substitui a função 'calcular_media')
if notas: # Garante que a lista não está vazia antes de dividir
    media = sum(notas) / len(notas)
else:
    # Caso não tenha notas (o que não deve acontecer se o try/except passar)
    media = 0.0

# 3. Mostrar o resultado (Substitui a função 'mostrar_resultado')
print(f"A média do aluno é {media:.2f}")

if media >= 6:
    print("APROVADO")
elif media < 3:
    print("RETIDO")
else:
    print("EXAME")
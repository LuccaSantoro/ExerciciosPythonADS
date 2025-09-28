# Calcule o novo preço de um produto

print("Calcule o novo preço de um produto")

# --- Recebe as entradas ---
try:
    preço_atual = float(input("Insira o valor atual do produto: "))
    venda_mensal = int(input("Insira a venda mensal do produto: "))
except ValueError:
    print("Entrada inválida. Por favor, insira números válidos.")
    # Define um valor para 'reajuste' que não será impresso no final, se houver erro
    reajuste = None 
    
    
# --- Lógica de Reajuste (Substitui a função 'novo_preço') ---

if 'reajuste' is not None: # Se não houve erro na entrada (mantendo o fluxo)
    
    # 1. Verifica valores negativos (tratativa de erro conforme o código original)
    if preço_atual < 0 or venda_mensal < 0:
        print("Valor inferior a 0, insira outro número")
        reajuste = None # Indica que o cálculo não deve prosseguir
        
    # 2. Regra 1: Venda baixa E Preço baixo
    elif venda_mensal < 500 and preço_atual < 30:
        # Reajuste de +10%
        reajuste = preço_atual * 1.1
        
    # 3. Regra 2: Venda média E Preço médio
    elif (venda_mensal >= 500 and venda_mensal < 1000) and (preço_atual >= 30 and preço_atual < 80):
        # Reajuste de +15%
        reajuste = preço_atual * 1.15
        
    # 4. Regra 3: Venda alta E Preço alto
    elif venda_mensal >= 1000 and preço_atual >= 80:
        # Reajuste de -5%
        reajuste = preço_atual * 0.95
        
    # 5. Regra Padrão: Nenhuma das regras anteriores se aplica
    else:
        # Sem reajuste
        reajuste = preço_atual

# --- Exibição do Resultado ---
if reajuste is not None:
    # O print foi replicado duas vezes no código original. Mantendo a replicação para fidelidade.
    print(f"O novo valor do produto será de R${reajuste:.2f}")
    print(f"O novo valor do produto será de R${reajuste:.2f}")
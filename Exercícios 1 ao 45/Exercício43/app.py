# Cálculo do tempo necessário para Ana ser mais alta que Maria

# Alturas e crescimentos anuais (em metros)
altura_ana = 1.10
altura_maria = 1.50
crescimento_ana = 0.03
crescimento_maria = 0.02
anos = 0

print("Cálculo do tempo necessário para Ana ser mais alta que Maria")

# Loop para simular o crescimento ano a ano
while altura_ana <= altura_maria:
    # Simula o crescimento de cada uma
    altura_ana += crescimento_ana
    altura_maria += crescimento_maria
    # Conta um ano
    anos += 1

# Exibe o resultado final
print(f"Serão necessários {anos} anos para que Ana seja mais alta que Maria.")
print(f"Altura final de Ana: {altura_ana:.2f} m")
print(f"Altura final de Maria: {altura_maria:.2f} m")
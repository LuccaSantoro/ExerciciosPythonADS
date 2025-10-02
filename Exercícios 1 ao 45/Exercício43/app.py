# Cálculo do tempo necessário para Ana ser mais alta que Maria

#Declarar
alt_ana = 1.10
alt_maria = 1.50
cresc_ana = 0.03
cresc_maria = 0.02
anos = 0

#Início
while alt_ana <= alt_maria:
  alt_ana = alt_ana + cresc_ana
  alt_maria = alt_maria + cresc_maria
  anos = anos + 1

print("Serao necessarios", anos, "anos.")
print("Altura final de Ana:", alt_ana)
print("Altura final de Maria:", alt_maria)

#fim

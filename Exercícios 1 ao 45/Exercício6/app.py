#Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

x = input("Digite o valor de x: ")
y = input("Digite o valor de y: ")

print("Antes a troca era: x =", x, "e y =", y)

# Variável auxiliar para guardar o valor de x
aux = x
x = y
y = aux

print("Depois da troca ficou: x =", x, "e y =", y)

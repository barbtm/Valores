valores = []

for x in range (5):
    produto = str(input("Código: "))
    valor = float(input("Preço: "))
    preco_final = [produto, valor]
    valores.append(preco_final)

print("quantidade de produtos", len(valores))

for n in valores:
    produto = n [0]
    valores = n[1]
    print ("O valor final", produto, "seria de", valores)

valores = []

contador = 1

while contador <= 5:
    produto = str(input("Código: "))
    valor = float(input("Preço: "))
    preco_final = [produto, valor]
    valores.append(preco_final)

    contador = contador + 1
    print("quantidade de produtos", len(valores))
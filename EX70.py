print("--" * 15)
print("{:-^30}".format(" BARATÃO "))
print("--" * 15)

total = totmil = menor = cont = 0
barato = " "

while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$ "))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break     
    
print("{:-^30}".format(" FIM DAS COMPRAS "))
print(f"O total das suas compras foi R${total:.2f}")
print(f"Temos {totmil} produtos valendo mais de R$1000.00")
print(f"O produto mais barato foi {barato} cuta R${menor:.2f}")   
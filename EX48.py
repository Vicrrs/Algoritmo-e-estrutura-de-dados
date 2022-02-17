soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 #soma+=1
        soma = soma + c #cont+=1
print(f"A soma de todos os {cont} valores é {soma}")


temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input("Digite seu Nome: ")))
    temp.append(int(input("Digite seu Peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:]) #vai adicionando os dados aos poucos na lista
    temp.clear() #vai deixando os dados em listas separadas


    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break
print("-=" * 30)

print(f"Os dados foram {princ}")

print(f"Ao todo você cadastrou {len(princ)} pessoas")

print(f"O maior peso foi de {mai}Kg. Peso de ", end="")
for p in princ:
    if p[1] == mai:
        print(f"[{p[0]}]", end="")
print()
print(f"O menor preço foi de {men}Kg")
for p in princ:
    if p[1] == men:
        print(f"[{p[0]}] ", end="")
print()
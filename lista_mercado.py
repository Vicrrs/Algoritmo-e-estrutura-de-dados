#Criação e impressão da lista de compras
compras = []

while True:
    produto = str(input("Produto: "))
    quantidade = int(input("Quantidade: "))
    preço = float(input("Preço: "))
    print("-=-" * 12)
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break   
    print("-=-" * 12)
    compras.append([produto, quantidade, preço])
    
soma = 0.0
for e in compras:
    print(f"{e[0]}  ⇨ {e[1]} x {e[2]} = {e[1]*e[2]} ")
    
    soma += e[1] * e[2]
print(f"Total das compras: {soma}")
def area(lg, cm):
    ar = lg * cm
    print(f"A área de um terreno {lg} x {cm} é de {ar}m²!")



print("    CONTROLE DE TERRENOS")
print("-"*30)
lg = float(input("LARGURA (m): "))
cm = float(input("COMPRIMENTO (m): "))
area(lg, cm)
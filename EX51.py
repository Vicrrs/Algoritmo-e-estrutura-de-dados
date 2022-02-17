print("===" * 10)
print("TERMOS DE UMA P.A")
print("===" * 10)
termos = int(input("Quantidade de termos: "))
prim = int(input("Primeiro Termo: "))
raz = int(input("Razão: "))
for c in range(prim, termos+1, raz):
    print(f"{c}", end=" ➙ ")
print("ACABOU")
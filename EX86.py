matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#for para colocar os valores na matriz
for l in range(0,3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

print("-=" * 30)
#for para mostrar a estrutura na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
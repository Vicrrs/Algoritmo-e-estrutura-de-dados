num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f"Digite o {c}° valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print("-=" * 30)
print(f"Todos os valores: {num}")
num[0].sort() #ordena a lista separadamente em ordem crescente#
num[1].sort()
print(f"Os valores pares digitados foram: {num[0]}")
print(f"Os valores impares impares digitados foram: {num[1]}")
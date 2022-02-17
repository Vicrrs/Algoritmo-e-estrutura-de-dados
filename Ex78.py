listanum = []

for c in range(0, 5):
    listanum.append(int(input(f"Digite um valor para POSIÇÃO {c}: ")))

print("=-" * 30)

print(f"Você digitou os valores {listanum}!")
print(f"O maior valor digitado foi {max(listanum)}!")
print(f"O menor valor digitado foi {min(listanum)}!")

print("=-" * 30)
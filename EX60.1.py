n = int(input("Digite um número para saber seu fatorial: "))
c = n #c=contador
f = 1

print(f"Calculando {n}! = ", end="")

while c > 0:
    print(f"{c}", end=" ")
    print(" x " if c > 1 else " = ", end="")
    f = f * c
    c = c - 1

print(f"{f}")
n = quant = s = 0
while True:
    n = int(input("Digite um valor [999 para parar]: "))
    if n == 999:
        break
    s += n
    quant += 1
print(f"A soma entre {quant} valores é {s}.")
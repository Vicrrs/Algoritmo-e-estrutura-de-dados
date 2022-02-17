n = s = 0
while True:
    n = int(input("Digite um número [999 para encerrar]: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")    
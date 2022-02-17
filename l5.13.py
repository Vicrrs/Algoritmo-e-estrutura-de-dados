s = cont = 0
v = int(input("Digite um número a somar ou 0 para sair: "))
while True:
    cont += 1
    v = int(input("Digite um número a somar ou 0 para sair: "))
    if v == 0:
        break
    s += v
print(f"Você digitou {cont} números e a soma deu {s}")
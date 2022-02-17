from time import sleep

def contador(i, f, p):
    print("-" * 30)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    print("-" * 30)
    sleep(2.5)
    if i < f:
        cont = 1
        while cont <= f:
            print(f"{cont}", end=' ')
            sleep(0.5)
            cont += p
        print("Fim!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=' ')
            sleep(0.5)
            cont -= p
        print("Fim!")

print("-~" * 30)
print("Agora sua vez de personalizar a contagem!")

ini = int(input("Inicío: "))
fim = int(input("Fim:    "))
pas = abs(int(input("Passo:  "))) #para levar em conta valores negativos

contador(ini, fim, pas)
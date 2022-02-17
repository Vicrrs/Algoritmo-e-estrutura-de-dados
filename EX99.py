from time import sleep

def maior(* num):
    cont = maior = 0
    print("-=" * 15)
    print("Analisando os valores passados")
    for valor in num:
        print(f"{valor }", end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")

maior(2, 5, 7, 8)
maior(5, 6, 1, 10, 9)
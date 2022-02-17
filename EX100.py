from random import randint
from time import sleep


print("-=" *15)


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n}", end=' ')
        sleep(0.5)
    print("Fim!")


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares {lista}, temos que a soma é igual a {soma}.")


numeros = list()
sorteia(numeros)
somapar(numeros)
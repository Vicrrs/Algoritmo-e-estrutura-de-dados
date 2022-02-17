def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


    '''->Calcula o aumento de um determinado preço, retornando o reultado
    com ou sem formatação.
    :param preço: o preço que quer rajustar
    :param taxa: qual é a porcentagem do aumento
    :param formato: quer saida formatada ou não?
    :return: o valor reajustado, com ou sem formato'''


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda = "R$"):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10, taxar=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preço)} ")
    print(f"Dobro do preço: \t{dobro(preço, True)}")
    print(f"Metade do preço: \t{metade(preço, True)}")
    print(f"Com {taxaa}% de aumento: {aumentar(preço, taxaa, True)}")
    print(f"Com {taxar}% de redução: \t{diminuir(preço, taxar, True)}")
    print("-" * 30)
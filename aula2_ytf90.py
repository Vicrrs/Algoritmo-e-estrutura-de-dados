acertos = int(input("Informe o seu número de acertos: "))

if acertos <= 10:
    print("Você não ganhou nada!")
elif acertos == 11:
    print("Você ganhou R$5,00!")
elif acertos == 12:
    print("Você ganhou R$10,00")
elif acertos == 13:
    print("Você ganhou R$20,00")
elif acertos == 14:
    print("Você ganhou R$2.000,00")
elif acertos == 15:
    print("Parabéns, você ganhou R$1.000.000,00")
else:
    print("Erro de entrada, confira se os acertos estão entre 5 e 15!")
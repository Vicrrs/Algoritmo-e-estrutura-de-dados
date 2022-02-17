repetir = " "
while True:
    idade = int(input("Digite sua idade: "))

    if idade >= 18 and idade < 70:
        print(f"Com {idade} anos, seu voto ainda é obrigatório!")
    elif idade >= 16:
        print(f"Com {idade} anos, seu voto é facultativo!")
    else:
        print(f"Com {idade} anos, você NÃO pode votar ainda!")
    
    repetir = str(input("Deseja repetir? [S/N]: ")).strip().upper()[0]
    if repetir == "N":
        break 
    else: 
        repetir = True

print("Obrigado, volte sempre!")
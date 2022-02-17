idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 70:
    print(f"Com {idade} anos de indade, seu voto é obrigatório!")
elif idade >= 16:
    print(f"Com {idade} anos de idade, seu voto é facultativo!")
else:
    print(f"Com {idade} anos de idade, você ainda não pode votar!")
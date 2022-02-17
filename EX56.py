somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for p in range(1, 5):
    print(f"----- {p}ª pessoa -----")
    nome = str(input(("Nome: "))).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade = somaidade + idade #+=idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
médiaidade = somaidade /4
print(f"A média de idade do grupo é de {médiaidade} anos")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
print(f"Ao todo se tem {totmulher20} mulheres com menos de 20 anos.")

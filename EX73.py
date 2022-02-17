Times = ("atlético Mineiro", "palmeiras", "fortaleza", "flamengo", "bragantino", "internacional", "corinthians", "fluminense", "atlético Goianiense", "américa-mg", "cuiabá", "athletico-pr","são paulo", "ceará", "bahia", "juventude", "santos", "sport recife", "grêmico", "chapecoense")
print("-=-" * 10)

print(f"Lista de times do brasileirão: {Times}")

print("-=-" * 10)

print(f"Os 5 primeiro são: {Times[:5]}")

print("-=-" * 10)

print(f"Os 4 ultimos são: {Times[-4:]}")

print("-=-" * 10)

print(f"Times em ordem Alfabética: {sorted(Times)}")

print("-=-" * 10)

while True:
    perg = str(input("A posição do time que vc deseja saber: ")).strip().lower()

    v = Times.index(perg)

    print(f"O {perg} está na {v + 1}ª posição! ")
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break   
print("Até a próxima!")
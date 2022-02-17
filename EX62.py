from time import sleep
print("-=" * 10)
print("GERADOR DE P.A.")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da P.A.: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} ➙ ", end="")
        termo += razão
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termo você quer a mais? "))
sleep(2)    
print(f"Progressão finalizada com {total} termos mostrados!")

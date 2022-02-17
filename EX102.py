def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
        f *= c
    return f


def mostralinha():
  print("-=" * 15)



repetir = " "
while True:
    num = int(input("Qual número você deseja saber o fatorial? "))
    
    mostralinha()
    
    cal = str(input(f"Deseja ver o cálculo da fatorial de {num}? [S/N]: ")).strip().upper()[0]
    if cal == "N":
        print(fatorial(num))
    else:
        print(fatorial(num, True))
    
    mostralinha()
    
    repetir = str(input("Deseja repetir para algum outro número? [S/N]: ")).strip().upper()[0]
    if repetir == "N":
        break 
    else: 
        repetir = True
        
    mostralinha()

print("Até mais")
print("--" * 15)
print("CADASTRE UMA PESSOA")
print("--" * 15)

tot18 = totH = totM20 = 0

while True:
    i = int(input("Idade da pessoa: "))
    
    s = " "
    
    while s not in "MF":
        s = str(input("Sexo [M/F]:")).strip().upper()[0]
    
    if i >= 18:
        tot18 += 1
    
    if s == "M":
        totH += 1
    
    if s == "F":
        totM20 += 1
    
    rsp = " "
    while rsp not in "SN":
        rsp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0] 
        
    if rsp == "N":
        break
    
print(f"Total de pessoas com mais de 18 anos é {tot18}")
print(f"O total de homens é {totH}")
print(f"O total de mulheres com menos de 20 anos é {totM20}")
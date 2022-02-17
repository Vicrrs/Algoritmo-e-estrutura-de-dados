#Escopo de importação

def voto(ano):
    from datetime import date 
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA!"
    elif 16 <= idade < 18:
        return f"Com {idade} anos: VOTO OPCIONAL!"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO!"


repetir = " "
while True:
    nasc = (int(input("Em que ano você nasceu? ")))
    
    print(voto(nasc))
    
    repetir = str(input("Deseja repetir? [S/N]: ")).strip().upper()[0]
    if repetir == "N":
        break 
    else: 
        repetir = True
    
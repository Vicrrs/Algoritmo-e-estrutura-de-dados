num = 0
def par_impar():
    if (num % 2) == 0:
        return "Número par"
    return "Número impar"   

num = int(input("Informe o número que deseja saber se é par ou ímpar: "))
print(par_impar())

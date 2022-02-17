resp = "S"
soma = quant = média = maior = menor = 0

while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar [S/N]  ")).upper().strip()[0]
média = soma / quant
print(f"Você digitou {quant} números e a méida foi {média}")
print("O maior valor foi {maior} e o menor valor foi {menor}")
#Fazendo_fatorial_usando_for
n1 = int(input('Digite um número inteiro qualquer: '))
ac= 1
for n1 in range(n1, 0, -1):
    ac *= n1
print(f'O produto de todos os números é {ac}')
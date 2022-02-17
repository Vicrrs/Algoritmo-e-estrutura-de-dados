aluno = {}
aluno["nome"] = str(input("Nome: "))
aluno["média"] = float(input(f"Média de {aluno['nome']}: "))

if aluno['média'] >= 7:
    aluno['situação'] = "Aporvado"
elif 5 <= aluno["média"] < 7:
    aluno['situação'] = "Recuperação"
else:
    aluno['situação'] = "Reprovado"

for k, v in aluno.items():
    print(f" - {k} é igual a {v}")
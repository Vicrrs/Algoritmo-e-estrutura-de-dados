print("{:=^40}".format(" LOJAS DO PAULO "))
preço = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opcao = int(input("Qual é sua opção? "))

if opcao == 1:
    print("Você ganha um desconto de 10% assim o valor a ser pago é R${}" .format(preço - (preço * 10/100)))
elif opcao == 2:
    print("Você ganha um desconto de 5% assim o valor a ser pago é R${}" .format(preço - (preço * 0.05)))
elif opcao == 3:
    print(f"O preço a ser pago é o mesmo preço do produto, de R${preço}")
elif opcao == 4:
    var = int(input("Quantas parcelas? "))
    juros = preço / var * 1.2
    print(f"Sua compra será parcelada em {var}x de R${juros} COM JUROS!")
    print(f"Sua compra de R${preço} vai custar R${preço + juros}")
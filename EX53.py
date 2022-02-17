frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()#vai_criar_uma_divisão_nos_espaços.Gera_lista_em_cada_palavra
junto = "".join(palavras)
inverso = frase[::-1]
print(f"Você digitou a palavra {frase.replace(' ' ,'')} e seu palíndromo é {inverso.replace(' ' ,'')}")
if frase.replace(' ' ,'') == inverso.replace(' ' ,''):
    print("É um palíndromo!!")
else:
    print("Não é um palíndromo!!")
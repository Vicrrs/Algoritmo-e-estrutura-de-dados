import fitz

with fitz.open("xxx.pdf") as pdf:
    texto = ""

    for pagina in pdf:
        texto += pagina.getText()

print(texto)
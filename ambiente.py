import pydf

pdf = pydf.generate_pdf('<h1>OLAÁ MUNDOOOOO</h1><p>testando o doc</p>')

with open('meuarquivo.pdf', 'wb') as arquivo:
    arquivo.write(pdf)
    
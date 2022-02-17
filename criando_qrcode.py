import qrcode
#em url voce coloca o link que deseja direcionar com o qrcode
url = "https://instagram.com/prof.victorroza?utm_medium=copy_link"
#vai converter os dados
imagem = qrcode.make(url)
#salva o qrcode em forma de png
imagem.save("qrcode(insta).png")
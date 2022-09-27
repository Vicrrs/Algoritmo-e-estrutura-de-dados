import smtplib

de = ''
senha = ''
para = ''

msg = """
Ola, mensagem de teste
"""




conexao = smtplib.SMTP('smtp.gmail.com', 587)
#Sabe se tem conexão com o servidor
conexao.ehlo()
#criptografando 
conexao.starttls()
#fazendo login
conexao.login(de, senha)
#enviando o e-mail
conexao.sendmail(de, para, msg)
#finalizando a conexao
conexao.quit()

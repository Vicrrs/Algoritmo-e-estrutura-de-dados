import smtplib

de = 'pythonhouse22@gmail.com'
senha = '@22PytestinHouse!'
para = 'roza.stephen22@gmail.com'

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

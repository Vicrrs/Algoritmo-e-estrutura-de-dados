import smtplib
import ssl
import email.message

setor = "contabilidade"
nome = "Equipe do financeiro"

msg = email.message.Message()
msg['Subject'] = f"Planilha do Financeiro departamento: {setor}"

body = f"""
<p>Olá, {nome}</p>
<p>Segue a planilha com os resultados desse mês.</p>
<p>Atenciosamente,</p>
<p>Gerente ADM</p>
"""


msg['From'] = 'pythonhouse22@gmail.com'
password = '@22PytestinHouse!'
msg['To'] = ('roza.stephen22@gmail.com')
msg.add_header('Content-Tyoe', 'text/html')
msg.set_payload(body)



context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:

    conexao.ehlo()

    conexao.starttls(context=context)

    conexao.login(msg['From'], password)

    conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    
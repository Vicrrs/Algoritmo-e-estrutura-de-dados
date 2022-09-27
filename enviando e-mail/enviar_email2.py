import smtplib
import ssl
import email.message

setor = "contabilidade"

msg = email.message.Message()
msg['Subject'] = f"Planilha do Financeiro departamento: {setor}"

body = """
Ola, mensagem de teste iai
"""


msg['From'] = ''
password = ''
msg['To'] = ('')
msg.add_header('Content-Tyoe', 'text/html')
msg.set_payload(body)



context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:

    conexao.ehlo()

    conexao.starttls(context=context)

    conexao.login(msg['From'], password)

    conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    

import smtplib
from email.mime.text import MIMEText

def enviar_correo_inseguro(destinatario, asunto, mensaje):
    smtp_usuario = "pruebas@inseguro.com"
    smtp_contrasena = "12345678" 
    
    msg = MIMEText(mensaje)
    msg['Subject'] = asunto
    msg['From'] = smtp_usuario
    msg['To'] = destinatario

    server = smtplib.SMTP("127.0.0.1", 1025)
    
    server.login(smtp_usuario, smtp_contrasena)
    server.sendmail(smtp_usuario, [destinatario], msg.as_string())
    server.quit()
import os
import smtplib
from email.message import EmailMessage

user = os.getenv('USER_GMAIL')
clave = os.getenv('PASSWORD_GMAIL')

def send_notifying_mail(user, passw):
  msg = EmailMessage()
  msg['From']=user
  msg['To']=user
  msg['Subject']= "Probando mandar mails!"
  msg.set_content('Este es un mail enviado con Python en la clase! =D')
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(user, passw)
  server.send_message(msg)
  server.quit();

send_notifying_mail(user, clave)
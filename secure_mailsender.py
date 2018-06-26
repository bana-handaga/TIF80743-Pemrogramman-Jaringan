
import getpass
import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 # ssl port 465, tls port 587

# sender : alamat email pengirim
# recipient : alamat email penerima
def send_email(sender, recipient):
	
	# Menyusun data email
	msg = MIMEMultipart()
	msg['To'] = recipient
	msg['From'] = sender
	subject = input ('Masukan topik/subject email:')
	msg['Subject'] = subject

	message = input('Masukan isi email, tekan ENTER jika sudah selesai:')
	part = MIMEText('text',"plain")
	part.set_payload(message)
	
	msg.attach(part)

	# Mengirim email
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.set_debuglevel(1)	
	session.ehlo()
	session.starttls()
	session.ehlo()
	password = getpass.getpass(prompt='Password: ')
	# login to server
	session.login(sender,password)
	# send mail
	session.sendmail(sender, recipient, msg.as_string())

	print("Email anda dikirim ke {0}.".format(recipient))
	session.quit()

if __name__ == '__main__':
	sender = input("Email pengirim: ")
	recipient = input("Email target: ")
	send_email(sender, recipient)



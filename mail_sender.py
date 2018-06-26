import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'aspmx.l.google.com'
SMTP_PORT = 25

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
	session.ehlo()
	session.set_debuglevel(1)
	session.sendmail(sender, recipient, msg.as_string())

	print("Email anda dikirim ke {0}.".format(recipient))
	session.quit()

if __name__ == '__main__':
	sender = input("Email pengirim: ")
	recipient = input("Email target: ")
	send_email(sender, recipient)



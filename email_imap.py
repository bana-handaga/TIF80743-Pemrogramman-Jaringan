import getpass  # library untuk input password supaya tidak tampil
import imaplib # library unuk membaca email dari server POP3
import pprint

# Setting server target
GOOGLE_IMAP_SERVER = 'imap.googlemail.com'
IMAP_SERVER_PORT = '993'

def check_email(username, password):
	mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER,IMAP_SERVER_PORT)
	mailbox.login(username,password)
	mailbox.select('inbox')

	tmp, data = mailbox.search(None,'ALL')
	for num in data[0].split():
		tmp, data = mailbox.fetch(num, '(RFC822)')
		print ('Message: {0}\n'.format(num))
		pprint.pprint(data[0][1])
		break
	mailbox.close()
	mailbox.logout()


if __name__ == '__main__':
	username = input("Enter your email user ID: ")
	password = getpass.getpass(prompt="Password: ")
	# membuaka email 
	check_email(username, password)


	



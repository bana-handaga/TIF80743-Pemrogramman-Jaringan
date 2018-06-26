import getpass  # library untuk input password supaya tidak tampil
import poplib # library unuk membaca email dari server POP3

# Setting server target
GOOGLE_POP3_SERVER = 'pop.googlemail.com'
POP3_SERVER_PORT = '995'

def fetch_email(username, password):
	mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER,POP3_SERVER_PORT)
	mailbox.user(username)
	mailbox.pass_(password)

	# mengidentifikasi jumlah email dalam mailbox
	num_messages = len( mailbox.list()[1] )
	# tampilkan jumlah email
	print("Total emails: {0}".format(num_messages))
	print("getting last message")  #menampilkan email terakhir 
	for msg in mailbox.retr(num_messages)[1]:
		print(msg)
	mailbox.quit()

if __name__ == '__main__':
	username = input("Enter your email user ID: ")
	password = getpass.getpass(prompt="Password: ")
	# membuaka email 
	fetch_email(username, password)


	







import socket
import ssl

import base64
from conn import cred as c

"""
this is an implementation of socket client

SMTP using start tls

step 1: establish a tcp connection

step 2 : send EHLO msg\r\n

step 3: establish start TLS connection

"""
CRLF = b'\r\n'


class Inlook():
    
	def __init__(self,host,port, debug=0):
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server = host
		self.port = port
		self.user = ""
		self.debug = debug
		self.context = ssl.create_default_context()
		if self.connect():
			self.smtp(self.sock)
	
	def debuging(self,val):
		self.debug = int(val)

	def connect(self):

		self.sock.connect((self.server,self.port))

		data = self.sock.recv(1024).decode()
		if self.debug>0 : print(data)
		if data[:3]=="220":
			return True
		else:
			return False
	
	def sender(self, cmd):
		
		if "byte" in str(type(cmd)):
			self.sock.sendall(cmd+CRLF)
			if self.debug>0: print(f"client: ",cmd+CRLF)
		if "str" in str(type(cmd)):
			self.sock.sendall(f"{cmd}\r\n".encode())
			if self.debug>0: print(f"client: ",f"{cmd}\r\n".encode())
		
		data = self.sock.recv(1024).decode()
		if self.debug>0: print("server: ",data)
		return data
	
	
	def smtp(self, sock):
		
		"""
		after connecting to server
		c->s EHLO  s->c 250
		c->s STARTTLS  s->c 
		"""
		data = self.sender("EHLO world")

		if data[:3]!="250":
			print("issue")

		data = self.sender("STARTTLS")

		self.sock = self.context.wrap_socket(self.sock,server_hostname=self.server)

		data= self.sender("EHLO tls")

		
	
	def login(self, user, passw):

		self.user = user
		user_64 = base64.b64encode(f"{user}".encode())
		passw_64 = base64.b64encode(f"{passw}".encode())
		mix = base64.b64encode(f"\0{user}\0{passw}".encode())
		
		data = self.sender(f"AUTH LOGIN")

		# val = "AUTH PLAIN ".encode()+user_64+"\r\n".encode()+passw_64+"\r\n".encode()

		

		while data[:3]=="334":

			if "password" in base64.b64decode(data[4:].encode()).decode().lower():
				data = self.sender(passw_64)
			elif "username" in base64.b64decode(data[4:].encode()).decode().lower():
				data = self.sender(user_64)
			else:
				print(f"something wrong {data}")

		if data[:3]=="235" and ("success" in data):
			pass

			
	
	def send_mail(self,mail,to_mail,msg):
		
		### MAIL FROM:<user@domain.com>\r\n

		data = self.sender(f"MAIL FROM:<{mail}>")
		data = self.sender(f"RCPT TO:<{to_mail}>")
		data = self.sender(f"DATA")
		data = self.sender(f"{msg}\r\n.")
		if (data.split()[0]=="250"):
			print(f"email sucessfully sent to {to_mail}")
			

			


		






		
		



		

## smtp server outlook
server_gmail = c().smtp_gmail
port_ssl = c().port_ssl
server_outlook = c().smtp_outlook
port_tls = c().port_tls
#smtp authentication details outlook
mail_outlook = c().email_outlook
password_outlook = c().passw_outlook
mail_to = c().email_gmail
msgi = """SUBJECT: my code\n

	This is the body of the email

    more ohohoiho body
"""



account1 = Inlook(server_outlook,port_tls)

account1.login(mail_outlook,password_outlook)
account1.send_mail(mail_outlook,mail_to,msgi)



# account2 = Inlook("smtp.aol.com",port_tls)
# account3 = Inlook(server_gmail,port_tls)


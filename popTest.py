
"""
Incoming Mail (POP) Server 	

pop.gmail.com

Requires SSL: Yes

Port: 995
Outgoing Mail (SMTP) Server 	

smtp.gmail.com

Requires SSL: Yes

Requires TLS: Yes (if available)

Requires Authentication: Yes

Port for TLS/STARTTLS: 587

If you use Gmail with your work or school account, check with your administrator for the correct SMTP configuration.
Server timeouts 	Greater than 1 minute (5 is recommended)
Full Name or Display Name :	Your name
Account Name, User Name, or Email address :	Your email address
Password :	Your Gmail password

"""

import  poplib
import socket
import ssl
from conn import cred as c 

mail_outlook = c().email_outlook
pass_outlook = c().passw_outlook
# Connect to the mail box 

mail_gmail = c().email_gmail
pass_gmail = c().passw_gmail

server_gmail = c().pop_gmail

server_outlook = c().pop_outlook
port_pop = 995
# Mailbox = poplib.POP3_SSL(server_outlook, '995') 
# Mailbox.user(mail_outlook) 
# Mailbox.pass_(pass_outlook) 
# NumofMessages = len(Mailbox.list()[1])
# print(NumofMessages)
# # for i in range(NumofMessages):
# #     for msg in Mailbox.retr(i+1)[1]:
# #         print()
# for msg in Mailbox.retr(2+1)[1]:
#     print(msg)
# Mailbox.quit()

class Poper():

    def __init__(self,host,mail,passw, port = 995):

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.context = ssl.create_default_context()
        self.sock = self.context.wrap_socket(self.sock,server_hostname=host) # initialises TLS connection from begining
        self.user = mail
        self.passw = passw
        self.server = host
        self.port = port
        self.debug = 0
        self.mailboxSize = 0
        self.connect(self.sock)
    
    def sender(self,cmd,siz=1024):

        self.sock.sendall(f"{cmd}\r\n".encode())
        data = self.sock.recv(siz).decode()
        if self.debug >0: print(data)
        return data
    
    def connect(self,sock):
        sock.connect((self.server,self.port))
        sock.recv(1024)
        # print(data)

        self.sender(f"USER {self.user}")      
        """
           No point of check if the username is worng, becuase it will be okay most
           most of the time, because it accepts any username but returns err if 
           password against that username is not matched
        """
        
        data =self.sender(f"PASS {self.passw}")
        
        if "OK" not in data[:4]:
            print(f"check the password against username: {self.user}")
        else: 
            print("login success, now retrive your emails")
            self.stat()
            
            self.retr(1)
            
            
    def stat(self):
        data = self.sender(f"STAT")
        lis = data.split()
        print(lis)
        if "OK"in lis[0]:
            self.mailboxSize = int(lis[1])
        return 
    
    def retr(self,msg):
        if self.debug>0 : print(self.mailboxSize)
        if int(msg)> int(self.mailboxSize):
            print("mail doesn't exist check again")
        else:
            
            te = self.sender(f"LIST {msg}")
            print(te.split())
            data = self.sender(f"RETR {msg}")
            
            nw = b""
            
            while b"\r\n.\r\n" not in nw:
                
                nw += self.sock.recv(1024)
                
                
            
            print(nw.decode())
            self.parse(nw)

    def parse(self, bmail): #yet to implement parser function
        pass

# def sender(cmd,sock):
#     sock.sendall(f"{cmd}\r\n".encode())
    
#     data = sock.recv(2048).decode()
#     print(data) 
#     return data

# context = ssl.create_default_context()
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock = ssl.wrap_socket(sock)
# sock.connect((pop_outlook,port_pop))
# data = sock.recv(1024)
# print(data)
# sender(F"USER {mail_outlook}",sock=sock)

# sender(f"PASS {pass_outlook}",sock=sock)

# sender(f"STAT",sock=sock)

# # sender(f"LIST",sock=sock)

# sender(f"RETR 2 ",sock=sock)
# sender(f"RETR 1",sock=sock)

account = Poper(server_outlook,mail_outlook,pass_outlook)

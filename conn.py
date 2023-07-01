
"""
Trying to implement SMTP ( simple mail transfer protocol) to send emails from your existing email service

Incoming Mail (IMAP) Server 	

imap.gmail.com  Requires SSL: Yes
Port: 993

Outgoing Mail (SMTP) Server 	

server: smtp.gmail.com Requires SSL: Yes
Port for SSL: 465
Port for TLS/STARTTLS: 587

Requires TLS: Yes (if available) Requires Authentication: Yes

Full Name or Display Name :Your name
Account Name, User name, or Email address :	Your full email address
Password :	Your Gmail password



"""
#cred
class cred():
    def __init__(self) -> None:
        
        self.email_gmail = "keerappareek@gmail.com"
        self.passw_gmail = "samaykakhel"

        self.email_outlook = "pareek_official@outlook.com"
        self.passw_outlook = "Zindagi@1998"
        # SMTP
        self.smtp_gmail = "smtp.gmail.com"
        self.smtp_outlook = "smtp.office365.com"
        #POP3
        self.pop_gmail = "pop.gmail.com"
        self.pop_outlook = "outlook.office365.com"

        #ports
        self.port_ssl = 465
        self.port_tls = 587
        self.port_pop = 995

        self.test_mail = "saurabhpareek31+testing@gmail.com"




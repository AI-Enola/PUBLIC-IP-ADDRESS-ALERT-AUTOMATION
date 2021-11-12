"""
Author : LA
Description : Connect to SMTP server and send mail to receiver
Version : Public V1
"""

import smtplib 
from email.message import EmailMessage

# More secure way to store login info in linux env : 
# EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
# EMAIL_ADDRESS_DEST = os.environ.get('EMAIL_ADDRESS_DEST')

class MailIO():


    def __init__(self, logger) -> None:
        """
        Description : Call logger and init email source, email destination and email password
        EMAIL_ADDRESS and EMAIL_PASSWORD is the mail sender and the receiver will get mail from email of sender.
        Return : None
        """
        self.logger = logger
        
        # Sender mail info
        self.EMAIL_ADDRESS = 'SENDER MAIL HERE'
        self.EMAIL_PASSWORD = 'SENDER MAIL PASSWORD HERE'
        
        # Receiver mail info
        self.EMAIL_ADDRESS_DEST = 'RECEIVER MAIL HERE'

        # SMTP server info
        self.SMTP = 'smtp-mail.outlook.com' # Example with outlook SMTP server domain
        self.SMTP_PORT = 587 # Example with outlook SMTP server port
    
    
    def connect_to_smtp(self) -> None:
        """
        Description : Connect to SMTP server using SMTP domain and server port
        Return : None
        """
        self.logger.info("Init connection with server SMTP...")
        self.smtp_server = smtplib.SMTP(self.SMTP, self.SMTP_PORT)
        
        try:
            self.smtp_server.ehlo()
            self.smtp_server.starttls()
            self.smtp_server.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
        except:
            self.logger.info("Error - Connection with server SMTP failed !")
            raise
        
        self.logger.info("Connection with server SMTP established !")
    

    def quit_smtp(self) -> None :
        """
        Description : Terminate SMTP session with SMTP server
        Return : None
        """
        self.smtp_server.quit()
    

    def send_email(self,data) -> None:
        """
        Description : Get data as function parameter and wrap data into message and send it to receiver
        Return : None
        """
        
        msg = EmailMessage()
        msg ['Subject'] = '[ RETURNED QUERY ] Message from BotWeb' # Subject can be changed
        msg ['From'] = self.EMAIL_ADDRESS
        msg ['To'] = self.EMAIL_ADDRESS_DEST

        msg.set_content('[ MESSAGE ] Hi ! This is your new public IP address : {}. Thank you.'.format(data)) # Message can be changed
        self.logger.info("Sending mail...")
        
        try:
            self.smtp_server.send_message(msg)
        except:
            self.logger.info("Error - Message not sended !")
            raise    
        self.logger.info("Mail sended.")
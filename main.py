"""
Author : LA
Description : When your public IP has changed the new Public IP will be send via mail
Version : Public V1
"""


from get_public_ip import get_public_ip
from email_io import MailIO
import time
from log import *


class Check_IP():
    
    
    def __init__(self) -> None :
        """
        Description : Init log for this instance, init mail to get ready to connect to SMTP and IMAP
        Return : None
        """
        # Init logger
        log = Log(log_in_file=True, encoding='utf-8', filename='log.txt', filemode='a', logger_name='PUBLIC IP EVENT ALERT', format='%(name)s - %(asctime)s - %(levelname)s: %(message)s')
        self.logger = log.get_logger() # Get logger object
        
        self.mail = MailIO(self.logger) # Send logger object to log mail data and return mail object
        
        self.actual_ip = get_public_ip() # Start with actual Public IP
        

    def main(self) -> None :
        """
        Description : Check Public IP address from external server, if Public IP has changed then send new IP to receiver else take a break and check again
        Return : None
        """
        
        self.logger.info("Starting task...")
        
        ip = str
        
        while 1 : # Keep program running. Note : Can also use bash to keep program running from shell script
            ip = get_public_ip() # Get Public IP
            
            if (self.actual_ip != ip): # Send Mail only if Public IP is different from actual Public IP
                
                self.logger.info("Public IP has been changed ! New Public IP is : {0}".format(ip))
                self.actual_ip = ip # Put new IP as actual IP because IP has been changed
                
                self.mail.connect_to_smtp() # Connect to SMTP server to send new IP to receiver
                
                self.mail.send_email(self.actual_ip) # Send Public IP to receiver
                
                self.mail.quit_smtp() # Terminate SMTP session
                
            else :
                self.logger.info("Public IP not changed, actual Public IP is : {0}".format(self.actual_ip))
               
            self.logger.info("Task done.") 
            time.sleep(1200) # Make a pause before checking if IP has been changed. Note : Can also use bash to make sleep from shell script
       
            
# Start main program
if __name__ == "__main__":
    ip = Check_IP() # Init program
    ip.main() # Run the program core 
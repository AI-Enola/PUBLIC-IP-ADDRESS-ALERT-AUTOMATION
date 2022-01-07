# PUBLIC-IP-ADDRESS-ALERT-AUTOMATION

Compatibility : Mac OS & GNU/Linux

For external query via Internet : CURL need to ne installed on your machine.

Python 3.9.5 - Send new IP public address via Mail to inform owner of new IP - Useful when using home VPN Server on ISP dynamic IP address


Before using this script :

  In email_io.py between lines 26 and 35, you need to put SMTP server informations (Domain & Port), your informations like sender email address, email password and finally receiver email address.
  
  Note : If you want to use a secure way to store sensitive data in Linux use os.environ.get() function


To use this script :

  python3 main.py
  
Enjoy !

Main project : https://github.com/AI-Enola/AUTOMATION_SERVICES_CORE
Note : This sub project is a service present in Main project

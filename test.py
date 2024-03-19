import yaml
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
smtp_server = "smtp.gmail.com"
port = 465
receiver_email="deepanjals1995@gmail.com"
'''
message="""\
Subject: Hi there : {}

This message is sent from sniperedr.""".format("SniperEDR detected incident")

======================================================================================

'''
message = MIMEMultipart("alternative")
message["Subject"] = "Sniper EDR has detected an incident - Detected mimikatz execution"
message["From"] = "sniperedr@gmail.com"
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
SniperEDR detected incident?
Please go through email:
www.protecte.in"""
html = """\
<html>
  <body>
    <p>Hi there,<br>
       Sniperedr has seen some malicious activity.<br>
       <a href="http://www.realpython.com">Detected Execution of mimikatz on endpoint Click to view full incident report</a>
    </p>
    <div>
    <img src="https://source.unsplash.com/200x200/?coding" alt="Mimikatz" width="200" height="200" >
    </div>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

def Reading_detection_signature(filename:str):
    
    with open(filename, "r") as read_file:
        data=yaml.safe_load(read_file)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            
            server.login(data['username'], data['cred'])
            server.sendmail(data['username'], receiver_email,message.as_string())
        server.close()
    read_file.close()
    print("Sent the email")

if __name__=="__main__":
    Reading_detection_signature("sample.yml")
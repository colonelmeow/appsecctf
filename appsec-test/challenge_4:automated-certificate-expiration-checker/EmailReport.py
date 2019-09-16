import ipaddress
import logging
from models import SSLCert
import htmlFormatting
import datetime
from mailer import Mailer
from mailer import Message

logging.basicConfig(filename = 'sslmon.log', level = logging.DEBUG)

def WeeklyEmail():
    now = datetime.datetime.now()

    # initialize the log settings
    logging.basicConfig(filename = 'sslmon.log', level = logging.DEBUG)
    filename = datetime.datetime.today()
    reportname = "SSL-Certificate-Report-" + str(filename)[0:10]
    with open(reportname, 'r') as myFile:
        ExpirationReport = myFile.read()
        for a in ExpirationReport:
            key = a.get()
        ExpirationReport += "</tbody></table></br><p>This is an automated email, please do not respond directly to this message, email <email address> for questions about this report</p>"
        print(ExpirationReport)

        message = Message(From="sslmon@<senderdomain>",
                          To=["recipients"])
        message.Subject = now.strftime("Test: Certificate Expiration Report %m/%d/%Y")
        message.Html = ExpirationReport

        sender = Mailer('inner-relay-3.corp.adobe.com')
        sender.send(message)
        logging.info("SSL Certifcate expiration report sent " + datetime.datetime.now())

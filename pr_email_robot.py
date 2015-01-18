import smtplib
import gspread

from gmail_variables import *

gc = gspread.login(GMAIL_USERNAME, GMAIL_PASSWORD)
wks = gc.open("NAME OF SPREADSHEET HERE").sheet1

recipients = wks.get_all_values()

def sendEmail(recipient):
	email_subject = "ENTER AN EMAIL SUBJECT HERE"
	#recipient = "nat@programmingformarketers.com"

	body_of_email = "<body><p>PUT YOUR HTML HERE, LEAVE THE STUFF AROUND IT IN PLACE</p></body>"

	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo()
	session.starttls()
	session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

	headers = "\r\n".join(["from: " + GMAIL_USERNAME,
	                       "subject: " + email_subject,
	                       "to: " + recipient[1],
	                       "mime-version: 1.0",
	                       "content-type: text/html"])

	# body_of_email can be plaintext or html!                    
	content = headers + "\r\n\r\n" + body_of_email
	session.sendmail(GMAIL_USERNAME, recipient[1], content)

[sendEmail(i) for i in recipients]

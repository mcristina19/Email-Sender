import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Megan'
email['to'] = 'dummy_email@yahoo.com'
email['subject'] = 'Congragulations!'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('fake_email@gmail.com', 'bbnmgvksdnoinsdof')
	smtp.send_message(email)
	

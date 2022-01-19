import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path    

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Unknown'
email['to'] = 'Receiver\'s_Mail_Address'
email['subject'] = 'Email With Python'
email.set_content(html.substitute({'name': 'Receiver\'s_Name'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('your_email_goes_here', 'your_password_goes_here')
  smtp.send_message(email)
  print('all good boss!')
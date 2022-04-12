# smtplib defines an SMTP client session object that can be used to send mail to any
# machine with an SMTP or ESTMP listener daemon

# The SMTP class encapsulates an SMTP connection. It has methods that support
# SMTP and ESMTP operations. If a host and port is provided to the constructor,
# the SMTP.connect() method is called automatically.

# The SMTP.connect() is used to connect to a host on a given port.

# The SMTP.sendmail() method is used to send mail to the SMTP server.
# It accepts a from_address, a to_address, and a mail message.

# The SMTP.quit() method is used to terminate the SMTP session and close the connection.
# The method will return the result of SMTP QUIT command

# The email library provides ways of managing email addresses, supporting RFCs for email formats
# and for MIMEs.
# The sub-module email.message defines an API to ask questions about an existing email, to construct
# a new email, or to add/remove email subcomponents.

import smtplib
import email.message
import time

start = time.time()

try:
    smtp_ssl = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    smtp_ssl.set_debuglevel(1)
except Exception as e:
    print(f"ErrorType: {type(e).__name__}\nError: {e}")
    smtp_ssl = None


print(f'Connection Object : {smtp_ssl}')
print(f'Total Time Taken  : {time.time() - start}')

print('\nLogging In........')
resp_code, response = smtp_ssl.login(user='email@example.com', password='123456')
print(f'Response Code     : {resp_code}')
print(f'Response          : {response.decode()}')


# NOOP ensures the connection is still valid
print(smtp_ssl.noop())

message = email.message.EmailMessage()

from_addr = 'email@example.com'
to_addr = 'email@example.com'

message.set_default_type('text/plain')
message['From'] = from_addr
message['To'] = to_addr
message['cc'] = 'email@example.com'
message['Subject'] = 'Test Email using sendmessage()'
body= '''
Bonjour,

Ca va?

Oui bien, merci beacoup.

Au revoir,
~Jacques
'''

message.set_content(body)
smtp_ssl.send_message(message)


smtp_ssl.quit()
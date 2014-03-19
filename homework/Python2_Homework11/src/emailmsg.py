"""
Homework:
Here are your instructions:
Write a function that takes an email address, a string, and a list argument. 
It should return an email message addressed to the email address passed as 
the first argument, with the second argument as the message body. If the list 
is non-empty, then each list item should be treated as the name of a file and 
the corresponding file should be attached (with an appropriate MIME type) to 
the message.
"""
import os
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio

def build(email_addr, body, attachments=None):
    msg = MIMEMultipart()
    msg['to'] = email_addr
    body_msg = MIMEText(body, 'plain')
    msg.attach(body_msg)
    
    if attachments:
        for fn in attachments:
            mimetype = mimetypes.guess_type(fn)[0]
            if mimetype:
                mimetype_main, mimetype_sub = mimetype.split('/')
    
            if mimetype_main == 'text':
                with open(fn, 'r') as fileobj:
                    attachment = MIMEText(fileobj.read(), mimetype_sub)
            elif mimetype_main == 'image':
                with open(fn, 'rb') as fileobj:
                    attachment = MIMEImage(fileobj.read(), mimetype_sub)
            elif mimetype_main == 'audio':
                with open(fn, 'rb') as fileobj:
                    attachment = MIMEAudio(fileobj.read(), mimetype_sub)
            else:
                with open(fn, 'rb') as fileobj:
                    attachment = MIMEApplication(fileobj.read(), 'octet-stream')

            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(fn))
            msg.attach(attachment)

    return msg
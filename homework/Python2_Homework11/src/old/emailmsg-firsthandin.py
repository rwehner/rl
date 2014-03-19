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
from binascii import b2a_base64

# for attachments, we need to map the attachment mime type
# to the correct Message object class.
mime_msg_class = {
           'text': MIMEText,
           'image': MIMEImage,
           'application': MIMEApplication,
           'audio': MIMEAudio
           }

def build(email_addr, body, attachments=None):
    msg = MIMEMultipart()
    msg['to'] = email_addr
    body_msg = MIMEText(body, 'plain')
    msg.attach(body_msg)
    #msg.set_payload(body)
    if attachments:
        for fn in attachments:
            with open(fn, 'rb') as fobj:
                filedata = b2a_base64(fobj.read()) #bug in email? pg954 Oreilly Programming Python
                attachment = get_mime_msg(fn)(filedata.decode('ascii'))
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(fn))
            msg.attach(attachment)
    return msg

def get_mime_msg(filename):
    """
    Return an instance of the correct MIME
    message type for the given filename.
    If correct type cannot be determined,
    return a more generic 'application/octet-stream'
    object.
    """
    mimetype = mimetypes.guess_type(filename)[0]
    if not mimetype:
        mimetype = 'application/octet-stream'
    mimetype = mimetype.split('/')[0]
    if mimetype not in mime_msg_class.keys():
        mimetype = 'application'
    return mime_msg_class[mimetype]



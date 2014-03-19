"""
Python Class 2, Lesson 12:
A program to create email messages and store them in a
database so they can be sent at a given future date.
NOTE: the email is stored as a string; the sending
program must convert this string to an email message
before sending.
"""
from email.utils import make_msgid
from datetime import timedelta
import mysql.connector as msc

from database import login_info
from settings import RECIPIENTS, STARTTIME, DAYCOUNT


conn = msc.Connect(**login_info)
curs = conn.cursor()

JOTD_template = """Date: {0}
From: website@example.com
To: {1}
Message-Id: {2}

This is a test message."""

def make_recipient_line(recipients):
    """
    Convert recipients -- a list of tuples in the form [("friendly name", "email_address")] --
    into a string suitable for use in a mail message "to:" field.
    """
    address_template = '"{0}" <{1}>'
    recipient_list = []
    for friendly_name, email_address in recipients:
        recipient_list.append(address_template.format(friendly_name,
                                                      email_address))
    return ", ".join(recipient_list)

def create_msg(recipientline, send_date, template=JOTD_template, messageid=None):
    """
    Function that takes a str.format()-style template representation of an email message
    and fills it in with a recipient email address, the intended send_date
    (as a datetime.datetime() object), and an appropriate Message-ID.
    """
    if not messageid:
        messageid = make_msgid()
    return template.format(send_date.strftime('%a, %b %d, %Y'), recipientline, messageid)

def store(msg, date):
    """
    Stores a string representation of an email message and its
    intended send date.
    """
    curs.execute("""INSERT INTO jotd_emails
                 (msgSendDate, msgText)
                 VALUES (%s, %s)""", (date.strftime('%Y-%m-%d'), msg))
    conn.commit()
    return

def main(starttime, daycount, recipients):
    """
    Create a message per day starting with starttime for each recipient
    and continuing for daycount days. Store them in the database for later
    retrieval, conversion to email messages and sending.
    """
    recipientline = make_recipient_line(recipients)
    for days in range(daycount):
        send_date = starttime + timedelta(days=days)
        store(create_msg(recipientline, send_date), send_date)
        
# After timing, I put these 'alternative' functions to see if performance
# could be improved by reducing the number of DB commits made. It seems to
# help a little.
def store_multi(messages):
    """
    Stores a string representation of multiple email messages and each
    message's send date. messages is a list of tuples in this format:
    [(message, senddate), (message, senddate)]
    Helps limit required DB commits.
    """
    for msg, date in messages:
        curs.execute("""INSERT INTO jotd_emails
                     (msgSendDate, msgText)
                     VALUES (%s, %s)""", (date.strftime('%Y-%m-%d'), msg))
    conn.commit()
    return

def main_multi(starttime, daycount, recipients):
    """
    Create a message per day starting with starttime for each recipient
    and continuing for daycount days. Store them in the database for later
    retrieval, conversion to email messages and sending.
    """
    all_messages = []
    recipientline = make_recipient_line(recipients)
    for days in range(daycount):
        send_date = starttime + timedelta(days=days)
        all_messages.append((create_msg(recipientline, send_date), send_date))
    store_multi(all_messages)
                            
        
if __name__ == "__main__":
    main(STARTTIME, DAYCOUNT, RECIPIENTS)

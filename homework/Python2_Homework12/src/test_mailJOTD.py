"""
Test mailJOTD

NOTE: This test creates the message table, dropping any
previous version and should leave it empty. DANGER: This 
test will delete any existing message table.
"""
import mysql.connector as msc
from database import login_info
import mailJOTD
import unittest
import datetime

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE jotd_emails (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgSendDate DATETIME,
     msgText LONGTEXT
)"""

class test_mailJOTD(unittest.TestCase):
    def setUp(self):
        """
        Prepare a new email_jotd table.
        
        DANGER: Any existing jotd_emails table WILL be lost.
        """
        curs.execute("DROP TABLE IF EXISTS jotd_emails")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        
        # create some known values we can test against
        self.expected_date = datetime.datetime(2013, 11, 10, 0, 0)
        self.nextday = self.expected_date + datetime.timedelta(days=1)
        self.single_recipient = [("Kermit the Frog", "kermit@example.com")]
        self.single_recipient_str = '"Kermit the Frog" <kermit@example.com>'
        self.multiple_recipient = [("Kermit the Frog", "kermit@example.com"),
                                    ("Miss Piggy", "thepig@example.com"),
                                    ("Gonzo", "thegreatgonzo@example.com") ]
        self.multiple_recipient_str = '"Kermit the Frog" <kermit@example.com>, "Miss Piggy" <thepig@example.com>, "Gonzo" <thegreatgonzo@example.com>'
        self.expected_messageid = '<20131109225343.67948.81453@eclipsets3.win.useractive.com>'
        self.expected_msg = """Date: %s
From: website@example.com
To: %s
Message-Id: %s

This is a test message.""" % (self.expected_date.strftime('%a, %b %d, %Y'),
                              self.single_recipient_str, self.expected_messageid)
        self.all_msgs = [(self.expected_msg, self.expected_date),
                    (self.expected_msg, self.nextday)]


    def test_make_recipient_line_single(self):
        """
        verify the make_recipient_line() function returns
        correct "to:" lines for a single recipient.
        """
        self.assertEqual(self.single_recipient_str, 
                         mailJOTD.make_recipient_line(self.single_recipient))
                
    def test_make_recipient_line_multiple(self):
        """
        verify the make_recipient_line() function returns
        correct "to:" line for multiple recipients.
        """
        self.assertEqual(self.multiple_recipient_str, 
                         mailJOTD.make_recipient_line(self.multiple_recipient))
                            
    def test_create_msg(self):
        """
        Verify the create_msg() function returns the expected
        message as a string.
        """
        self.assertEqual(self.expected_msg, mailJOTD.create_msg(recipientline=self.single_recipient_str,
                                                                send_date=self.expected_date,                                                                 
                                                                messageid=self.expected_messageid))
    def test_table_empty(self):
        """
        Make sure the jotd_emails table is empty (as the setUp
        should have left it) so we know the message put there later
        are from these tests.
        """
        curs.execute("SELECT COUNT(*) FROM jotd_emails")
        self.msgcount = curs.fetchone()[0]
        self.assertEqual(self.msgcount, 0, "Message count should be empty")

    def test_store(self):
        """
        Make sure the store() function puts the expected message 
        in the database with the expected date.
        """
        mailJOTD.store(self.expected_msg, self.expected_date)
        curs.execute("""SELECT MsgText FROM jotd_emails
                      WHERE DATE(msgSendDate)=%s""", (self.expected_date.strftime('%Y-%m-%d'),))
        self.msgtext = curs.fetchone()[0]
        self.assertEqual(self.expected_msg, self.msgtext)
        
    def test_main(self):
        """
        Make sure the mailJOTD.main() function inserts the expected
        number of records into the DB. Since we put all recipients
        on a single message, we expect one message per day.
        """
        mailJOTD.main(self.expected_date, 5, self.multiple_recipient)
        curs.execute("SELECT COUNT(*) FROM jotd_emails")
        self.msgcount = curs.fetchone()[0]
        self.assertEqual(self.msgcount, 5)

# just for fun, check the 'multi' functions
    def test_store_multi(self):
        """
        Make sure the store_multi() function puts the expected messages 
        in the database with the expected date.
        """
        mailJOTD.store_multi(self.all_msgs)
        curs.execute("""SELECT MsgText FROM jotd_emails
                      WHERE DATE(msgSendDate)=%s""", (self.expected_date.strftime('%Y-%m-%d'),))
        self.msgtext = curs.fetchone()[0]
        self.assertEqual(self.expected_msg, self.msgtext)
        
        curs.execute("""SELECT MsgText FROM jotd_emails
                      WHERE DATE(msgSendDate)=%s""", (self.nextday.strftime('%Y-%m-%d'),))
        self.msgtext = curs.fetchone()[0]
        self.assertEqual(self.expected_msg, self.msgtext)
        
    def test_main_multi(self):
        """
        Make sure the mailJOTD.main_multi() function inserts the expected
        number of records into the DB. Since we put all recipients
        on a single message, we expect one message per day.
        """
        mailJOTD.main_multi(self.expected_date, 5, self.multiple_recipient)
        curs.execute("SELECT COUNT(*) FROM jotd_emails")
        self.msgcount = curs.fetchone()[0]
        self.assertEqual(self.msgcount, 5)
                            
if __name__ == "__main__":
    unittest.main()
        
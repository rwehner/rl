import os
import unittest
        
import emailmsg

class TestEmailmsgBuild(unittest.TestCase):
    
    def setUp(self):
        self.email_addr = 'bob@example.com'
        self.email_body = 'This is the email body\nSigned Somebody'
        # (mimetype, test_file_path)
        # test_file_path must be a file that already exists
        self.attachments = (('text', 'file.txt'),
                            ('image', 'file.gif'),
                            ('image', 'cclicense.png'),
                            ('audio', 'file.mp3'),
                            ('application', 'python.exe'),
                            ('application', 'file.unlistedsuffix'),
                            ('application', 'file')
                            )
    def test_no_files(self):
        msg = emailmsg.build(self.email_addr, self.email_body)
        self.assertEqual(msg['to'], self.email_addr)
        self.assertEqual(msg.get_payload()[0].get_payload(), self.email_body)
      
    def test_with_attachments(self):
        all_files = [t[1] for t in self.attachments]
        msg = emailmsg.build(self.email_addr, self.email_body, all_files)
        for count, part in enumerate(msg.walk()):
            mainmimetype = part.get_content_type().split('/')[0]
            if count in (0, 1): # skip the container msg and 'body' msg
                pass
            else:
                expectedtype = self.attachments[count - 2][0]
                filename = os.path.basename(self.attachments[count - 2][1])
                self.assertEqual(mainmimetype, expectedtype)
                self.assertEqual(part.get_filename(), filename)
                          
if __name__ == "__main__":
    unittest.main()
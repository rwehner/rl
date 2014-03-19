import unittest
import mysql.connector
from database import login_info
from classFactory import build_row

class RowTest(unittest.TestCase):
    
    def setUp(self):
        # Create a test row
        C = build_row("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
        
    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
        
    def test_repr(self):
        self.assertEqual(repr(self.c), "user_record(1, 'Steve Holden', 'steve@holdenweb.com')")
                         
class DBTest(unittest.TestCase):
    
    def setUp(self):
        # Create a test row
        self.row_values = ((1, "Steve Holden", "steve@holdenweb.com"),
                           (2, "Maggie Mae", "mmae@example.net"),
                           (3, "John Smith", "smith.j@example.com"),
                           (4, "John Smith", "jsmith@example.org"))
        C = build_row("user", "id name email")
        self.c = C(self.row_values[0])        
        self.db = mysql.connector.Connect(**login_info)
        self.cursor = self.db.cursor()
        self.cursor.execute('''DROP TABLE IF EXISTS user''')
        self.cursor.execute('''CREATE TABLE user(
                            id INTEGER PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(50),
                            email VARCHAR(50))''')
        for sampledata in self.row_values:
            self.cursor.execute('''INSERT INTO user (name, email)
                            VALUES (%s, %s)''', sampledata[1:])
        #self.cursor.execute('''SELECT * FROM user''')
        #from pprint import pprint
        #pprint(self.cursor.fetchall())
        
    def tearDown(self):
        self.cursor.execute('''DROP TABLE IF EXISTS user''')
        self.db.commit()      
        
    def test_retrieve_one_match_condition(self):
        rows = self.c.retrieve(self.cursor, "WHERE id = 1")
        for row in rows:
            self.assertEqual(row.id, 1)
            self.assertEqual(row.name, "Steve Holden")
            self.assertEqual(row.email, "steve@holdenweb.com")
        
    def test_retrieve_no_condition(self):
        rows = self.c.retrieve(self.cursor, None)
        for knownrow, foundrow in zip(self.row_values, rows):
            id, name, email = knownrow
            self.assertEqual(foundrow.id, id)
            self.assertEqual(foundrow.name, name)
            self.assertEqual(foundrow.email, email)
               
    def test_retrieve_multiple_rows_with_condition(self):
        rows = self.c.retrieve(self.cursor, "WHERE name = 'John Smith'")
        for knownrow, foundrow in zip(self.row_values[2:], rows):
            id, name, email = knownrow
            self.assertEqual(foundrow.id, id)
            self.assertEqual(foundrow.name, name)
            self.assertEqual(foundrow.email, email)


if __name__ == "__main__":
    unittest.main()
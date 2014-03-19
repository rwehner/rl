import unittest

from novalueerror import novalueerror

def create_valueerror():
    with novalueerror():
        raise ValueError
    
def create_othererror():
    with novalueerror():
        raise Exception

class Testnovalueerror(unittest.TestCase):
    def test_novalueerror(self):
        self.assertRaises(Exception, create_othererror)
        self.assertEqual(create_valueerror(), None)
        
if __name__ == "__main__":
    unittest.main()
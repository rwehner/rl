"""Python2 Homework01 unittest example"""

import unittest

def title(s):
    """Returns same string with first character capitalized.
       Modified to handle strings with whitespace and uppercase like str.title()
    """
    #return s[0].upper()+s[1:]
    return ' '.join([c[0].upper() + c[1:].lower() for c in s.split()])

class TestTitle(unittest.TestCase):
    
    def test_lowercase_singleword_string(self):
        self.assertEqual(title('hamlet'), 'hamlet'.title(), "title on 'hamlet' did not return 'Hamlet'.")

    def test_lowercase_multiword_string(self):
        self.assertEqual(title('moby dick'), 'moby dick'.title(), "title on 'moby dick' did not return 'Moby Dick'.")
    
    def test_uppercase_singleword_string(self):
        self.assertEqual(title('HAMLET'), 'HAMLET'.title(), "title on 'HAMLET' did not return 'Hamlet'.")
        
    def test_uppercase_multiword_string(self):
        self.assertEqual(title('MOBY DICK'), 'MOBY DICK'.title(), "title on 'MOBY DICK' did not return 'Moby Dick'.")
   
    def test_nonstring_input(self):
        "test integer, list, tuple, dict"
        for nonstring in 1, ['a', 'b', 2, 3], ('a', 'b', 2, 3), {'a':1, 'b':2, 3:4}:  
            self.assertRaises(AttributeError, title, (nonstring,))
        
if __name__ == "__main__":
    unittest.main()
"""
Validate correctness of find_regex.py module
"""
import unittest
from find_regex import find_start_end

class TestFindRegex(unittest.TestCase):
    
    def test_find_start_end(self):
        # tuple of tuples
        # [(targettext, pattern, (expected_start, expected_end)), ...]
        self.test_collection = (('In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.',
                                 'Regular\sExpressions', (231, 250)),
                                ('Some text with an address (123 Oak Street) and phone number: (123) 654-9876. Will we find this?', 
                                 '\(\d\d\d\)\s\d\d\d-\d\d\d\d', (61, 75)),
                                ('We will not find the pattern in here on purpose since the pattern is all numbers.', '\d+', None))
        
        for text, pattern, expected_result in self.test_collection:
            result = find_start_end(pattern, text)
            self.assertEqual(result, expected_result, "Got %s, but should have got %s" % (result, expected_result))
            
if __name__ == "__main__":
    unittest.main()
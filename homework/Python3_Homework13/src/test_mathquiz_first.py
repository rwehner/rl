import unittest

from mathquiz_first import *

class TestMathQuiz(unittest.TestCase):
    'Test the mathquiz module'
    def test_get_addends(self):
        # verify tuple length
        self.assertEqual(len(get_addends()), 2)
        self.assertEqual(len(get_addends(length=3)), 3)
        
        # verify we get integers and in the right range
        result = get_addends(length=1)[0]
        self.assertTrue(isinstance(result, int))
        self.assertTrue(1 <= result <= 10)
        
if __name__ == "__main__":
    unittest.main()
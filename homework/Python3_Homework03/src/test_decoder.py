from string import ascii_uppercase
import unittest

from decoder import alphabator

class TestAlpha(unittest.TestCase):

    def test_easy_26(self):
        a = alphabator(range(1,27))
        self.assertEqual(list(ascii_uppercase), list(a))

    def test_upper_range(self):
        a = alphabator(range(40,50))          
        self.assertEqual(list(range(40, 50)), list(a))

    def test_various_objects(self):
        l = ['python', object, ascii_uppercase, 10, alphabator]
        a = list(alphabator(l))
        self.assertNotEqual(l[3], a[3])
        self.assertEqual("J", a[3])
        self.assertTrue(isinstance(a[1], object))

if __name__ == "__main__":
    unittest.main()

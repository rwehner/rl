"""
test_composable.py: simple tests of composable functions
"""
import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing"
    return s[::-1]

def square(x):
    " multiply a number by itself"
    return x*x

class ComposableTestCase(unittest.TestCase):
    
    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        reverser_pow1 = reverser**1
        reverser_pow2 = reverser**2
        reverser_pow3 = reverser**3
        for s in "", "a", "0123456789", "abcdefghijklmnoprstuvwxyz":
            self.assertEquals(nulltran(s), s)
            self.assertEqual(reverser_pow1(s), ''.join(reversed(s)))            
            self.assertEqual(reverser_pow2(s), s)
            self.assertEqual(reverser_pow3(s), ''.join(reversed(s)))
            
    def test_square(self):
        squarer = Composable(square)
        po4 = squarer * square
        pow2 = squarer**2
        pow5 = squarer**5
        for v,r,r2 in ((1,1,1), (2,16,4294967296), (3,81,1853020188851841)):
            self.assertEqual(po4(v), r)
            self.assertEqual(pow2(v), r)
            self.assertEqual(pow5(v), r2)
    
    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = fc**'imastring'
        with self.assertRaises(ValueError):
            fc = fc**-2
            
if __name__ == "__main__":
    unittest.main()
            
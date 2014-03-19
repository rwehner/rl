'''
Created on Nov 19, 2013

@author: rwehner

Test the adder() function of the adder.py module
'''
import unittest
from adder import adder

class Test(unittest.TestCase):


    def test_adder_failures(self):
        """
        Test input that is expected to make adder()
        fail.
        """
        self.assertRaises(TypeError, adder, "four", 2)
        self.assertRaises(TypeError, adder, 2, 2.0)
        self.assertRaises(TypeError, adder, [1,2], (1,2))

    def test_adder_successes(self):
        """
        Test input that is expected to make 
        adder() return valid results.
        """
        self.assertEquals(adder(2,1), 3, "Correctly add integers")

if __name__ == "__main__":
    unittest.main()
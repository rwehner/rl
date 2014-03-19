import unittest

from groffle import groffle_slow, groffle_faster1, groffle_faster2, groffle_faster3

class TestGroffle(unittest.TestCase):
    
    def setUp(self):
        self.mass = 2.5
        self.density = 12.0
        self.expected_result = 33.2895800225
        
    def test_groffle_slow(self):
        self.assertAlmostEqual(groffle_slow(self.mass, self.density), 
                         self.expected_result)
    def test_groffle_faster1(self):
        self.assertAlmostEqual(groffle_faster1(self.mass, self.density), 
                         self.expected_result)        
    def test_groffle_faster2(self):
        self.assertAlmostEqual(groffle_faster2(self.mass, self.density), 
                         self.expected_result)
    def test_groffle_faster3(self):
        self.assertAlmostEqual(groffle_faster3(self.mass, self.density), 
                         self.expected_result)        


if __name__ == "__main__":
    unittest.main()
        
    
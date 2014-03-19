import unittest

from dictdefault import DictDefault

class Test_DictDefault(unittest.TestCase):
    
    def test_dictdefault(self):
        dd = DictDefault('A')
        dd['realitem'] = 'B'
        # returns default when key not present
        self.assertEqual(dd['IDontExist'], "A")
        self.assertEqual(dd['realitem'], "B")
        with self.assertRaises(TypeError):
            DictDefault()
            DictDefault("A", "B")
        
if __name__ == "__main__":
    unittest.main()
"""
test furnishings.py and the various
bits of furniture defined there.
"""
import unittest
from furnishings import Furnishing, Sofa, Bookshelf, Bed, Table, map_the_home, counter

class TestFurnishings(unittest.TestCase):
    def test_furniture(self):
        "Basic test of classes derived from Furnishing"
        furnishing = Furnishing("Kitchen")
        sofa = Sofa('Living Room')
        bookshelf = Bookshelf('Library')
        bed = Bed('Bedroom')
        table = Table('Dining Room')
        self.assertEqual(furnishing.room, 'Kitchen')
        self.assertEqual(sofa.room, 'Living Room')
        self.assertEqual(bookshelf.room, 'Library')
        self.assertEqual(bed.room, 'Bedroom')
        self.assertEqual(table.room, 'Dining Room')
        
        self.assertEqual(sofa.name, 'Sofas')
        self.assertEqual(bookshelf.name, 'Bookshelves')
        self.assertEqual(bed.name, 'Beds')
        self.assertEqual(table.name, 'Tables')
        
    def test_map_the_home(self):
        # make sure it handles objects not derived from Furnishing
        home = [Bed('Bedroom'), 1, [1,2,3]]
        with self.assertRaises(AttributeError):
            map_the_home(home)
        
        # works as expected
        home = [Bed('Bedroom'), Sofa('Living Room')]
        result = map_the_home(home)
        self.assertTrue(isinstance(result['Bedroom'][0], Bed))
        self.assertTrue(isinstance(result['Living Room'][0], Sofa))
        
    def test_counter(self):
        # make sure it handles objects not derived from Furnishing
        home = [Bed('Bedroom'), 1, [1,2,3]]
        with self.assertRaises(AttributeError):
            counter(home)
        
        # works as expected    
        home = [Bed('Bedroom'), Sofa('Living Room')]
        expected = "Beds: 1\nBookshelves: 0\nSofas: 1\nTables: 0"
        self.assertEqual(counter(home), expected)
        
if __name__ == "__main__":
    unittest.main()
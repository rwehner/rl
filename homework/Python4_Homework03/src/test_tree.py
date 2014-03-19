'''
Test the tree.Tree class
'''
import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def test_tree_init(self):
        t = Tree("D", 4)
        self.assertEqual(list(t.walk()), ['D'])
   
    def test_tree_no_right(self):
        t = Tree('D', 4)
        for c, i in (('C', 3), ('A', 1), ('B', 2)):
            t.insert(c, i)
        self.assertEqual(list(t.walk()), ['A', 'B', 'C', 'D'])
        
    def test_tree_no_left(self):
        t = Tree('D')
        for c in 'FGE':
            t.insert(c)
        self.assertEqual(list(t.walk()), ['D', 'E', 'F', 'G'])
        
    def test_tree_both_lr(self):
        'Test tree with both L and R nodes. Also no data passed in.'
        t = Tree('D')
        for c in 'FGCAEB':
            t.insert(c)
        self.assertEqual(list(t.walk()), ['A', 'B', 'C', 'D', 'E', 'F', 'G']) 
        
    def test_tree_duplicate_key(self):       
        t = Tree('D')
        self.assertRaises(ValueError, t.insert, 'D')

    def test_tree_find(self):
        'Verify find method, with data and without'
        t = Tree('D')
        for c, i in (('F', [6,7,8]),('C', 3), ('G', dict(one=1, two=2)), ('A', 1), ('E', 5), ('B', 2)):
            t.insert(c, i)
        self.assertEqual(t.find('D'), None)
        self.assertEqual(t.find('A'), 1)
        self.assertEqual(t.find('F'), [6,7,8])
        self.assertEqual(t.find('G'), {'one':1, 'two':2})
        self.assertRaises(KeyError, t.find, 'Z')
       
if __name__ == "__main__":
    unittest.main()
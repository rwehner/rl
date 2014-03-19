import unittest
import os
import tempfile
import shutil
import sys
from io import StringIO

import countext

WORKSPACE = 'V:\\tmp'

class TestCountextFiles(unittest.TestCase):
    """Test for countext that require files to be created in setUp"""
    
    def setUp(self):
        self.filenames = ['file1.doc', 'file1.txt', 'file1.py',
                          'file1', 'file2.doc', 'file2.py', 'file3.py']
        self.curdir = os.path.abspath(os.curdir)
        self.tempdir = tempfile.mkdtemp(dir=WORKSPACE)
        os.chdir(self.tempdir)
        for file in self.filenames:
            f = open(file, 'w')
            f.close()             
    
    def tearDown(self):
        os.chdir(self.curdir)    
        shutil.rmtree(self.tempdir)
        
    def test_countext_with_files(self):
        """Make sure countext.countext returns a correct count
        of files with any given extension (or no extension)"""
        expected = set([('.doc', 2), ('.txt', 1), ('.py', 3), ('', 1)])
        found = set(countext.countext())
        self.assertEqual(found, expected)
        
    def test_printcountext(self):
        """Make sure printed output is as expected."""
        expected = "In %s:\nExt \tCount\n----\t-----\n.py\t3\n.doc\t2\n<none>\t1\n.txt\t1" % self.tempdir
        old_stdout = sys.stdout
        sys.stdout = found = StringIO()
        countext.printextcount()
        self.assertEqual(found.getvalue().strip(), expected)
        sys.stdout = old_stdout 
        
class TestCountextNoFiles(unittest.TestCase):
    """Tests for countext that require an empty directory to check"""
    
    def setUp(self):
        self.curdir = os.path.abspath(os.curdir)
        self.tempdir = tempfile.mkdtemp(dir=WORKSPACE)
        os.chdir(self.tempdir)
    
    def tearDown(self):
        os.chdir(self.curdir)    
        shutil.rmtree(self.tempdir)
        
    def test_countext_without_files(self):
        """Make sure countext.countext returns correct output
        when no files are in current dir"""
        self.assertEqual(countext.countext(), [])
        
    def test_printcountext_without_files(self):
        """Make sure printed output is sensible when no files are there to get extensions for."""
        expected = "No files in %s" % self.tempdir
        old_stdout = sys.stdout
        sys.stdout = found = StringIO()
        countext.printextcount()
        self.assertEqual(found.getvalue().strip(), expected)
        sys.stdout = old_stdout
         
if __name__ == '__main__':
    unittest.main()
        
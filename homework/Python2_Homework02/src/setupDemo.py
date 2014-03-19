"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test_1(self):
        "Verify creation of files is possible"
        files = {"this.txt", "that.txt", "the_other.txt"}
        for filename in files:
            f = open(filename, 'w')
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        self.assertEqual(files, set(os.listdir(self.dirname)), 
                         "Files created %s do not match what really exists %s" % 
                         (files, set(os.listdir(self.dirname))))
                    
    def test_2(self):
        "Verify the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        "Verify a binary file is exactly the size we expect."
        filename = 'testsize.txt'
        f = open(filename, 'wb')
        f.write(bytes(1000000))
        f.close()
        self.assertEqual(1000000, os.stat(filename).st_size, "File size is not 1000000 bytes, but should be.")
             
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
if __name__ == '__main__':
    unittest.main()
        
import os
import shutil
import unittest
import zipfile

import relativezip

class TestRelativeZip(unittest.TestCase):
    
    def setUp(self):
        self.path = "v:\\workspace\\Python2_Homework05\\src\\archive_me"
        self.archivedir = os.path.split(self.path)[1]
        self.excludedir = 'exclude_me'
        os.makedirs(os.path.join(self.path, self.excludedir))
        self.zip_fn = os.path.join(self.path, "relative.zip")
        self.files_to_archive = ["groucho", "harpo", "chico"]
        self.files_to_exclude = ["file1", "file2", "file3"]
        for fn in self.files_to_archive:
            f = open(os.path.join(self.path, fn), "w")
            f.close()
        for fn in self.files_to_exclude:
            f = open(os.path.join(self.path, self.excludedir, fn), "w")
            f.close()
        
    def tearDown(self):
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass

    def test_relativezip(self):
        """
        Make sure the paths in the zip are relative.
        This also verifies no subdirs or files in subdirs were archived
        """
        relativezip.relativezip(self.path, self.zip_fn)
        zf = zipfile.ZipFile(self.zip_fn)
        observed = set(zf.namelist())
        # zipfile uses '/' as path separator no matter the OS
        # so we can't use os.path.join reliably in the next line.
        expected = set([self.archivedir + '/' + f for f in self.files_to_archive])
        self.assertEquals(observed, expected)
        
        
if __name__ == "__main__":
    unittest.main()
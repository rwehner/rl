import unittest

from ccn_safety2 import obfuscate_ccn

original_text = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
ccn_cleaned_text = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts."

class TestCCN(unittest.TestCase):
    
    def test_obfuscate_ccn(self):
        self.assertEqual(obfuscate_ccn(original_text), ccn_cleaned_text)
        
    def test_obfuscate_ccn_no_ccn(self):
        self.assertEqual(obfuscate_ccn(ccn_cleaned_text), ccn_cleaned_text)
        
if __name__ == "__main__":
    unittest.main()
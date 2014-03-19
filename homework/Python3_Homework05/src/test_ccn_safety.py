import unittest

from ccn_safety import obfuscate_ccn

original_text = """Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number
that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and
security experts.
"""
obfuscated_text = """Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a number
that appears to be real, such as XXXX-XXXX-XXXX-5678, triggers the attention of privacy and
security experts.
"""
original_text_clean = """Have you ever noticed, in television and movies, that phone numbers and tears
are obviously fake numbers like 555-123-4567 or "buah buah buah"? It is because a number
that appears to be imaginary, such as a + bi, triggers the attention of privacy and
security experts.
"""

class TestCCN(unittest.TestCase):
    
    def test_obfuscate_ccn(self):
        self.assertEqual(obfuscate_ccn(original_text), obfuscated_text)
        
    def test_obfuscate_ccn_no_ccn(self):
        self.assertEqual(obfuscate_ccn(original_text_clean), original_text_clean)
        
if __name__ == "__main__":
    unittest.main()
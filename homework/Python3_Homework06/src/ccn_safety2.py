import re

def obfuscate_ccn(text):
    """
    Replace a credit card number of the form
    XXXX-XXXX-XXXX-XXXX with the safe text
    'CCN REMOVED FOR YOUR SAFETY'
    """
    ccn_regex = re.compile(r"""
                            \d{4}-    # four digits and a dash
                            \d{4}-    # four digits and a dash
                            \d{4}-    # four digits and a dash
                            \d{4}     ## four digits
                            """, re.VERBOSE)
    return ccn_regex.sub("CCN REMOVED FOR YOUR SAFETY", text)
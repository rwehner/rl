import re

#1234-5678-1234-5678
def obfuscate_ccn(text):
    return re.sub(r"\d{4}-\d{4}-\d{4}-", "XXXX-XXXX-XXXX-", text)
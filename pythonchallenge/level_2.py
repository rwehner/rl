import string
from util import get_url_word

url = 'http://www.pythonchallenge.com/pc/def/map.html'
secret = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

rot2ascii = string.ascii_lowercase[-2:] + string.ascii_lowercase[:-2] 
magicring = string.maketrans(rot2ascii, string.ascii_lowercase)

print string.translate(secret, magicring)

word_to_alter = get_url_word(url)
altered_word = string.translate(word_to_alter, magicring)

print url.replace(word_to_alter, altered_word)

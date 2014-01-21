from util import get_url_word

url = "http://www.pythonchallenge.com/pc/def/0.html"
print url.replace(get_url_word(url), str(2 ** 38))

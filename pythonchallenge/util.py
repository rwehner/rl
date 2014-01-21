def get_url_word(url):
    """
    Pull the last word out of a string url.
    This is typically the part of the url that 
    needs to be changed in PythonChallenge.
    """
    return url.split('/')[-1].split('.')[0]

if __name__ == "__main__":
    url = 'http://www.pythonchallenge.com/pc/def/map.html'
    assert get_url_word(url) == 'map'

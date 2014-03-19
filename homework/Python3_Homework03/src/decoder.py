from string import ascii_uppercase

def alphabator(lst):
    for item in lst:
        if not isinstance(item, int) or item < 1 or item > 26:
            yield item
        else:
            yield ascii_uppercase[item - 1]
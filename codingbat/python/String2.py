'''
String-2 exercises from codingbat.com

Medium python string problems -- 1 loop.. Use + to combine strings, len(str)
is the number of chars in a String, str[i:j] extracts the substring starting
at index i and running up to but not including index j.
'''
def double_char(str):
    '''
    Given a string, return a string where for every char in the original,
    there are two chars.
    '''
    return ''.join([ch + ch for ch in str])

def count_hi(str):
    '''
    Return the number of times that the string "hi" appears anywhere in
    the given string.
    '''
    return str.count('hi')

def cat_dog(str):
    '''
    Return True if the string "cat" and "dog" appear the same number of times
    in the given string.
    '''
    return str.count('dog') ==  str.count('cat')

def count_code(str):
    '''
    Return the number of times that the string "code" appears anywhere in the
    given string, except we'll accept any letter for the 'd', so "cope" and
    "cooe" count.
    regex is disallowed  :(
    import re
    return len(re.findall("co.e", str))
    '''
    if 'co' not in str or len(str) < 4:
        return 0

    count = 0
    for index, character in enumerate(str):
        if character == 'c':
            word = str[index:index + 4]
            if word.startswith('co') and word.endswith('e'):
                count += 1
    return count

def end_other(a, b):
    '''
    Given two strings, return True if either of the strings appears at the
    very end of the other string, ignoring upper/lower case differences (in
    other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    '''
    return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

def xyz_there(str):
    '''
    Return True if the given string contains an appearance of "xyz" where the
    xyz is not directly preceded by a period (.). So "xxyz" counts but "x.xyz"
    does not.
    '''
    if 'xyz' not in str:
        return False

    remaining = str[:]
    next_index = remaining.find('xyz')
    while next_index >= 0:
        if next_index == 0 or remaining[next_index - 1] != '.':
            return True
        else:
            remaining = remaining[next_index + 3:]
            next_index = remaining.find('xyz')
    return False
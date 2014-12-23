'''
Warmup-2 exercises from codingbat.com

Medium warmup string/list problems with loops
'''

def string_times(str, n):
    '''
    Given a string and a non-negative int n, return a larger string that is n copies of the original string.
    '''
    return str * n

def front_times(str, n):
    '''
    Given a string and a non-negative int n, we'll say that the front of the
    string is the first 3 chars, or whatever is there if the string is less
    than length 3. Return n copies of the front;
    '''
    if len(str) < 3:
        return str * n
    return str[:3] * n

def string_bits(str):
    '''
    Given a string, return a new string made of every other char starting with
    the first, so "Hello" yields "Hlo".
    '''
    return str[0::2]

def string_splosion(str):
    '''
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    '''
    newstr = ''
    for i in range(1, len(str)+1):
        newstr += str[:i]
    return newstr

def last2(str):
    '''
    Given a string, return the count of the number of times that a substring
    length 2 appears in the string and also as the last 2 chars of the string,
    so "hixxxhi" yields 1 (we won't count the end substring).
    '''
    if len(str) < 2:
        return 0

    front, last_two = str[:-2], str[-2:]
    print(front,last_two)
    count = 0
    for i in range(len(front)):
        substr = front[i:i+2]
        if substr == last_two:
            count += 1
    return count

def array_count9(nums):
    '''
    Given an array of ints, return the number of 9's in the array.
    '''
    return nums.count(9)

def array_front9(nums):
    '''
    Given an array of ints, return True if one of the first 4 elements in the
    array is a 9. The array length may be less than 4.
    '''
    return 9 in nums[:4]

def array123(nums):
    '''
    Given an array of ints, return True if .. 1, 2, 3, .. appears in the
    array somewhere.
    '''
    for i in range(len(nums)):
        if nums[i:i+3] == [1,2,3]:
            return True
    return False


def string_match(a, b):
    '''
    Given 2 strings, a and b, return the number of the positions where they
    contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
    since the "xx", "aa", and "az" substrings appear in the same place in
    both strings.
    '''
    if len(a) <= len(b):
        str1, str2 = a, b
    else:
        str1, str2 = b, a

    count = 0
    for i in range(len(str1) - 1):
        if str1[i:i+2] == str2[i:i+2]:
            count += 1
    return count

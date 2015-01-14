'''
List-1 exercises from codingbat.com

Basic python list problems -- no loops.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.
'''
def first_last6(nums):
    '''
    Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be
    length 1 or more.
    '''
    return (nums[0] == 6 or nums[-1] == 6)

def same_first_last(nums):
    '''
    Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are
    equal.
    '''
    if len(nums) > 0:
        return ( nums[0] == nums[-1] )
    else:
        return False

"""
def
    '''
    
    '''
    pass

def
    '''
    
    '''
    pass

def
    '''
    
    '''
    pass

def
    '''

    '''
    pass

def
    '''

    '''
    pass
"""

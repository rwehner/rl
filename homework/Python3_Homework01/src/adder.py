'''
a function that takes two objects and 
adds them together oly if they are both
of the integer type.
'''

def adder(obj1, obj2):
    """
    Add obj1 to obj2 if they are both integers
    """
    if type(obj1) != type(1) or type(obj2) != type(1):
        raise TypeError
    return obj1 + obj2
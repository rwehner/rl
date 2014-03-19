"""
composable.py: defines a composable function class
extended to allow integer powers for homework 1
"""
import types

class Composable:
    def __init__(self, f):
        "Store reference to proxied function"
        self.func = f
        
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    
    def __mul__(self, other):
        "Return the composition of proxied and another function"
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
    
    def __pow__(self, nth):
        """
        Return the proxied function to the nth power. This class makes the 
        assumption that  f**2 is the same as f*f, f**3 is the same as f*f*f, 
        and so on. So (f**3)(x) is f(f(f(x))).
        """
        if not isinstance(nth, int):
            raise TypeError("Must use integer for __pow__")
        if nth <= 0:
            raise ValueError("Must use positive integer for __pow__")
        if nth == 1:
            return self
        pow_func = self
        count = nth - 1 
        while count > 0:
            pow_func = pow_func * self
            count -= 1
        return pow_func
    
    def __repr__(self):
        return "<Composable function {0} at 0x{1:X}>".format(self.func.__name__, id(self))
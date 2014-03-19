class sstr(str):
    def __init__(self, s, *args, **kw):
        self.initial_string = s
        str.__init__(self, *args, **kw)
    def __lshift__(self, n):
        return self._rotate_str(self.initial_string, -n)
    def __rlshift__(self, n):
        return NotImplemented
    def __rshift__(self, n):
        return self._rotate_str(self.initial_string, n)
    def __rrlshift__(self, n):
        return NotImplemented   
    def _rotate_str(self, s, n):
        """
        Rotate the characters in string s by n places (int).
        A negative n is lshift. A postive n is rshift.
        """
        result = []
        for i,c in enumerate(s):
            newindex = (i+n) % len(s)
            result.insert(newindex, c)
        return sstr(''.join(result))

# Alternate implementation offered by Kirby
# appears to break with shifts larger than 5?
class sstralt(str):
    def __rshift__(self,other):
        return sstralt(self[-other:] + self[:-other])     
    def __lshift__(self,other):
        return sstralt(self[other:] + self[:other]) 
'''
class-based dict allowing tuple subscripting & sparse data
'''

class array:
    
    def __init__(self, M, N, O):
        "Create an M-element list of N-element row lists with O-element zaxis lists."
        self._data = {}
        self._rows = M
        self._cols = N
        self._zaxis = O
            
    def __getitem__(self, key):
        "Returns the appropriate element for the three-element subscript tuple"
        row, col, zaxis = self._validate_key(key)
        try:
            return self._data[row, col, zaxis]
        except KeyError:
            return 0
    
    def __setitem__(self, key, value):
        "Sets the appropriate element for a three-element subscript tuple"
        row, col, zaxis = self._validate_key(key)
        if value == 0:
            try:
                del self._data[row, col, zaxis]
            except KeyError:
                pass
        else:
            self._data[row, col, zaxis] = value
        
    def _validate_key(self, key):
        """
        Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems.
        """
        row, col, zaxis = key
        if (0 <= row < self._rows and 
            0 <= col < self._cols and
            0 <= zaxis < self._zaxis):
            return key
        raise KeyError("Subscript out of range")
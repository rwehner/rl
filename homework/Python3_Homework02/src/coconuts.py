"""
Track inventory of different varieties of coconut
"""

class Coconut(object):
    """
    Container for data about a coconut.
        type is a sring identifying a known
        coconut type.
        Unknown types raise AttributeError.
        get_weight() gives the weight (float)
        of the individual coconut.
    """
    def __init__(self, type):
        """
        constructor method. type is required. It must be a string
        and defined in the _known_coconuts dict.
        """
        self._known_coconuts = {"south_asian": 3.0,
                            "middle_eastern": 2.5,
                            "american": 3.5}
        
        if not isinstance(type, str):
            raise TypeError("Required argument 'type' must be a string")
        
        if type in self._known_coconuts:
            setattr(self, "_type", type)
            setattr(self, "_weight", self._known_coconuts[type])
        else:
            raise AttributeError("Invalid coconut type '%s'" % (type,))
        
    def get_weight(self):
        """
        return the weight of the coconut as a float
        """
        return float(self._weight)
        
                
class Inventory(object):
    """
    Tracks any number of coconut objects
    and calculates and returns information
    about the full coconut inventory.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.all_coconuts = []
    
    def _get_weights(self):    
        """
        A generator that returns the weight of
        all coconuts in inventory
        """
        for coconut in self.all_coconuts:
            yield coconut.get_weight()
            
    def add_coconut(self, coconut):
        """
        Add a coconuts.Coconut() object to the inventory. All
        other object types raise AttributeError
        """
        if isinstance(coconut, Coconut):
            self.all_coconuts.append(coconut)
        else:
            raise AttributeError("Can only add Coconut objects.")
            
    def total_weight(self):
        """
        sum the weights of all coconuts in the inventory
        """
        return sum(self._get_weights())
        
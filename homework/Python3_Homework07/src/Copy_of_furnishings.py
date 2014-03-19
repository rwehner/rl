"""
Python3_Homework07
Model furniture and a house map
"""
from collections import defaultdict, Counter

class Furnishing:
    def __init__(self, room):
        self.room = room
        
class Sofa(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        self.name = "Sofas"

class Bookshelf(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        self.name = "Bookshelves"

class Bed(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        self.name = "Beds"
        
class Table(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        self.name = "Tables"

def _validate_furniture(furniture_list):
    """
    Internal helper function to validate that 
    furniture_list is a list of objects that
    subclass Furnishings.
    """
    for item in furniture_list:
        if not issubclass(type(item), Furnishing):
            raise AttributeError('All furniture must subclass Furnishing')
    
def map_the_home(furniture_list):
    """
    Take a list of Furnishing-based objects
    and return a dict (defaultdict, anyway)
    of them keyed by room.
    """
    if _validate_furniture_list(furniture_list):
        home_map = defaultdict(list)
        for item in furniture_list:
        if not issubclass(type(item), Furnishing):
            raise AttributeError('All furniture must subclass Furnishing')
        home_map[item.room].append(item)
    return home_map

def counter(furniture_list):
    """
    Take a list of Furnishing-based objects
    and print a sorted list of the furniture types and
    the quantity of each.
    """
    # Initializing the counts to 0 with a hard-coded list of
    # furniture for furniture we might not have in
    # furniture_list feels wrong.
    furniture_quantities = Counter(Beds=0, Bookshelves=0, Sofas=0, Tables=0)
    furniture_quantities.update((item.name for item in furniture_list))
    result = []
    for k, cnt in furniture_quantities.items():
        result.append("{0}: {1}".format(k, cnt))
    return '\n'.join(sorted(result))
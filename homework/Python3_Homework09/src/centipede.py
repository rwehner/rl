"""
homework project for Lesson 09:
use magic methods
"""
class Centipede:
    def __init__(self):
        object.__setattr__(self, "stomach", [])
        object.__setattr__(self, "legs", [])
        
    def __call__(self, arg):
        self.stomach.append(arg)
        
    def __str__(self):
        return ','.join(self.stomach)
    
    def __repr__(self):    
        return ','.join(self.legs)

    def __setattr__(self, key, value):
        if key in ["stomach", "legs"]:
            raise AttributeError("{0} is for internal use only.".format(key))
        object.__setattr__(self, key, value)
        self.legs.append(key)
   
    
    
        
    
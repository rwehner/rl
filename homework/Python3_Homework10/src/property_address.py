"""
homework lesson 10:
"""
import re

class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

class Address:
    
    valid_state = re.compile(r"^[A-Z]{2}$")
    valid_zip = re.compile(r"^\d{5}$")
    
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        
    @property
    def name(self):
        return self._name
   
    ''' This is not really needed. just don't add a setter and it won't be settable 
    @name.setter
    def name(self, value):
        if self._name:
            raise AttributeError("'name' is read-only after first assignment.")
        self._name = str(value)
    '''
        
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        if not self.valid_zip.match(str(value)):
            raise ZipCodeError("{0} is not a valid zip code.".format(value))
        self._zip_code = str(value)
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        if not self.valid_state.match(str(value)):
            raise StateError("{0} is not a valid state abbreviation.".format(value))
        self._state = str(value)
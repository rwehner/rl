"""
homework lesson 11: add logging to homework from lesson 10
"""
import logging
import re

LOG_FILENAME = 'property_address.log'
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "info"
LEVELS = dict(debug=logging.DEBUG,
              info=logging.INFO,
              warning=logging.WARNING,
              error=logging.ERROR,
              critical=logging.CRITICAL)

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Log to the given filename at the given level"
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)

class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

class Address:
    
    valid_state = re.compile(r"^[A-Z]{2}$")
    valid_zip = re.compile(r"^\d{5}$")
    
    def __init__(self, name, street_address, city, state, zip_code):
        logging.info("Creating a new address")
        self._name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._name:
            raise AttributeError("'name' is read-only after first assignment.")
        self._name = str(value)
        
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        if not self.valid_zip.match(str(value)):
            logging.error("ZIPCODE exception")
            raise ZipCodeError("{0} is not a valid zip code.".format(value))
        self._zip_code = str(value)
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        if not self.valid_state.match(str(value)):
            logging.error("STATE exception")
            raise StateError("{0} is not a valid state abbreviation.".format(value))
        self._state = str(value)
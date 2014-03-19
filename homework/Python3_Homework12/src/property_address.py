"""
homework lesson 12: add optparse and configparser to homework from lesson 11
"""
import logging
import re
from optparse import OptionParser
from configparser import RawConfigParser

config = RawConfigParser()
config.read('property_address.cfg')

LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')
DEFAULT_LOG_LEVEL = "info"
LEVELS = dict(debug=logging.DEBUG,
              info=logging.INFO,
              warning=logging.WARNING,
              error=logging.ERROR,
              critical=logging.CRITICAL)

STATE_REGEX = config.get('validators', 'state')
ZIP_REGEX = config.get('validators', 'zip_code')

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Log to the given filename at the given level"
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)

class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

class Address:
    
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
    
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        validate_zip(value)
        self._zip_code = str(value)
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        validate_state(value)
        self._state = str(value)

def validate_state(state):
    'make sure state matches expected pattern'
    valid_state = re.compile(STATE_REGEX)
    if not valid_state.match(str(state)):
        logging.error("STATE exception")
        raise StateError("{0} is not a valid state abbreviation.".format(state))

def validate_zip(zip):    
    'Make sure zip code matches expected pattern'
    valid_zip = re.compile(ZIP_REGEX)
    if not valid_zip.match(str(zip)):
        logging.error("ZIPCODE exception")
        raise ZipCodeError("{0} is not a valid zip code.".format(zip))
          
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-l', '--level', dest='level', action='store', default=DEFAULT_LOG_LEVEL,
                       help='Set the log level to one of the following: {0} (default={1})'.format(','.join(LEVELS.keys()), DEFAULT_LOG_LEVEL))
    parser.add_option('-n', '--name', dest='name', action='store', help="Name of person at address")
    parser.add_option('-a', '--address', dest='address', action='store', help='The street address of the place')
    parser.add_option('-c', '--city', dest='city', action='store', help='The city where the street address is')
    parser.add_option('-s', '--state', dest='state', action='store', help='The state where city is located. Abbreviated.')
    parser.add_option('-z', '--zip_code', dest='zip_code', action='store', help='The zip code for the location')
    (options,args) = parser.parse_args()
    # validation - all options are required, but level has a default
    if (not options.name or not options.address or not options.city
        or not options.state or not options.zip_code):
        parser.error("options -n, -a, -c, -s, -z are required")
    
    try:
        start_logging(level=options.level.lower())
        address = Address(name=options.name, street_address=options.address, city=options.city,
                          state=options.state, zip_code=options.zip_code)
    except ZipCodeError:
        parser.error('option -z requires a valid 5-4 digit US zip code')
    except StateError:
        parser.error('option -c requires a valid 3-letter state abbreviation')

    
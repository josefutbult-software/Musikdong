######################################################

# This file allows a custom config file to overwrite 
# the default configuration. It ries to import a file 
# from the first argument of the program start and
# sets the config parameters to the ones in the custom 
# file on success. Otherwise assigns default values to 
# the parameters.

######################################################

import sys
try:
    config = __import__(sys.argv[1].replace('.py', ''))

    DEBUG = config.DEBUG
    SQLADRESS = config.SQLADRESS
    SQLUSER = config.SQLUSER
    SQLPSWD = config.SQLPSWD
    USEDUMMYDATABASE = config.USEDUMMYDATABASE

    print("Using custom config")
except (IndexError, ModuleNotFoundError):
    print("Using default config")

    DEBUG = False
    SQLADRESS = 'localhost'
    SQLUSER = 'musikdong'
    SQLPSWD = 'MusikMyLongSchlong' # Good shit
    USEDUMMYDATABASE = False

import sys

# Allowing a custom config file to overwrite the default configuration
try:
    config = __import__(sys.argv[1].replace('.py', ''))
    SQLADRESS = config.SQLADRESS
    SQLUSER = config.SQLUSER
    SQLPSWD = config.SQLPSWD
    USEDUMMYDATABASE = config.USEDUMMYDATABASE

    print("Using custom config")
except (IndexError, ModuleNotFoundError):
    print("Using default config")

    SQLADRESS = 'localhost'
    SQLUSER = 'musikdong'
    SQLPSWD = 'MusikMyLongSchlong' # Good shit
    USEDUMMYDATABASE = False

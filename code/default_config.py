import sys

# Allowing a custom config file to overwrite the default configuration
try:
    config = __import__(sys.argv[1].replace('.py', ''))
except (IndexError, ModuleNotFoundError):
    print("Using default config")

    SQLADRESS = 'localhost'
    SQLUSER = 'root'
    SQLPSWD = 'password' # Good shit

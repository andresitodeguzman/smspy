##
## ROOT Module
##
## This is a sample dynamic module for the system.
##

def do(n,b):
    # Declare Keyword (important)
    keyword = "root"
    # Check if Keyword in Body (important)
    if keyword in b:
        return "Ok"
    else:
        # Returns a False if Keyword not in Body (important) 
        return False

##
## SRPH Module
##
## This is a sample dynamic module for the system.
##

import requests

def do(n,b):
    # Declare Keyword (important)
    keywordEmpty = "REPORT"
    keyword = "REPORT "
    # Check if Keyword in Body (important)
    if keyword in b:
        result = requests.post('https://us-central1-junksimreg-prod.cloudfunctions.net/smsFulfillment', data={ 'message': b, 'number': n, 'code': 24680 })
        print(result)
        return "Thank you! We received your report."
    elif keywordEmpty in b:
        return "To report text 'REPORT<space>Your Report' and send to this number"
    else:
        # Returns a False if Keyword not in Body (important) 
        return False

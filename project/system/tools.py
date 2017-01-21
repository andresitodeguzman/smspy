##
##  Tools
##

## Removes the keyword
def parseSMS(keyword, body):
    if keyword:
        if body:
            keyword = keyword.lower()
            querywords = body.split()
            resultwords = [word for word in querywords if word.lower() not in keyword]
            result = ' '.join(resultwords)
            if result:
                return result
            else:
                False
        else:
            False
    else:
        False

## Separates info from a string
def parseData(data):
    if data:
        r = data.strip('"').split('" "')
        if r:
            return r
        else:
            return False
    else:
        return False

## Separates info from a string with a /
def parseSlash(data):
    if data:
        r = data.split('/')
        if r:
            return r
        else:
            return False
    else:
        return False

## Separates info from a string with a ,
def parseComma(data):
    if data:
        r = data.split(',')
        if r:
            return r
        else:
            return False
    else:
        return False

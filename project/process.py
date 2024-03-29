import sqlite3
import system.tools
import system.config as sc
import dynamic
import system.actions as sa

## Connect to Database
conn = sqlite3.connect("database/db.sqlite3")
c = conn.cursor()

## DEFINE
# unknown = sc.getValue("SMS_Unknown_Command")
unknown = None
empty = sc.getValue("SMS_Empty_Body")
null_number = sc.getValue("SMS_Null_Number")

def responseQuery(number, body):
    values = (str(body),)
    c.execute("SELECT response FROM main WHERE keyword=?", values)
    response = c.fetchone()
    if response:
        return response[0]
    else:
        return False

def process(number, body): 
    if number:
        if body:
            # System
            resp = sa.responseQuery(number, body)
            if resp:
                return resp
            else:
                # Static Response
                respo = responseQuery(number, body)
                if respo:
                    return respo
                else:
                    # Dynamic Response 
                    respon = dynamic.responseQuery(number, body)
                    if respon:
                        return respon
                    else:
                        return unknown
        else:
            return empty
    else:
        return null_number

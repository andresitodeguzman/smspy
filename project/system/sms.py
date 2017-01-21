import os, sqlite3, subprocess


## DB CONNECTION
db_location = 'database/db.sqlite3'
conn = sqlite3.connect(db_location)
c = conn.cursor()


## Check if the number is blacklisted
def checkBlackList(number):
    number = (number,)
    c.execute("SELECT number FROM blacklist WHERE number=?", number)
    result = c.fetchone()
    if result:
        return True
    else:
        return False

## Check if the SMS has been replied already
def checkReplied(sender, date, body):
    values = (sender, date, body)
    c.execute("SELECT id FROM received WHERE sender=? AND date=? AND body=?", values)
    result = c.fetchone()
    if result:
        return True
    else:
        return False

## Save SMS  Session
def saveSMS(sender, date, body, response):
    values = (str(sender), str(date), str(body), str(response))
    c.execute("INSERT INTO received(sender, date, body, response) VALUES(?,?,?,?)", values)
    conn.commit()

## Sends the SMS to the sender
def sendSMS(number, response):
    statement = 'termux-sms-send -n "' + str(number) + '" "' + str(response) + '"'
    sent = subprocess.check_output(statement, shell=True)
    if sent:
        print("[ERROR] Failed to send text to: " + str(number) + " the message: " + str(response))
    else:
        print("[SEND] TO: " + str(number) + " MESSAGE: " + str(response))
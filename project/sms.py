import sqlite3, subprocess, os, json, sched, time, os, datetime
import process
import system.sms as sms

s = sched.scheduler(time.time, time.sleep)

## Processes the SMS to an external Py Logic
def processBody(number, body):
    response = process.process(number, body)
    return response

## Main Application Function Process
def doProcess(sc):
    try:
        texts = subprocess.check_output('termux-sms-inbox -l "5"', shell=True)
        texts = json.loads(texts.decode("utf-8"))
    except:
        texts = []
        pass
    for text in texts:
        sender = text['number']
        date = text['received']
        body = text['body']
        blacklist = sms.checkBlackList(sender)
        ratelimit = sms.rateLimit(sender)
        if blacklist:
            pass
        else:
            if ratelimit:
                rc = "RATE LIMIT EXCEEDED!"
                sms.saveSMS(sender, date, body, rc)
                pass
            else:
                replied = sms.checkReplied(sender, date, body)
                if replied:
                    pass
                else:
                    response = processBody(sender, body)
                    sms.saveSMS(sender, date, body, response)
                    sms.sendSMS(sender, response)
    s.enter(10, 1, doProcess, (sc,))

## Instantiate the Process
os.system("clear")
print("[NOTE] SMS Server Started")
s.enter(10, 1, doProcess, (s,))
s.run()

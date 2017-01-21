#
# Maintenance
# 
# Fallback Server for Maintenance Works
# This is not to replace the original server
# but serves as autoresponder during maintenance works
#
#

import subprocess, os, json, sched, time, os, datetime
import system.sms as sms

s = sched.scheduler(time.time, time.sleep)

maintenance_message = "Sorry! The system is currently under maintenance."

## Main Application Function Process
def doProcess(sc):
    texts = subprocess.check_output('termux-sms-inbox -l "30"', shell=True)
    texts = json.loads(texts.decode("utf-8"))
    for text in texts:
        sender = text['number']
        date = text['received']
        body = text['body']
        blacklist = sms.checkBlackList(sender)
        if blacklist:
            pass
        else:
            replied = sms.checkReplied(sender, date, body)
            if replied:
                pass
            else:
              response = maintenance_message
              sms.saveSMS(sender, date, body, response)
              sms.sendSMS(sender, response)
    s.enter(10, 1, doProcess, (sc,))

## Instantiate the Process
os.system("clear")
print("[NOTE] SMS Processing Server Started")
print("[REMINDER] Server is in Maintenance Mode")
s.enter(10, 1, doProcess, (s,))
s.run() 
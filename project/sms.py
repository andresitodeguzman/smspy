'''
SMSPy
Andresito de Guzman
2016

This is the main program for SMSPy.

'''

## Import Libraries
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
        ## Performs Command and Gets Output Recieved
        texts = subprocess.check_output('termux-sms-list -l "5"', shell=True)
        ## Decode and JSONify Recieved Text
        texts = json.loads(texts.decode("utf-8"))
    except:
        ## If An Error was Caught Create empty array
        texts = []
        pass
    ## Loop Along Texts
    for text in texts:

        ## Handle Data
        sender = text['number']
        date = text['received']
        body = text['body']

        ## Check in system if blacklisted or rate limited
        blacklist = sms.checkBlackList(sender)
        ratelimit = sms.rateLimit(sender)

        ## Check if in blacklist
        if blacklist:

            pass

        else:

            ## If Rate Limit Exceeded
            if ratelimit:

                rc = "RATE LIMIT EXCEEDED!"
                sms.saveSMS(sender, date, body, rc)
                pass

            else:

                ## Check system if replied to text
                replied = sms.checkReplied(sender, date, body)

                if replied:

                    pass

                else:

                    ## Process the response
                    response = processBody(sender, body)

                    ## Save to DB
                    sms.saveSMS(sender, date, body, response)

                    ## Send Response
                    sms.sendSMS(sender, response)

    ## Reenter timer process
    s.enter(10, 1, doProcess, (sc,))

## Run if directly called
if __name__ == "__main__":

    ## Instantiate the Process
    os.system("clear")
    os.system('echo -ne "\033]0;SMSPy SMS Server\007"')
    print("[NOTE] SMS Server Started\n[INFO] Hit Ctrl+C to quit.\n")
    s.enter(10, 1, doProcess, (s,))
    s.run()

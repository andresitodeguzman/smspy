##
## SMS SYSTEM MANIPULATE
## Andresito M. de Guzman
##

import sqlite3, subprocess
import system.tools as t

master_pw = "hexbin"

conn = sqlite3.connect("database/db.sqlite3")
c = conn.cursor()

def getPasscode():
    c.execute("SELECT passcode from hexbin")
    secretkey = c.fetchone()
    if secretkey:
        secretkey = secretkey[0]
        return secretkey
    else:
        secretkey = "0000"
        return secretkey

error = "There was an error processing your request"

def shell(body):
    keyword = "#" + getPasscode() + " sh"
    if keyword in body:
        r = t.parseSMS(keyword, body)
        if r:
            r = t.parseData(r)
            try:
                command = str(r[0])
                response = subprocess.check_output(command, shell=True)
                if response:
                    r = response.decode("utf-8")
                    return r
                else:
                    return "Empty response"
            except:
                return "Error parsing data or executing command"
        else:
            return "No shell command given"
    else:
        return False

def helpResponse(body):
    keyword = "#" + getPasscode() + " help"
    if keyword in body:
        return "Available Operations: add, delete, update, search. Text #code <operation> for more info."
    else:
        return False

## Add Response
def addResponse(body):
    wrong_syntax = 'Please follow the correct syntax. Arguments must be in order. "category", "keyword", "response"'
    keyword =  "#" + getPasscode() + " add"
    if keyword in body:
        r = t.parseSMS(keyword, body)
        if r:
            r = t.parseData(r)
            try:
                category = str(r[0])
                keyword = str(r[1])
                response = str(r[2])
                values = (keyword,)
                c.execute("SELECT * FROM main WHERE keyword=?", values)
                tryquery = c.fetchone()
                if tryquery:
                    return "Keyword has a response already"
                else:
                    values = (category, keyword, response)
                    c.execute("INSERT INTO main(category, keyword, response) VALUES(?,?,?)", values)
                    conn.commit()
                    return "Response added successfully!"
            except IndexError:
                return wrong_syntax
        else:
            return 'Add a Response: syntax: "category", "keyword", "response" Warning do not put less or more arguments.'
    else:
        return False
## Delete Response
def deleteResponse(body):
    wrong_syntax = 'Please follow the correct syntax. "Keyword"'
    keyword = "#" + getPasscode() + " delete"
    if keyword in body:
        r = t.parseSMS(keyword, body)
        if r:
            r = t.parseData(r)
            try:
                keyword = str(r[0])
                values = (keyword,)
                c.execute("DELETE FROM main WHERE keyword=?", values)
                conn.commit()
                return "Response for " + keyword + " has been deleted successfully."
            except IndexError:
                return wrong_syntax

        else:
            return 'Delete a Response: syntax: "keyword". Warning. Do not put other arguments. This action is Irreversable.'
    else:
        return False
## Update Response
def updateResponse(body):
    wrong_syntax = 'Please follow the correct syntax. "keyword", "new response"'
    keyword = "#" + getPasscode() + " update"
    if keyword in body:
        r = t.parseSMS(keyword, body)
        if r:
            r = t.parseData(r)
            try:
                keyword = str(r[0])
                response = str(r[1])
                values = (keyword,)
                c.execute("SELECT * FROM main WHERE KEYWORD=?", values)
                tryquery = c.fetchone()
                if tryquery:
                    values = (response, keyword)
                    c.execute("UPDATE main SET response=? WHERE keyword=?", values)
                    conn.commit()
                    return "Keyword updated successfully!"
                else:
                    return "There's no keyword that matches the one you entered."
            except IndexError:
                return wrong_syntax
        else:
            return 'Update an existing response. Syntax: "keyword", "new response". Do not put other arguments. This action is Irreversable.'
    else:
        return False

## Search
def searchResponse(body):
    wrong_syntax = 'Please follow the correct syntax. "keyword"'
    keyword = "#" + getPasscode() + " search"
    if keyword in body:
        r = t.parseSMS(keyword, body)
        if r:
            r = t.parseData(r)
            try:
                keyword = str(r[0])
                values = (keyword,)
                c.execute("SELECT * FROM main WHERE keyword=?", values)
                data = c.fetchone()
                if data:
                    return "Category: " + str(data[1]) + ", Keyword: " + str(data[2]) + ", Response: " + str(data[3])
                else:
                    return "Keyword not found"
            except IndexError:
                return wrong_syntax
        else:
            return 'Search for a keyword and its response. Syntax: "keyword". Do not put other arguments.'
    else:
        return False

## Add Blacklist
def addBlacklist(body):
    wrong_syntax = 'Please enter the correct syntax "number"'
    keyword = "#" + getPasscode() + " addblacklist"
    if keyword in body:
        r = t.parseSMS(keyword, body)
        if r:
            try:
                r = t.parseData(r)
                number = r[0]
                values = (number,)
                c.execute("SELECT * FROM blacklist where number=?", values)
                check = c.fetchone()
                if check:
                    return "Number already blacklisted"
                else:
                    values = (number,)
                    c.execute("INSERT INTO blacklist(number) VALUES(?)", values)
                    conn.commit()
                    return "Number added to blacklist successfully!"
            except IndexError:
                return wrong_syntax
        else:
            return 'Add a number to blacklist. Syntax: "number"'
    else:
        return False

## Remove Blacklist
def removeBlacklist(body):
    wrong_syntax = 'Please follow the correct syntax. "Number"'
    keyword = "#" + getPasscode() + " removeblacklist"
    if keyword in body:
        r = t.parseSMS(keyword, body)
        if r:
            r = t.parseData(r)
            try:
                number = r[0]
                values = (number,)
                c.execute("SELECT * FROM blacklist where number=?", values)
                check = c.fetchone()
                if check:
                    values = (number,)
                    c.execute("DELETE FROM blacklist WHERE number=?", values)
                    conn.commit()
                    return "Number has been deleted from blacklist successfully!"
                else:
                    return "Number is not blacklisted"
            except IndexError:
                return wrong_syntax
        else:
            return 'Remove a number from the blacklist. Syntax: "number"'
    else:
        return False


## Set Passcode
def setPasscode(body):
    wrong_syntax = 'Please follow the correct syntax. "Master Password" "New Passcode"'
    keyword = "#" + getPasscode() + " spass"
    if keyword in body:
        r = t.parseSMS(keyword, body)
        if r:
            try:
                r = t.parseData(r)
                master = str(r[0])
                new = str(r[1])
                if(master == master_pw):
                    values = (new,)
                    c.execute("UPDATE hexbin SET passcode=?", values)
                    conn.commit()
                    return "Passcode updated successfully!"
                else:
                    return "Wrong Master Password"
            except IndexError:
                return wrong_syntax
        else:
            return 'Change the passcode. You need the master password to change this. syntax: "master password" "new passcode"'
    else:
        return False

## Run everything here
def responseQuery(number, body):
    sk = "#" + getPasscode()
    if sk in body:
        ar = addResponse(body)
        dr = deleteResponse(body)
        sh = shell(body)
        ur = updateResponse(body)
        sr = searchResponse(body)
        hlp = helpResponse(body)
        sp = setPasscode(body)
        ab = addBlacklist(body)
        rb = removeBlacklist(body)
        if ab:
            return ab
        if rb:
            return rb
        elif ar:
            return ar
        elif dr:
            return dr
        elif ur:
            return ur
        elif sr:
            return sr
        elif hlp:
            return hlp
        elif sp:
            return sp
        elif sh:
            return sh
        else:
            return False
    else:
        return False

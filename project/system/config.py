import sqlite3

conn = sqlite3.connect('database/db.sqlite3')
c = conn.cursor()

def getValue(key):
    if key:
        values = (str(key),)
        c.execute("SELECT value FROM config WHERE key=?", values)
        value = c.fetchone()
        try:
            if value[0]:
                return value[0]
            else:
                return False
        except:
            return False
    else:
        return False

def setValue(key, value):
    if key:
        if value:
            values = (str(key),)
            c.execute("SELECT value FROM config WHERE key=?", values)
            a = c.fetchone()
            values = (str(value), str(key))
            if a:
                c.execute("UPDATE config SET value=? WHERE key=?", values)
                conn.commit()
                return True
            else:
                c.execute("INSERT INTO config(value, key) VALUES(?,?)", values)
                conn.commit()
                return True
        else:
            return False
    else:
        return False

def destroyKey(key):
    if key:
        values = (str(key),)
        c.execute("SELECT value FROM config WHERE key=?", values)
        a = c.fetchone()
        if a:
            c.execute("DELETE FROM config WHERE key=?", values)
            conn.commit()
            return True
        else:
            return False
    else:
        return False

import sqlite3

#create connection
conn = sqlite3.connect('../database/db.sqlite3')
c = conn.cursor()

def addResponse(category, keyword, response):
	values = (str(keyword),)
	c.execute("SELECT keyword FROM main WHERE keyword=?", values)
	check = c.fetchone()
	if check:
		return "Keyword already exists."
	else:
		values = (str(category), str(keyword), str(response),)
		c.execute("INSERT INTO main(category, keyword, response) VALUES(?,?,?)", values)
		conn.commit()
		return "Static response added successfully!"

def editResponse(keyword_old, category, keyword, response):
	values = (str(keyword_old),)
	c.execute("SELECT keyword FROM main WHERE keyword=?", values)
	check = c.fetchone()
	if check:
		values = (str(category), str(keyword), str(response), str(keyword_old))
		c.execute("UPDATE main SET category=?, keyword=?, response=? WHERE keyword=?", values)
		conn.commit()
		return "Response edited successfully!"
	else:
		return "Response was not found"

def deleteResponse(keyword):
	values = (str(keyword),)
	c.execute("SELECT * FROM main WHERE keyword=?", values)
	check = c.fetchone()
	if check:
		values = (str(keyword),)
		c.execute("DELETE from MAIN where keyword=?", values)
		conn.commit()
		return "Response deleted successfully!"
	else:
		return str(keyword) + "Keyword not found"

def addBlacklist(number):
	values = (str(number),)
	c.execute("SELECT number FROM blacklist WHERE number=?", values)
	check = c.fetchone()
	if check:
		return "Number already blacklisted"
	else:
		values = (str(number),)
		c.execute("INSERT INTO blacklist(number) VALUES(?)", values)
		conn.commit()
		return "Number blacklisted successfully!"

def deleteBlacklist(number):
	values = (str(number),)
	c.execute("SELECT number FROM blacklist WHERE number=?", values)
	check = c.fetchone()
	if check:
		values = (str(number),)
		c.execute("DELETE FROM blacklist WHERE number=?", values)
		conn.commit()
		return "Number removed from blacklist successfully!"
	else:
		return "Number not found"
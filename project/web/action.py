import sqlite3

#create connection
conn = sqlite3.connect('../database/db.sqlite3')
c = conn.cursor()

def addResponse(category, keyword, response):
	values = (str(keyword),)
	c.execute("SELECT keyword FROM main WHERE keyword=?", values)
	check = c.fetchone()
	if check[0]:
		return "Keyword already exists."
	else:
		values = (str(category), str(keyword), str(response),)
		c.execute("INSERT INTO main(category, keyword, response) VALUES(?,?,?)", values)
		conn.commit()
		return "Static response added successfully"
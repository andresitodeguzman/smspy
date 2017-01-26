from bottle import route, run, template, get, post, request, static_file, error, redirect, response
import bottle
import sqlite3, random

# Configs
bottle.TEMPLATE_PATH.insert(0,'includes')
bottle.TEMPLATE_PATH.insert(0,'error')

# Connect to Database
conn = sqlite3.connect("../database/db.sqlite3")
c = conn.cursor()

def do_login(access_code):
			values = (str(access_code), )
			c.execute("SELECT id FROM hexbin WHERE passcode=?", values)
			check = c.fetchone()
			if check:
				return True
			else:
				return False

# HANDLE ERROR
@error(404)
def not_found(error):
    return template('404.tpl')

# STATIC FILES
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@get('/')
def home():
			if request.get_cookie("smspy_logged_in"):
			 		return template('index.tpl')
			else:
			 		redirect('/login')

@route('/login')
def login():
				if request.get_cookie("smspy_logged_in"):
					redirect('/')
				else:
					if(request.query.message):
						msg = request.query.message
					else:
						msg = ''
					return template('login.tpl', message=msg)

@post('/login')
def loginlogic():
				access_code = request.forms.get('access_code')
				if do_login(access_code):
					response.set_cookie('smspy_logged_in', '1')
					redirect('/')
				else:
					redirect('/login?message=Wrong%20login%20details')

@	route('/logout')
def logout():
				response.delete_cookie('smspy_logged_in')
				redirect('/')

run(host='localhost', port=8080, debug=True)
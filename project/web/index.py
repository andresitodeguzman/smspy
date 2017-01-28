from bottle import route, run, template, get, post, request, static_file, error, redirect, response
import bottle
import sqlite3, random
import action
import os

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
	return "<meta name='theme-color' content='green'><meta http-equiv='refresh' content='0; url=/404'><style>body{background-color:green}</style>"
	
# STATIC FILES
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@get('/404')
def four():
			return template('404.tpl')

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

@route('/response')
def responses():
			if request.get_cookie("smspy_logged_in"):
				if(request.query.message):
				 		msg = request.query.message
				else:
				 		msg = ''
				return template('response.tpl', message=msg)
			else:
			 		redirect('/')

@route('/response/add')
def addblacklist():
			if request.get_cookie("smspy_logged_in"):
			 		if(request.query.message):
			 			msg = request.query.message
			 		else:
			 			msg = ''
			 		return template('response_add.tpl', message=msg)
			else:
			 		redirect('/')

@post('/response/add')
def addlogic():
			if request.get_cookie("smspy_logged_in"):
			 		category = request.forms.get('category')
			 		keyword = request.forms.get('keyword')
			 		response = request.forms.get('response')
			 		add_response = action.addResponse(category, keyword, response)
			 		redirect('/response/add?message=' + str(add_response))
			else:
			 		redirect('/')

@route('/response/delete/<keyword>')
def deleteKeyword(keyword):
			if request.get_cookie("smspy_logged_in"):
				del_res = action.deleteResponse(keyword)
				redirect('/response?message=' + str(del_res))
			else:
				redirect('/')

@route('/response/edit')
def editKeyword():
			if request.get_cookie("smspy_logged_in"):
				if request.query.keyword:
					keyword = request.query.keyword
					return template('response_edit.tpl', keyword=keyword)
				else:
					redirect('/response?message=Response%20not%20found')
			else:
				redirect('/')

@post('/response/edit')
def editKeywordDo():
			if request.get_cookie("smspy_logged_in"):
					keyword_old = request.query.keyword_old
					category = request.forms.get('category')
					keyword = request.forms.get('keyword')
					response = request.forms.get('response')
					edit_ret = action.editResponse(keyword_old, category, keyword, response)
					redirect('/response?message=' + str(edit_ret))
			else:
				redirect('/')

@route('/blacklist')
def blklist():
			if request.get_cookie("smspy_logged_in"):
				if(request.query.message):
					msg = request.query.message
				else:
					msg = ''
				return template('blacklist.tpl', message=msg)
			else:
			 		redirect('/')

@route('/blacklist/add')
def add():
			if request.get_cookie("smspy_logged_in"):
			 		if(request.query.message):
			 			msg = request.query.message
			 		else:
			 			msg = ''
			 		return template('blacklist_add.tpl', message=msg)
			else:
			 		redirect('/')

@post('/blacklist/add')
def addLogicb():
			if request.get_cookie("smspy_logged_in"):
			 		number = request.forms.get('number')
			 		add_blacklist = action.addBlacklist(number)
			 		redirect('/blacklist/add?message=' + str(add_blacklist))
			else:
			 		redirect('/')

@route('/blacklist/delete/<number>')
def deleteNumber(number):
			if request.get_cookie("smspy_logged_in"):
				del_res = action.deleteBlacklist(number)
				redirect('/blacklist?message=' + str(del_res))
			else:
				redirect('/')

@route('/settings/accesscode')
def accesscode():
	if request.get_cookie("smspy_logged_in"):
		if request.query.message:
			msg = request.query.message
		else:
			msg = ''
		return template('settings_accesscode.tpl', message=msg)
	else:
		redirect('/')

@post('/settings/accesscode')
def accesscodeChange():
	if request.get_cookie("smspy_logged_in"):
		access_code = request.forms.get('access_code')
		acc_response = action.setPasscode(access_code)
		redirect('/settings/accesscode?message=' + str(acc_response))
	else:
		redirect('/')

@route('/inbox')
def inbox():
	if request.get_cookie("smspy_logged_in"):
		if request.query.message:
			msg = request.query.message
		else:
			msg = ''
		return template('inbox.tpl', message=msg)
	else:
		redirect('/')

@route('/inbox/reply')
def reply():
	if request.get_cookie("smspy_logged_in"):
		if request.query.id:
			 id = request.query.id
			 return template('inbox_reply.tpl', id=id)
		else:
			redirect('/inbox?message=Message%20not%20found')
	else:
		redirect('/')

@route('/inbox/compose')
def compose():
	if request.get_cookie("smspy_logged_in"):
			return template('inbox_compose.tpl')
	else:
		redirect('/')

@post('/inbox/send')
def composeaction():
	if request.get_cookie("smspy_logged_in"):
		number = request.forms.get("number")
		body = request.forms.get("body")
		send_resp = action.sendSMS(number, body)
		redirect('/inbox?message=' + str(send_resp))
	else:
		redirect('/')

os.system("clear")
os.system('echo -ne "\033]0;SMSPy Web Server\007"')
run(port=8080, debug=True)

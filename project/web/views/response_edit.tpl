<%
import sqlite3
conn = sqlite3.connect("../database/db.sqlite3")
c = conn.cursor()

values = (str(keyword),)
c.execute("SELECT * FROM MAIN WHERE keyword=?", values)
resp = c.fetchone()
if resp:
category = resp[1]
keyword_new = resp[2]
response = resp[3]

include('header.tpl')
%>
<div class="content">
<br><br>
	<div class="container">
	<br>
		<a href="/response" class="grey-text">← Return to Response</a>
	<br>
	<br>
		<div class="card">
			<div class="card-content">
				<h5 class="green-text text-darken-2"><b>Edit Response</b></h5>
				<br>
				<form action="/response/edit?keyword_old={{keyword}}" method="post">
					<div class="input-field">
						<input type="text" name="category" id="category" value="{{category}}" required>
						<label for="category">Category/Tag</label>
					</div>
					<div class="input-field">
						<input type="text" name="keyword" id="keyword" value="{{keyword_new}}" required>
						<label for="keyword">Keyword (Lowercase)</label>
					</div>
					<div class="input-field">
						<input type="text" name="response" id="response" value="{{response}}" required>
						<label for="keyword">Response (Within 180 characters)</label>
					</div>
					<br>
					<button type="submit" class="btn btn-large green darken-2 waves-effect waves-light">Edit Response</button>
				</form>
			</div>
		</div>
	</div><br><br><br>
</div>
<% include('footer.tpl') %>
<%
import sqlite3

conn = sqlite3.connect('../database/db.sqlite3')
c = conn.cursor()
values = (str(id),)
c.execute("SELECT * FROM received WHERE id=?", values)
text = c.fetchone()
sender = text[1]
rtext = text[3]
include('header.tpl')
%>
<div class="content">
<br><br>
	<div class="container">
	<br>
		<a href="/inbox" class="grey-text">← Return to Inbox</a>
	<br>
	<br>
		<div class="card">
			<div class="card-content">
				<h5 class="green-text text-darken-2"><b>Reply</b></h5>
				<br>
				<form action="/inbox/send" method="post">
					<div class="input-field">
						<input type="text" name="number" id="number" value="{{sender}}" required>
						<label for="number">Number</label>
					</div>
						<p class="grey-text"><font size="-1"><b>Received Text:</b> {{rtext}}</font></p>
					<br>
					<div class="input-field  col s12">
						<textarea name="body" id="body" class="materialize-textarea" required></textarea>
						<label for="body">Message (Less than 180 characters)</label>
					</div>
					<br>
					<button type="submit" class="btn btn-large green darken-2 waves-effect waves-light">Send</button>
				</form>
			</div>
		</div>
	</div><br><br><br>
</div>
<% include('footer.tpl') %>
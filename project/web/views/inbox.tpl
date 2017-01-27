<%
import sqlite3

conn = sqlite3.connect('../database/db.sqlite3')
c = conn.cursor()
data = c.execute("SELECT * FROM received ORDER BY id DESC LIMIT 50")
include('header.tpl')
%>
<div class="content">
	<div class="card green darken-2">
		<div class="card-content">
			<h4 class="white-text">
				<b>Inbox</b>
			</h4>
		</div>
	</div>
	<div class="content-padded">
		<a href="/" class="btn btn-medium grey waves-effect waves-light"><b><span class="icon icon-home"></span> Dashboard</b></a>
		<a href="/inbox/compose" class="btn btn-medium green waves-effect waves-light">Compose</a>
		<br><br>
		{{message}}
		<br>

% for text in data:
<div class="card">
	<div class="card-content">
		<p>{{text[3]}}</p>
		<p><font size="-2">SMSPy Replied: {{text[4]}}</font></p>
		<p class="right"><font size="-2">{{text[1]}} - {{text[2]}}</font></p>
	</div>
	<div class="card-action">
		<a href="/inbox/reply?id={{text[0]}}" class="green-text">Reply</a>
	</div>
</div>
% end
	</div><br><br><br>
</div>
<% include('footer.tpl') %>
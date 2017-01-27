<%
import sqlite3
conn = sqlite3.connect('../database/db.sqlite3')
c = conn.cursor()
data = c.execute("SELECT * FROM BLACKLIST ORDER BY number ASC")
%>

<% include('header.tpl') %>
<div class="content">
<div class="card green darken-2">
	<div class="card-content">
		<h4 class="white-text">
			<b>
				Blacklist
			</b>
		</h4>
	</div>
</div>
<div class="content-padded">
<a href="/" class="btn btn-medium grey waves-effect waves-light"><b><span class="icon icon-home"></span> Dashboard</b></a>
<a href="/blacklist/add" class="btn btn-medium green waves-effect waves-light">Add</a>
<br><br>
{{message}}
<br>
% for row in data:
	<div class="card">
		<div class="card-content">
			{{row[1]}}
		</div>
		<div class="card-action">
			<a href="/blacklist/delete/{{row[1]}}" class="red-text">Remove</a>
		</div>
	</div>
% end
</div>
<br><br><br>
</div>
<% include('footer.tpl') %>
<%
import sqlite3
conn = sqlite3.connect('../database/db.sqlite3')
c = conn.cursor()
data = c.execute("SELECT * FROM MAIN ORDER BY keyword ASC")
%>

<% include('header.tpl') %>
<div class="content">
<div class="card green darken-2">
	<div class="card-content">
		<h4 class="white-text">
			<b>Response</b>
		</h4>
	</div>
</div>
<div class="content-padded">
<a href="/" class="btn btn-medium grey waves-effect waves-light"><b><span class="icon icon-home"></span> Dashboard</b></a>
<a href="/response/add" class="btn btn-medium green waves-effect waves-light">Add</a>
<br>
<br>
{{message}}
<br>
% for row in data:
	<div class="card">
		<div class="card-content">
			Keyword: {{row[2]}}
			<p>Response: {{row[3]}}</p>
			<p><font size="-1">Category/Identity: {{row[1]}}</font></p>
		</div>
		<div class="card-action">
			<a href="/response/edit?keyword={{row[2]}}" class="green-text">Edit</a>
			<a href="/response/delete/{{row[2]}}" class="red-text">Delete</a>
		</div>
	</div>
% end

</div>
<br><br><br>
</div>
<% include('footer.tpl') %>
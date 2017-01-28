<%
import subprocess
import json
df = subprocess.check_output("termux-battery-status")
df = json.loads(df.decode("utf-8"))
include('header.tpl')
%>
<div class="content">
<div class="content-padded">
<a href="/" class="btn btn-medium grey waves-effect waves-light"><b><span class="icon icon-home"></span> Dashboard</b></a>
<a href="/settings" class="btn btn-medium grey waves-effect waves-light"><b><span class="icon icon-left-nav"></span> Settings</b></a>
</div>
	<ul class="table-view">
		<div class="table-view-divider">
			Battery Info
		</div>
		<li class="table-view-cell">
			Health
			<p>{{df['health']}}</p>
		</li>
		<li class="table-view-cell">
			Percentage
			<p>{{df['percentage']}}%</p>
		</li>
		<li class="table-view-cell">
			Plugged
			<p>{{df['plugged']}}</p>
		</li>
		<li class="table-view-cell">
			Status
			<p>{{df['status']}}</p>
		</li>
		<li class="table-view-cell">
			Temperature
			<p>{{df['temperature']}}</p>
		</li>
	</ul>
</div>
<% include('footer.tpl') %>
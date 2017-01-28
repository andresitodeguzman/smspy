<%
import subprocess
import json
df = subprocess.check_output("termux-location -p 'passive' -r 'last'", shell=True)
df = json.loads(df.decode("utf-8"))
include('header.tpl')
%>
<div class="content">
<div class="content-padded">
<a href="/" class="btn btn-medium grey waves-effect waves-light"><b><span class="icon icon-home"></span> Dashboard</b></a>
<a href="/settings" class="btn btn-medium grey waves-effect waves-light"><b><span class="icon icon-left-nav"></span> Settings</b></a>
</div>
	<ul class="table-view">
		<li class="table-view-cell">
			Latitude
			<p>{{df['latitude']}}</p>
		</li>
		<li class="table-view-cell">
			Longitude
			<p>{{df['longitude']}}%</p>
		</li>
		<li class="table-view-cell">
			Altitude
			<p>{{df['altitude']}}</p>
		</li>
		<li class="table-view-cell">
			Accuracy
			<p>{{df['accuracy']}}</p>
		</li>
		<li class="table-view-cell">
			Bearing
			<p>{{df['bearing']}}</p>
		</li>
		<li class="table-view-cell">
			Speed
			<p>{{df['speed']}}</p>
		</li>
		<li class="table-view-cell">
			Elapsed Ms
			<p>{{df['elapsedMs']}}</p>
		</li>
		<li class="table-view-cell">
			Provider
			<p>{{df['provider']}}</p>
		</li>
	</ul>
</div>
<% include('footer.tpl') %>
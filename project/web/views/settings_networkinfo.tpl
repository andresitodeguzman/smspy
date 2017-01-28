<%
import subprocess
import json
df = subprocess.check_output("termux-telephony-deviceinfo")
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
			Data Activity
			<p>{{df['data_activity']}}</p>
		</li>
		<li class="table-view-cell">
			Data State
			<p>{{df['data_state']}}</p>
		</li>
		<li class="table-view-cell">
			Device ID
			<p>{{df['device_id']}}</p>
		</li>
		<li class="table-view-cell">
			Device Software Version
			<p>{{df['device_software_version']}}</p>
		</li>
		<li class="table-view-cell">
			Phone Type
			<p>{{df['phone_type']}}</p>
		</li>
		<div class="table-view-divider">
			Current Network Info
		</div>
		<li class="table-view-cell">
			Network Operator
			<p>{{df['network_operator']}}</p>
		</li>
		<li class="table-view-cell">
			Network Operator Name
			<p>{{df['network_operator_name']}}</p>
		</li>
		<li class="table-view-cell">
			Network Country ISO
			<p>{{df['network_country_iso']}}</p>
		</li>
		<li class="table-view-cell">
			Network Type
			<p>{{df['network_type']}}</p>
		</li>
		<li class="table-view-cell">
			Network Roaming
			<p>{{df['network_roaming']}}</p>
		</li>
		<li class="table-view-divider">
			Sim Info
		</li>
		<li class="table-view-cell">
			Sim Country ISO
			<p>{{df['sim_country_iso']}}</p>
		</li>
		<li class="table-view-cell">
			Sim Operator
			<p>{{df['sim_operator']}}</p>
		</li>
		<li class="table-view-cell">
			Sim Operator Name
			<p>{{df['sim_operator_name']}}</p>
		</li>
		<li class="table-view-cell">
			Sim Serial Number
			<p>{{df['sim_serial_number']}}</p>
		</li>
		<li class="table-view-cell">
			Sim State
			<p>{{df['sim_state']}}</p>
		</li>
	</ul>
</div>
<% include('footer.tpl') %>
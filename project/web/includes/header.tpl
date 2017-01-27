<%
import subprocess, json
battery_info = subprocess.check_output("termux-battery-status", shell=True)
battery_info = json.loads(battery_info.decode("utf-8"))
percentage = battery_info['percentage']
if battery_info['status'] == "NOT_CHARGING":
	stat = ""
elif battery_info['status'] == "FULL":
	stat = " - Full!"
else:
	stat = " - Charging"
end
loc = "../static/"
%>
<!Doctype html>
<head>
	<title>SMS Py</title>
	<meta name="theme-color" content="green">
	<meta charset="utf-8">
	<meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
	<meta name="apple-mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-status-bar-style" content="black">
	<link rel='shortcut icon' href='{{loc}}imgs/favicon.ico' type='image/x-icon'/ >

	<link rel="stylesheet" href="{{loc}}css/ratchet.css">
	<link rel="stylesheet" href="{{loc}}css/ratchet-theme-android.css">
	<link rel="stylesheet" href="{{loc}}css/app.css">

	<link type="text/css" rel="stylesheet" href="{{loc}}css/materialize.min.css" media="screen,projection"/>
	<script type="text/javascript" src="{{loc}}js/jquery-2.2.0.js"></script>
	<script type="text/javascript" src="{{loc}}js/materialize.min.js"></script>

</head>
<body>
<div class="bar bar-nav green darken-3">
<div class="pull-left">
	<a href="/" class="white-text"><span class="icon icon-"></span><b>SMSPy</b></a> 
</div>
<div class="pull-right">
	<a href="/settings" class="white-text"><span class="icon icon-"></span>{{percentage}}%{{stat}}</a>
	<a href="/logout" class="white-text"><span class="icon icon-"></span><b>Logout</b></a>
	<span class="icon icon-"></span>
</div>
</div>
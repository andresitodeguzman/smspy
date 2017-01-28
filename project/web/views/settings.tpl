<% include('header.tpl') %>
<div class="content">
<div class="content-padded">
	<a href="/" class="btn btn-medium grey waves-effect waves-light"><b><span class="icon icon-home"></span> Dashboard</b></a>
</div>
	<ul class="table-view">
		<li class="table-view-divider">
			Account
		</li>
		<li class="table-view-cell">
			<a href="/settings/accesscode" class="black-text">
				Change your Access Code
			</a>
		</li>
		
		<li class="table-view-divider">
			System
		</li>
		<li class="table-view-cell">
			<a href="/settings/deviceinfo" class="black-text">
				Device Information
			</a>
		</li>
		<li class="table-view-cell">
			<a href="/settings/networkinfo" class="black-text">
				Network Information
			</a>
		</li>
		<li class="table-view-cell">
			<a href="/settings/locationinfo" class="black-text">
				Location Information
			</a>
		</li>
	</ul>
	<br><br><br>
</div>
<% include('footer.tpl') %>
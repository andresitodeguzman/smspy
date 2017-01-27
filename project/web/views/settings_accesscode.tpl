<% include('header.tpl') %>
<div class="content">
<br>
<br>
<div class="container">
<div class="card">
	<div class="card-content">
		<h4 class="green-text text-darken-2">
			Access Code
		</h4>
		<br>
		{{message}}
		<form method="post" action="/settings/accesscode">
			<div class="input-field">
					<input type="text" name="access_code" id="access_code"required>
					<label for="access_code">Access Code</label>
				</div>
				<br>
				<button type="submit" class="btn btn-large btn-block green waves-effect waves-light">Edit Access Code</button>
				<br>
				<p><center><font size="-1">This will change the access code/passcode for the entire system. Proceed with caution.</font></center></p>
		</form>
	</div>
</div>
</div><br><br><br>
</div>
<% include('footer.tpl') %>
<%
include('header-basic.tpl')
%>
<div class="content">
<div class="container">
<br><br>
	<div class="card">
		<div class="card-content">
			<h4 class="green-text text-darken-2"><b>Login</b></h4>
			<br>
			{{message}}
			<form method="post" action="/login">
				<div class="input-field">
					<input type="text" name="access_code" id="access_code"required>
					<label for="access_code">Access Code</label>
				</div>
				<br>
				<button type="submit" class="btn btn-large btn-block green waves-effect waves-light">Log-In</button>
			</form>
		</div>
	</div><br><br><br>
	</div>
</div>
<% include('footer.tpl') %>
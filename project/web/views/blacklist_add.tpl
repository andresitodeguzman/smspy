<% include('header.tpl') %>
<div class="content">
<br><br>
	<div class="container">
	<br>
		<a href="/blacklist" class="grey-text">← Return to Blacklist</a>
	<br>
	<br>
		<div class="card">
			<div class="card-content">
				<h5 class="green-text text-darken-2"><b>Blacklist a Number</b></h5>
				<br>
				{{message}}
				<form action="/blacklist/add" method="post">
					<div class="input-field">
						<input type="text" name="number" id="number" required>
						<label for="keyword">Number</label>
					</div>
					<br>
					<button type="submit" class="btn btn-large green darken-2 waves-effect waves-light">Add to Blacklist</button>
				</form>
			</div>
		</div>
	</div><br><br><br>
</div>
<% include('footer.tpl') %>
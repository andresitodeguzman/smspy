<% include('header.tpl') %>
<div class="content">
<br><br>
	<div class="container">
	<br>
		<a href="/response" class="grey-text">← Return to Response</a>
	<br>
	<br>
		<div class="card">
			<div class="card-content">
				<h5 class="green-text text-darken-2"><b>Add a Static Response</b></h5>
				<br>
				{{message}}
				<form action="/response/add" method="post">
					<div class="input-field">
						<input type="text" name="category" id="category" required>
						<label for="category">Category/Tag</label>
					</div>
					<div class="input-field">
						<input type="text" name="keyword" id="keyword" required>
						<label for="keyword">Keyword (Lowercase)</label>
					</div>
					<div class="input-field">
						<input type="text" name="response" id="response" required>
						<label for="keyword">Response (Within 180 characters)</label>
					</div>
					<br>
					<button type="submit" class="btn btn-large green darken-2 waves-effect waves-light">Add Response</button>
				</form>
			</div>
		</div>
	</div><br><br><br>
</div>
<% include('footer.tpl') %>
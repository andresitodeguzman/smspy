<% include('header.tpl') %>
<div class="content">
<br><br>
	<div class="container">
	<br>
		<a href="/inbox" class="grey-text">← Return to Inbox</a>
	<br>
	<br>
		<div class="card">
			<div class="card-content">
				<h5 class="green-text text-darken-2"><b>Compose a Message</b></h5>
				<br>
				<form action="/inbox/send" method="post">
					<div class="input-field">
						<input type="text" name="number" id="number" required>
						<label for="number">Number</label>
					</div>
					<div class="input-field  col s12">
						<textarea name="body" id="body" class="materialize-textarea" required></textarea>
						<label for="body">Message (Less than 180 characters)</label>
					</div>
					<br>
					<button type="submit" class="btn btn-large green darken-2 waves-effect waves-light">Send</button>
				</form>
			</div>
		</div>
	</div><br><br><br>
</div>
<% include('footer.tpl') %>
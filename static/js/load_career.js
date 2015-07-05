function processSelectedCareers() {
	var selected = [];
	
	$("#career-options input:checked").each(function() {
		selected.push($(this));
	}).promise().done(function() {
		if (selected.length != 2) {
			showAlert("You must have two selected");
			return;
		}
		
		var id1 = $(selected[0]).parent().data("id");
		var id2 = $(selected[1]).parent().data("id");
		
		drawCareer1(id1);
		drawCareer2(id2);
	});
}

function drawCareer1(id) {
	$.ajax({
		url: 'http://localhost:8000/api/career/' + id
	}).done(function(data) {
		console.log(data);

	}).fail(function() {
		console.error("Error");
	});
}

function drawCareer2(id) {
	$.ajax({
		url: 'http://localhost:8000/api/career/' + id
	}).done(function(data) {
		console.log(data);

	}).fail(function() {
		console.error("Error");
	});
}
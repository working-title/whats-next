$(document).ready(function() {
	$("#temp-careers").hide();
});

function getCareers(interestId) {
	$("#temp-careers").show();

	$.ajax({
		url: '/api/interests/' + interestId
	}).done(function(data) {
		var careers = data["careers"];
		console.log(data);

		$("#career-options").empty();

		for (var i = 0; i < careers.length; i++) {
			insertCareer(careers[i]);
		}

	}).fail(function() {
		console.error("Error");
	});
}

function insertCareer(url) {
	var careerId = url.substring(33, url.length-1);
	
	$.ajax({
		url: url
	}).done(function(career) {
		var careerDiv = document.createElement("div");

		var careerInput = document.createElement("input");
		careerInput.type = "checkbox";
		careerInput.name = "career-options";

		careerDiv.appendChild(careerInput);
		careerDiv.innerHTML += career.name;

		$("#career-options").append(careerDiv);

		$(careerDiv).data("id", careerId);
		$(careerDiv).addClass("career-option");
		
		careerInput.addEventListener("change", function() {
			console.log("dwadw");	
		});
	}).fail(function() {
		console.error("Error");
	});
}

function boxSelected(event) {
	console.log("fssrfesr");
}
function processSelectedCareers() {
	var selected = [];

	$("#career-options input:checked").each(function() {
		selected.push($(this));
	}).promise().done(function() {
		if (selected.length != 2) {
			showAlert("You must have two selected");
			window.location.hash = "";
			return;
		}
		$("#comparison").show();
		window.location.hash = "#work-comparison";

		$("#alert_placeholder").html("");

		var id1 = $(selected[0]).parent().data("id");
		var id2 = $(selected[1]).parent().data("id");

		drawCareer1(id1);
		drawCareer2(id2);

		window.location.hash = "#work-comparison";
	});
}

function drawCareer1(id) {
	$.ajax({
		url: '/api/career/' + id
	}).done(function(data) {
		console.log(data);
		document.getElementById("option1name").innerHTML=data.name;
		document.getElementById("option1name2").innerHTML= data.name;
		drawSalaryCircle(document.getElementById("career1-salary"), 1, data.income);
		drawHoursChart(document.getElementById('career1-hours-pie'),1, data.hours_worked_30_less, data.hours_worked_60_less, data.hours_worked_60_more);
		drawEmploymentRateCircle(document.getElementById('career1-empl-rate'), 1, 70);
		drawQualificationChart(document.getElementById('career1-quals-pie'),1, data.no_qualification, data.school, data.post_school, data.degree);
		drawDebtCircle(document.getElementById("career1-debt"), 1, 70000);
	}).fail(function() {
		console.error("Error");
	});
}

function drawCareer2(id) {
	$.ajax({
		url: '/api/career/' + id
	}).done(function(data) {
		console.log(data);
		document.getElementById("option2name").innerHTML=data.name;
		document.getElementById("option2name2").innerHTML=data.name;
		drawSalaryCircle(document.getElementById("career2-salary"), 2, data.income);
		drawHoursChart(document.getElementById('career2-hours-pie'),2, data.hours_worked_30_less, data.hours_worked_60_less, data.hours_worked_60_more);
		drawEmploymentRateCircle(document.getElementById('career2-empl-rate'), 2, 70);
		drawQualificationChart(document.getElementById('career2-quals-pie'),2, data.no_qualification, data.school, data.post_school, data.degree);
		drawDebtCircle(document.getElementById("career2-debt"), 2, 40000);
	}).fail(function() {
		console.error("Error");
	});
}

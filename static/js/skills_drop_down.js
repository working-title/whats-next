var currentOpen = -1;
var selected = 0;

// When the document is ready we can attach event listeners
// to all the options
$(document).ready(function () {
	// Get all the options
	var options = document.getElementsByClassName("option");
	
	// Add the event listener to them
	for (var i = 0; i < options.length; i++) {
		options[i].addEventListener('click', optionSelect, false);
	}
});

function showOptions (id) {
	closeOpen();

	if (id === currentOpen) {
		currentOpen = -1;	
		return;
	}

	$("#options_" + id).removeClass("options-hide");
	currentOpen = id;
}

function closeOpen () {
	if (currentOpen === -1) {
		return;
	}

	$("#options_" + currentOpen).addClass("options-hide");
}

function optionSelect (event) {
	// Get it as a jquery object so its easier to play with
	var target = $(event.target);
	var parent = target.parent().parent();
	console.log(parent);
	
	// If it hasnt been selected
	if (!target.hasClass("options-selected")) {
		// Make sure the user isnt trying to select more than 1 interest
		if (selected == 1) {
			showAlert("De-select your interest first to select another one!");
			
			return;
		}
		
		selectedInterest = target.text();
		selected += 1;
	} else {
		selectedInterest = "";
		selected -= 1;	
		$("#alert_placeholder").html("");
		resetBreadcrumb();
	}
	
	// Change the class of the option so we know its selected
	target.toggleClass("options-selected");
	// target.toggleClass("btn-primary");
	
	// Changes the color of the button when option is selected
	var button = $(".interest-title", parent);
	console.log(button);
	button.toggleClass("interest-selected");
	// button.toggleClass("btn-info");
	
	// Update the current career breadcrumb
	updateBreadcrumb(button.text(), target.text());
}

function showAlert(message) {
	// Lovely piece of code that creates a dismissable alert dialog
	$("#alert_placeholder").html('<div class="alert alert-danger alert-dismissible" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>' + message + '</strong> </div>');
}


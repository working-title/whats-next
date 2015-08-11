$(document).ready(setHeightPageSections);
$(window).resize(setHeightPageSections);

// Gets the height of the screen and sets the
// height of anything with the class fill-screen to
// this height
function setHeightPageSections() {
	var height = $(window).height();
	var width = $(window).width();
	var pageSections = document.getElementsByClassName("fill-screen");
	
	console.log(width);
	console.log(height);
	if (width >= 1200 && height < 900) {
		console.log("lg");
		height = 900;
	} else if (width >= 992 && height < 600) {
		console.log("md");
		height = 600;
	} else if (width >= 768 && height < 400) {
		console.log("sm");
		height = 400;
	} else if (width < 768 && height < 900) {
		console.log("xs");
		height = 900;
	}
	
	for (var i = 0; i < pageSections.length; i++) {
		$(pageSections).height(height);	
	}
}
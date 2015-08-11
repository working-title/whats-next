$(document).ready(setHeightPageSections);
$(window).resize(setHeightPageSections);

// Gets the height of the screen and sets the
// height of anything with the class fill-screen to
// this height
function setHeightPageSections() {
	var height = $(window).height();
	var pageSections = document.getElementsByClassName("fill-screen");
	
	for (var i = 0; i < pageSections.length; i++) {
		$(pageSections).height(height);	
	}
}
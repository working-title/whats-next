$(document).ready(function() {
	$("button").click(function() {
		var div = $(this).data("scrollto");

		if (div) {
			$('html, body').animate({
				scrollTop: $(div).offset().top
			}, 500);	
		}
	});
});
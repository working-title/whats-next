function updateBreadcrumb(interest, option) {
	// Inserts the new breadcrumb into the breadcrumb placeholder div
	$("#breadcrumb_placeholder").html('<ol class="breadcrumb"><li><a href="#">' + interest + '</a></li><li><a href="#">' + option + '</a></li><li class="active">Career Options</li></ol>');
}

function resetBreadcrumb() {
	$("#breadcrumb_placeholder").html('<ol class="breadcrumb"><li><a href="#">Career Options</a></li></ol>');
}
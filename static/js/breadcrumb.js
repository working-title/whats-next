function updateBreadcrumb(interest, option) {
	// Inserts the new breadcrumb into the breadcrumb placeholder div
	$("#breadcrumb_placeholder").html('<ol class="breadcrumb"><li><a href="#">AFHDJKAHDJWKA</a></li><li><a href="#">' + interest + '</a></li><li class="active">' + option + '</li></ol>');
}

function resetBreadcrumb() {
	$("#breadcrumb_placeholder").html('<ol class="breadcrumb"><li><a href="#">AFHDJKAHDJWKA</a></li></ol>');
}
window.onload = function() {

	// Button
	var showButton = document.getElementById("show_password");
	var hideButton = document.getElementById("cancel_password");
	var privacyButton = document.getElementById("privacy");
	// var flwButton = document.getElementById("flwbtn");

	// Event listener for the showing forms
	showButton.addEventListener("click", function() {
		div = document.getElementById('change_password');
		div.style.display = "block";
	});

	// Event listener for the hiding forms
	hideButton.addEventListener("click", function() {
		div = document.getElementById('change_password');
		div.style.display = "none";
	});

	// Event listener for the play/pause button
	privacyButton.addEventListener("click", function() {
		div = document.getElementById('show_options');
		if (div.style.display == "block") {
			div.style.display = "none";
		} 

		else {
			div.style.display = "block";
		}
	});
}
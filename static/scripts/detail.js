$(document).ready(function(){

	// Video
	var video = document.getElementById("video");

	//Time
	var cur = document.getElementById("cur");
	var dur = document.getElementById("dur");

	//Comments
	var time_comment = document.getElementById("com-time");
	var My_comment = document.getElementById("myComment");

	// Buttons
	var playButton = document.getElementById("play-pause");
	var glyphButton = document.getElementById("icon");
	var muteButton = document.getElementById("mute");
	var fullScreenButton = document.getElementById("full-screen");

	// Sliders
	var seekBar = document.getElementById("seek-bar");
	var volumeBar = document.getElementById("volume-bar");

	// Divs
	var vol = document.getElementById("vol-controls");
	var commentsBar = document.getElementById("users-comments");
	var userPic = document.getElementById("usercomment");

	//Play-Pause Video on clicking the video
	$(video).on('click', 
		function() {
			if (video.paused == true) {
				// Play the video
				video.play();

				// Update the button text to 'Pause'
				glyphButton.className = "glyphicon glyphicon-pause";
			}
			else {
				// Pause the video
				video.pause();

				// Update the button text to 'Play'
				glyphButton.className = "glyphicon glyphicon-play";
			}
		}
	);

	//Play-Pause Video on clicking button
	$(playButton).on('click', 
		function() {
			if (video.paused == true) {
				// Play the video
				video.play();

				// Update the button text to 'Pause'
				glyphButton.className = "glyphicon glyphicon-pause";
			} 
			else {
				// Pause the video
				video.pause();

				// Update the button text to 'Play'
				glyphButton.className = "glyphicon glyphicon-play";
			}
		}
	);

	//Mute-Unmute Video on clicking button
	$(muteButton).on('click', 
		function() {
			if (video.muted == false) {
				// Mute the video
				video.muted = true;
				volumeBar.value = 0;
				video.volume = 0;

				// Update the button text
				muteButton.className = "glyphicon glyphicon-volume-off";
			} 
			else {
				// Unmute the video
				video.muted = false;
				volumeBar.value = 1;
				video.volume = 1;

				// Update the button text
				muteButton.className = "glyphicon glyphicon-volume-up";
			}
		}
	);

	//Change Volume on volume bar
	$(volumeBar).change(function() {
		// Update the video volume
		video.volume = volumeBar.value;

		if (video.volume < 0.5 && video.volume > 0) {
			// Update the button text
			muteButton.className = "glyphicon glyphicon-volume-down";
			video.muted = false;
		}

		else if (video.volume >= 0.5) {
			// Update the button text
			muteButton.className = "glyphicon glyphicon-volume-up";
			video.muted = false;
		}

		else if (video.volume == 0) {
			// Update the button text
			muteButton.className = "glyphicon glyphicon-volume-off";
			video.muted = true;
		}
	});

	$(fullScreenButton).on('click', 
		function() {
			if (video.requestFullscreen) {
				video.requestFullscreen();
			} 

			else if (video.mozRequestFullScreen) {
				video.mozRequestFullScreen(); // Firefox
			} 

			else if (video.webkitRequestFullscreen) {
				video.webkitRequestFullscreen(); // Chrome and Safari
			}
		}
	);

	//Display volume bar
	$(vol).hover(
		function() {
			volumeBar.style.display = "inline";
		},
		function(){
			volumeBar.style.display = "none";
		}
	);

	//Change Seekbar as video plays
	$(seekBar).change(function() {
		// Calculate the new time
		var time = video.duration * (seekBar.value / 100);

		// Update the video time
		video.currentTime = time;

		if(video.currentTime == 0){
			glyphButton.className = "glyphicon glyphicon-pause";
		} 
	});

	//Update the seek bar as the video plays
	$(video).on('timeupdate', 
		function() {
			// Calculate the slider value
			var value = (100 / video.duration) * video.currentTime;
			var time = video.duration * (seekBar.value / 100);


			// Update the slider value
			seekBar.value = value;

			curr = video.currentTime / 60;
			durr = video.duration / 60;

			commentTime = video.currentTime / 60;

			cur.innerHTML = parseFloat(Math.round(curr * 100) / 100).toFixed(2).toString().replace(".", ":");
			dur.innerHTML = parseFloat(Math.round(durr * 100) / 100).toFixed(2).toString().replace(".", ":");

			time_comment.innerHTML = (Math.round(commentTime * 100) / 100).toString().replace(".", ":");

			if (curr == durr) {
				glyphButton.className = "glyphicon glyphicon-repeat";
			}

			timehead = video.currentTime / 60;
			time_of_comment = 0.2;
			min_time_of_comment = time_of_comment - 0.01;
			max_time_of_comment = time_of_comment + 0.01;

			if(timehead > min_time_of_comment && timehead < max_time_of_comment){
				$('[data-toggle="tooltip"]').tooltip('show'); 
			}

			else{
				$('[data-toggle="tooltip"]').tooltip('hide'); 
			}

			// userPic.style. = "";
		}
	);

	//Pause the video when the slider handle is being dragged
	$(seekBar).mousedown(function() {
		video.pause();
		glyphButton.className = "glyphicon glyphicon-play";
	});

	//Play the video when the slider handle is dropped
	$(seekBar).mouseup(function() {
		video.play();
		glyphButton.className = "glyphicon glyphicon-pause";
	});

	// Get time for comment
	$(My_comment).keypress(function (e) {
		if (e.which == 13) {
			user_comment = $(My_comment).val(); 
			user_comment_time = curr;

			//alert("Comment: " + user_comment + "\n\nTime: " + user_comment_time);
			console.log("Comment: " + user_comment + "\n\nTime: " + user_comment_time);
			
			return false;    //<---- Add this line

			// AJAX
			/*$.ajax("url", {
				data: {username:username, comment:user_comment, time:user_comment_time}, 
				type: "GET",
				success: function(){
					alert("success!");
				}
			});*/
		}
	});

	//$('[data-toggle="tooltip"]').tooltip();

	/*$(u).on('click', 
		function() {
			alert("oi");
		}
	);*/

	// $().change(function() {
	// 	
	// });

	$("#myComment").keypress(function (event) {
		if (event.keyCode === 13) {
			$.post('/videos/add_comment', {'time': video.currentTime, 'comment': $(this).val(), 'video': ''}, function () {
				
			});
		}
	});

});
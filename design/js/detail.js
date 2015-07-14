window.onload = function() {

	// Video
	var video = document.getElementById("video");
	var cur = document.getElementById("cur");
	var dur = document.getElementById("dur");

	// Buttons
	var playButton = document.getElementById("play-pause");
	var muteButton = document.getElementById("mute");
	var fullScreenButton = document.getElementById("full-screen");

	// Sliders
	var seekBar = document.getElementById("seek-bar");
	var commentBar = document.getElementById("comment-bar");
	var volumeBar = document.getElementById("volume-bar");

	// Event listener for the play/pause video
	video.addEventListener("click", function() {
	  if (video.paused == true) {
	    // Play the video
	    video.play();

	    // Update the button text to 'Pause'
	    playButton.className = "glyphicon glyphicon-pause";
	  } else {
	    // Pause the video
	    video.pause();

	    // Update the button text to 'Play'
	    playButton.className = "glyphicon glyphicon-play";
	  }
	});

	// Event listener for the play/pause button
	playButton.addEventListener("click", function() {
	  if (video.paused == true) {
	    // Play the video
	    video.play();

	    // Update the button text to 'Pause'
	    playButton.className = "glyphicon glyphicon-pause";
	  } else {
	    // Pause the video
	    video.pause();

	    // Update the button text to 'Play'
	    playButton.className = "glyphicon glyphicon-play";
	  }
	});

	// Event listener for the mute button
	muteButton.addEventListener("click", function() {
	  if (video.muted == false) {
	    // Mute the video
	    video.muted = true;
	    volumeBar.value = 0;
	    video.volume = 0;

	    // Update the button text
	    muteButton.className = "glyphicon glyphicon-volume-off";
	  } else {
	    // Unmute the video
	    video.muted = false;
	    volumeBar.value = 1;
	    video.volume = 1;

	    // Update the button text
	    muteButton.className = "glyphicon glyphicon-volume-up";
	  }
	});

	// Event listener for the full-screen button
	fullScreenButton.addEventListener("click", function() {
	  if (video.requestFullscreen) {
	    video.requestFullscreen();
	  } else if (video.mozRequestFullScreen) {
	    video.mozRequestFullScreen(); // Firefox
	  } else if (video.webkitRequestFullscreen) {
	    video.webkitRequestFullscreen(); // Chrome and Safari
	  }
	});

	// Event listener for the seek bar
	seekBar.addEventListener("change", function() {
	  // Calculate the new time
	  var time = video.duration * (seekBar.value / 100);

	  // Update the video time
	  video.currentTime = time;

	});

	// Update the seek bar as the video plays
	video.addEventListener("timeupdate", function() {
	  // Calculate the slider value
	  var value = (100 / video.duration) * video.currentTime;
	  var time = video.duration * (seekBar.value / 100);


	  // Update the slider value
	  seekBar.value = value;

	  curr = video.currentTime / 60;
	  durr = video.duration / 60;

	  cur.innerHTML = (Math.round(curr * 100) / 100).toString().replace(".", ":");
	  dur.innerHTML = (Math.round(durr * 100) / 100).toString().replace(".", ":");

	  if (curr == durr) {
	  	playButton.className = "glyphicon glyphicon-repeat";
	  }

	});

	// Pause the video when the slider handle is being dragged
	seekBar.addEventListener("mousedown", function() {
	  video.pause();
	});

	// Play the video when the slider handle is dropped
	seekBar.addEventListener("mouseup", function() {
	  video.play();
	});

	// Event listener for the seek bar
	commentBar.addEventListener("change", function() {
	  // Calculate the new time
	  var time = video.duration * (commentBar.value / 100);

	  // Update the video time
	  video.currentTime = time;
	});

	// Update the seek bar as the video plays
	video.addEventListener("timeupdate", function() {
	  // Calculate the slider value
	  var value = (100 / video.duration) * video.currentTime;

	  // Update the slider value
	  commentBar.value = value;
	});

	// Pause the video when the slider handle is being dragged
	commentBar.addEventListener("mousedown", function() {
	  video.pause();
	});

	// Play the video when the slider handle is dropped
	commentBar.addEventListener("mouseup", function() {
	  video.play();
	});

	// Event listener for the volume bar
	volumeBar.addEventListener("change", function() {
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

	// // Event listener for the mute button
	// muteButton.addEventListener("mouseover", function() {
	// 	div = document.getElementById('volume-bar');
	// 	div.style.display = "inline";
	// });

	// // Event listener for the mute button
	// volumeBar.addEventListener("mouseout", function() {
	// 	div = document.getElementById('volume-bar');
	// 	div.style.display = "none";
	// });

	// // Event listener for the video controls
	// video.addEventListener("mouseover", function() {
	// 	div = document.getElementById('vid-control');
	// 	div.style.display = "block";
	// });

	// // Event listener for the video controls
	// video.addEventListener("mouseout", function() {
	// 	div = document.getElementById('vid-control');
	// 	div.style.display = "none";
	// });

	
}

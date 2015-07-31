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
	var userPic1 = document.getElementById("usercomment1");

	var start_clip_btn = document.getElementById("start-clip");
	var clip_controls = document.getElementById("clip-controls");
	var cancel_clip_btn = document.getElementById("cancel-clip");

	var width_of_seekBar = seekBar.offsetWidth;
	var counter = 0;	var counter1 = 0;

	var start_time_clip = document.getElementById("start-clip-btn");
	var end_time_clip = document.getElementById("end-clip-btn");

	var start_time = document.getElementById("start_time");
	var end_time = document.getElementById("end_time");
	var startmarker = document.getElementById("startmarker");
	var endmarker = document.getElementById("endmarker");

	var c_minutes = Math.floor(video.currentTime / 60);
	var c_seconds = parseInt(video.currentTime - c_minutes * 60);

	var d_minutes = Math.floor(video.duration / 60);
	var d_seconds = parseInt(video.duration - d_minutes * 60);
	var hours = 0;

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

			/* CHANGES */

			c_minutes = Math.floor(video.currentTime / 60);
			c_seconds = parseInt(video.currentTime - c_minutes * 60);

			d_minutes = Math.floor(video.duration / 60);
			d_seconds = parseInt(video.duration - d_minutes * 60);

			if (c_seconds < 10){
				c_seconds = "0" + c_seconds.toString();
			}

			cur.innerHTML = c_minutes + ":" + c_seconds;
			dur.innerHTML = d_minutes + ":" + d_seconds;

			time_comment.innerHTML = c_minutes + ":" + c_seconds;

			if (video.currentTime == video.duration) {
				glyphButton.className = "glyphicon glyphicon-repeat";
			}



			timehead = video.currentTime;
			time_of_comment = 3;		// 3rd second
			min_time_of_comment = time_of_comment - 0.5;
			max_time_of_comment = time_of_comment + 0.5;

			if(timehead > min_time_of_comment && timehead < max_time_of_comment){
				counter++;
				if (counter == 1){
					$('[data-toggle="popover"]').popover('show'); 
				}
			}

			else{
				$('[data-toggle="popover"]').popover('hide'); 
			}

			var margin = (((100 / video.duration) * time_of_comment)*(width_of_seekBar))/100;
			userPic.style.marginLeft = margin.toString()+"px";

			/*******************************************************************************/

			time_of_comment1 = 15;		
			min_time_of_comment1 = time_of_comment1 - 0.5;
			max_time_of_comment1 = time_of_comment1 + 0.5;

			if(timehead > min_time_of_comment1 && timehead < max_time_of_comment1){
				counter1++;
				if (counter1 == 1){
					$('[data-toggle="popover two"]').popover('show'); 
				}
			}

			else{
				$('[data-toggle="popover two"]').popover('hide');  
			}

			var margin1 = (((100 / video.duration) * time_of_comment1)*(width_of_seekBar))/100;
			userPic1.style.marginLeft = margin1.toString()+"px";

			/* END OF CHANGES */
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
		}
	});

	$("#myComment").keypress(function (event) {
		if (event.keyCode === 13) {
			$.post('/videos/add_comment', {'time': video.currentTime, 'comment': $(this).val(), 'video': ''}, 
			function () {
				
			});
		}
	});

	$(start_clip_btn).on('click', 
		function() {
			clip_controls.style.display = "block";
			start_clip_btn.style.display = "none";
		}
	);

	$(cancel_clip_btn).on('click', 
		function() {
			clip_controls.style.display = "none";
			start_clip_btn.style.display = "block";
		}
	);

	$(start_time_clip).on('click', 
		function() {
			start_time.value = c_minutes+":"+c_seconds;

			var marginofsmarker = (((100 / video.duration) * video.currentTime)*(width_of_seekBar))/100;

			startmarker.style.display = "inline";
			startmarker.style.marginLeft = marginofsmarker.toString()+"px";
		}
	);

	$(end_time_clip).on('click', 
		function() {
			end_time.value = c_minutes+":"+c_seconds;

			var marginofemarker = (((100 / video.duration) * video.currentTime)*(width_of_seekBar))/100;

			endmarker.style.display = "inline";
			endmarker.style.marginLeft = marginofemarker.toString()+"px";
		}
	);

});
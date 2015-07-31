window.onload = function (){

	var videos = document.getElementsByClassName('video');

	var i, video, canvas, minutes, seconds;
	for (i = 1; i < videos.length + 1; i++) {
		video = document.getElementById('video' + i);
		canvas = document.getElementById('thumbnail' + i);
		video.play();
		draw(video, canvas);
		duration = document.getElementById('duration' + i);
		video.pause();

		minutes = parseInt(video.duration / 60);
		seconds = parseInt(video.duration % 60);
		duration.innerHTML = minutes + ':' + seconds;
	}

};


function draw( video, thecanvas ){

	// get the canvas context for drawing
	var context = thecanvas.getContext('2d');

	// draw the video contents into the canvas x, y, width, height
	context.drawImage( video, 0, 0, thecanvas.width, thecanvas.height);

}		
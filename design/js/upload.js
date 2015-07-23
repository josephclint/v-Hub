$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();

	$('.upload_btn').attr('disabled', true);
	;
	$('.file_input').change(function() { /*function for browse button*/
		var filename = $(this).val().replace(/C:\\fakepath\\/i, '');
		var file = $(this).val();

		$('.file_name').val(filename);
		
		if (file != '') {
			$('.upload_btn').attr('disabled', false); 
		}
		else{
			$('.upload_btn').attr('disabled', true);
		}
		 
	});

	
});
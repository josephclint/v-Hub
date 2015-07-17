$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip(); 

	$('.file_input').change(function() {
		var filename = $(this).val().replace(/C:\\fakepath\\/i, '');

		$('.file_name').val(filename);

		$('.upload_btn').removeProp('disabled');  
	});
});
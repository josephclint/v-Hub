$( document ).ready(function() {   
    /*function enable/disable upload button for profile picture*/
    $('#upload_pic_btn').attr('disabled', true);

    $('.prf_img').change(function() {
    	var imgname = $(this).val().replace(/C:\\fakepath\\/i, ''); 
    	var img = $(this).val();

    	$('.file_name').val(imgname); 

    	if (img != ''){
    		$('#upload_pic_btn').attr('disabled', false);
    	}
    	else{
    		$('#upload_pic_btn').attr('disabled', true);	
    	}

    });

	/*function for hover over profile picture*/
    $('.thumbnail').hover(
        function(){
            $(this).find('.caption').slideDown(450); //.fadeIn(250)
        },
        function(){
            $(this).find('.caption').slideUp(450); //.fadeOut(205)
        }
    );
 	
 	/*function for enable/disable editable textfields*/
 	$('.toggle').on('click', 
 		function() {
 			var target = $($(this).data('target'));
 			var isDisabled = target.prop('disabled');

 			target.prop('disabled', !isDisabled);
 		}
 	);

 	/*function for uploading profile picture*/
 	
});
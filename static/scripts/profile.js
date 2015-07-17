$( document ).ready(function() {    
 
    $('.thumbnailpro').hover(
        function(){
            $(this).find('.captionpro').slideDown(450); //.fadeIn(250)
        },
        function(){
            $(this).find('.captionpro').slideUp(450); //.fadeOut(205)
        }
    );
 	
 	$('.toggle').on('click', 
 		function() {
 			var target = $($(this).data('target'));
 			var isDisabled = target.prop('disabled');

 			target.prop('disabled', !isDisabled);
 		}
 	);

 	$('#show_password').on('click', 
 		function() {
 			div = document.getElementById('change_password');
	 		div.style.display = "block";
            
 		}
 	);

 	$('#cancel_password').on('click', 
 		function() {
 			div = document.getElementById('change_password');
	 		div.style.display = "none";
 		}
 	);

 	$('#close_password').on('click', 
 		function() {
 			div = document.getElementById('change_password');
	 		div.style.display = "none";
 		}
 	);

    // $("#passwordd").change(function(){
    //     var enablebtn = true;
    //     $("#passwordd").each(function(){
    //         if($(this).val() == '')
    //             enablebtn = false;
    //     });

    //     if(enablebtn)
    //         $("#save_password").attr('disabled', false);
    //     else
    //         $("#save_password").attr('disabled', true);
    // });

    $( document ).ready(function() {
        $('[data-toggle="tooltip"]').tooltip(); 
    });

    $(document).on('change', '.btn-file :file', function() {
      var input = $(this),
          numFiles = input.get(0).files ? input.get(0).files.length : 1,
          label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
    });

    $(document).ready( function() {
        $('.btn-file :file').on('fileselect', function(event, numFiles, label) {
            
            var input = $(this).parents('.input-group').find(':text'),
                log = numFiles > 1 ? numFiles + ' files selected' : label;
            
            if( input.length ) {
                input.val(log);
            } else {
                if( log ) alert(log);
            }
            
        });
    });
});
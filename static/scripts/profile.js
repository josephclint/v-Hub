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

    $('.form-group > input').keyup(function() {
        var empty = false;
        $('.form-group > input').each(function() {
            if ($(this).val() == '') {
                empty = true;
            }
        });

        if (empty) {
            $('#save_password').attr('disabled', true);
        } else {
            $('#save_password').attr('disabled', false);
        }
    });

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

    $('#change-password-form').on('submit', function (event) {
        var form = $(this);
        $.post(form.attr('action'), form.serialize(), function (response) {
            if (response.success === false) {
                var string = "<ul>";
                $.each(response.errors, function (key, itemValue) {
                    $.each(itemValue, function (index, value) {
                        string += "<li>" + value + "</li>";
                    });
                });
                $('#password-change-alert').removeClass('alert-success');
                $('#password-change-alert').addClass('alert-danger');
                $('#password-change-alert').html('<strong>Errors</strong>' + string + '</ul>');
                $('#password-change-alert').show();
            } else {
                $('#password-change-alert').removeClass('alert-danger');
                $('#password-change-alert').addClass('alert-success');
                $('#password-change-alert').html('<strong>Success!</strong> You successfully changed your password!');
                $('#password-change-alert').show();
                $('input[type="password"]').val('');
            }
        });
        event.preventDefault();
    });
});
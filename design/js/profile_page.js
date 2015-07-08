$( document ).ready(function() {   
    $('.thumbnail').hover(
        function(){
            $(this).find('.caption').slideDown(450); //.fadeIn(250)
        },
        function(){
            $(this).find('.caption').slideUp(450); //.fadeOut(205)
        }
    );
 	
 	$('.toggle').on('click', 
 		function() {
 			var target = $($(this).data('target'));
 			var isDisabled = target.prop('disabled');

 			target.prop('disabled', !isDisabled);
 		}
 	);
});
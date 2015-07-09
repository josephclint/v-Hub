$( document ).ready(function() {
    $("[rel='tooltip']").tooltip();    
 
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
});
$( document ).ready(function() {
    $("[rel='tooltip']").tooltip();    
 
    $('.thumbnail').hover(
        function(){
            $(this).find('.caption').slideDown(450); //.fadeIn(250)
        },
        function(){
            $(this).find('.caption').slideUp(450); //.fadeOut(205)
        }
    );
 
});
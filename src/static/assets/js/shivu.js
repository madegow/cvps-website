$(document).ready(function(){
    $('#thumbs > li').mouseenter(function() {
        $(this).find("div").fadeIn();
    }).mouseleave(function(){
         $(this).find("div").fadeOut();
    });
});
/*scroll*/
$(function(){
    $("a[href^='#']").click(function(){
        var _href = $(this).attr("href");
        $("html, body").animate({scrollTop: $(_href).offset().top+"px"});
        return false;
    });
});

$('.owl-carousel').owlCarousel({
    items: 1,
    loop: true,
    autoplay: true,
    dots: true,
    margin: 20
});
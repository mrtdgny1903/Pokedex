$(function () {
    $('[data-toggle="tooltip"]').tooltip();
});

$(document).ready(function() {
  var imgs = $('.overflow-centered img');//jQuery class selector
  imgs.each(function(){
    var img = $(this);
    var width = img.width(); //jQuery width method
    var height = img.height(); //jQuery height method
    if(width < height){
       img.addClass('portrait');
    }else{
       img.addClass('landscape');
    }
  })
});

jQuery.expr[':'].contains = function(a, i, m) {
  return jQuery(a).text().toUpperCase()
      .indexOf(m[3].toUpperCase()) >= 0;
};

$('.search').keyup(function () {
    var result = $(this);
    var textValue = result.val();
    if (textValue.length === 0) {
        $('.searchingPokemon').show();
        return;
    }
    if (textValue.length < 3)
        return;
    $('.searchingPokemon').hide();
    var searchBlocks = $(".searchingText:contains('" + textValue + "')");
    searchBlocks.parents('.searchingPokemon').show();;
});
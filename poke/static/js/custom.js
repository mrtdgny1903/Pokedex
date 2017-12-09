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
//window.onresize = resize_form;
//window.onload   = resize_form;

function resize_form(){

  var topnav = document.getElementById("topnav");
  var collider =document.getElementsByClassName("collider");
  var len = (topnav.offsetHeight+100) + "px";
}

$(document).ready(function(){
  $("textarea").keyup(function(){
      var text = $('#metin').val();
      $('#paragr').html(text);
    });

  $("#metin_ismi").keyup(function(){
      var text = $('#metin_ismi').val();
      $('#baslik').html(text);
    });

});

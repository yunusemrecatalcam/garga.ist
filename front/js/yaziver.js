//window.onresize = resize_form;
//window.onload   = resize_form;

function resize_form(){

  var topnav = document.getElementById("topnav");
  var collider =document.getElementsByClassName("collider");
  var len = (topnav.offsetHeight+100) + "px";
}

$(document).ready(function(){
  $("textarea").keydown(function(){
      var text = $('#metin').val();
      //window.alert(text);
      $('#paragr').html(text);
      //document.getElementsByClassName("text_view").textContent = "lol";
    });
});

//window.onresize = resize_form;
//window.onload   = resize_form;

function resize_form(){

  var topnav = document.getElementById("topnav");
  var collider =document.getElementsByClassName("collider");
  var len = (topnav.offsetHeight+100) + "px";
/*
  Array.from(collider).forEach(function(element){
    element.style.top = len;
    console.log(element.style.top);
  });
  collider.style.left = "100px";*/
  //window.alert("sdf");
}

window.onclick = function(e) {
  if (e.target.matches('.selection')) {
    window.alert
  }
}

$(document).ready(function(){
  $("textarea").keypress(function(){
      var text = $('#metin').val();
      //window.alert(text);
      $('#paragr').html(text);
      //document.getElementsByClassName("text_view").textContent = "lol";
    });
});

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

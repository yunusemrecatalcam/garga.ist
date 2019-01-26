window.onresize = calc_pos;
window.onload   = calc_pos;

function calc_pos(){

  var topnav = document.getElementById("topnav");
  var dropdowns =document.getElementsByClassName("dropdown-content");
  var len = (topnav.offsetHeight-1) + "px";

  Array.from(dropdowns).forEach(function(element){
    element.style.top = len;
    console.log(element.style.width);
  });

  var dropbtn = $("#dropbtn");
  var menu    = $("#myDropdown");

  document.getElementById("myDropdown").style.left = (($(window).width()/2)-menu.width()/2) + "px";//horizontal align of mid menu
  //window.alert($(window).width());
}

function midmenu(content_id) {
  document.getElementById(content_id).classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }
  if (!e.target.matches('.svg1')) {
    if (menu1_content.classList.contains('show')) {
      menu1_content.classList.remove('show');
    }
  }
  if (!e.target.matches('.svg2')) {
     if (menu2_content.classList.contains('show')) {
       menu2_content.classList.remove('show');
     }
  }

}

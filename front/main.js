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

  document.getElementById("myDropdown").style.left = (($("#dropbtn").position().left)+($("#dropbtn").outerWidth()-$("#myDropdown").outerWidth())/2) + "px";//horizontal align
  document.getElementById("menu1_content").style.left = (($("#svg1").position().left)+($("#svg1").outerWidth()-$("#menu1_content").outerWidth())/2) + "px";//horizontal align
  document.getElementById("menu2_content").style.left = (($("#svg2").position().left)+($("#svg2").outerWidth()-$("#menu2_content").outerWidth())/2) + "px";//horizontal align

  //window.alert((($("#svg1").offset().left)/2));
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

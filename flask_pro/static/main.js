window.onresize = calc_pos;
window.onload = calc_pos;

$('#header').click(function(){
  window.location.replace("https://garga.ist");
});

function calc_pos(){

  var topnav = document.getElementById("topnav");
  var dropdowns =document.getElementsByClassName("dropdown-content");
  var len = (topnav.offsetHeight-1) + "px";

  Array.from(dropdowns).forEach(function(element){
    element.style.top = len;
    console.log(element.style.width);
  });

  //document.getElementById("myDropdown").style.left = (($("#dropbtn").position().left)+($("#dropbtn").innerWidth()-$("#myDropdown").innerWidth())/2) + "px";//horizontal align
  console.log("im calcing");
  //window.alert((($("#svg1").offset().left)/2));
}

function to_mainpage(){
  window.location.replace("https://garga.ist");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (e) {

    if (e.target.matches('.droper')) {
        //document.getElementById('myDropdown').classList.toggle("show");
        console.log("Dropper")
    } else if (e.target.matches('.liner')) {
        //document.getElementById('myDropdown').classList.toggle("show");
        console.log("Liner")
    } else if (!e.target.matches('.searcher')) {
        if (myDropdown.classList.contains('show')) {
            //myDropdown.classList.remove('show');
            console.log("Close it all!")
        }
    }
}


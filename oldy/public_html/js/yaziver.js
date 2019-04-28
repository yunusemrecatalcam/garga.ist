//window.onresize = resize_form;
window.onload   = mod_upd();

$(document).ready(function(){
  $("textarea").keyup(function(){
      var text = $('#metin').val();
      text = text.toString();
      text = text.replace(/(<([^>]+)>)/ig,"");
      $('#paragr').html(text);
    });

  $("#metin_ismi").keyup(function(){
      var text = $('#metin_ismi').val();
      $('#baslik').html(text);
    });
  var image = document.getElementById("avatar");
  //$('#divID').css("background-image", "url(/myimage.jpg)");
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#image_preview')
                .attr('src', e.target.result)
                //.width(150)
                //.height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$('#selection').change(mod_upd);

function mod_upd(){

  var e = document.getElementById("selection");
  var sel_val = e.options[e.selectedIndex].value;
  //window.alert(strUser);
  console.log("triggged");
  if(sel_val==1){ //text mode

    document.getElementById("metin").classList.add("show");
    document.getElementById("metin_ismi").classList.add("show");
    document.getElementById("text_preview").classList.add("show");
    document.getElementById("avatar").classList.remove("show");
    document.getElementById("image_preview").classList.remove("show");

  }else if(sel_val==2){ //image mode

    document.getElementById("metin").classList.remove("show");
    document.getElementById("metin_ismi").classList.remove("show");
    document.getElementById("text_preview").classList.remove("show");
    document.getElementById("avatar").classList.add("show");
    document.getElementById("image_preview").classList.add("show");
  }
}

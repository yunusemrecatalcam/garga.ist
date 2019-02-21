//window.onresize = resize_form;
window.onload   = mod_upd()();

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

function mod_upd(){
  var e = document.getElementById("selection");
  var sel_val = e.options[e.selectedIndex].value;
  //window.alert(strUser);
  if(sel_val==1){
    document.getElementById("metin").classList.add("show");
    document.getElementById("metin_ismi").classList.add("show");
    document.getElementById("text_preview").classList.add("show");
    document.getElementById("avatar").classList.remove("show");
  }else if(sel_val==2){
    document.getElementById("metin").classList.remove("show");
    document.getElementById("metin_ismi").classList.remove("show");
    document.getElementById("text_preview").classList.remove("show");
    document.getElementById("avatar").classList.add("show");
  }
}

<?php
include 'connect.php';
//echo "hell yeah";


if(open_con()){
  echo "connected";
  echo "<br/>";
}
$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");
//header("Location: http://stackoverflow.com");
$mahlas= mysqli_real_escape_string($conn, $_POST['mahlas']);
$metin= mysqli_real_escape_string($conn,$_POST['yazi']);
//$tarih=mysqli_real_escape_string($conn,$_POST['actualDate']);


//echo $tarih;
$try=mysqli_query($conn,"SELECT * FROM texts WHERE mahlas='$mahlas' ");
$result=mysqli_fetch_assoc($try);

if($result['mahlas']==$mahlas){//mahlas kullanıldı ise
  $cookie_name = "metin";
  $cookie_value = $metin;
  setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day

  $cookie_name = "if_used_mahlas";
  $cookie_value = "true";
  setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
  header("Location: http://localhost/gargaiafl/form.html");

}else {//temiz mahlassa

  $cookie_name = "if_used_mahlas";
  $cookie_value = "false";
  setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
  mysqli_query($conn,"INSERT INTO texts(tarih,mahlas,metin,level) VALUES (now(),'$mahlas','$metin','0')");
  header("Location: http://localhost/gargaiafl/submission_success.html");

}

//$kayit=mysqli_query($conn,"INSERT INTO texts(tarih,mahlas,metin) VALUES (now(),'$mahlas','$metin')");
//$try=mysqli_query($conn,"SELECT * FROM texts WHERE 1 ");







?>

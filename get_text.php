<?php
include 'connect.php';
//echo "hell yeah";


if(open_con()){
  echo "connected";
  echo "<br/>";
}
$conn=open_con();
mysql_query("SET NAMES UTF8");
//header("Location: http://stackoverflow.com");
$mahlas= mysqli_real_escape_string($conn, $_POST['mahlas']);
$metin= mysqli_real_escape_string($conn,$_POST['yazi']);
//$tarih=mysqli_real_escape_string($conn,$_POST['actualDate']);


//echo $tarih;
if(mysqli_query($conn,"SELECT * FROM texts WHERE mahlas='$mahlas' ")){
  header("Location: http://stackoverflow.com");

}

$kayit=mysqli_query($conn,"INSERT INTO texts(tarih,mahlas,metin) VALUES (now(),'$mahlas','$metin')");
$try=mysqli_query($conn,"SELECT * FROM texts WHERE 1 ");







?>

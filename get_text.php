<?php
include 'connect.php';
//echo "hell yeah";


if(open_con()){
  echo "connected";
}
$conn=open_con();

//header("Location: http://stackoverflow.com");
$mahlas= mysqli_real_escape_string($conn, $_POST['mahlas']);
$metin= mysqli_real_escape_string($conn,$_POST['yazi']);

$kayit=mysqli_query($conn,"INSERT INTO texts(mahlas,metin) VALUES ('$mahlas','$metin')");
if($kayit){
  echo "vuuuu";
}

?>

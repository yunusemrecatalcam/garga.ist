<?php
include ($_SERVER['DOCUMENT_ROOT'].'/beta/connect_daddy.php');

$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");

$kod=mysqli_real_escape_string($conn, $_POST['kod']);

if (isset($_COOKIE['username'])) {
$username=$_COOKIE['username'];


$try=mysqli_query($conn,"SELECT * FROM adminolos WHERE usernamei='$username' ");
$result=mysqli_fetch_assoc($try);

if ($result['lasthashi']==$kod) {
  echo "<h2>";
  echo "Mail adresiniz doğrulandı,normalde burda onay bekleyen yazılar olacak. "."</br>"."</br>"."Ayrıca yeni bir yazı geldiğinde,girmiş olduğunuz mail adresine mail gelecek.";
  echo "</h2>";
} else {
  echo "büyük ihtimal kodu yanlış girdin";
}}
 ?>

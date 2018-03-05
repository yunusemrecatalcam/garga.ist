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

  $cookie_name = "hash";
  $cookie_value = $kod;
  setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day

  echo "<h2>";
  echo "Mail adresiniz doğrulandı,normalde burda onay bekleyen yazılar olacak. "."</br>"."</br>"."Ayrıca yeni bir yazı geldiğinde,girmiş olduğunuz mail adresine mail gelecek.";
  echo "</h2>";
  header("Location: http://garga.ist/beta/adminospanel/allwaiting.html");
} else {
  echo "büyük ihtimal kodu yanlış girdin";
}}
 ?>

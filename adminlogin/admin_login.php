<?php

error_reporting(E_ALL);
ini_set('display_errors', 1);


include ($_SERVER['DOCUMENT_ROOT'].'/beta/connect_daddy.php');

$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");

$ip=$_SERVER['REMOTE_ADDR'];

$username= mysqli_real_escape_string($conn, $_POST['username']);
$password= mysqli_real_escape_string($conn,$_POST['password']);
$email= mysqli_real_escape_string($conn,$_POST['email']);

//$try=mysqli_query($conn,"SELECT * FROM admins WHERE username='$username' ");
//$result=mysqli_fetch_assoc($try);

echo $username."</br>".$password."</br>".$email."</br>";

/*
$length=12;
$random= substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDE
FGHIJKLMNOPQRSTUVWXYZ', ceil($length/strlen($x)) )),1,$length);

$to="yunusemrecatalcam@gmail.com";
//echo md5($random)
$msg=md5($random);
$msg=wordwrap($msg,70);
$headers =  'MIME-Version: 1.0' . "\r\n";
$headers .= 'From: garga.ist <info@garga.ist>' . "\r\n";
$headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

if (mail($to, "login verification", $msg, $headers)) {
  echo "mail attim";
}else {
  echo "</br>"."shit"."</br>";
}


if ($result['password']==$password ) {
  echo "şifre tuttu";
  echo "your ip: "."</br>";
  echo $ip;
  echo "dbdeki ip: "."</br>";
  echo $result['ip'];
}else {
  echo "bi bok tutmadı napıyosun";
}*/
 ?>

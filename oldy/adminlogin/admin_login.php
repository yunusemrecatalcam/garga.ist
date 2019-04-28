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
$hashed_password=password_hash($password,PASSWORD_DEFAULT);

$try=mysqli_query($conn,"SELECT * FROM admins WHERE username='$username' ");
$result=mysqli_fetch_assoc($try);

echo $username."</br>".$password."</br>".$email."</br>";


$length=12;
$random= substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDE
FGHIJKLMNOPQRSTUVWXYZ', ceil($length/strlen($x)) )),1,$length);

$to=$email;
//echo md5($random)
$msg=md5($random);
$msg=wordwrap($msg,70);

$headers =  'MIME-Version: 1.0' . "\r\n";
$headers .= 'From: garga  <info@garga.ist>' . "\r\n";
$headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

if(empty($username)|| empty($password) ||empty($email)){
  $cookie_name = "wrong";
  $cookie_value = "1";
  setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
  header("Location: http://garga.ist/beta/adminlogin/index.html");
}else{


if ($result['password']==$password ) {
  $cookie_name = "wrong";
  $cookie_value = "0";
  setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
  echo "şifre tuttu,holaaaa"."</br>";
  if (mail($to, "login verification", $msg, $headers)) {
    echo "mail attim";
  }else {
    echo "</br>"."shit"."</br>";
  }
  $in=mysqli_query($conn,"INSERT INTO adminolos(usernamei, hashedpassi, maili, lasthashi, lastlogini) VALUES ('$username','$hashed_password','$email','$msg',now())");
  if ($in) {
    $cookie_name = "username";
    $cookie_value = $username;
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day

    $cookie_name = "password";
    $cookie_value = $password;
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day


    header("Location: http://garga.ist/beta/adminlogin/verificate.html");
  }else {
    echo "olmaması gereken problemler yaşandı";
  }



}else {
  $cookie_name = "wrong";
  $cookie_value = "1";
  setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
  header("Location: http://garga.ist/beta/adminlogin/index.html");
}
}
 ?>

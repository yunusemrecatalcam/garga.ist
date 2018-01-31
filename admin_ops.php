<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

include 'connect_daddy.php';

$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");

$ip=$_SERVER['REMOTE_ADDR'];

$username=mysqli_real_escape_string($conn,$_POST['username']);
$password=mysqli_real_escape_string($conn,$_POST['password']);

echo $ip;
echo "</br>";
echo "kayıt başarılı,denedim çalışıyordu zaten dsknsj,yukarıdaki sayilari bana mesaj/ekran görüntüsü olarak atar mısın,güvenlik açısından yaptığım bir şey için bu --YEÇ"."</br>"."</br>";
echo "belirlediğin kullanıcı ismi:";
echo $username;
echo "</br>";


$in=mysqli_query($conn,"INSERT INTO admins(username,password,ip) VALUES ('$username','$password','$ip')");


 ?>

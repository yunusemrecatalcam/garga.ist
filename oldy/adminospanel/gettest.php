<?php

include ($_SERVER['DOCUMENT_ROOT'].'/beta/connect_daddy.php');
$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");

$id=mysqli_real_escape_string($conn,$_GET['idsi']);

$try=mysqli_query($conn,"SELECT * FROM texts WHERE id='$id' ");
$result=mysqli_fetch_assoc($try);

echo $result['metin'];

$cookie_name = "js";
$cookie_value = "bakalim";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day

 ?>

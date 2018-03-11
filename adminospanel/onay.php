<?php

include ($_SERVER['DOCUMENT_ROOT'].'/beta/connect_daddy.php');

$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");

$username= mysqli_real_escape_string($conn, $_POST['username']);
$password= mysqli_real_escape_string($conn,$_POST['password']);
$id= mysqli_real_escape_string($conn, $_POST['idsi']);

echo $username." ".$password." ".$id;

 ?>

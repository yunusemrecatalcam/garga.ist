<?php

include ($_SERVER['DOCUMENT_ROOT'].'/beta/connect_daddy.php');

$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");

$username= mysqli_real_escape_string($conn, $_GET['username']);
$password= mysqli_real_escape_string($conn,$_GET['password']);

 ?>

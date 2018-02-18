<?php
include('connect.php');

$conn = open_con();
$name= mysqli_real_escape_string($conn, $_GET['username']);
$pass= mysqli_real_escape_string($conn, $_GET['password']);

echo $name;
 ?>

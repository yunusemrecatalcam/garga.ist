<?php
include 'connect.php';

define('HOST','localhost');
define('USER','root') ;
define('DB','gargaiafl');
define('PASS','qwerty');

$dbConnection = new PDO('mysql:dbname=DB;host=localhost;charset=utf8', 'USER', 'PASS');

$conn=open_con();


 ?>

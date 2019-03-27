<?php
define('HOST','localhost');//160.153.128.39
define('USER','gargaproject') ;
define('DB','garga');
define('PASS','123456');

function open_con(){


  $conn = mysqli_connect(HOST,USER,PASS,DB);

  return $conn;
}
 ?>

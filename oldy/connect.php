<?php
define('HOST','localhost');
define('USER','insert_only') ;
define('DB','gargaiafl');
define('PASS','123456');

function open_con(){


  $conn = mysqli_connect(HOST,USER,PASS,DB);

  return $conn;
}
 ?>

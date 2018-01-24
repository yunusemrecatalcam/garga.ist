<?php
define('HOST','localhost');
define('USER','root') ;
define('DB','gargaiafl');
define('PASS','qwerty');

function open_con(){


  $conn = mysqli_connect(HOST,USER,PASS,DB);

  return $conn;
}
 ?>

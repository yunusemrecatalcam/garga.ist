<?php
function open_con(){

  define('HOST','localhost');
  define('USER','root') ;
  define('DB','gargaiafl');
  define('PASS','qwerty');
  $conn = mysqli_connect(HOST,USER,PASS,DB);

  return $conn;
}
 ?>

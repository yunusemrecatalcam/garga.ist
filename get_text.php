<?php
//echo "hell yeah";
define('HOST','localhost');
define('USER','root') ;
define('DB','gargaiafl');
define('PASS','qwerty');
$con = mysqli_connect(HOST,USER,PASS,DB);

if($con){
  echo "connected";
}
?>

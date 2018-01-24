<?php
include 'connect.php';
//echo "hell yeah";


if(open_con()){
  echo "connected";
}
header("Location: http://stackoverflow.com");
?>

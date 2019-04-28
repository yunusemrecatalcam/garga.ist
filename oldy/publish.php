<?php

include 'connect.php';

$try=mysqli_query($conn,"SELECT * FROM texts WHERE 1 ");
//$result=mysqli_fetch_assoc($try);
while ($result=mysqli_fetch_assoc($try)) {
  # code...
  echo $result['mahlas'];
  echo "<br/>";
  echo $result['metin']."<br/>"."<br/>";
}

 ?>

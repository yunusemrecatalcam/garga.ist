<?php

include ($_SERVER['DOCUMENT_ROOT'].'/beta/connect_daddy.php');

$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");

$username= mysqli_real_escape_string($conn, $_POST['username']);
$password= mysqli_real_escape_string($conn,$_POST['password']);
$id= mysqli_real_escape_string($conn, $_POST['idsi']);
$hash = mysqli_real_escape_string($conn, $_POST['hash']);
//echo $username." ".$password." ".$id;

$try=mysqli_query($conn,"SELECT * FROM adminolos WHERE usernamei='$username' ");
$result=mysqli_fetch_assoc($try);
//echo $hash;
$lolnumi ="numan";

if($result['usernamei']==$username && password_verify($password,$result['hashedpassi'])
&& $result['lasthashi']==$hash ){
  $lk=mysqli_query($conn,"UPDATE textstate SET $lolnumi='2' WHERE id=$id");
  if ($lk) {
    echo "qwsss";
  }
  echo "lol,it worked-- ".$id;
}else{
  echo "fluff";
}


 ?>

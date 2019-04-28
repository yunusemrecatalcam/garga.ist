<?php
include ($_SERVER['DOCUMENT_ROOT'].'/beta/connect_daddy.php');
//echo "hell yeah";


if(open_con()){
  echo "connected";
  echo "<br/>";
}
$conn=open_con();
mysqli_query($conn,"SET NAMES UTF8");
//header("Location: http://stackoverflow.com");
$mahlas= mysqli_real_escape_string($conn, $_POST['mahlas']);
$metin= mysqli_real_escape_string($conn,$_POST['yazi']);
$password= mysqli_real_escape_string($conn,$_POST['password']);
$metinadi= mysqli_real_escape_string($conn,$_POST['metinadi']);

$hashed_password=password_hash($password,PASSWORD_DEFAULT);

$cookie_name = "mahlas";
$cookie_value = $mahlas;
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day


$try=mysqli_query($conn,"SELECT * FROM writers WHERE mahlas='$mahlas' ");
$result=mysqli_fetch_assoc($try);

if($result['mahlas']==$mahlas && password_verify($password,$result['password'])){//used mahlas and true password

    $cookie_name = "if_pass_wrong";
    $cookie_value = "false";
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day

    mysqli_query($conn,"INSERT INTO texts(tarih,mahlas,metin,level,metinadi) VALUES (now(),'$mahlas','$metin','1','$metinadi')");
    header("Location: http://garga.ist/beta/yaziver/submission_success.html");
    //echo "1";

}elseif ($result['mahlas']==$mahlas && !password_verify($password,$result['password']) ) {//used mahlas and wrong password

    $cookie_name = "metin";
    $cookie_value = $metin;
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
    echo "</br>";
    echo "oleeeyy";

    $cookie_name = "if_pass_wrong";
    $cookie_value = "true";
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
    //echo "2";
    header("Location: http://garga.ist/beta/yaziver/");

}elseif ($result['mahlas'] != $mahlas) {//new mahlas

    $cookie_name = "if_used_mahlas";
    $cookie_value = "false";
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day

    $cookie_name = "if_pass_wrong";
    $cookie_value = "false";
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day

    mysqli_query($conn,"INSERT INTO texts(tarih,mahlas,metin,level,metinadi) VALUES (now(),'$mahlas','$metin','1','$metinadi')");
    mysqli_query($conn,"INSERT INTO writers(mahlas,password) VALUES ('$mahlas','$hashed_password')");
    //mysqli_query($conn,"INSERT INTO textstate(id)  SELECT MAX(id) FROM texts WHERE 1");

    header("Location: http://garga.ist/beta/yaziver/submission_success.html");
    //echo "3";
}

//$kayit=mysqli_query($conn,"INSERT INTO texts(tarih,mahlas,metin) VALUES (now(),'$mahlas','$metin')");
//$try=mysqli_query($conn,"SELECT * FROM texts WHERE 1 ");


?>

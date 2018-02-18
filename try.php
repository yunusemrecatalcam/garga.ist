<?php
echo "e çalışıyor";

echo md5("asfdsg")."</br>";

$length=12;
$random= substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDE
FGHIJKLMNOPQRSTUVWXYZ', ceil($length/strlen($x)) )),1,$length);

echo md5($random)."</br>";
?>

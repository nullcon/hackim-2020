<?php 
header("Content-Type: application/json");

function httpGet($url){
 $ch = curl_init();
 curl_setopt($ch,CURLOPT_URL,$url);
 curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
 //prevent any output
 ob_start();
 $output=curl_exec($ch);
 $info = curl_getinfo($ch);
 ob_end_clean();
 curl_close ($ch);
 unset($ch);
 return $output;
} 


$search=$_GET['search'];

if (stripos($search, 'UNLOAD') !== false) {
    echo 'blocked';
    exit();
}

if (stripos($search, 'unload') !== false) {
    echo 'blocked';
    exit();
}

 if($search){
  $url="http://solr:8983/solr/hackimsearch/select?df=name&q=$search";
  $get=httpGet($url);
  $check=json_decode($get,true);
  unset($check["responseHeader"]);
  echo json_encode($check);
 }
 else{
  echo "please provide some search parameter";
 }

?>

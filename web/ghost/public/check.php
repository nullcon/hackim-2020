<?php

session_start();


function impersonate($impersonator,$impersonatee){
 
 if($impersonatee===$_SESSION['admin']){
   if($_SESSION['role']!=$_SESSION['admin_role']){
    echo "cannot impersonate admin role";
    exit();
   }
  }
  
 if($impersonator===$_SESSION['admin']){
    $_SESSION['admin_role']="user";
  }

  $_SESSION['impname']=$impersonatee;
  $_SESSION['imp']=true;
}

function unimpersonate($impersonator){
 if($impersonator===$_SESSION['admin']){
    $_SESSION['admin_role']="admin";
    return;
  }

 if($impersonator===$_SESSION['backup']){ 
  $_SESSION['name']=$_SESSION['backup'];
  $_SESSION['imp']=false;
  $_SESSION['impname']="";
 }
}

function signup($name){
  $_SESSION['name']=$name;
  $_SESSION['backup']=$name;
  $_SESSION['role']="user";
  $_SESSION['impname']="";
  $_SESSION['imp']=false;
  $_SESSION['admin']=$name."-admin";
  $_SESSION['admin_role']="admin";
}

function status(){
 echo "name: ".$_SESSION['name']."</br>";
 echo "impersonating: ".$_SESSION['impname']."</br>";
 echo "role: ".$_SESSION['role']."</br>";
 echo "admin name: ".$_SESSION['admin']."</br>" ;
 echo "admin role: ".$_SESSION['admin_role']."</br>";
}

echo "<center><h1>Welcome to password less authentication system</h1></center>";


if($_GET['signup']){
 signup($_GET['name']);
}

if(!$_SESSION['name']){
 echo "please signup";
 exit();
}

if($_GET['impersonatee'] && $_GET['impersonator']){
 impersonate($_GET['impersonator'],$_GET['impersonatee']);
}

if($_GET['unimpersonate']){
 unimpersonate($_GET['unimpersonate']);
}

if($_GET['status']){
 status();
}

if($_SESSION['imp']){
 if($_SESSION['impname']===$_SESSION['admin']){
  if($_SESSION['admin_role']==="admin"){
   echo "hackim20{We_Never_Thought_it_Was_That_Vulnerable}";
  }
  else{
    echo "You admin role is not admin";
   }
  }
 else{
  echo "You are not admin";
 }
}
else{
 $name=$_SESSION['admin'];
 echo "Please become admin, username: $name \n";
}



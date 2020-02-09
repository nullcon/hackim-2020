<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Hackim Search</title>
<script>

function printNames(item, index){
    document.getElementById("result").innerHTML += index + ":" + item.name[0] + "<br>";
}


function req() {
  search=document.getElementById('search').value;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var result = this.responseText;
      try {
 
       var jsonparse = JSON.parse(result);
       if(jsonparse.response){
         var h=jsonparse.response.docs
         h.forEach(printNames);
       }
      else if(jsonparse.error){      
       document.getElementById("result").innerHTML = "Some error with backend";
       }
     }
     catch(err){
       document.getElementById("result").innerHTML= result;
     }
    }
  };
  xhttp.open("GET", "search.php?search="+search, true);
  xhttp.withCredentials = true;
  xhttp.send();
}
</script>
 
</head>
<body>

<center><h1>Hackim search</h1>
<h3>The fastest book search in the world</h3>

        <label>Search something:</label>
        <input type="text" id="search" name="search">
        <button type="button" onclick=req()>Submit Form</button>



<div id="result">
</div>

</center>


</body>
</html>


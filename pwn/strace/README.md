#### strace

##### Description

pwn while you trace

##### Points

200/250

##### Flag

hackim20{trace_or_pwn_what_did_you_do}

##### Solution
without the diff, it might take some time to get to the format string bug. beware of the "unintended" solutions

strace binary built from
```bash
root@056084cf6080:/strace# git remote -v
origin	https://github.com/strace/strace.git (fetch)
origin	https://github.com/strace/strace.git (push)
root@056084cf6080:/strace# git log -1 --stat | head -n 4
commit ce2c968a614ae2a3cf2354620b3b8200f003e87c
Author: Dmitry V. Levin <ldv@altlinux.org>
Date:   Fri Jan 17 01:01:21 2020 +0000
```

##### Build
```shell
docker build -t strace .
```
##### Run:
```shell
docker run --privileged --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -p 8000:8000 strace
```
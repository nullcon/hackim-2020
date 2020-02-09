// gcc -O0 -fno-stack-protector -no-pie main.c -o main

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

char s[35];

void nothing() {
    asm(
        "pop %rdi;"
        "ret;"
        "pop %rsi;"
        "ret;"
        "pop %rdx;"
        "ret;"
        "pop %rcx;"
        "ret;"
        "pop %rax;"
        "ret;"
        "add %rdi, %rax;"
        "ret;"
        "add %rsi, %rax;"
        "ret;"
        "add %rdx, %rax;"
        "ret;"
        "add %rcx, %rax;"
        "ret;"
        "add %rax, %rax;"
        "ret;"
        "add $1, %rax;"
        "ret;"
        "xor %rax, %rax;"
        "ret;"
        "sub %rdi, %rax;"
        "ret;"
        "sub %rsi, %rax;"
        "ret;"
        "sub %rdx, %rax;"
        "ret;"
        "sub %rcx, %rax;"
        "ret;"
        "sub $1, %rax;"
        "ret;"
        "movzbq 0x0(%rdi), %rdi;"
        "ret;"
        "movzbq 0x0(%rsi), %rsi;"
        "ret;"
        "movzbq 0x0(%rdx), %rdx;"
        "ret;"
        "movzbq 0x0(%rcx), %rcx;"
        "ret;"
        "mov %rax, %rdi;"
        "ret;"
        "mov %rax, %rsi;"
        "ret;"
        "mov %rax, %rdx;"
        "ret;"
        "mov %rax, %rcx;"
        "ret;"
    );
    exit(0);
}

int main() {
    printf("Hello world!\n");
    char buf[35];
    FILE *fp;
    fp = fopen("flag", "r");
    if (fp == NULL)
        exit(1);
    fgets(buf, sizeof(buf), fp);
    fclose(fp);
    memset(s, 0, sizeof(s));
    strcpy(s, buf);
    read(0, buf, 1024);
    return 0;
}

#include <alloca.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

volatile int count = 0;
char *p;
int main() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    char buf[100];
    short int i;
    if (count == 0) {
        if (fgets(buf, 100, stdin) == NULL)
            return -1;
        i = atoi(buf);
    } else {
        i = 200;
    }
    p = alloca(i);
    read(0, p, (unsigned short int)i);
    printf(p);
    if (count != 0) {
        read(0, buf, 0);
        printf("JK, you lose!");
        _exit(0);
    }
    count++;
}

#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

#include "rng.h"

uint32_t arr[10] = {0};

void nothing() {
    __asm__("pop %rdx;"
            "ret");
}

void read_uint64(const char *fname, uint64_t *n) {
    FILE *f = fopen(fname, "r");
    fscanf(f, "%lu", n);
    fclose(f);
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    rand_t rand;
    uint64_t cookie = 0;
    read_uint64("ch0c0l4te-chip", &cookie);
    set_seed(&rand, cookie);
    for (int i = 0; i < 10; i++) {
        arr[i] = next_int(&rand);
    }

    printf("I think I dropped something yummy! sssh");
    for (int i = 0; i < 10; i += 2) {
        printf("%u\n", arr[i]);
    }
    for (int i = 1; i < 10; i += 2) {
        printf("%u\n", arr[i]);
    }

    char buf[28];
    memcpy(buf + 20, &cookie, sizeof(cookie));

    write(1, "hello\n", 6);
    read(0, buf, 500);

    cookie = 0;
    read_uint64("ch0c0l4te-chip", &cookie);
    if (memcmp(buf+20, &cookie, sizeof(cookie)) != 0) {
        write(1, "Stack smashing detected! Exiting...\n", 36);
        exit(1);
    }
    
    return 0;
}

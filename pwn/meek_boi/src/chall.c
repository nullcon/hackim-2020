#define _GNU_SOURCE
#include <assert.h>
#include <ctype.h>
#include <errno.h>
#include <fcntl.h>
#include <linux/audit.h>
#include <linux/filter.h>
#include <linux/seccomp.h>
#include <signal.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/prctl.h>
#include <sys/ptrace.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <sys/user.h>
#include <sys/wait.h>
#include <unistd.h>

#define BUF_SIZE (0x4000 & ~(getpagesize() - 1))

int putchr(char out) { return write(1, &out, 1); }

void put(const char *out) {
    while (*out) {
        putchr(*(out++));
    }
}

static long forbidden_syscalls[] = {SYS_execve, SYS_execveat, SYS_connect,
                                    SYS_bind,   SYS_accept,   SYS_accept4};

#define forbidden_syscalls_len                                                 \
    ((sizeof(forbidden_syscalls) / sizeof(forbidden_syscalls[0])))

static void setup_syscall_filter() {
    assert(prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) == 0);

    struct sock_filter instrs[forbidden_syscalls_len + 5];
#define NUM_INSTRS (sizeof(instrs) / sizeof(instrs[0]))
#define FAIL_IDX (NUM_INSTRS - 1)
#define ACCEPT_IDX (NUM_INSTRS - 2)
    instrs[0] = (struct sock_filter)BPF_STMT(
        BPF_LD | BPF_W | BPF_ABS, offsetof(struct seccomp_data, arch));
    unsigned int my_arch =
#ifdef __x86_64__
        AUDIT_ARCH_X86_64
#else
#error unknown architecture
#endif
        ;
    instrs[1] = (struct sock_filter)BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, my_arch,
                                             0, FAIL_IDX - (1 + 1));
    instrs[2] = (struct sock_filter)BPF_STMT(BPF_LD | BPF_W | BPF_ABS,
                                             offsetof(struct seccomp_data, nr));
    for (int i = 0; i < forbidden_syscalls_len; i++) {
        instrs[i + 3] = (struct sock_filter)BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K,
                                                     forbidden_syscalls[i],
                                                     FAIL_IDX - (i + 3 + 1), 0);
    }
    instrs[ACCEPT_IDX] =
        (struct sock_filter)BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW);
    instrs[FAIL_IDX] = (struct sock_filter)BPF_STMT(BPF_RET | BPF_K,
                                                    SECCOMP_RET_ERRNO | 0x1234);
    struct sock_fprog fprog = {.len = NUM_INSTRS, .filter = instrs};

    assert(prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &fprog, 0, 0) == 0);
}

void child_do(void (*f)()) {
    fclose(stdin);
    fclose(stdout);
    fclose(stderr);
    int fd = open("/dev/null", O_RDWR);
    dup2(fd, STDIN_FILENO);
    dup2(fd, STDOUT_FILENO);
    dup2(fd, STDERR_FILENO);
    f();
    exit(0);
}

int main(int argc, char **argv) {
    int fd, i, count;
    char *psc, *c;
    void (*f)();
    psc = mmap(NULL, BUF_SIZE, PROT_READ | PROT_WRITE | PROT_EXEC,
               MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    assert(psc != NULL);
    fflush(stdout);
    f = (void (*)())psc;
    c = psc;
    count = read(0, psc, BUF_SIZE);
    *(c + count) = '\xc3';

    pid_t p = fork();
    if (p < 0) {
        perror("fork");
    }
    if (p > 0) {
        wait(NULL);
        exit(0);
    } else {
        child_do(f);
    }
    return 0;
}

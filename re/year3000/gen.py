import random
import subprocess

template = '''
#include <stdio.h>
#include <stdint.h>
#include <string.h>

%s canary = %s;

int f(const char *s) {
    int x = %s;
    char c = '%s';
    int flag = 1;
    for (int i = 0; i < x; i++) {
        if (s[i] != c) {
            flag = 0;
            break;
        }
    }

    if (memcmp(s + x, &canary, %d) != 0)
        flag = 0;

    return flag;
}

int main() {
    char in[100];
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    fgets(in, 100, stdin);
    int ret = f(in);
    if (ret)
        printf("Well done\\n");
    else
        printf("You have failed\\n");
    return (ret != 1);
}
'''

solution = '''
import sys
import struct
import base64

buf = b'%s'
buf += struct.pack('%s', %d)
buf = base64.b64encode(buf)
buf += b'\\n'

sys.stdout.buffer.write(buf)
'''

def get_canary(arch):
    def get_num():
        x = random.randint(0x00, 0xff)
        while x in [0x00, 0x0a, 0x0d]:
            x = random.randint(0x00, 0xff)
        return x
    n = get_num()
    n <<= 8
    n |= get_num()
    n <<= 8
    n |= get_num()
    n <<= 8
    n |= get_num()
    if arch == 32:
        return n
    n <<= 8
    n |= get_num()
    n <<= 8
    n |= get_num()
    n <<= 8
    n |= get_num()
    n <<= 8
    n |= get_num()
    return n

def get_idx():
    return random.randint(10, 90)

def get_ch():
    if random.choice([False, True]):
        x = random.randint(97, 122)
    else:
        x = random.randint(65, 90)
    return chr(x)

def main():
    for i in range(1, 3001):
        print('[+] Generating %d.bin' % i)
        arch = random.choice([32, 64])
        canary = get_canary(arch)
        idx = get_idx()
        ch = get_ch()
        cmp_sz = 4 if arch == 32 else 8
        src = template % ('uint%d_t' % arch, hex(canary), idx, ch, cmp_sz)
        sol = solution % (ch * int(idx), '<I' if arch == 32 else '<Q', canary)
        with open('{}.c'.format(i), 'w') as f:
            f.write(src)
        with open('sol_{}.py'.format(i), 'w') as f:
            f.write(sol)
        if arch == 64:
            subprocess.call(['gcc', '-O0', '-o', '%d.bin' % i, '%d.c' % i])
        else:
            subprocess.call(['gcc', '-m32', '-O0', '-o', '%d.bin' % i, '%d.c' % i])

main()

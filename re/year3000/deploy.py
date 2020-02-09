import subprocess
import random
import sys
import base64
import time
import binascii

bins = set()

def main():
    while (len(bins) < 10):
        n = random.randint(1, 3000)
        bins.add('{}.bin'.format(n))

    for b in bins:
        print(b)
        start = time.time()
        sys.stdout.flush()
        i = input('> ')
        sys.stdin.flush()
        end = time.time()
        if (end - start) > 7:
            print('too slow...')
            sys.stdout.flush()
            return 1
        i = i.strip('\n')
        i = i.encode('utf-8')
        try:
            i = base64.b64decode(i)
        except binascii.Error:
            print('i want base64...')
            return 1
        i = i[:99]
        p = subprocess.Popen([f'./{b}'], stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        o, e = p.communicate(input=i)
        print(o)
        if b'failed' in o:
            return 1

    print('hackim20{h3_sa1d_1v3_b3en_t0_th3_ye4R_3O0O}')

main()

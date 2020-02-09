import struct

o = [296, 272, 272, 272, 296, 360, 272, 424, 272, 208, 120, 120, 120, 96, 120, 120, 120, 120, 120, 120, 120, 208, 120, 120, 208, 208, 208, 208, 208, 272, 120, 208, 208]
r = [208, 225, 237, 20, 214, 183, 79, 105, 207, 217, 125, 66, 123, 104, 97, 99, 107 , 105, 109, 50, 48, 202, 111, 111, 29, 63, 223, 36, 0, 124, 100, 219, 32]

bufs = []
gadgets = set()

with open('../dist/blob', 'rb') as f:
    for offset in o:
        data = f.read(offset)
        bufs.append(data)

def decode(buf):
    na = 56
    data_l = []
    data = None
    for i in range(na, len(buf), 8):
        data = buf[i:i+8]
        data = struct.unpack('<Q', data)[0]
        data_l.append(data)
        if data > 0x400000:
            gadgets.add(data)
    return data_l

# for buf in bufs:
#     addrs = decode(buf)
# for g in gadgets:
#     print(hex(g)[2:])
# for i in `python solution.py`; do echo $i; objdump -d ../dist/main -j.text -M intel | grep $i; echo "--------------------"; done

dis = {}
dis[0x40119a] = 'pop rdi'
dis[0x40119c] = 'pop rsi'
dis[0x40019e] = 'pop rdx'

'''
 23 .bss          00000048  0000000000404080  0000000000404080  00003068  2**5
                  ALLOC
'''
dis[0x4040a0] = 'flag'
dis[0x4011a0] = 'pop rcx'
dis[0x4011a2] = 'pop rax'
dis[0x4011a4] = 'add rax, rdi'
dis[0x4011a8] = 'add rax, rsi'
dis[0x4011ac] = 'add rax, rdx'
dis[0x4011b0] = 'add rax, rcx'
dis[0x4011bd] = 'xor rax, rax'
dis[0x4011c1] = 'sub rax, rdi'
dis[0x4011c5] = 'sub rqx, rsi'
dis[0x4011c9] = 'sub rax, rdx'
dis[0x4011cd] = 'sub rax, rcx'
dis[0x4011d6] = 'movzx rdi, BYTE PTR [rdi]'
dis[0x4011db] = 'movzx rsi, BYTE PTR [rsi]'
dis[0x4011e0] = 'movzx rdx, BYTE PTR [rdx]'
dis[0x4011e5] = 'movzd rcx, BYTE PTR [rcx]'
dis[0x4011ea] = 'mov rdi, rax'
dis[0x4011ee] = 'mov rsi, rax'
dis[0x4011f2] = 'mov rdx, rax'
dis[0x4011f6] = 'mov rcx, rax'
dis[0x4011ff] = 'call exit@plt'

for buf in bufs:
    addrs = decode(buf)
    for addr in addrs:
        try:
            print(dis[addr])
        except KeyError:
            print(hex(addr))

    print('---------------------------')

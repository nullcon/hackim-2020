import pwn 
import ast
from Crypto.Util.number import *
from hashlib import sha256


r = pwn.remote("crypto2.ctf.nullcon.net", 5000)
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff

r.recvline()
cs = r.recvline().decode().strip()
cs = ast.literal_eval(cs)

response = " ".join([f"({c},{1},{c})" for c in cs])
r.sendline(response)

r.recvuntil("Server response:")
r.recvline()
crs = r.recvline().decode().strip()
crs = ast.literal_eval(crs)

a_ = []
b_ = []
for i, (c0, c1) in enumerate(crs):
	c = cs[i]
	m0 = int(sha256(long_to_bytes(1)).hexdigest(), 16) ^ c0[1]
	m1 = int(sha256(long_to_bytes(c1[0])).hexdigest(), 16) ^ c1[1]
	b = m0
	a = (m1 - b) % 2
	a_.append(a)
	b_.append(b)

r.recvuntil("Enter a:")
r.sendline(str(a_))
r.recvuntil("Enter b:")
r.sendline(str(b_))
r.interactive()


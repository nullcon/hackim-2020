import pwn as p
import rps

r = p.remote("crypto1.ctf.nullcon.net", 5000)

def get_commitments():
	r.recvuntil("Here are the possible commitments, the first one is my move: ")
	res = r.recvline().strip()
	res = res.split(" ")
	return res

def send_move(a):
	r.recvuntil("Your move:")
	r.sendline(str(a))


rev_sbox = [0] * 256
rev_p = [0] * 16


for i in range(len(rev_sbox)):
    rev_sbox[rps.sbox[i]] = i
for i in range(len(rev_p)):
    rev_p[rps.p[i]] = i


def reverse_permutation(data):
    temp = bytearray([0]) * 16
    for i in range(len(temp)):
        temp[rev_p[i]] = data[i]
    return temp

def reverse_sbox(data):
    for i in range(len(data)):
        data[i] = rev_sbox[data[i]]
    return data

def reverse_round(h, key):
    h = bytearray(rps.int_to_bytes(int(h, 16)))
    key = rps.pad(bytearray(key.encode()))
    for i in range(rps.round):
        h = reverse_permutation(h)
        h = reverse_sbox(h)
        h = rps.repeated_xor(h, key)
    h = hex(rps.bytes_to_int(h))[2:]
    return h

def hash(data, state=bytearray([208, 151, 71, 15, 101, 206, 50, 225, 223, 14, 14, 106, 22, 40, 20, 2])):
    data = rps.pad(data, 16)
    data = rps.group(data)
    for roundkey in data:
        for _ in range(rps.round):
            state = rps.repeated_xor(state, roundkey)
            for i in range(len(state)):
                state[i] = rps.sbox[state[i]]
            temp = bytearray(16)
            for i in range(len(state)):
                temp[rps.p[i]] = state[i]
            state = temp
    return hex(rps.bytes_to_int(state))[2:]

def gen_commitments(commitment, move):
	state = reverse_round(commitment, move)
	state = bytearray(rps.int_to_bytes(int(state, 16)))
	rc = hash(bytearray(b"r"), state=state)
	pc = hash(bytearray(b"p"), state=state)
	sc = hash(bytearray(b"s"), state=state)
	return [rc, pc, sc]


for _ in range(20):
	cs = get_commitments()
	rcs = gen_commitments(cs[0], "r")
	pcs = gen_commitments(cs[0], "p")
	scs = gen_commitments(cs[0], "s")

	if set(rcs) == set(cs):
		send_move("p")
	elif set(pcs) == set(cs):
		send_move("s")
	elif set(scs) == set(cs):
		send_move("r")
	else:
		raise NotImplementedError
r.interactive()
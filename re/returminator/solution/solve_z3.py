from z3 import *

s = Solver()
n = 31

bv = []
for i in range(n):
    bv.append(BitVec('bv_{}'.format(i), 32))

alphabet = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}'

for i in range(n):
    s.add(bv[i] >= min(alphabet))
    s.add(bv[i] <= max(alphabet))

s.add(bv[0] + bv[2] + bv[4] - 100 == 208)
s.add(bv[6] + bv[8] + bv[10] == 225)
s.add(bv[12] + bv[14] + bv[16] == 237)
s.add(bv[18] + bv[1] - bv[30] == 20)
s.add(bv[3] + bv[22] + bv[3] - 100 == 214)
s.add(bv[5] + bv[29] + bv[28] - bv[7] - 100 == 183)
s.add(bv[9] + bv[17] - bv[11] == 79)
s.add(bv[13] + bv[15] - bv[19] + bv[20] - bv[27] == 105)
s.add(bv[21] + bv[23] + bv[24] == 207)
s.add(bv[25] + bv[26] == 217)
s.add(bv[30] == 125)
s.add(bv[9] == 66)
s.add(bv[8] == 123)
s.add(bv[0] == 104)
s.add(bv[1] == 97)
s.add(bv[2] == 99)
s.add(bv[3] == 107)
s.add(bv[4] == 105)
s.add(bv[5] == 109)
s.add(bv[6] == 50)
s.add(bv[7] == 48)
s.add(bv[11] + bv[0] == 202)
s.add(bv[29] == 111)
s.add(bv[28] == 111)
s.add(bv[29] - bv[13] == 29)
s.add(bv[28] - bv[14] == 63)
s.add(bv[28] + bv[15] == 223)
s.add(bv[0] - bv[27] == 36)
s.add(bv[23] - bv[24] == 0)
s.add(bv[26] + bv[0] - bv[1] == 124)
s.add(bv[19] == 100)
s.add(bv[11] + bv[12] == 219)
s.add(bv[21] - bv[20] == 32)

s.check()
m = s.model()
ans = bytearray()

for i in range(n):
    c = m[bv[i]].as_long()
    ans.append(c)

print(ans.decode('utf-8'))

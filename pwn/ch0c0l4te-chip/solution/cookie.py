from z3 import *

known = [478994381, 2959297414, 562871126, 3854106449, 1639526364, 3657511224, 31753054, 4141874356, 2238833981, 2228163041]

mul = BitVecVal(0x5deece66d, 64)
add = BitVecVal(0xb, 64)
mask = BitVecVal((1 << 48) - 1, 64)
n = len(known)
seed = BitVec('seed', 64)
seeds = [BitVec('seed_{}'.format(i), 64) for i in range(n)]
out = [BitVec('out_{}'.format(i), 32) for i in range(0, n-1)]

s = Solver()
s.add(seeds[0] == (seed ^ mul) & mask)

for i in range(1, n):
    s.add(
        seeds[i] == simplify(
            (seeds[i-1] * mul + add) & mask
        ))

for i in range(0, n-1):
    s.add(
        out[i] == simplify(
            Extract(31, 0, LShR(seeds[i+1], 16))
        ))

for i in range(0, n-1):
    s.add(out[i] == known[i])

print(s)
print(s.check())
m = s.model()
seed_val = m[seed].as_long()
print(hex(seed_val))

# for i in range(10):    
#     print(s.check())
#     m = s.model()
#     seed_val = m[seed].as_long()
#     print(seed_val)
#     s.add(seed != seed_val)

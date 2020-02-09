from pwn import *
from base64 import b64decode
from time import sleep
# context.log_level = "debug"
ims = []
lines = []
with open("b64","r") as f:
    lines = f.read().split("\n")
for line in lines:
    ims.append(line.split("."))

d = dict()

for i in ims:
    if len(i) > 1:
        d[i[0]] = i[1]

s = remote("misc.ctf.nullcon.net", 8000)

print s.recvline()

for i in xrange(800):
    print i
    img = s.recvline().strip()
    # open("test/%d.png" % i, "a").write(b64decode(img))
    s.recvline()
    # sleep(0.1)
    s.sendline(d[img])

print s.recvall()
s.close()
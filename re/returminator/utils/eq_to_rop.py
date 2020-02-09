template_idx = '''
    buf += p64(pop_rax)
    buf += p64({data})
    buf += p64(pop_{reg})
    buf += p64({idx})
    buf += p64(add_rax_{reg})
    buf += p64(mov_{reg}_rax)
    buf += p64(mov_{reg}_deref_{reg})
'''

template_imm = '''
    buf += p64(pop_{reg})
    buf += p64({imm})
'''

template_add = '''
    buf += p64(add_rax_{reg})
'''

template_sub = '''
    buf += p64(sub_rax_{reg})
'''

template_exit = '''
    buf += p64(mov_rdi_rax)
    buf += p64(call_exit)
'''

bss_string = 0x404080

def a():
    # bv[0] + bv[2] + bv[4] - 100 == 208
    idxs = [0, 2, 4]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_imm.format(reg='rdi', imm=100)
    code += template_sub.format(reg='rdi')
    code += template_exit

    print(code)


def b():
    # bv[6] + bv[8] + bv[10] == 225
    idxs = [6, 8, 10]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_exit

    print(code)

def c():
    # bv[12] + bv[14] + bv[16] == 237
    idxs = [12, 14, 16]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_exit

    print(code)

def d():
    # bv[18] + bv[1] - bv[30] == 20
    idxs = [18, 1, 30]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for i in range(2):
        code += template_add.format(reg=regs_used[i])
    code += template_sub.format(reg=regs_used[-1])
    code += template_exit

    print(code)

def e():
    # bv[3] + bv[22] + bv[3] - 100 == 214
    idxs = [3, 22, 3]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_imm.format(reg='rdi', imm=100)
    code += template_sub.format(reg='rdi')
    code += template_exit

    print(code)

def f():
    # bv[5] + bv[29] + bv[28] - bv[7] - 100 == 183
    idxs = [5, 29, 28, 7]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for i in range(3):
        code += template_add.format(reg=regs_used[i])
    code += template_sub.format(reg=regs_used[-1])
    code += template_imm.format(reg='rdi', imm=100)
    code += template_sub.format(reg='rdi')
    code += template_exit

    print(code)

def g():
    # bv[9] + bv[17] - bv[11] == 79)
    idxs = [9, 17, 11]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for i in range(2):
        code += template_add.format(reg=regs_used[i])
    code += template_sub.format(reg=regs_used[-1])
    code += template_exit

    print(code)

def h():
    # bv[13] + bv[15] - bv[19] + bv[20] - bv[27] == 105
    idxs = [19, 27]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += '    buf += p64(mov_rcx_rax)'

    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    regs_used = []

    idxs = [13, 15, 20]
    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_sub.format(reg='rcx')
    code += template_exit

    print(code)

def i():
    # bv[21] + bv[23] + bv[24] == 207
    idxs = [21, 23, 23]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_exit

    print(code)

def j():
    # bv[25] + bv[26] == 217
    idxs = [25, 26]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_exit

    print(code)

def k():
    # bv[30] == 125
    idx = 30
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def l():
    # bv[9] == 66
    idx = 9
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def m():
    # bv[8] == 123
    idx = 8
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def n():
    # bv[0] == 104
    idx = 0
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def o():
    # bv[1] == 97
    idx = 1
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def p():
    # bv[2] == 99
    idx = 2
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def q():
    # bv[3] == 107
    idx = 3
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def r():
    # bv[4] == 105
    idx = 4
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def s():
    # bv[5] == 109
    idx = 5
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def t():
    # bv[6] == 50
    idx = 6
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def u():
    # bv[7] == 48
    idx = 7
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def v():
    # bv[11] + bv[0] == 202
    idxs = [11, 0]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_exit

    print(code)

def w():
    # bv[29] == 111
    idx = 29
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def x():
    # bv[28] == 111
    idx = 29
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def y():
    # bv[29] - bv[13] == 29
    idxs = [29, 13]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    code += template_add.format(reg=regs_used[0])
    code += template_sub.format(reg=regs_used[1])
    code += template_exit

    print(code)

def z():
    # bv[28] - bv[14] == 63
    idxs = [28, 14]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    code += template_add.format(reg=regs_used[0])
    code += template_sub.format(reg=regs_used[1])
    code += template_exit

    print(code)

def aa():
    # bv[28] + bv[15] == 223
    idxs = [28, 15]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_exit

    print(code)

def ab():
    # bv[0] - bv[27] == 36
    idxs = [0, 27]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    code += template_add.format(reg=regs_used[0])
    code += template_sub.format(reg=regs_used[1])
    code += template_exit

    print(code)

def ac():
    # bv[23] - bv[24] == 0
    idxs = [23, 24]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    code += template_add.format(reg=regs_used[0])
    code += template_sub.format(reg=regs_used[1])
    code += template_exit

    print(code)

def ad():
    # bv[26] + bv[0] - bv[1] == 124
    idxs = [26, 0, 1]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for i in range(2):
        code += template_add.format(reg=regs_used[i])
    code += template_sub.format(reg=regs_used[-1])
    code += template_exit

    print(code)

def ae():
    # bv[19] == 100
    idx = 19
    reg = 'rdi'

    code = ''
    code += '    buf = \'\''
    code += template_idx.format(data=bss_string, reg=reg, idx=idx)
    code += '    buf += p64(call_exit)'

    print(code)

def af():
    # bv[11] + bv[12] == 219
    idxs = [11, 12]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    for reg in regs_used:
        code += template_add.format(reg=reg)
    code += template_exit

    print(code)

def ag():
    # bv[21] - bv[20] == 32
    idxs = [21, 20]
    regs = iter(['rdi', 'rsi', 'rdx', 'rcx'])
    code = ''
    code += '    buf = \'\''
    regs_used = []

    for idx in idxs:
        regs_used.append(next(regs))
        code += template_idx.format(data=bss_string, reg=regs_used[-1], idx=idx)
    code += '    buf += p64(xor_rax_rax)'
    code += template_add.format(reg=regs_used[0])
    code += template_sub.format(reg=regs_used[1])
    code += template_exit

    print(code)

ag()

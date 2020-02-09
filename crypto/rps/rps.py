#!/usr/bin/env python3
from Crypto import Random
from Crypto.Random import random
from Crypto.Util.number import *
from secret import flag

sbox = [221, 229, 120, 8, 119, 143, 33, 79, 22, 93, 239, 118, 130, 12, 63, 207, 90, 240, 199, 20, 181, 4, 139, 98, 78, 32, 94, 108, 100, 223, 1, 173, 220, 238, 217, 152, 62, 121, 117, 132, 2, 55, 125, 6, 34, 201, 254, 0, 228, 48, 250, 193, 147, 248, 89, 127, 174, 210, 57, 38, 216, 225, 43, 15, 142, 66, 70, 177, 237, 169, 67, 192, 30, 236, 131, 158, 136, 159, 9, 148, 103, 179, 141, 11, 46, 234, 36, 18, 191, 52, 231, 23, 88, 145, 101, 17, 74, 44, 122, 75, 235, 175, 54, 40, 27, 109, 73, 202, 129, 215, 83, 186, 7, 163, 29, 115, 243, 13, 105, 184, 68, 124, 189, 39, 140, 138, 165, 219, 161, 150, 59, 233, 208, 226, 176, 144, 113, 146, 19, 224, 111, 126, 222, 178, 47, 252, 99, 87, 134, 249, 69, 198, 164, 203, 194, 170, 26, 137, 204, 157, 180, 168, 162, 56, 81, 253, 213, 45, 21, 58, 24, 171, 37, 82, 53, 50, 84, 196, 232, 242, 244, 64, 80, 10, 114, 212, 187, 205, 28, 51, 182, 16, 107, 245, 211, 85, 92, 195, 5, 197, 200, 31, 183, 61, 123, 86, 167, 154, 41, 151, 35, 247, 246, 153, 95, 206, 149, 76, 112, 71, 230, 106, 188, 172, 241, 72, 156, 49, 14, 214, 155, 110, 102, 116, 128, 160, 135, 104, 77, 91, 190, 60, 42, 185, 96, 97, 251, 218, 133, 209, 65, 227, 3, 166, 255, 25]
p = [5, 9, 1, 8, 3, 11, 0, 12, 7, 4, 14, 13, 10, 15, 6, 2]
round = 16


def pad(data, size = 16):
    pad_byte = (size - len(data) % size) % size
    data = data + bytearray([pad_byte]) * pad_byte
    return data


def repeated_xor(p, k):
    return bytearray([p[i] ^ k[i % len(k)] for i in range(len(p))])


def bytes_to_int(xbytes):
    return bytes_to_long(xbytes)


def int_to_bytes(x):
    return long_to_bytes(x, 16)


def group(input, size = 16):
    return [input[i * size: (i + 1) * size] for i in range(len(input) // size)]


def hash(data):
    state = bytearray([208, 151, 71, 15, 101, 206, 50, 225, 223, 14, 14, 106, 22, 40, 20, 2])
    data = pad(data, 16)
    data = group(data)
    for roundkey in data:
        for _ in range(round):
            state = repeated_xor(state, roundkey)
            for i in range(len(state)):
                state[i] = sbox[state[i]]
            temp = bytearray(16)
            for i in range(len(state)):
                temp[p[i]] = state[i]
            state = temp
    return hex(bytes_to_int(state))[2:]

def gen_commitments():
    secret = bytearray(Random.get_random_bytes(16))
    rc = hash(secret + b"r")
    pc = hash(secret + b"p")
    sc = hash(secret + b"s")
    secret = hex(bytes_to_int(secret))[2:]
    rps = [("r", rc), ("p", pc), ("s", sc)]
    random.shuffle(rps)
    return secret, rps

def check_win(a, b):
    if a == "r":
        if b == "p":
            return True
        else:
            return False
    elif a == "s":
        if b == "r":
            return True
        else:
            return False
    elif a == "p":
        if b == "s":
            return True
        else:
            return False
    return False

def main():
    print("Beat me in Rock Paper Scissors 20 consecutive times to get the flag")
    for i in range(20):
        secret, rps = gen_commitments()
        move = rps[0][0]
        print("Here are the possible commitments, the first one is my move:", " ".join(map(lambda s: s[1], rps)))
        inp = input("Your move:")
        res = check_win(move, inp)
        print("My move was:", move, "Secret was:", secret)
        if not res:
            print("You lose!")
            exit(0)

    print("You win")
    print("Your reward is", flag)
    exit(0)

if __name__ == '__main__':
    main()

def LFSR(input):
    output = input
    output ^= (input << 13) & 0xffffffff
    output ^= output >> 17
    output ^= (output << 5) & 0xffffffff
    return output & 0xffffffff


import string

dir = string.ascii_letters + string.digits
flag = "********************************"
key = 0xf34b7cd59a31a3
encrypted = []
for c in flag:
    key = LFSR(key)
    encrypted.append(ord(c) ^ (key & 0xff))

list1 = [186, 129, 71, 182, 123, 98, 225, 89, 234, 255, 171, 118, 85, 23, 85, 99, 15, 214, 193, 101, 42, 140, 19, 5, 8,
         201, 241, 228, 112, 36, 91, 147]
key = 0xf34b7cd59a31a3
for i in list1:
    key = LFSR(key)
    print(chr(i ^ (key & 0xff)), end='')

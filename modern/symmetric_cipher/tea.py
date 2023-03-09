from ctypes import *


def encrypt(v, k):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    delta = 0x9e3779b9
    k0, k1, k2, k3 = k[0], k[1], k[2], k[3]

    total = c_uint32(0)
    for i in range(32):
        total.value += delta
        v0.value += ((v1.value << 4) + k0) ^ (v1.value + total.value) ^ ((v1.value >> 5) + k1)
        v1.value += ((v0.value << 4) + k2) ^ (v0.value + total.value) ^ ((v0.value >> 5) + k3)

    return v0.value, v1.value


def decrypt(v, k):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    delta = 0x9e3779b9
    k0, k1, k2, k3 = k[0], k[1], k[2], k[3]

    total = c_uint32(delta * 32)
    for i in range(32):
        v1.value -= ((v0.value << 4) + k2) ^ (v0.value + total.value) ^ ((v0.value >> 5) + k3)
        v0.value -= ((v1.value << 4) + k0) ^ (v1.value + total.value) ^ ((v1.value >> 5) + k1)
        total.value -= delta

    return v0.value, v1.value


# test
if __name__ == "__main__":
    # 待加密的明文，两个32位整型，即64bit的明文数据
    value = [0x12345678, 0x78563412]
    # 四个key，每个是32bit，即密钥长度为128bit
    key = [0x1, 0x2, 0x3, 0x4]

    print("Data is : ", hex(value[0]), hex(value[1]))
    res = encrypt(value, key)
    print("Encrypted data is : ", hex(res[0]), hex(res[1]))
    res = decrypt(res, key)
    print("Decrypted data is : ", hex(res[0]), hex(res[1]))
"""
Data is :  0x12345678 0x78563412
Encrypted data is :  0x9a65a69a 0x67ed00f6
Decrypted data is :  0x12345678 0x78563412
"""

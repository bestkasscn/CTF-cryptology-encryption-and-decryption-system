"""
-------------------------------------------------
@FileName:tea.py
@Description:TEA算法
@Author:bestkasscn
@Time:2023/3/21
@Principle: TEA（Tiny Encryption Algorithm）是一个基于对称密钥的轻量级加密算法，
由 David Wheeler 和 Roger Needham 在 1994 年提出。TEA 算法使用 64 位数据块和 128 位密钥，
采用分组密码的模式进行加密。TEA 的主要优点是其简单、紧凑且易于实现，特别适合需要低资源消耗的加密场景。

TEA 算法的工作原理如下：

1. 将 64 位明文数据块分为两部分，左半部分为 v0，右半部分为 v1。
2. 将 128 位密钥分为四个 32 位子密钥（K0，K1，K2，K3）。
3. 选择一个常量 delta（0x9e3779b9），这是一个特殊的常数，它是黄金比例的倒数乘以 2^32。
4. 进行 32 轮加密操作（默认轮数为 32，可以根据需要调整）： a. 将 delta 累加到一个名为 sum 的变量中。 b. 使用以下加密操作更新 v0 和 v1：
   - v0 = v0 + (((v1 << 4) + K0) ^ (v1 + sum) ^ ((v1 >> 5) + K1))
   - v1 = v1 + (((v0 << 4) + K2) ^ (v0 + sum) ^ ((v0 >> 5) + K3)) c. 每轮完成后，v0 和 v1 分别用于下一轮操作。
5. 将 v0 和 v1 拼接成一个 64 位密文数据块。
-------------------------------------------------
@TestCase:
plaintext = "NSSCTF{this_is_a_test_flag}"
key = generate_random_key(16)  # 16-byte key

ciphertext = TEA_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = TEA_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
@Status:已测试
-------------------------------------------------
"""
import struct
from utils import *


def TEA_encrypt(plaintext: str, key: bytes) -> bytes:
    key_ints = struct.unpack(">4I", key)
    plaintext_blocks = to_byte_blocks(plaintext)
    ciphertext_blocks = []

    for block in plaintext_blocks:
        v0, v1 = struct.unpack(">2I", block.encode("utf-8"))
        delta = 0x9e3779b9
        sum_ = 0

        for _ in range(32):
            sum_ = (sum_ + delta) & 0xffffffff
            v0 += ((v1 << 4) + key_ints[0]) ^ (v1 + sum_) ^ ((v1 >> 5) + key_ints[1])
            v0 &= 0xffffffff
            v1 += ((v0 << 4) + key_ints[2]) ^ (v0 + sum_) ^ ((v0 >> 5) + key_ints[3])
            v1 &= 0xffffffff

        ciphertext_blocks.append(struct.pack(">2I", v0, v1))

    return b''.join(ciphertext_blocks)


def TEA_decrypt(ciphertext: bytes, key: bytes) -> str:
    key_ints = struct.unpack(">4I", key)
    ciphertext_blocks = to_byte_blocks(ciphertext.decode("latin1"))
    plaintext_blocks = []

    for block in ciphertext_blocks:
        v0, v1 = struct.unpack(">2I", block.encode("latin1"))
        delta = 0x9e3779b9
        sum_ = (delta * 32) & 0xffffffff

        for _ in range(32):
            v1 -= ((v0 << 4) + key_ints[2]) ^ (v0 + sum_) ^ ((v0 >> 5) + key_ints[3])
            v1 &= 0xffffffff
            v0 -= ((v1 << 4) + key_ints[0]) ^ (v1 + sum_) ^ ((v1 >> 5) + key_ints[1])
            v0 &= 0xffffffff
            sum_ -= delta

        plaintext_blocks.append(struct.pack(">2I", v0, v1))

    return from_byte_blocks(plaintext_blocks)

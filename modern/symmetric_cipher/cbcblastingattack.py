"""
-------------------------------------------------
@FileName:cbcblastingattack.py
@Description:CBC字节翻转攻击
@Author:bestkasscn
@Time:2023/3/19
@Principle: 
-------------------------------------------------
@TestCase:
@Status:
-------------------------------------------------
"""


def bytes_xor(a: bytes, b: bytes) -> bytes:
    """计算两个字节字符串的逐元素异或结果"""
    return bytes(i ^ j for i, j in zip(a, b))


def get_last_byte(known_bytes: bytes, cipher: bytes, iv: bytes, encrypt_func: callable) -> tuple:
    """
    尝试找到“known_bytes + ?”的最后一个字节，使得Ek（known_bytes + ？）等于“cipher”。
    返回元组，包括找到的字节和新的IV值。
    """
    for i in range(256):
        # 将候选字节与已知字节进行异或运算
        candidate_bytes = known_bytes + bytes([i])
        # 将候选字节与IV进行异或运算
        xored_bytes = bytes_xor(iv, candidate_bytes)
        # 加密得到新的IV和密文
        result_bytes = encrypt_func(xored_bytes)
        iv = result_bytes[-16:]
        # 判断加密结果的前16个字节是否与给定的密文相同
        if result_bytes[:16] == cipher:
            return bytes([i]), iv
    return None


def cbc_blasting_attack(n_blocks: int, iv: bytes, encrypt_func: callable) -> bytes:
    """
    对CBC模式下的块加密算法进行爆破攻击，恢复明文。
    n_blocks: 明文的块数
    iv: CBC模式下的初始向量
    encrypt_func: 块加密函数
    返回恢复的明文
    """
    plaintext = b""
    # 从最后一个明文块开始，逐个块地进行操作
    for block_num in range(n_blocks - 1, -1, -1):
        # flag变量存储已恢复的明文
        flag_bytes = plaintext
        # 从块的最后一个字节开始，逐个字节地进行操作
        for byte_num in range(15, -1, -1):
            # 确定需要对flag_bytes进行异或运算的起始和结束位置
            start_idx = byte_num if block_num == n_blocks - 1 else byte_num + 1
            end_idx = byte_num + 1 if block_num == 0 else 16
            xored_bytes = b"\x00" * (16 - end_idx) + bytes_xor(iv[start_idx:end_idx], flag_bytes[start_idx:end_idx])
            # 如果当前块是第一个块，则使用IV和当前块的最后一个字节作为参数调用get_last_byte
            if block_num == n_blocks - 1:
                last_byte = iv[byte_num:byte_num + 1]
                cipher_bytes = encrypt_func(iv)
            # 否则，使用前一个块和当前块作为参数调用get_last_byte
            else:
                start_idx = block_num * 16
                last_byte = plaintext[start_idx + byte_num:start_idx + byte_num + 1]
                cipher_bytes = encrypt_func(plaintext[start_idx:start_idx + 16])
            # 使用get_last_byte恢复当前块的最后一个
            byte, iv = get_last_byte(xored_bytes, cipher_bytes, iv, encrypt_func)
            # 将找到的字节与上一个块的最后一个字节进行异或运算，并添加到flag_bytes中
            flag_bytes += bytes([byte[0] ^ last_byte[0]])
            # 将当前块的明文添加到plaintext中
        plaintext = flag_bytes + plaintext
        return plaintext


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

from Crypto.Cipher import AES
from Crypto.Util import Padding
import os


def test_cbc_blasting_attack():
    key = os.urandom(16)
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    message = b'Hello, world!' * 10
    padded_message = Padding.pad(message, AES.block_size)
    ciphertext = encryptor.encrypt(padded_message)

    plaintext = cbc_blasting_attack(len(ciphertext) // 16, iv, lambda x: encryptor.encrypt(x))
    unpadded_plaintext = Padding.unpad(plaintext, AES.block_size)
    assert unpadded_plaintext == message, f'Incorrect decryption: {unpadded_plaintext}'


test_cbc_blasting_attack()

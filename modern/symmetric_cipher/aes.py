"""
-------------------------------------------------
@FileName:aes.py
@Description:Advanced Encryption Standard对称加密算法
@Author:bestkasscn
@Time:2023/3/18
@Principle: AES（Advanced Encryption Standard）是一种对称加密算法，使用相同的密钥进行加密和解密。
AES是一种块密码（Block Cipher）算法，将明文分为固定大小的块，并使用密钥将每个块加密。

AES算法中，密钥的长度可以是128比特、192比特或256比特，分别对应AES-128、AES-192和AES-256三种加密方式。
AES算法的核心是四个基本操作：SubBytes、ShiftRows、MixColumns和AddRoundKey。

SubBytes操作：使用一个S盒（Substitution Box）对每个字节进行替换，这个S盒是由一个固定的置换表构成的。SubBytes操作混淆了明文的字节，增加了加密的强度。

ShiftRows操作：将每个字节所在的行循环移位，每一行移位的数量不同。这个操作使得每个块中的字节位置发生改变，增加了加密的复杂度。

MixColumns操作：对每一列进行线性变换，使得每个字节与其他字节之间产生一定的关系，增加了加密的强度。

AddRoundKey操作：将当前块与密钥进行按位异或运算，将密钥的信息与当前块混合在一起，增加了加密的强度。

AES算法将这四个基本操作循环执行多次，每次执行称为一个“轮（Round）”，每种AES加密方式的轮数不同。
在最后一轮，SubBytes和ShiftRows操作仍然会执行，但是MixColumns操作会被省略，最后只进行AddRoundKey操作。这样，得到的密文就是经过AES加密后的结果。
-------------------------------------------------
@TestCase:
key = '0123456789abcdef'
plaintext = 'Hello, world!'
mode = 'OFB'
iv = b'\x00' * 16

ciphertext = aes_encrypt(plaintext, key, mode, iv)
decrypted_text = aes_decrypt(ciphertext, key, mode, iv)

print("明文:", plaintext)
print("加密后的密文:", ciphertext)
print("解密后的明文:", decrypted_text)
print('-' * 50)
@Status:已测试
-------------------------------------------------
"""

import base64
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def aes_encrypt(plaintext: str, key: str, mode: str = 'CBC', iv: bytes = None) -> str:
    """
    AES加密函数
    :param plaintext: 明文
    :param key: 密钥，必须为16、24或32字节长度
    :param mode: 加密模式，可选 ECB、CBC、CFB、OFB，默认为CBC
    :param iv: 加密向量，必须为16字节长度，如果不传则由函数生成
    :return: 密文
    """
    if len(key) not in (16, 24, 32):
        raise ValueError("AES密钥长度必须为16、24或32字节长度")

    if mode not in ('ECB', 'CBC', 'CFB', 'OFB'):
        raise ValueError("加密模式必须为 ECB、CBC、CFB 或 OFB")

    # 使用标准的PKCS#7填充方案对明文进行填充
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext = plaintext + chr(padding_length) * padding_length
    cipher = None
    if mode == 'ECB':
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    else:
        if iv is None:
            iv = os.urandom(16)  # 生成随机的16字节iv
        elif len(iv) != 16:
            raise ValueError("加密向量长度必须为16字节长度")

        if mode == 'CBC':
            cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        elif mode == 'CFB':
            cipher = AES.new(key.encode('utf-8'), AES.MODE_CFB, iv)
        elif mode == 'OFB':
            cipher = AES.new(key.encode('utf-8'), AES.MODE_OFB, iv)

    # 加密明文并使用base64编码
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')


def aes_decrypt(ciphertext: str, key: str, mode: str = 'CBC', iv: bytes = None) -> str:
    """
    AES解密函数
    :param ciphertext: 密文
    :param key: 密钥，必须为16、24或32字节长度
    :param mode: 加密模式，可选 ECB、CBC、CFB、OFB，默认为CBC
    :param iv: 初始化向量，必须为16字节长度，如果未指定则随机生成
    :return: 明文
    """
    if len(key) not in (16, 24, 32):
        raise ValueError("AES密钥长度必须为16、24或32字节长度")

    if mode not in ('ECB', 'CBC', 'CFB', 'OFB'):
        raise ValueError("加密模式必须为 ECB、CBC、CFB 或 OFB")

    if iv is None:
        # 生成随机初始化向量
        iv = os.urandom(16)
    elif len(iv) != 16:
        raise ValueError("初始化向量长度必须为16字节长度")

    # 使用base64将密文转化为二进制字符串
    def b64decode(s: str) -> bytes:
        return base64.b64decode(s)

    cipher = None
    # 根据加密模式选择不同的方法进行解密
    if mode == 'ECB':
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    elif mode == 'CBC':
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv=iv)
    elif mode == 'CFB':
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CFB, iv=iv)
    elif mode == 'OFB':
        cipher = AES.new(key.encode('utf-8'), AES.MODE_OFB, iv=iv)

    plaintext = cipher.decrypt(b64decode(ciphertext))
    plaintext = unpad(plaintext, AES.block_size)

    # 返回解密后的明文
    return plaintext.decode('utf-8')



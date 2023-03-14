"""
-------------------------------------------------
@FileName:des.py
@Description:Data Encryption Standard对称加密算法
@Author:bestkasscn
@Time:2023/3/13
@Principle: DES（Data Encryption Standard）是一种对称加密算法，使用相同的密钥进行加密和解密。其加密原理如下：

1.初始置换（Initial Permutation）：将明文按照指定顺序进行置换，得到一个初始的 64 位二进制数据块。

2.轮函数（Round Function）：将 64 位明文分成左右两个 32 位的数据块，然后对右边的 32 位进行扩展置换（Expansion Permutation），使其变成 48 位。

3.密钥混合（Key Mixing）：将 48 位的扩展数据块和一个 48 位的子密钥进行异或运算，得到一个 48 位的结果。

4.S盒代替（S-Box Substitution）：将上一步的 48 位结果分成 8 个 6 位的数据块，然后使用 8 个不同的 S 盒（Substitution Box）进行代替，将每个 6 位数据块映射为 4 位数据块。

5.置换运算（Permutation）：将上一步得到的 32 位数据块按照指定的置换表进行置换，得到一个新的 32 位数据块。

6.左右交换（Swap）：将上一步得到的 32 位数据块与左边的 32 位数据块进行异或运算，然后将左右两个 32 位数据块互换，进行下一轮的运算。

经过 16 轮的运算，最后将左右两个 32 位数据块按照指定的逆置换进行置换，得到最终的 64 位密文。

解密的过程与加密的过程类似，只是在轮函数中使用的子密钥需要按照相反的顺序使用，最终得到原始明文。

DES一共有五种加密模式，分别是：

ECB（Electronic Codebook）电子密码本模式：
将明文分成固定长度的块，每个块独立加密，不需要保存上一个块的加密结果。
该模式简单易实现，但不能保证机密性和完整性，因为相同的明文块加密后得到的密文块相同，因此容易受到攻击。

CBC（Cipher Block Chaining）加密块链模式：
将前一个块的加密结果与当前块进行异或运算，再进行加密，这样相同的明文块在不同的块中加密后得到的密文块也不同，提高了安全性。
但该模式不能并行处理，因为需要依赖前一个块的加密结果。

CFB（Cipher Feedback）加密反馈模式：
将前一个块的加密结果作为密钥，对当前块进行加密，然后将加密结果与明文异或得到密文，
再将密文的前几位作为下一个块的加密密钥，这样可以实现流式加密，提高了灵活性和效率。

OFB（Output Feedback）输出反馈模式：
将前一个块的加密结果作为密钥，对当前块进行加密，得到一个随机的伪随机数流，
然后将该流与明文异或得到密文，该模式也可以实现流式加密，但不需要依赖前一个块的加密结果。

CTR（Counter）计数器模式：
将明文块与计数器进行异或运算，得到一个随机数流，
然后将该流与密钥进行加密，得到密文，该模式可以并行处理，适合于高速数据传输。
-------------------------------------------------
@TestCase:
key = b'secretke'
plaintext = b'hello world'
mode = 'CBC'
iv = b'initialv'

ciphertext = des_encrypt(key, plaintext, mode, iv)
print('密文:', ciphertext)

decrypted = des_decrypt(key, ciphertext, mode, iv)
print('明文:', decrypted)
@Status:已测试
-------------------------------------------------
"""

from Crypto.Cipher import DES
from Crypto.Util import Counter
from Crypto.Util.Padding import pad, unpad


def des_encrypt(key: bytes, plaintext: bytes, mode: str, iv=None) -> bytes:
    """
    DES加密函数，对明文进行加密操作。

    :param key: 加密密钥，必须为8个字节（64位）。
    :param plaintext: 明文数据，必须是字节串类型。
    :param mode: 加密模式，包括ECB、CBC、CFB、OFB和CTR。
    :param iv: 初始化向量，仅在使用CBC、CFB、OFB和CTR模式时需要提供。
    :return: 加密后的密文，返回字节串类型。
    """
    if mode == 'ECB':
        des = DES.new(key, DES.MODE_ECB)
    elif mode == 'CBC':
        des = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)
    elif mode == 'CFB':
        des = DES.new(key, DES.MODE_CFB, iv, segment_size=8)
    elif mode == 'OFB':
        des = DES.new(key, DES.MODE_OFB, iv)
    elif mode == 'CTR':
        nonce = iv if iv else b'\x00' * 8
        ctr = Counter.new(64, prefix=nonce)
        des = DES.new(key, DES.MODE_CTR, counter=ctr)
    else:
        raise ValueError('Invalid mode')

    ciphertext = des.encrypt(pad(plaintext, block_size=8))
    return ciphertext


def des_decrypt(key: bytes, ciphertext: bytes, mode: str, iv=None) -> bytes:
    """
    DES解密函数，对密文进行解密操作。

    :param key: 解密密钥，必须为8个字节（64位）。
    :param ciphertext: 密文数据，必须是字节串类型。
    :param mode: 解密模式，包括ECB、CBC、CFB、OFB和CTR。
    :param iv: 初始化向量，仅在使用CBC、CFB、OFB和CTR模式时需要提供。
    :return: 解密后的明文，返回字节串类型。
    """
    if mode == 'ECB':
        des = DES.new(key, DES.MODE_ECB)
    elif mode == 'CBC':
        des = DES.new(key, DES.MODE_CBC, iv)
    elif mode == 'CFB':
        des = DES.new(key, DES.MODE_CFB, iv, segment_size=8)
    elif mode == 'OFB':
        des = DES.new(key, DES.MODE_OFB, iv)
    elif mode == 'CTR':
        nonce = iv if iv else b'\x00' * 8
        ctr = Counter.new(64, prefix=nonce)
        des = DES.new(key, DES.MODE_CTR, counter=ctr)
    else:
        raise ValueError('Invalid mode')

    plaintext = unpad(des.decrypt(ciphertext), block_size=8)
    return plaintext

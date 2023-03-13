"""
-------------------------------------------------
@FileName:affine.py
@Description:仿射密码
@Author:bestkasscn
@Time:2023/2/5
@Principle: 仿射密码是一种经典的加密方法，其加解密原理如下：

加密： 设 $m$ 为字母表的大小（一般为 $26$），$a$ 为加密时用到的一个常数，
要求 $a$ 与 $m$ 互质，$b$ 为加密时用到的另一个常数，可以是任意整数。对于明文中的每个字母 $x$，
计算 $(ax+b)\bmod m$，得到密文中的对应字母 $y$。

解密： 首先求出 $a$ 的逆元 $a^{-1}$，
即满足 $a \times a^{-1} \equiv 1 \pmod{m}$ 的整数 $a^{-1}$。
然后对于密文中的每个字母 $y$，计算 $a^{-1} \times (y-b) \bmod m$，得到明文中的对应字母 $x$。

需要注意的是，加密和解密时使用的 $a$ 和 $b$ 值必须相同，否则无法正确解密。
此外，如果使用的字母表大小 $m$ 不同，则也需要使用不同的 $a$ 和 $b$ 值。
-------------------------------------------------
@TestCase:
plaintext = 'this is a test flag'
a = 7
b = 12
ciphertext = affine_encrypt(plaintext, a, b)
print(ciphertext)
print(affine_decrypt(ciphertext, a, b))
@Status:已测试
-------------------------------------------------
"""
import gmpy2
from string import ascii_uppercase,ascii_lowercase


def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    """
    Affine encryption
    :param plaintext:明文
    :param a:要求与字母表大小（通常为26）互质
    :param b:任意整数
    :return:密文
    """
    ciphertext = ""
    for c in plaintext:
        if c in ascii_uppercase:
            ciphertext += chr(((ord(c) - 65) * a + b) % 26 + 65)
        elif c in ascii_lowercase:
            ciphertext += chr(((ord(c) - 97) * a + b) % 26 + 97)
        else:
            ciphertext += c
    return ciphertext


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    """
    Affine decryption
    :param ciphertext:密文
    :param a:要求与字母表大小（通常为26）互质
    :param b:任意整数
    :return:
    """
    plaintext = ""
    a_inv = gmpy2.invert(a, 26)
    for c in ciphertext:
        if c in ascii_uppercase:
            plaintext += chr((ord(c) - 65 - b) * a_inv % 26 + 65)
        elif c in ascii_lowercase:
            plaintext += chr((ord(c) - 97 - b) * a_inv % 26 + 97)
        else:
            plaintext += c
    return plaintext



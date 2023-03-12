"""
-------------------------------------------------
@FileName:vigenere.py
@Description:维吉尼亚密码
@Author:bestkasscn
@Time:2023/3/11
@Principle:
维吉尼亚密码（Vigenère cipher）是一种多表替换密码（polyalphabetic substitution cipher），
与凯撒密码类似，但更加复杂和安全。该密码使用了一系列不同的凯撒密码，按照特定的方式组合在一起，使得破解者很难通过简单的频率分析来破解密码。

在维吉尼亚密码中，使用一个密钥字符串（称为密钥词）来对明文进行加密。
密钥词与明文一一对应，对于每个明文字符，都会使用不同的凯撒密码进行替换。具体地，使用密钥词中每个字符对应的凯撒密码，
按顺序对明文中的每个字符进行替换。如果密钥词的长度小于明文长度，就将密钥词重复使用，直到与明文等长为止。

因为维吉尼亚密码使用了多个凯撒密码，所以破解者需要知道密钥词的长度和内容，才能进行破解。
即使破解者知道了某个凯撒密码的内容，也不一定能够得到其他凯撒密码的信息，从而无法还原出整个密文。
-------------------------------------------------
@TestCase:
plaintext = 'this is a test flag'
key = 'nss'
print(vigenere_encrypt(plaintext, key))
@Status:已测试
-------------------------------------------------
"""

from string import ascii_uppercase, ascii_lowercase


def vigenere_encrypt(plaintext: str, key: str) -> str:
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char in ascii_uppercase:
            # 计算偏移量
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            # 加密字符
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        elif char in ascii_lowercase:
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('a')
            # 加密字符
            ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char in ascii_uppercase:
            # 计算偏移量
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            # 解密字符
            plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        elif char in ascii_lowercase:
            # 计算偏移量
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('a')
            # 解密字符
            plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            plaintext += char
    return plaintext

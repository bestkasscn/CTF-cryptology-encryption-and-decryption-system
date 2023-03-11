"""
-------------------------------------------------
@FileName:vigenere.py
@Description:维吉尼亚密码
@Author:bestkasscn
@Time:2023/3/11
@Principle:
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

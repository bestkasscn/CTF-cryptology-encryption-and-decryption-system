"""
-------------------------------------------------
@FileName:rot.py
@Description:rot5,13,18,47
@Author:bestkasscn
@Time:2023/1/10
@Principle:ROT密码是一种简单的加密方法，也称为“字母转换密码”。
其原理是通过按照一定的规律对明文中的每个字母进行替换来生成密文。

ROT密码中的“ROT”代表“rotate”，意为“旋转”。
具体来说，ROT密码通过将明文中的每个字母按照字母表中的顺序向后“旋转”一定数量的位置来进行加密。
例如，ROT13加密方法将明文中的每个字母向后“旋转”13个位置，即A替换成N，B替换成O，C替换成P，以此类推。
-------------------------------------------------
@TestCase:
# 测试ROT47加密
plaintext = "Hello, world!"
ciphertext = rot47_encrypt(plaintext)
print("加密后的密文为：", ciphertext)

# 测试ROT47解密
decrypted_text = rot47_decrypt(ciphertext)
print("解密后的明文为：", decrypted_text)
@Status:已测试
-------------------------------------------------
"""


def rot5_encrypt(plaintext: str) -> str:
    ciphertext = ""
    for c in plaintext:
        if c.isdigit():
            new_digit = (int(c) + 5) % 10
            ciphertext += str(new_digit)
        else:
            ciphertext += c
    return ciphertext


def rot5_decrypt(ciphertext: str) -> str:
    plaintext = ""
    for c in ciphertext:
        if c.isdigit():
            new_digit = (int(c) - 5) % 10
            plaintext += str(new_digit)
        else:
            plaintext += c
    return plaintext


def rot13_encrypt(plaintext: str) -> str:
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 + 13) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 + 13) % 26 + 97
            ciphertext += chr(new_ascii)
        else:
            ciphertext += c
    return ciphertext


def rot13_decrypt(ciphertext: str) -> str:
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 - 13) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 - 13) % 26 + 97
            plaintext += chr(new_ascii)
        else:
            plaintext += c
    return plaintext


def rot18_encrypt(plaintext: str) -> str:
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 + 18) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 + 18) % 26 + 97
            ciphertext += chr(new_ascii)
        else:
            ciphertext += c
    return rot5_encrypt(rot13_encrypt(plaintext))


def rot18_decrypt(ciphertext: str) -> str:
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 - 18) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 - 18) % 26 + 97
            plaintext += chr(new_ascii)
        else:
            plaintext += c
    return rot5_decrypt(rot13_decrypt(ciphertext))


def rot47_encrypt(plaintext: str) -> str:
    ciphertext = ""
    for c in plaintext:
        if 33 <= ord(c) <= 126:
            ciphertext += chr((ord(c) - 33 + 47) % 94 + 33)
        else:
            ciphertext += c
    return ciphertext


def rot47_decrypt(ciphertext: str) -> str:
    plaintext = ""
    for c in ciphertext:
        if 33 <= ord(c) <= 126:
            plaintext += chr((ord(c) - 33 - 47) % 94 + 33)
        else:
            plaintext += c
    return plaintext



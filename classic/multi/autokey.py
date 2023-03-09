"""
-------------------------------------------------
@FileName:autokey.py
@Description:Autokey加密算法是一种多表密码（Polyalphabetic Cipher）算法
@Author:bestkasscn
@Time:2023/3/5
@Principle: Autokey加密算法是一种多表密码（Polyalphabetic Cipher）算法，
它通过使用明文本身中的字符作为密钥的一部分，从而消除了像维吉尼亚密码那样的周期性密钥。

具体来说，Autokey算法中，密钥不是固定的，而是随着明文的加密而不断增长。
首先，从密钥中取出一个固定长度的字符串，称之为“种子”（seed），作为加密过程的起始密钥。
接着，使用该密钥对明文进行加密。加密时，使用明文中的一个字符与密钥中的一个字符相加，然后将该值作为密文中的一个字符。
使用的明文字符和密钥字符都要从表格中查找。

在每个新的字符加密之后，将该字符添加到密钥的末尾，形成一个新的密钥。
因此，后续加密过程中使用的密钥将会包含明文中前面加密过的字符。

解密过程中，同样使用明文字符和密钥字符相减的方式，再查表格得到明文字符。

Autokey算法的安全性依赖于密钥的长度，因此密钥必须足够长。然而，如果密钥太长，那么加密和解密的效率将会降低。
因此，在实际应用中，需要根据需要平衡密钥长度和效率。
-------------------------------------------------
@TestCase:
key = 'KEY'
plaintext = 'HELLO WORLD'
ciphertext = autokey_encrypt(key, plaintext)
res = autokey_decrypt(key, ciphertext)
print(ciphertext)
print(res)
@Status:已测试
-------------------------------------------------
"""


def autokey_encrypt(key: str, plaintext: str) -> str:
    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = []
    for i, c in enumerate(plaintext):
        if c == ' ':
            ciphertext.append(' ')
            continue
        k = ord(key[i % len(key)]) - ord('A')
        c = chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        ciphertext.append(c)
        key += c if i < len(plaintext) - 1 else plaintext[i]
    return ''.join(ciphertext)


def autokey_decrypt(key: str, ciphertext: str) -> str:
    key = key.upper()
    plaintext = []
    for i, c in enumerate(ciphertext):
        if c == ' ':
            plaintext.append(' ')
            continue
        k = ord(key[i % len(key)]) - ord('A')
        c = chr((ord(c) - ord('A') - k + 26) % 26 + ord('A'))
        plaintext.append(c)
        key += ciphertext[i] if i < len(ciphertext) - 1 else plaintext[i]
    return ''.join(plaintext)

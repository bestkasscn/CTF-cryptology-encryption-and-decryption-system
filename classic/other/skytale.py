"""
-------------------------------------------------
@FileName:skytale.py
@Description:云影密码
@Author:bestkasscn
@Time:2023/3/11
@Principle: 云影密码是一种古老的密码算法，它基于将文本围绕一根棒子上卷，然后从棒子上取下来的顺序来加密和解密文本。
具体而言，该算法将明文分成多行，然后将每行字符从左到右写在一个棒子上，然后将棒子拿下来，
以从上到下的顺序读取所有字符，以此生成密文。解密的过程是将密文放回原来的棒子上，并以从左到右的顺序读取所有字符，以此生成明文。
-------------------------------------------------
@TestCase:
plaintext = 'this is a test flag'
key = 3
ciphertext = skyTale_encrypt(plaintext, key)
print(ciphertext)
print(skyTale_decrypt(ciphertext, key))
@Status:已测试
-------------------------------------------------
"""


def skyTale_encrypt(plaintext: str, key: int) -> str:
    plaintext = plaintext.replace(" ", "").replace("\n", "")
    rows = (len(plaintext) + key - 1) // key
    padding = rows * key - len(plaintext)
    plaintext += "X" * padding
    ciphertext = ""
    for i in range(key):
        for j in range(rows):
            ciphertext += plaintext[j * key + i]
    return ciphertext


def skyTale_decrypt(ciphertext: str, key: int) -> str:
    rows = (len(ciphertext) + key - 1) // key
    plaintext = ""
    for i in range(rows):
        for j in range(key):
            index = j * rows + i
            if index < len(ciphertext):
                plaintext += ciphertext[index]
    return plaintext

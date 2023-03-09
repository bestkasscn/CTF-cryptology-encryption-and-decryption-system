"""
-------------------------------------------------
@FileName:adfgx.py
@Description:ADFGX密码是一种基于多表置换和替代的密码技术
@Author:bestkasscn
@Time:2023/2/7
@principle:ADFGX密码是一种基于多表置换和替代的密码技术，由德国陆军在一战期间使用。
-------------------------------------------------
@TestCase:
key = 'PHQGMEAYNOKSFBDLRCIVUXWTZ'
keyword = 'SPRING'

plaintext = 'HELLO WORLD'

# 加密
ciphertext = ADFGX(key, keyword).encipher(plaintext)

# 解密
decryptedtext = ADFGX(key, keyword).decipher(ciphertext)

print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decryptedtext: ", decryptedtext)

@Status:已测试
-------------------------------------------------
其加密过程如下：

生成一个 5x5 的多表，包含字母 A-Z 和数字 0-9。在此基础上，加上字母 ADFGX。

将明文转换为大写字母，并且将 I/J 视为一个字符。然后使用多表中的字母进行置换，例如，字母 A 用 ADFGX 代替，字母 B 用 ADGGX 代替，以此类推。

将替换后的字母分组为两个一组，并将它们在多表中找到相应的行和列。这样就得到了一对坐标，即 ADFGX 字母对应的行和列。这两个坐标就是密文的一组。

重复步骤 2 和 3 直到整个明文都被转换成密文。

解密过程与加密过程类似，只需要反向应用多表的置换和替换规则即可。

"""
from pycipher import ADFGX


def adfgx_encrypt(plaintext: str, key: str, keyword: str) -> str:
    return ADFGX(key, keyword).encipher(plaintext)


def adfgx_decrypt(ciphertext: str, key: str, keyword: str) -> str:
    return ADFGX(key, keyword).decipher(ciphertext)


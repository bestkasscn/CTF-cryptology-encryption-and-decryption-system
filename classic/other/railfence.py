"""
-------------------------------------------------
@FileName:railfence.py
@Description:栅栏密码
@Author:bestkasscn
@Time:2023/3/11
@Principle:
栅栏密码把要加密的明文分成 N 个一组，然后把每组的第 1 个字连起来，形成一段无规律的话。这里给出一个例子

```
明文：THERE IS A CIPHER
```

去掉空格后变为

```
THEREISACIPHER
```

分成两栏，两个一组得到

```
TH ER EI SA CI PH ER
```

先取出第一个字母，再取出第二个字母

```
TEESCPE
HRIAIHR
```

连在一起就是

```
TEESCPEHRIAIHR
```

上述明文也可以分为 2 栏。

```
THEREIS ACIPHER
```

组合得到密文

```
TAHCEIRPEHIESR
```


-------------------------------------------------
@TestCase:
plaintext = "HELLO WORLD"
key = 4

# 加密
ciphertext = railFence_w_encrypt(plaintext, key)
print("密文：", ciphertext)

# 解密
plaintext = railFence_w_decrypt(ciphertext, key)
print("明文：", plaintext)
@Status:已测试
-------------------------------------------------
"""
from pycipher.railfence import Railfence


def railFence_encrypt(plaintext: str, key: int) -> str:
    """
    :param plaintext: 明文
    :param key:大于0的整数
    :return:
    """
    return Railfence(key).encipher(plaintext)


def railFence_decrypt(ciphertext: str, key: int) -> str:
    """

    :param ciphertext:密文
    :param key: 大于0的整数
    :return:
    """
    return Railfence(key).decipher(ciphertext)


def railFence_w_encrypt(plaintext: str, key: int) -> str:
    rails = [[] for _ in range(key)]
    rail, delta = 0, 1
    for ch in plaintext:
        rails[rail].append(ch)
        if rail == 0:
            delta = 1
        elif rail == key - 1:
            delta = -1
        rail += delta
    ciphertext = ''.join([ch for rail in rails for ch in rail])
    return ciphertext


def railFence_w_decrypt(ciphertext: str, key: int) -> str:
    fence = [[None] * len(ciphertext) for _ in range(key)]
    rail, delta = 0, 1
    for i in range(len(ciphertext)):
        fence[rail][i] = 1
        if rail == 0:
            delta = 1
        elif rail == key - 1:
            delta = -1
        rail += delta
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if fence[i][j] == 1:
                fence[i][j] = ciphertext[index]
                index += 1
    rail, delta = 0, 1
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += fence[rail][i]
        if rail == 0:
            delta = 1
        elif rail == key - 1:
            delta = -1
        rail += delta
    return plaintext



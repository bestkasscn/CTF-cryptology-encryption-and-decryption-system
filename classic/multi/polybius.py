"""
-------------------------------------------------
@FileName:polybius.py
@Description:棋盘密码
@Author:bestkasscn
@Time:2023/3/9
@Principle: 棋盘密码（也称为方格密码）是一种简单的加密技术，用于对短文本进行加密。它得名于它的工作原理类似于在棋盘上移动棋子。

棋盘密码使用一个5×5的方格棋盘，其中每个方格填充了一个字母，通常是26个英文字母中的24个（字母"i"和"j"共用一个方格）。
在加密消息时，将明文分成双字母组，例如“hello”将被分为“he”、“ll”和“o”。然后，对于每个双字母组，执行以下步骤：

1. 如果双字母组中的两个字母相同，则在它们之间插入字母“x”（或“q”）来使它们不同。例如，“ll”会变成“lxl”。
2. 如果双字母组中的两个字母不同，则找到它们在棋盘上的位置。将它们替换为另一对字母，方法是沿着相同的行（或列）移动一个方格，
然后用该行（或列）中的下一个字母替换。如果该字母位于棋盘的边缘，则将其替换为该行（或列）的第一个字母。
例如，如果双字母组是“he”，并且在棋盘上，h位于第2行第1列，e位于第1行第2列，那么可以将“he”替换为“dw”。
3. 重复第2步，直到所有双字母组都已替换为新的双字母组。然后将所有双字母组连接起来，得到密文。

解密消息时，只需使用相反的过程，即找到双字母组在棋盘上的位置，并向左或向上移动一个方格，然后用该行或列中的前一个字母替换。

棋盘密码虽然简单，但已经被认为是不安全的加密方法。因此，现在很少用于实际的加密。
-------------------------------------------------
@TestCase:
key = 'phqgiumeaylnofdxkrcvstzwb'
plaintext = 'hello world'

ciphertext = polybius_encrypt(plaintext, key)
print(ciphertext)

decrypted_text = polybius_decrypt(ciphertext, key)
print(decrypted_text)
@Status:已测试
-------------------------------------------------
"""
from pycipher import PolybiusSquare


def polybius_encrypt(plaintext: str, key: str) -> str:
    """

    :param plaintext: 明文
    :param key:密钥必须是一个包含所有英文字母的字符串，且没有重复的字母。
    :return: 密文
    """
    polybius = PolybiusSquare(key)
    ciphertext = polybius.encipher(plaintext)
    return ciphertext


def polybius_decrypt(ciphertext: str, key: str) -> str:
    """

    :param ciphertext: 密文
    :param key: 密钥必须是一个包含所有英文字母的字符串，且没有重复的字母。
    :return: 明文
    """
    polybius = PolybiusSquare(key)
    plaintext = polybius.decipher(ciphertext)
    return plaintext

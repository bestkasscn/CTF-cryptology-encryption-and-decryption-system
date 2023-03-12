"""
-------------------------------------------------
@FileName:columnartransposition.py
@Description:列移位密码
@Author:bestkasscn
@Time:2023/3/11
@Principle:
列移位密码是一种简单的替换密码，也称为栅栏密码。
它的原理是将明文按照一定的规律分成若干列，然后将各列组成密文。
常见的规律是以一定的列数为周期，依次将明文中的字符分别填充到各列中。
填充完后，将各列按照规定的顺序连接起来就形成了密文。由于密文的每一列中的字符出现的位置被打乱，
因此可以增加密码的复杂度，增加破解的难度。对于较长的文本，为了加强加密强度，还可以多次重复上述过程，
使密文更为难以破解。但是，该密码的弱点在于当列数被确定之后，密文的排列规则也随之确定，只有在列数和排列规则都被破解之后，才能还原明文。
-------------------------------------------------
@TestCase:
plaintext = 'this is a test flag'
ciphertext = columnar_encrypt(plaintext, 'German')
print(columnar_encrypt(plaintext, 'German'))
print(columnar_decrypt(ciphertext, 'German'))
@Status:已测试
-------------------------------------------------
"""

from pycipher.columnartransposition import ColTrans


def columnar_encrypt(plaintext: str, key: str) -> str:
    return ColTrans(key).encipher(plaintext)


def columnar_decrypt(ciphertext: str, key: str) -> str:
    return ColTrans(key).decipher(ciphertext)


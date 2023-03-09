"""
-------------------------------------------------
@FileName:adfgvx.py
@Description:ADFGVX密码是一种基于置换和替换的加密方法
@Author:bestkasscn
@Time:2023/2/5
@principle: ADFGVX密码的加密过程包括以下步骤：

1.生成一个5x5的多表，其中包含字母A至Z和数字0至9，以及ADFGVX六个字母。
这个表是由一个密钥和一个加密单元共同生成的。

2.将明文分割成单个字母，然后用多表中的对应字母进行替换。
例如，字母A用ADFGVX替换，字母B用ADFGVX的下一个字母DF替换，以此类推。

3将替换后的字母分组，每组包含两个字母。
这些字母会在多表中找到对应的行和列，组成一个二维坐标，形成一个新的密文。

4.对于每个密文坐标，都用相应的ADFGVX字母来替换。
例如，坐标(3,4)用字母G替换，坐标(1,1)用字母A替换。

5.最后，将所有替换后的字母组合在一起，形成一个密文。

注意，这里的密钥必须包含 36 个不同的字符，否则程序会抛出异常。
-------------------------------------------------
@TestCase:
[{'key': 'IPY8XZ4GT7VRW5ENLO32MCSK910UJDFQ6HAB', 'plaintext': 'YMVGEHFZUA', 'ciphertext': 'DXVFDAVADXXFFXVGGGFA'},
{'key': 'GUAHTWXOD7SRV8M6FC14YLQIB2Z39P5KN0EJ', 'plaintext': 'LUEKJGSOFX', 'ciphertext': 'XAFGDVAGXDDDXDVAVAXD'},
{'key': '12M8DZWHUQN35J6G0ECSABVKITLRY7FO4X9P', 'plaintext': 'SQWFIRDHNB', 'ciphertext': 'DVDDAVGGXAGGADAGVDVD'}]

@Status:已测试
-------------------------------------------------
"""

from pycipher import ADFGVX
import random


def adfgvx_encrypt(key: str, plaintext: str) -> str:
    """

    :param key: 密钥必须包含 36 个不同的字符
    :param plaintext:
    :return:
    """
    cipher = ADFGVX(key)
    return cipher.encipher(plaintext)


def adfgvx_decrypt(key: str, ciphertext: str) -> str:
    """

    :param key: 密钥必须包含 36 个不同的字符
    :param ciphertext:
    :return:
    """
    cipher = ADFGVX(key)
    return cipher.decipher(ciphertext)


def generate_adfgvx_test_cases(times=None) -> list:
    """

    :param times:生成多少组测试用例
    :return:
    """
    # generate some test cases
    test_cases = []
    for i in range(times or 3):
        # generate key
        key = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 36))
        # generate plaintext and ciphertext
        plaintext = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 10))
        ciphertext = adfgvx_encrypt(key, plaintext)
        # add test case
        test_case = {
            'key': key,
            'plaintext': plaintext,
            'ciphertext': ciphertext
        }
        test_cases.append(test_case)
    return test_cases


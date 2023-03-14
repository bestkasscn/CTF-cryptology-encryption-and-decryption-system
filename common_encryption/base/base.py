"""
-------------------------------------------------
@FileName:base.py
@Description:base家族编解码算法
@Author:bestkasscn
@Time:2023/1/10
@Principle:
-------------------------------------------------
@TestCase:
@Status:
-------------------------------------------------
"""
import binascii
from base64 import *
import string
import base62
import base91
import pybase100

dir_base16 = '0123456789ABCDEF'
dir_base58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
dir_base61 = string.ascii_uppercase + string.ascii_lowercase + string.digits
table_base61 = {c: i for i, c in enumerate(dir_base61)}


def base16encode(plaintext: str):
    res = ''
    for s in plaintext:
        bin_1, bin_2 = bin(ord(s))[2:-4], bin(ord(s))[-4:]  # 将字符对应ascii码转成二进制
        res_1, res_2 = dir_base16[int(bin_1, 2)], dir_base16[int(bin_2, 2)]  # 与字典作映射
        res += ''.join(res_1 + res_2)
    return res


def base16decode(plaintext: str):
    plaintext = plaintext.upper()
    res = ''
    for i in range(0, len(plaintext), 2):
        bin_1, bin_2 = bin(dir_base16.index(plaintext[i])), bin(dir_base16.index(plaintext[i + 1]))[2:]
        while len(bin_2) != 4:
            bin_2 = '0' + bin_2  # 低位补齐4位
        res += ''.join(chr(int(bin_1 + bin_2, 2)))
    return res


def base32encode(plaintext: str):
    return b32encode(plaintext)


def base32decode(plaintext: str):
    return b32decode(plaintext)


def base58encode(plaintext: str):
    """
        base58编码典型应用是比特币钱包，与base64相比，去除了0、I、O、l、/ +等不易辨认的6个字符
        base58的编码思路是反复除以58取余数直至为0，base64的编码原理是64进制，2的6次方刚好等于64
        :param plaintext: 输入待编码的字符
        :return: base58的编码值
    """

    text_bin = ''
    res = ''
    for s in plaintext:
        s = bin(ord(s))[2:]
        while len(s) != 8:
            s = '0' + s  # 字符串转二进制
        text_bin += ''.join(s)
    text_decimal = int(text_bin, 2)
    res_list = []
    while True:
        res_list.insert(0, text_decimal % 58)  # 头插法
        text_decimal = text_decimal // 58
        if text_decimal == 0:
            break
    for i in res_list:
        res += dir_base58[i]
    return res


def base58decode(plaintext: str) -> str:
    """
    base58编码典型应用是比特币钱包，与base64相比，去除了0、I、O、l、/ +等不易辨认的6个字符
    :param plaintext: 输入base58编码值
    :return: base58的解码值
    """
    #  定义base58的58个编码
    cipher = plaintext
    #  检查密文字符的有效性，密文字符必须是base58中的字符，否则返回提示
    bad = ''
    for item in cipher:
        if dir_base58.find(item) == -1:
            bad += item
    if bad != '':
        return '不是有效的Base58编码，请仔留意如下字符：' + bad

    #    获取密文每个字符在base58中的下标值
    tmp = []
    for item in cipher:
        tmp.append(dir_base58.find(item))
    temp = tmp[0]
    for i in range(len(tmp) - 1):
        temp = temp * 58 + tmp[i + 1]
    temp = bin(temp).replace('0b', '')

    #   判断temp二进制编码数量能否被8整除，例如编码长度为18，首先截取（18%8）余数个字符求对应的ascii字符
    remainder = len(temp) % 8
    res = ''

    if remainder != 0:
        temp_start = temp[0:remainder]
        res = chr(int(temp[0:remainder], 2))

    for i in range(remainder, len(temp), 8):
        res += chr(int((temp[i:i + 8]), 2))
        i += 8
    return res


def base61encode(plaintext: str) -> str:
    # 将数据转换为整数
    num = int.from_bytes(plaintext, 'big')

    # 将整数转换为 Base61 编码字符串
    result = ''
    while num > 0:
        num, r = divmod(num, 61)
        result += dir_base61[r]
    return result[::-1]


def base61decode(plaintext: str) -> str:
    # 将 Base61 编码字符串转换为整数
    num = 0
    for c in plaintext:
        num = num * 61 + table_base61[c]

    # 将整数转换为字节数组
    length = (num.bit_length() + 7) // 8
    return num.to_bytes(length, 'big').decode()


def base62encode(plaintext: str):
    return base62.encode(plaintext)


def base62decode(plaintext: str):
    return base62.decode(plaintext)


def base64encode(plaintext: str, altchars=None):
    if altchars is None:
        return b64encode(plaintext).decode()
    else:
        return b64encode(plaintext, altchars=altchars).decode()


def base64decode(plaintext: str, altchars=None):
    if altchars is None:
        return b64decode(plaintext).decode()
    else:
        return b64decode(plaintext, altchars=altchars).decode('utf-8')


def base85encode(plaintext: str):
    return b85encode(plaintext)


def base85decode(plaintext: str):
    return b85decode(plaintext)


def base91encode(plaintext: str):
    return base91.encode(plaintext.encode())


def base91decode(plaintext: str):
    return base91.decode(plaintext)


def base100encode(plaintext: str):
    return pybase100.encode(plaintext)


def base100decode(plaintext: str):
    return pybase100.decode(plaintext)


def attack(plaintext: str, format: str) -> str:
    if format is None:
        format = 'flag{'
    if not isinstance(plaintext, str):
        raise TypeError("The plaintext argument must be a string.")
    while format not in plaintext:
        try:
            plaintext = b64decode(plaintext).decode()
        except (binascii.Error, UnicodeDecodeError):
            try:
                plaintext = b32decode(plaintext).decode()
            except (binascii.Error, UnicodeDecodeError):
                try:
                    plaintext = b16decode(plaintext).decode()
                except (binascii.Error, UnicodeDecodeError):
                    raise Exception("Unable to decode plaintext.")
    return plaintext


plaintext = 'NSSCTF{this_is_a_test_flag}'
print(base16encode(plaintext))

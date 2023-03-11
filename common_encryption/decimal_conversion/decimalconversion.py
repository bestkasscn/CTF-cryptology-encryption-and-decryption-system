"""
-------------------------------------------------
@FileName:decimalconversion.py
@Description:任意进制转换
@Author:bestkasscn
@Time:2023/3/11
@Principle:
-------------------------------------------------
@TestCase:print(dec_to_base(123, 3))
@Status:已测试
-------------------------------------------------
"""


def dec_to_base(number, base):
    """
    将十进制数转换为任意进制数
    :param number: 十进制数
    :param base: 要转换的进制数
    :return: 转换后的进制数
    """
    result = ""
    while number > 0:
        remainder = number % base
        if remainder < 10:
            result += str(remainder)
        else:
            result += chr(ord('A') + remainder - 10)
        number //= base
    return result[::-1] if result else "0"


def base_to_dec(number, base):
    """
    将任意进制数转换为十进制数
    :param number: 要转换的进制数
    :param base: 进制数的基数
    :return: 转换后的十进制数
    """
    result = 0
    power = 0
    for digit in number[::-1]:
        if digit.isdigit():
            result += int(digit) * base ** power
        else:
            result += (ord(digit.upper()) - ord('A') + 10) * base ** power
        power += 1
    return result



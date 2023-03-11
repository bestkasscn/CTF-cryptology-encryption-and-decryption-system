"""
-------------------------------------------------
@FileName:url.py
@Description:url编解码
@Author:bestkasscn
@Time:2023/3/11
@Principle: 
-------------------------------------------------
@TestCase:print(urldecode(urlencode(encoded)))
@Status:已测试
-------------------------------------------------
"""
from urllib.parse import unquote, quote

encoded = 'www.baidu.com/?key=this&value=that'


def url_encode(string: str, safe=None) -> str:
    """

    :param string:待编码的字符串
    :param safe:指定不需要进行编码的字符，如safe=','则逗号不会被编码
    :return:url编码后的字符串
    """
    return quote(string, safe)


def url_decode(string: str) -> str:
    return unquote(string)



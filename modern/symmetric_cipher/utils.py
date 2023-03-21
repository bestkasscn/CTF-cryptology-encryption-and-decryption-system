"""
-------------------------------------------------
@FileName:utils.py
@Description:工具类
@Author:bestkasscn
@Time:2023/3/21
@Principle: 
-------------------------------------------------
@TestCase:
@Status:
-------------------------------------------------
"""
import secrets
from typing import List


def generate_random_key(key_length=16):
    return secrets.token_bytes(key_length)


def to_byte_blocks(s: str, block_size: int = 8) -> List[str]:
    """
    将字符串按照指定块大小分块，不足的部分用'\0'补齐
    :param s: 待分块的字符串
    :param block_size: 块大小
    :return: 分块后的字符串列表
    """
    while len(s) % block_size != 0:
        s += '\0'
    return [s[i:i + block_size] for i in range(0, len(s), block_size)]


def from_byte_blocks(blocks: List[str]) -> str:
    """
    将分块后的字符串列表合并为一个字符串
    :param blocks: 分块后的字符串列表
    :return: 合并后的字符串
    """
    return b''.join(blocks).decode("utf-8").rstrip('\0')

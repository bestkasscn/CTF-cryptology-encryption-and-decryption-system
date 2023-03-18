"""
-------------------------------------------------
@FileName:proof.py
@Description:CTF工作量证明
@Author:bestkasscn
@Time:2023/3/18
@Principle: 这两个函数分别是生成工作量证明（Proof of Work）和执行 Proof of Work 的函数。
Proof of Work 是一种防止恶意攻击者耗尽服务器计算资源的技术，它通常被用于保护网络上的分布式系统。
-------------------------------------------------
@TestCase:
print(proof_of_work('6ichwbw5dkuisd1c', 'a3c546c35cc3ceb7f64d4ee80e6fb4c2cd40a29a56dd08a13b445ed4588f50bf'))
@Status:已测试
-------------------------------------------------
"""

import string
import random
import hashlib

default_alphabet = string.hexdigits[:16]
table = string.ascii_letters + string.digits


def generate_proof_of_work(
        proof_len: int = 20,  # 随机字符串 proof 的长度，默认为 20
        user_input_len: int = 4,  # 用户需要输入的字符串长度，默认为 4
        hash_func: callable = hashlib.sha256  # 哈希函数，默认为 hashlib.sha256
) -> bool:
    """
    这个函数的作用是生成一个工作量证明，即一个随机字符串 proof，它会与用户输入的字符串组合后进行哈希运算，得到一个哈希值 sha。
    用户需要在输入框中输入一个长度为 user_input_len 的字符串 XXXX，并与 proof 进行哈希运算得到一个新的哈希值，
    如果这个新的哈希值等于 sha，则说明用户完成了 Proof of Work。

    :param proof_len: 随机字符串 proof 的长度，默认为 20
    :param user_input_len: 用户需要输入的字符串长度，默认为 4
    :param hash_func: 哈希函数，默认为 hashlib.sha256
    :return: 如果用户输入的 XXXX 长度为 user_input_len，
    并且 sha256(XXXX + proof[user_input_len:]) 的哈希值等于 sha，则返回 True，否则返回 False
    """
    proof = ''.join([random.choice(table) for _ in range(proof_len)]).encode()
    sha = hash_func(proof).hexdigest().encode()
    print(proof)
    print(f"{hash_func.__name__[8:]} (XXXX + {proof[user_input_len:].decode()}) == {sha.decode()}")
    XXXX = input(f"Plz Tell Me {hash_func.__name__[8:]} ({user_input_len} chars): ").encode()
    if len(XXXX) != user_input_len or hash_func(XXXX + proof[user_input_len:]).hexdigest().encode() != sha:
        return False
    return True


def proof_of_work(user_input_len: int,  # 用户需要输入的字符串长度
                  salt: str,  # 要加盐的字符串
                  target_hash: str,  # 目标哈希值
                  hash_func: callable = hashlib.sha256  # 哈希函数，默认为 hashlib.sha256
                  ) -> str:
    """
    这个函数的作用是执行 Proof of Work，它会生成一个随机的前缀，
    将它添加到用户输入的字符串的前面，形成一个待加密的字符串，
    然后给这个字符串添加一个随机的盐，并使用指定的哈希函数计算出一个哈希值。
    如果计算出的哈希值等于目标哈希值，则返回前缀。否则，继续生成新的前缀并计算，直到找到一个满足条件的前缀。

    :param user_input_len: 用户需要输入的字符串长度
    :param salt: 要加盐的字符串
    :param target_hash: 目标哈希值
    :param hash_func: 哈希函数，默认为 hashlib.sha256
    :return: 返回生成的前缀
    """
    prefix = ''.join(
        random.choices(string.ascii_letters + string.digits, k=user_input_len))  # 随机生成长度为 user_input_len 的前缀
    while True:
        candidate = prefix + salt  # 添加盐生成待加密字符串
        hash_value = hash_func(candidate.encode()).hexdigest()  # 使用指定的哈希函数计算哈希值
        if hash_value == target_hash:  # 如果计算出的哈希值等于目标哈希值，则返回前缀
            return prefix
        prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=user_input_len))  # 否则，生成新的前缀并继续计算


generate_proof_of_work(32, 4, hashlib.md5)

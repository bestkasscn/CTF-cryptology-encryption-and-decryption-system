"""
-------------------------------------------------
@FileName:hashencode.py
@Description:哈希函数
@Author:bestkasscn
@Time:2023/3/18
@Principle: 哈希函数是一种将任意长度的消息压缩到固定长度输出的函数，它的主要用途是确保数据的完整性和验证身份。以下是一些常见的哈希函数：

MD5：产生128位哈希值，已经被广泛使用，但是因其存在较大安全隐患，现已被弃用。

SHA-1：产生160位哈希值，现已被广泛使用，但随着计算能力的提高，其安全性也逐渐被质疑。

SHA-2：包括SHA-224、SHA-256、SHA-384、SHA-512等多个版本，产生的哈希值长度从224位到512位不等，目前被广泛使用。

SHA-3：新一代的哈希算法，取代了原有的Keccak算法，目前还没有被广泛使用。

此外，还有一些其他的哈希函数，如RIPEMD、Whirlpool等，但它们的使用并不像上述几种广泛。
-------------------------------------------------
@TestCase:print(hash_encrypt("Hello, world!"))
@Status:已测试
-------------------------------------------------
"""
import hashlib


def hash_encrypt(data: str, hash_type: str = 'md5') -> str:
    """
    计算字符串的哈希值

    :param data: 待计算哈希值的字符串
    :param hash_type: 哈希算法类型，可选值为'md5'、'sha1'、'sha256'、'sha512'，默认为'md5'
    :return: 计算出的哈希值，以字符串形式返回
    """
    # 根据传入的哈希算法类型选择对应的哈希函数
    if hash_type == 'md5':
        hash_func = hashlib.md5()
    elif hash_type == 'sha1':
        hash_func = hashlib.sha1()
    elif hash_type == 'sha256':
        hash_func = hashlib.sha256()
    elif hash_type == 'sha512':
        hash_func = hashlib.sha512()
    else:
        raise ValueError('Invalid hash type: {}'.format(hash_type))

    # 计算哈希值
    hash_func.update(data.encode('utf-8'))
    return hash_func.hexdigest()


print(hash_encrypt("Hello, world!"))
"""
-------------------------------------------------
@FileName:vigenereAttack.py
@Description:暴力破解维吉尼亚密码
@Author:bestkasscn
@Time:2023/3/11
@Principle:
基于Kasiski试验的Vigenere攻击函数用于未知密钥的情况
1.实现一个函数，用于寻找在加密文本中重复的三元组，并计算它们之间的距离。

2.使用Kasiski试验算法分析三元组之间的距离，以确定可能的密钥长度。

3.对于每个可能的密钥长度，使用频率分析技术破解密文。

4.最终返回最有可能的密钥和解密后的明文。

重合指数测试算法
当加密文本采用了经典密码学中的多表代换密码时，密文的字母分布与明文的字母分布不同。
因为密文的每个字母是通过将明文中的一个字母替换为另一个字母而得到的。
在这种情况下，可以通过计算密文中每一列（相当于一个“子文本”）的字母频率来推断密钥的长度。
由于密钥中不同的字母表进行不同的代换，这些不同的字母表导致了密文中每一列的字母频率不同。
根据“指数相似性”（Index of Coincidence, IC）的概念，可以测量不同列之间的相似度，从而得到密钥长度的候选项。
这个方法利用了子文本（列）的相似性和它们之间的差异来确定可能的密钥长度。具体而言，它通过比较各列的IC值和IC值的平均值来选择密钥长度的候选项。
1.首先，通过循环尝试所有可能的密钥长度（从1到max_key_length）来计算每个可能的密钥长度下的重合指数。

2.计算每个可能密钥长度下所有列的平均重合指数，与英文的平均重合指数进行比较。

3.程序选择使差值最小的密钥长度作为最终猜测的密钥长度，并将其作为函数的返回值。
-------------------------------------------------
@TestCase:
ciphertext = "PZEPHCIZYOYMBAPGIDLZMQEMAOCTRQOHGSDAXLYAIVUWKLCFHKZZDZCFZWYOAQOTTZZELWOWDTSMKWVZTFCMIWTLHGSMWWGKCCE" \
             "ETVVUDBQTBKVKDGSMWMEASSDBHOTSCHUWKLCFLVLBAMTWFIPAMACFSYPMIPKEWOAXRCPKJFAZBAKFVZJRHZFSCGNWETGSVIPAKMISG" \
             "RSQFIUEPBTXNTCLXJPIGLRMHVJJNBVZTMOMVQFWICYWMZCAHSEPXQUKJSTVMPGZDDPBAIVBPBPIIXTWRWLBXAVZTWCIMBKLJRPIGLVZ" \
             "PHEPXQTSRVTMOMOWCHDAIMCCUCCBAMOKTZGMLACVAMEPXQTKIFLBXOAAHTLZEMUKTTQMVBKNTHSIGRQJSOYAPPKUWQLCLMUEDFPWYR" \
             "CFTGCMIWTLHHZJNTNQWSCQGBQSEFZUHBKGC"
print(attack(ciphertext, 'ic'))
@Status:已测试
-------------------------------------------------
"""

import kasiski
import ic
import processing
import freq_analysis as fa
from const import (SEQ_LEN, MAX_KEY_LEN)
import string


def decipher(ciphertext: str, key: str) -> str:

    letters = string.ascii_uppercase
    shifts = [letters.index(letter) for letter in key]
    blocks = processing.get_blocks(text=ciphertext, size=len(key))
    cols = processing.get_columns(blocks)
    deciphered_blocks = processing.to_blocks([fa.shift_text(col, shift) for col, shift in zip(cols, shifts)])
    deciphered = ''.join(deciphered_blocks)
    return deciphered


def attack(ciphertext: str, method=None):
    """

    :param ciphertext:密文必须是全大写，且不能包含空格等特殊字符
    :param method: 可选kasiski算法或ic算法，默认为kasiski算法
    :return: 可能的密钥和明文
    """
    if method is None: method = 'kasiski'
    key_len = 0
    if method == 'kasiski':
        print('应用kasiski实验算法\n')
        key_len = kasiski.find_key_length(ciphertext, SEQ_LEN, MAX_KEY_LEN)
    elif method == 'ic':
        print('应用重合指数测试算法\n')
        key_len = ic.find_key_length(ciphertext, MAX_KEY_LEN)
    key = fa.restore_key(ciphertext, key_len)
    deciphered = decipher(ciphertext, key)
    print('可能的密钥长度: ' + str(key_len))
    print('已推导出的密钥: ' + str(key))
    print('明文: ' + str(deciphered))


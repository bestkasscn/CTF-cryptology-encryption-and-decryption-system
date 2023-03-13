"""
-------------------------------------------------
@FileName:atbash.py
@Description:埃特巴什码
@Author:bestkasscn
@Time:2023/2/4
@Principle:Atbash 加密是一种简单的替换密码，在该密码中，字母表中的每个字母都与相应字母表的反向字母对应。
例如，在 Atbash 加密中，字母“A”对应于字母“Z”，字母“B”对应于字母“Y”，以此类推。
因此，对于一个 Atbash 加密的密文，只需要将密文中的每个字母与相应的反向字母进行替换即可得到原始明文。
-------------------------------------------------
@TestCase:
plaintext = 'MHHXGU{gsrh_rh_z_gvhg_uozt}'
print(atbash_attack(plaintext))
@Status:已测试
-------------------------------------------------
"""
from string import ascii_lowercase, ascii_uppercase

dir_atbash_lower = ascii_lowercase[::-1]
dir_atbash_upper = ascii_uppercase[::-1]


def atbash_attack(plaintext: str):
    res = ''
    for s in plaintext:
        if s.isupper():
            res += ''.join(dir_atbash_upper[ascii_uppercase.index(s)])
        elif s.islower():
            res += ''.join(dir_atbash_lower[ascii_lowercase.index(s)])
        else:
            res += ''.join(s)
    return res


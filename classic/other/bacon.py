"""
-------------------------------------------------
@FileName:bacon.py
@Description:培根密码
@Author:bestkasscn
@Time:2023/3/11
@Principle:
培根密码（Bacon cipher）是一种古典密码，它的原理是将一段明文（plaintext）通过替换成另一组字符的方式加密，从而形成密文（ciphertext）。
这个替换规则是由英国哲学家、科学家培根（Francis Bacon）在16世纪提出的。

具体来说，培根密码将明文中的每个字母转化为一组由A和B组成的5位二进制码
（例如，字母A对应的二进制码是AAAAA，字母B对应的二进制码是AAAAB，以此类推）。
这些二进制码可以用任何可以表示二进制的符号表示，例如用点和横线表示。
然后，将这些二进制码与另一组由A和B组成的5位二进制码相对应，这组码被称为培根密码字母表（Baconian alphabet）。
这个字母表通常有两种形式，分别称为普通字母表（plain alphabet）和扭曲字母表（distorted alphabet）。

在加密时，将明文中的每个字母转换为对应的二进制码，并将这些二进制码替换为培根密码字母表中相应的二进制码。
然后将这些二进制码转换为对应的字母即可得到密文。

解密时，只需要将密文中的每个二进制码与培根密码字母表中的二进制码相匹配，
然后将匹配的二进制码转换为对应的明文字母即可还原明文。
-------------------------------------------------
@TestCase:

plaintext = 'this is a test flag'
ciphertext = 'BAABAAABBBABAAABAAABABAAABAAABAAAAABAABAAABAABAAABBAABAAABABABABAAAAAAAABBA'
print(bacon_encrypt(plaintext))
print(bacon_decrypt(ciphertext))
@Status:已测试
-------------------------------------------------
"""
from string import ascii_lowercase

bacon_table = {
    'a': 'AAAAA', 'g': 'AABBA', 'n': 'ABBAA', 't': 'BAABA',
    'b': 'AAAAB', 'h': 'AABBB', 'o': 'ABBAB', 'u': 'BAABB', 'v': 'BAABB',
    'c': 'AAABA', 'i': 'ABAAA', 'j': 'ABAAA', 'p': 'ABBBA', 'w': 'BABAA',
    'd': 'AAABB', 'k': 'ABAAB', 'q': 'ABBBB', 'x': 'BABAB',
    'e': 'AABAA', 'l': 'ABABA', 'r': 'BAAAA', 'y': 'BABBA',
    'f': 'AABAB', 'm': 'ABABB', 's': 'BAAAB', 'z': 'BABBB'
}
distorted_bacon_table = {
    'A': 'ABBAA', 'B': 'AABAB', 'C': 'BBAAB', 'D': 'BBAAA',
    'E': 'BAABB', 'F': 'BAAAA', 'G': 'AABBA', 'H': 'ABAAA',
    'I': 'ABBAB', 'J': 'AABAA', 'K': 'BBBAB', 'L': 'BBBAA',
    'M': 'BAAAB', 'N': 'ABABA', 'O': 'BABBA', 'P': 'BBAAB',
    'Q': 'BBABB', 'R': 'BAABA', 'S': 'AABBB', 'T': 'BABAB',
    'U': 'ABABB', 'V': 'ABBBB', 'W': 'BBBBA', 'X': 'BAABB',
    'Y': 'BAABA', 'Z': 'ABAAA'
}


def bacon_encrypt(plaintext: str, alphabet=None) -> str:
    """
    编码规则:i=j,u=v
    :param alphabet: 字母表规则，可任意设置
    :param plaintext:明文
    :return:
    """
    if alphabet is None: alphabet = bacon_table
    ciphertext = ''
    for s in plaintext.lower():
        if s in alphabet:
            ciphertext += ''.join(alphabet[s])
        else:
            pass
    return ciphertext


def bacon_decrypt(ciphertext: str, alphabet=None) -> str:
    if alphabet is None: alphabet = bacon_table
    plaintext = ''
    for i in range(0, len(ciphertext), 5):
        for s in ascii_lowercase:
            if alphabet[s] == ciphertext[i:i + 5]:
                plaintext += s
                break
    return plaintext


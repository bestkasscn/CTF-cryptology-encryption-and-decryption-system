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


plaintext = 'this is a test flag'
ciphertext = 'BAABAAABBBABAAABAAABABAAABAAABAAAAABAABAAABAABAAABBAABAAABABABABAAAAAAAABBA'
print(bacon_encrypt(plaintext))
print(bacon_decrypt(ciphertext))

from string import ascii_uppercase
from pycipher.vigenere import Vigenere


def vigenere_encrypt(plaintext: str, key: str) -> str:
    key = key.upper()
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char.upper() in ascii_uppercase:
            # 计算偏移量
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            # 加密字符
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key = key.upper()
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.upper() in ascii_uppercase:
            # 计算偏移量
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            # 解密字符
            plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            plaintext += char
    return plaintext


def vigenereAttack(ciphertext: str) -> (str, str):
    """
    基于Kasiski试验的Vigenere攻击函数用于未知密钥的情况
    1.实现一个函数，用于寻找在加密文本中重复的三元组，并计算它们之间的距离。

    2.使用Kasiski试验算法分析三元组之间的距离，以确定可能的密钥长度。

    3.对于每个可能的密钥长度，使用频率分析技术破解密文。

    4.最终返回最有可能的密钥和解密后的明文。
    :param ciphertext:密文
    :return:密钥和解密后的明文
    """
    # 1.实现一个函数，用于寻找在加密文本中重复的三元组，并计算它们之间的距离。
    repeats = {}
    for i in range(len(ciphertext) - 2):
        triplet = ciphertext[i:i + 3]
        if triplet in repeats:
            repeats[triplet].append(i)
        else:
            repeats[triplet] = [i]
    distances = {}
    for triplet, positions in repeats.items():
        if len(positions) > 1:
            distances[triplet] = []
            for i in range(len(positions) - 1):
                distances[triplet].append(positions[i + 1] - positions[i])

    # 2.使用Kasiski试验算法分析三元组之间的距离，以确定可能的密钥长度。
    factors = []
    for triplet, dists in distances.items():
        for dist in dists:
            for i in range(2, min(len(ciphertext), len(triplet) * 3)):
                if dist % i == 0:
                    factors.append(i)
    key_len = 0
    factor_counts = {}
    for factor in factors:
        if factor in factor_counts:
            factor_counts[factor] += 1
        else:
            factor_counts[factor] = 1
        if factor_counts[factor] > key_len:
            key_len = factor

    # 3.对于每个可能的密钥长度，使用频率分析技术破解密文。
    possible_keys = []
    for i in range(key_len):
        segment = ciphertext[i::key_len]
        freqs = {}
        for letter in segment:
            if letter in freqs:
                freqs[letter] += 1
            else:
                freqs[letter] = 1
        sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        possible_keys.append(chr((ord(sorted_freqs[0][0]) - ord('E')) % 26 + ord('A')))

    # 4.最终返回最有可能的密钥和解密后的明文。
    key = ''.join(possible_keys)
    plaintext = ''
    for i in range(len(ciphertext)):
        shift = ord(key[i % len(key)]) - ord('A')
        plaintext += chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))

    return key, plaintext


def advancedVigenereAttack(ciphertext: str) -> (str, str):
    """
    1.在Kasiski试验的第二步中，可以改用一个更高效的算法来找到重复的三元组并计算它们之间的距离。例如，使用散列表（Hash Table）来存储三元组和它们的位置信息，可以将时间复杂度从O(n^2)降至O(n)。
    2.在Kasiski试验的第二步中，可以用欧几里得算法（Euclidean Algorithm）来计算可能的密钥长度，而不是检查所有因子。这可以将时间复杂度降至O(nlogn)。
    3.在使用频率分析破解密文时，可以将计算频率和排序操作合并为一个步骤，以提高效率。
    4.在解密密文时，可以避免使用字符串拼接操作，而是将解密后的字符直接添加到一个列表中，然后最后再将列表合并成一个字符串。这可以避免不必要的字符串复制操作，提高效率。
    :param ciphertext:密文
    :return:密钥和解密后的明文
    """
    # Step 1: Find repeated triplets and calculate their distances
    repeats = {}
    for i in range(len(ciphertext) - 2):
        triplet = ciphertext[i:i + 3]
        if triplet in repeats:
            repeats[triplet].append(i)
        else:
            repeats[triplet] = [i]
    distances = {}
    for triplet, positions in repeats.items():
        if len(positions) > 1:
            distances[triplet] = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]

    # Step 2: Use Kasiski examination to determine key length
    factors = []
    for triplet, dists in distances.items():
        for dist in dists:
            gcd = dist
            while triplet in distances and any([d % gcd == 0 for d in distances[triplet]]):
                gcd = min([d for d in distances[triplet] if d % gcd == 0])
            factors.append(gcd)
    key_len = max(set(factors), key=factors.count)

    # Step 3: Use frequency analysis to crack the cipher for each possible key length
    possible_keys = []
    for i in range(key_len):
        segment = ciphertext[i::key_len]
        freqs = [0] * 26
        for letter in segment:
            freqs[ord(letter) - ord('A')] += 1
        key = (freqs.index(max(freqs)) - 4) % 26
        possible_keys.append(chr(key + ord('A')))

    # Step 4: Return the most likely key and the decrypted plaintext
    key = ''.join(possible_keys)
    plaintext = [chr((ord(c) - ord('A') - ord(key[i % key_len]) + 26) % 26 + ord('A')) for i, c in
                 enumerate(ciphertext)]
    return key, ''.join(plaintext)


plaintext = 'thiscryptosystemisnotsecure'
key = 'cipher'
print(vigenereAttack('VPXZGIAXIVWPUBTTMJPWIZITWZT'))

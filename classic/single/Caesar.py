from string import ascii_letters


def caesar_encrypt(plaintext: str, key: int) -> str:
    """
    :param plaintext: 待加密明文
    :param key: 位移量
    :return: 密文
    """
    if key < 0:
        raise Exception("Key must be non-negative")
    res = ''
    key = key % 26
    for s in plaintext:
        if s in ascii_letters:
            if chr(ord(s) + key) in ascii_letters:
                res += chr(ord(s) + key)
            else:
                res += chr(ord(s) + key - 26)
        else:
            res += s
    return res


def caesar_decrypt(ciphertext: str, key: int) -> str:
    """
    :param ciphertext: 待解密密文
    :param key: 位移量
    :return: 明文
    """
    if key < 0:
        raise Exception("Key must be non-negative")
    res = ''
    key = key % 26
    for s in ciphertext:
        if s in ascii_letters:
            if chr(ord(s) - key) in ascii_letters:
                res += chr(ord(s) - key)
            else:
                res += chr(ord(s) - key + 26)
        else:
            res += s
    return res


def caesarAttack(ciphertext: str):
    """
    :param ciphertext: 待解密密文
    :return: 明文
    """
    for key in range(1, 26):
        res = caesar_decrypt(ciphertext, key)
        print(f"key为{key}时：{res}")



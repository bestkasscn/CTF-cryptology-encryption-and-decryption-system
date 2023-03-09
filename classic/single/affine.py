import gmpy2


def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    """
    Affine encryption
    :param plaintext:明文
    :param a:要求与字母表大小（通常为26）互质
    :param b:任意整数
    :return:密文
    """
    ciphertext = ""
    for c in plaintext.upper():
        ciphertext += chr(((ord(c) - 65) * a + b) % 26 + 65)
    return ciphertext


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    """
    Affine decryption
    :param ciphertext:密文
    :param a:
    :param b:
    :return:
    """
    plaintext = ""
    a_inv = gmpy2.invert(a, 26)
    for c in ciphertext:
        plaintext += chr((ord(c) - 65 - b) * a_inv % 26 + 65)
    return plaintext

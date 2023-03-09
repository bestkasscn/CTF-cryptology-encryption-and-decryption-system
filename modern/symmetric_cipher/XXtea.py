import xxtea


def xxtea_encrypt(plain_text: str, key: str) -> bytes:
    # 填充key至16字节
    key = key.ljust(16, '\0')
    # 将明文转换成bytes类型
    plain_text_bytes = plain_text.encode('utf-8')
    # 使用xxtea进行加密
    cipher_bytes = xxtea.encrypt(plain_text_bytes, key)
    return cipher_bytes


def xxtea_decrypt(cipher_bytes: bytes, key: str) -> str:
    # 填充key至16字节
    key = key.ljust(16, '\0')
    # 使用xxtea进行解密
    plain_text_bytes = xxtea.decrypt(cipher_bytes, key)
    # 将解密后的bytes转换成字符串
    plain_text = plain_text_bytes.decode('utf-8')
    return plain_text


def test_xxtea():
    key = 'MyKey1234567890'
    plaintext = 'Hello, World!'
    ciphertext = xxtea_encrypt(plaintext, key)
    decrypted_text = xxtea_decrypt(ciphertext, key)
    assert decrypted_text == plaintext, "Decryption failed!"
    print("Encryption and decryption successful.")


if __name__ == '__main__':
    test_xxtea()

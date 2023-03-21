"""
-------------------------------------------------
@FileName:xx_tea.py
@Description:
@Author:bestkasscn
@Time:2023/3/21
@Principle: 
-------------------------------------------------
@TestCase:
plaintext = "Hello, world!"
key = "my secret key"

ciphertext = xxtea_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = xxtea_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
@Status:已测试
-------------------------------------------------
"""
import xxtea


def xxtea_encrypt(plaintext: str, key: str) -> bytes:
    # 填充key至16字节
    key = key.ljust(16, '\0')
    # 将明文转换成bytes类型
    plaintext_bytes = plaintext.encode('utf-8')
    # 使用xxtea进行加密
    ciphertext = xxtea.encrypt(plaintext_bytes, key)
    return ciphertext


def xxtea_decrypt(ciphertext: bytes, key: str) -> str:
    # 填充key至16字节
    key = key.ljust(16, '\0')
    # 使用xxtea进行解密
    plaintext_bytes = xxtea.decrypt(ciphertext, key)
    # 将解密后的bytes转换成字符串
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext

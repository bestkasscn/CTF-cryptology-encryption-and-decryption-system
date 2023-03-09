# 简单替换密码加密脚本
def encrypt(plaintext:str, key:int) -> str:
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # 将明文字符替换为密文字符
            # ASCII码值 + 密钥值 - 'A'的ASCII码值
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        else:
            # 非字母字符直接添加
            ciphertext += char
    return ciphertext


# 简单替换密码解密脚本
def decrypt(ciphertext:str, key:int) -> str:
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # 将密文字符替换为明文字符
            # ASCII码值 - 密钥值 - 'A'的ASCII码值
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        else:
            # 非字母字符直接添加
            plaintext += char
    return plaintext


plaintext = "HELLO WORLD!"
key = 7

# 加密
ciphertext = encrypt(plaintext, key)
print("密文: ", ciphertext)

# 解密
decrypted_text = decrypt(ciphertext, key)
print("明文: ", decrypted_text)

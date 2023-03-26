"""
-------------------------------------------------
@FileName:xx_tea.py
@Description:
@Author:bestkasscn
@Time:2023/3/21
@Principle: XXTEA（Extended Tiny Encryption Algorithm）是一种对称加密算法，
由 David Wheeler 和 Roger Needham 在 1998 年提出。XXTEA 是 TEA 和 XTEA 加密算法的扩展，
它改进了这些算法的弱点并提供了更好的安全性。XXTEA 算法与 TEA 和 XTEA 不同之处在于，
它采用了可变长度的数据块（而不是固定的 64 位数据块）和 128 位密钥。

XXTEA 算法的工作原理如下：

1. 将明文分成 n 个 32 位无符号整数的数据块（v0, v1, ..., vn-1）。
2. 将 128 位密钥分为四个 32 位子密钥（k0, k1, k2, k3）。
3. 选择一个常量 delta（0x9e3779b9），这是一个特殊的常数，它是黄金比例的倒数乘以 2^32。
4. 设置一个名为 sum 的变量，初始化为 0。
5. 进行固定轮数（例如 6 + 52/n）的加密操作： a. 将 delta 累加到 sum 中。 b. 对于每个数据块 vi，执行以下操作：
   - 计算左侧邻居数据块 (v[i-1] 或 v[n-1]，如果 i=0) 的变换值：z = v[i-1] if i > 0 else v[n-1]
   - 计算右侧邻居数据块 (v[i+1] 或 v[0]，如果 i=n-1) 的变换值：y = v[i+1] if i < n-1 else v[0]
   - 更新数据块 vi：vi = (vi + ((z >> 5) ^ (y << 2)) + y ^ (sum + k[sum & 3] ^ (z + k[(sum >> 11) & 3]))) & 0xffffffff
6. 最后，将更新后的数据块连接起来形成密文。
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

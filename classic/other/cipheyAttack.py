"""
-------------------------------------------------
@FileName:cipheyAttack.py
@Description:
@Author:bestkasscn
@Time:2023/3/11
@Principle: 
-------------------------------------------------
@TestCase:
@Status:
-------------------------------------------------
"""
from ciphey import decrypt
from ciphey.iface import Config


def ciphey_attack(ciphertext: str) -> str:
    plaintext = decrypt(
        Config().library_default().complete_config(),
        ciphertext,
    )
    return plaintext


ciphertext = '4E53534354467B746869735F6973a15F746573745F666C61677D'
print(ciphey_attack(ciphertext))

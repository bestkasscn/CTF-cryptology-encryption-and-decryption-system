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
import time


def ciphey_attack(ciphertext: str) -> str:
    return decrypt(
        Config().library_default().complete_config(),
        ciphertext,
    )


import threading
import sys


def timeout_handler():
    print("程序运行时间超过了最大限制")
    sys.exit(1)


# 设置程序最长运行时间为5秒钟
timer = threading.Timer(16.0, timeout_handler)
timer.start()
ciphertext = '4E53534354467B746869735F69735F615F746573745F666C61677D'
try:
    print(ciphey_attack(ciphertext))
    timer.cancel()
except:
    pass

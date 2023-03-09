from pycipher.columnartransposition import ColTrans


def columnar_encrypt(plaintext: str, key: str) -> str:
    return ColTrans(key).encipher(plaintext)


def columnar_decrypt(ciphertext: str, key: str) -> str:
    return ColTrans(key).decipher(ciphertext)


plaintext = 'this is a test flag'
ciphertext = columnar_encrypt(plaintext, 'German')
print(columnar_encrypt(plaintext, 'German'))
print(columnar_decrypt(ciphertext, 'German'))

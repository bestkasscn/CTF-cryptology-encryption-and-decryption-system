def base8encode(plaintext: str) -> str:
    ciphertext = ''
    for s in plaintext:
        res = oct(ord(s))[2:]
        while len(res) < 3:
            res = '0' + res
        ciphertext += res
    return ciphertext


def base8decode(ciphertext: str) -> str:
    plaintext = ''
    for s in range(0, len(ciphertext), 3):
        plaintext += chr(int('' + ciphertext[s:s + 3], 8))
    return plaintext


plaintext = 'NSSCTF{base8_is_funny_right?}'
print(base8encode(plaintext))
print(base8decode(base8encode(plaintext)))

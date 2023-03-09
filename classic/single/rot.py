def rot5_encrypt(plaintext:str) -> str:
    ciphertext = ""
    for c in plaintext:
        if c.isdigit():
            new_digit = (int(c) + 5) % 10
            ciphertext += str(new_digit)
        else:
            ciphertext += c
    return ciphertext


def rot5_decrypt(ciphertext:str) -> str:
    plaintext = ""
    for c in ciphertext:
        if c.isdigit():
            new_digit = (int(c) - 5) % 10
            plaintext += str(new_digit)
        else:
            plaintext += c
    return plaintext


def rot13_encrypt(plaintext:str) -> str:
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 + 13) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 + 13) % 26 + 97
            ciphertext += chr(new_ascii)
        else:
            ciphertext += c
    return ciphertext


def rot13_decrypt(ciphertext:str) -> str:
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 - 13) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 - 13) % 26 + 97
            plaintext += chr(new_ascii)
        else:
            plaintext += c
    return plaintext


def rot18_encrypt(plaintext:str) -> str:
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 + 18) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 + 18) % 26 + 97
            ciphertext += chr(new_ascii)
        else:
            ciphertext += c
    return rot5_encrypt(rot13_encrypt(plaintext))


def rot18_decrypt(ciphertext:str) -> str:
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 - 18) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 - 18) % 26 + 97
            plaintext += chr(new_ascii)
        else:
            plaintext += c
    return rot5_decrypt(rot13_decrypt(ciphertext))


def rot47_encrypt(plaintext:str) -> str:
    ciphertext = ""
    for c in plaintext:
        if 33 <= ord(c) <= 126:
            new_ascii = (ord(c) + 47) % 94 + 33
            ciphertext += chr(new_ascii)
        elif ord(c) > 126:
            new_ascii = (ord(c) - 94 + 47) % 94 + 33
            ciphertext += chr(new_ascii)
        else:
            ciphertext += c
    return ciphertext


def rot47_decrypt(ciphertext:str) -> str:
    plaintext = ""
    for c in ciphertext:
        if 33 <= ord(c) <= 126:
            new_ascii = (ord(c) - 47) % 94 + 33
            plaintext += chr(new_ascii)
        elif ord(c) > 126:
            new_ascii = (ord(c) - 47 - 94) % 94 + 126
            plaintext += chr(new_ascii)
        else:
            plaintext += c
    return plaintext


plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ciphertext = rot18_encrypt(plaintext)
print(ciphertext)

plaintext = "Hello, World!"
ciphertext = rot18_encrypt(plaintext)
print(ciphertext)

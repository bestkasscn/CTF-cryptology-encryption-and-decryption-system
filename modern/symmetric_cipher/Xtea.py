import struct


def pad_key(key):
    while len(key) < 16:
        key += b'\x00'
    return key[:16]


def encrypt_block(v, k):
    delta = 0x9E3779B9
    sum = 0
    for i in range(32):
        sum += delta
        v[0] += ((v[1] << 4 ^ v[1] >> 5) + v[1]) ^ (sum + k[sum >> 11 & 3])
        v[1] += ((v[0] << 4 ^ v[0] >> 5) + v[0]) ^ (sum + k[sum & 3])
    return v


def decrypt_block(v, k):
    delta = 0x9E3779B9
    sum = delta << 5
    for i in range(32):
        v[1] -= ((v[0] << 4 ^ v[0] >> 5) + v[0]) ^ (sum + k[sum & 3])
        v[0] -= ((v[1] << 4 ^ v[1] >> 5) + v[1]) ^ (sum + k[sum >> 11 & 3])
        sum -= delta
    return v


def xtea_encrypt(plaintext, key):
    # add padding to plaintext
    padding_length = 8 - len(plaintext) % 8
    plaintext += bytes([padding_length] * padding_length)

    # pad key if necessary
    key = pad_key(key)

    # convert key to list of integers
    k = struct.unpack('4I', key)

    # encrypt blocks of plaintext
    ciphertext = b''
    for i in range(0, len(plaintext), 8):
        block = list(struct.unpack('2I', plaintext[i:i + 8]))
        block = encrypt_block(block, k)
        ciphertext += struct.pack('2I', *block)

    return ciphertext


def xtea_decrypt(ciphertext, key):
    # pad key if necessary
    key = pad_key(key)

    # convert key to list of integers
    k = struct.unpack('4I', key)

    # decrypt blocks of ciphertext
    plaintext = b''
    for i in range(0, len(ciphertext), 8):
        block = list(struct.unpack('2I', ciphertext[i:i + 8]))
        block = decrypt_block(block, k)
        plaintext += struct.pack('2I', *block)

    # remove padding from plaintext
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]

    return plaintext


key = b'secret_ksecret_k'  # 8-byte key
plaintext = b'Thisisas'
ciphertext = xtea_encrypt(plaintext, key)
decrypted = xtea_decrypt(ciphertext, key)
print(decrypted)  # b'This is a secret message.'

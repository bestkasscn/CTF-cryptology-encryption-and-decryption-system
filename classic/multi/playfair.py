"""
-------------------------------------------------
@FileName:playfair.py
@Description:Playfair 密码（Playfair cipher or Playfair square）是一种替换密码
@Author:bestkasscn
@Time:2023/3/9
@Principle: Playfair 密码（Playfair cipher or Playfair square）是一种替换密码，
1854 年由英国人查尔斯 · 惠斯通（Charles Wheatstone）发明，基本算法如下：

1. 选取一串英文字母，除去重复出现的字母，将剩下的字母逐个逐个加入 5 × 5 的矩阵内，剩下的空间由未加入的英文字母依 a-z 的顺序加入。
注意，将 q 去除，或将 i 和 j 视作同一字。
2. 将要加密的明文分成两个一组。若组内的字母相同，将 X（或 Q）加到该组的第一个字母后，重新分组。若剩下一个字，也加入 X 。
3. 在每组中，找出两个字母在矩阵中的地方。
   - 若两个字母不同行也不同列，在矩阵中找出另外两个字母（第一个字母对应行优先），使这四个字母成为一个长方形的四个角。
   - 若两个字母同行，取这两个字母右方的字母（若字母在最右方则取最左方的字母）。
   - 若两个字母同列，取这两个字母下方的字母（若字母在最下方则取最上方的字母）。

新找到的两个字母就是原本的两个字母加密的结果。

以 playfair example 为密匙，得

```
P L A Y F
I R E X M
B C D G H
K N O Q S
T U V W Z
```

要加密的讯息为 Hide the gold in the tree stump

```
HI DE TH EG OL DI NT HE TR EX ES TU MP
```

就会得到

```
BM OD ZB XD NA BE KU DM UI XM MO UV IF
```
-------------------------------------------------
@TestCase:
plaintext = "HELLO WORLD"
key = "SECRETKEY"
ciphertext = playfair_encrypt(plaintext, key)
decryptedtext = playfair_decrypt(ciphertext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decryptedtext)
@Status:已测试
-------------------------------------------------
"""


def prepare_input_string(input_string: str) -> str:
    """
    准备输入字符串：将所有字符转换为大写字母，并删除所有非字母字符
    """
    input_string = input_string.upper()
    input_string = ''.join(filter(str.isalpha, input_string))
    return input_string


def prepare_key(key: str) -> str:
    """
    准备密钥：将所有字符转换为大写字母，并删除所有非字母字符和重复字母
    """
    key = key.upper()
    key = ''.join(filter(str.isalpha, key))
    key = ''.join(sorted(set(key), key=key.index))
    return key


def generate_playfair_table(key:str):
    """
    生成 Playfair 密码表
    """
    key = prepare_key(key)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = []
    for letter in key:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, '')
            table.append(letter)
    table += alphabet
    return [table[i:i + 5] for i in range(0, 25, 5)]


def find_letter_coords(table, letter):
    """
    查找字母在密码表中的坐标
    """
    for row_idx, row in enumerate(table):
        if letter in row:
            col_idx = row.index(letter)
            return row_idx, col_idx


def encode_pair(table, pair):
    """
    加密一对字母
    """
    a_row, a_col = find_letter_coords(table, pair[0])
    b_row, b_col = find_letter_coords(table, pair[1])
    if a_row == b_row:
        return table[a_row][(a_col + 1) % 5] + table[b_row][(b_col + 1) % 5]
    elif a_col == b_col:
        return table[(a_row + 1) % 5][a_col] + table[(b_row + 1) % 5][b_col]
    else:
        return table[a_row][b_col] + table[b_row][a_col]


def decode_pair(table, pair):
    """
    解密一对字母
    """
    a_row, a_col = find_letter_coords(table, pair[0])
    b_row, b_col = find_letter_coords(table, pair[1])
    if a_row == b_row:
        return table[a_row][(a_col - 1) % 5] + table[b_row][(b_col - 1) % 5]
    elif a_col == b_col:
        return table[(a_row - 1) % 5][a_col] + table[(b_row - 1) % 5][b_col]
    else:
        return table[a_row][b_col] + table[b_row][a_col]


def playfair_encrypt(plaintext, key):
    """
    使用 Playfair 密码加密明文
    """
    plaintext = prepare_input_string(plaintext)
    table = generate_playfair_table(key)
    pairs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
    ciphertext = ''
    for pair in pairs:
        if len(pair) == 1:
            pair += 'X'
        ciphertext += encode_pair(table, pair)
    return ciphertext


def playfair_decrypt(ciphertext, key):
    key = key.upper().replace('J', 'I')
    ciphertext = ciphertext.upper().replace('J', 'I')
    matrix = generate_playfair_table(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i + 1]
        a_row, a_col = find_letter_coords(matrix, a)
        b_row, b_col = find_letter_coords(matrix, b)
        if a_row == b_row:
            plaintext += matrix[a_row][(a_col - 1) % 5] + matrix[b_row][(b_col - 1) % 5]
        elif a_col == b_col:
            plaintext += matrix[(a_row - 1) % 5][a_col] + matrix[(b_row - 1) % 5][b_col]
        else:
            plaintext += matrix[a_row][b_col] + matrix[b_row][a_col]
    return plaintext



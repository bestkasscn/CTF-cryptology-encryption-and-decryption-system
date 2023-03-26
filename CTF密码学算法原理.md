# CTFCrypto

[TOC]



## 古典密码

### 单表替换加密

- Caesar（凯撒密码）

  **原理**

  凯撒密码（Caesar）加密时会将明文中的 **每个字母** 都按照其在字母表中的顺序向后（或向前）移动固定数目（**循环移动**）作为密文。例如，当偏移量是左移 3 的时候（解密时的密钥就是 3）：

  ```
  明文字母表：ABCDEFGHIJKLMNOPQRSTUVWXYZ
  密文字母表：DEFGHIJKLMNOPQRSTUVWXYZABC
  ```

  使用时，加密者查找明文字母表中需要加密的消息中的每一个字母所在位置，并且写下密文字母表中对应的字母。需要解密的人则根据事先已知的密钥反过来操作，得到原来的明文。例如：

  ```
  明文：THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
  密文：WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
  ```

  **例题**

  ```
  已知密文为vzsx，位移量为3，求明文？
  解：第一步，写出密文中字母对应的位置（下标），比如说a在字母表中为第一位，就记作1（记作0也可以,最后一个字母z = 25）
      所以我们可以写出v = 22,z = 26,s = 19,x = 24
      第二步，因为位移量为3，所以我们将以上数字都减3，即19,23,16,21
      第三步，将以上数字还原为字母，19对应s,23对应w,16对应p,21对应u,我们就解出了明文swpu.
      
  ```

  **加解密脚本**

  ```python
  from string import ascii_letters
  
  
  def caesarEncrypt(plaintext: str, key: int) -> str:
      """
      :param plaintext: 待加密明文
      :param key: 位移量
      :return: 密文
      """
      if key < 0:
          raise Exception("Key must be non-negative")
      res = ''
      key = key % 26
      for s in plaintext:
          if s in ascii_letters:
              if chr(ord(s) + key) in ascii_letters:
                  res += chr(ord(s) + key)
              else:
                  res += chr(ord(s) + key - 26)
          else:
              res += s
      return res
  
  
  def caesarDecrypt(ciphertext: str, key: int) -> str:
      """
      :param ciphertext: 待解密密文
      :param key: 位移量
      :return: 明文
      """
      if key < 0:
          raise Exception("Key must be non-negative")
      res = ''
      key = key % 26
      for s in ciphertext:
          if s in ascii_letters:
              if chr(ord(s) - key) in ascii_letters:
                  res += chr(ord(s) - key)
              else:
                  res += chr(ord(s) - key + 26)
          else:
              res += s
      return res
  
  
  def caesarAttack(ciphertext: str):
      """
      :param ciphertext: 待解密密文
      :return: 明文
      """
      for key in range(1, 26):
          res = caesarDecrypt(ciphertext, key)
          print(f"key为{key}时：{res}")
  
  ```

- Atbash（埃特巴什码）

  **原理**

  Atbash 加密是一种简单的替换密码，在该密码中，字母表中的每个字母都与相应字母表的反向字母对应。例如，在 Atbash 加密中，字母“A”对应于字母“Z”，字母“B”对应于字母“Y”，以此类推。因此，对于一个 Atbash 加密的密文，只需要将密文中的每个字母与相应的反向字母进行替换即可得到原始明文。

  本质上是一种映射，即

  | A    | B    | C    | D    | E    | F    | G    | H    | I    | J    | K    | L    | M    | N    | O    | P    | Q    | R    | S    | T    | U    | V    | W    | X    | Y    | Z    |
  | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
  | Z    | Y    | X    | W    | V    | U    | T    | S    | R    | Q    | P    | O    | N    | M    | L    | K    | J    | I    | H    | G    | F    | E    | D    | C    | B    | A    |

  **加解密脚本**

  ```python
  from string import ascii_lowercase, ascii_uppercase
  
  dir_atbash_lower = ascii_lowercase[::-1]
  dir_atbash_upper = ascii_uppercase[::-1]
  
  
  def atbashAttack(plaintext):
      res = ''
      for s in plaintext:
          if s.isupper():
              res += ''.join(dir_atbash_upper[ascii_uppercase.index(s)])
          elif s.islower():
              res += ''.join(dir_atbash_lower[ascii_lowercase.index(s)])
          else:
              res += ''.join(s)
      return res
  
  plaintext = 'MHHXGU{gsrh_rh_z_gvhg_uozt}'
  
  ```

- Morse(摩斯电码)

  **原理**
  
  摩斯电码是一种通信方法，它使用点和划的组合来表示字母、数字和符号。点是短脉冲，划是长脉冲，它们之间需要有一个短暂的间隔，而字符之间需要有一个较长的间隔。通过听觉或视觉方式解码摩斯电码可以识别字符。这种通信方法非常简单而且可靠，特别适用于在没有共同语言的情况下进行通信，例如在海上、航空或军事通信中。
  
  **加解密脚本**
  
  ```python
  morse_table = {
      'A': '.-', 'N': '-.', '.': '.-.-.-', '+': '.-.-.', '1': '.----',
      'B': '-...', 'O': '---', ',': '--..--', '_': '..--.-', '2': '..---',
      'C': '-.-.', 'P': '.--.', ':': '---...', '$': '...-..-', '3': '...--',
      'D': '-..', 'Q': '--.-', '"': '.-..-.', '&': '.-...', '4': '....-',
      'E': '.', 'R': '.-.', '\'': '.----.', '/': '-..-.', '5': '.....',
      'F': '..-.', 'S': '...', '!': '-.-.--', '6': '-....',
      'G': '--.', 'T': '-', '?': '..--..', '7': '--...',
      'H': '....', 'U': '..-', '@': '.--.-.', '8': '---..',
      'I': '..', 'V': '...-', '-': '-....-', '9': '----.',
      'J': '.---', 'W': '.--', ';': '-.-.-.', '0': '-----',
      'K': '-.-', 'X': '-..-', '(': '-.--.',
      'L': '.-..', 'Y': '-.--', ')': '-.--.-',
      'M': '--', 'Z': '--..', '=': '-...-',
  }
  morse_dir = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!@#$%^&*()_+:"?/=,\''
  
  
  def morse_encrypt(plaintext: str) -> str:
      ciphertext = ''
      for s in plaintext:
          if s.upper() not in morse_table:
              return "无法解密"
          ciphertext += ''.join(morse_table.get(s.upper())) + " "
      return ciphertext
  
  
  def morse_decrypt(plaintext: str) -> str:
      table = plaintext.split(" ")
      plaintext = ''
      for s in table:
          for i in morse_dir:
              if morse_table.get(i) == s:
                  plaintext += ''.join(i)
      return plaintext
  
  ```
  
- ROT家族

  **ROT5加解密算法**
  
  加密方法：
  
  1. 将数字字符转换为整数
  2. 将整数加5，对10取模，得到加密后的整数
  3. 将加密后的整数转换为数字字符
  
  解密方法：
  
  1. 将数字字符转换为整数
  2. 将整数减去5，若结果小于0，则加上10
  3. 将解密后的整数转换为数字字符
  
  **加解密脚本**
  
  ```python
  def rot5_encrypt(plaintext):
      ciphertext = ""
      for c in plaintext:
          if c.isdigit():
              new_digit = (int(c) + 5) % 10
              ciphertext += str(new_digit)
          else:
              ciphertext += c
      return ciphertext
  
  def rot5_decrypt(ciphertext):
      plaintext = ""
      for c in ciphertext:
          if c.isdigit():
              new_digit = (int(c) - 5) % 10
              plaintext += str(new_digit)
          else:
              plaintext += c
      return plaintext
  
  ```
  
  **ROT13加解密算法**
  
  加密过程：
  
  1. 首先，将明文中的每个字母替换成它在字母表中顺序排列的第13个字母。例如，明文中的字母A将替换为N，字母B将替换为O，以此类推。
  2. 如果字母表中的字母已经到了Z，则继续从字母表的开头（即字母A）开始计数。
  3. 对于非字母字符（例如数字、标点符号和空格），不进行加密，直接保留原样。
  4. 最终输出加密后的密文。
  
  解密过程：
  
  1. 将密文中的每个字母替换为它在字母表中顺序排列的前13个字母，即将字母N替换为A，字母O替换为B，以此类推。
  2. 如果字母表中的字母已经到了A，则继续从字母表的末尾（即字母Z）开始计数。
  3. 对于非字母字符，不进行解密，直接保留原样。
  4. 最终输出解密后的明文。
  
  **加解密脚本**
  
  ```python
  def rot13_encrypt(plaintext: str) -> str:
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
  
  
  def rot13_decrypt(ciphertext: str) -> str:
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
  ```
  
  **ROT18加解密算法**
  
  加密过程：
  
  1. 首先，将明文中的每个字母替换成它在字母表中顺序排列的第18个字母。例如，明文中的字母A将替换为S，字母B将替换为T，以此类推。
  2. 如果字母表中的字母已经到了Z，则继续从字母表的开头（即字母A）开始计数。
  3. 对于非字母字符（例如数字、标点符号和空格），不进行加密，直接保留原样。
  4. 最终输出加密后的密文。
  
  解密过程：
  
  1. 将密文中的每个字母替换为它在字母表中顺序排列的前18个字母，即将字母S替换为A，字母T替换为B，以此类推。
  2. 如果字母表中的字母已经到了A，则继续从字母表的末尾（即字母Z）开始计数。
  3. 对于非字母字符，不进行解密，直接保留原样。
  4. 最终输出解密后的明文。
  
  **加解密脚本**
  
  ```python
  def rot18_encrypt(plaintext: str) -> str:
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
  
  
  def rot18_decrypt(ciphertext: str) -> str:
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
  ```
  
  **ROT47加解密算法**
  
  加密过程：
  
  1. 首先，将明文中的每个字符转换为其对应的ASCII码值。
  2. 对于每个可打印字符，将其ASCII码值加上47。
  3. 如果加上47后的ASCII码值超过了126，则从33开始重新计数。
  4. 将加密后的ASCII码值转换回字符形式。
  5. 最终输出加密后的密文。
  
  解密过程：
  
  1. 首先，将密文中的每个字符转换为其对应的ASCII码值。
  2. 对于每个可打印字符，将其ASCII码值减去47。
  3. 如果减去47后的ASCII码值小于33，则从126开始重新计数。
  4. 将解密后的ASCII码值转换回字符形式。
  5. 最终输出解密后的明文。
  
  **加解密脚本**
  
  ```python
  def rot47_encrypt(plaintext: str) -> str:
      ciphertext = ""
      for c in plaintext:
          if 33 <= ord(c) <= 126:
              ciphertext += chr((ord(c) - 33 + 47) % 94 + 33)
          else:
              ciphertext += c
      return ciphertext
  
  
  def rot47_decrypt(ciphertext: str) -> str:
      plaintext = ""
      for c in ciphertext:
          if 33 <= ord(c) <= 126:
              plaintext += chr((ord(c) - 33 - 47) % 94 + 33)
          else:
              plaintext += c
      return plaintext
  ```
  
  
  
- **仿射密码**

  **原理**

  仿射密码是一种经典的加密方法，其加解密原理如下：

  加密： 设 $m$ 为字母表的大小（一般为 $26$），$a$ 为加密时用到的一个常数，要求 $a$ 与 $m$ 互质，$b$ 为加密时用到的另一个常数，可以是任意整数。对于明文中的每个字母 $x$，计算 $(ax+b)\bmod m$，得到密文中的对应字母 $y$。

  解密： 首先求出 $a$ 的逆元 $a^{-1}$，即满足 $a \times a^{-1} \equiv 1 \pmod{m}$ 的整数 $a^{-1}$。然后对于密文中的每个字母 $y$，计算 $a^{-1} \times (y-b) \bmod m$，得到明文中的对应字母 $x$。

  需要注意的是，加密和解密时使用的 $a$ 和 $b$ 值必须相同，否则无法正确解密。此外，如果使用的字母表大小 $m$ 不同，则也需要使用不同的 $a$ 和 $b$ 值。

  **加解密脚本**

  ```python
  import gmpy2
  
  
  def affine_encrypt(plaintext: str, a: int, b: int) -> str:
      """
      Affine encryption
      :param plaintext:明文
      :param a:要求与字母表大小（通常为26）互质
      :param b:任意整数
      :return:密文
      """
      ciphertext = ""
      for c in plaintext.upper():
          ciphertext += chr(((ord(c) - 65) * a + b) % 26 + 65)
      return ciphertext
  
  
  def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
      """
      Affine decryption
      :param ciphertext:密文
      :param a:
      :param b:
      :return:
      """
      plaintext = ""
      a_inv = gmpy2.invert(a, 26)
      for c in ciphertext:
          plaintext += chr((ord(c) - 65 - b) * a_inv % 26 + 65)
      return plaintext
  
  ```
  
- **简单替换密码**

  **原理**

  简单替换密码（也称作凯撒密码）是一种基本的密码算法，它的原理是将明文中的每个字母替换为一个固定数量的字母位置下移后的字母。例如，如果密钥为3，则明文中的每个字母都将替换为向下移动3个字母位置后的字母，例如'A'会替换为'D'，'B'会替换为'E'，以此类推。

  这种加密算法的安全性很弱，因为它容易受到各种攻击。例如，攻击者可以使用频率分析来确定密文中最常见的字母，从而猜测它们对应的明文字母。攻击者还可以使用已知明文攻击，即已知一些明文和对应的密文，从而推断出密钥的值。因此，简单替换密码不适合用于安全通信，但它可以作为一种学习密码学的入门算法。

  **加解密脚本**

  ```python
  # 简单替换密码加密脚本
  def simpleSubstitution_encrypt(plaintext: str, key: int) -> str:
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
  def simpleSubstitution_decrypt(ciphertext: str, key: int) -> str:
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
  ```

  

### 多表替换加密

- PlayFair

  **原理**

  Playfair 密码（Playfair cipher or Playfair square）是一种替换密码，1854 年由英国人查尔斯 · 惠斯通（Charles Wheatstone）发明，基本算法如下：

  1. 选取一串英文字母，除去重复出现的字母，将剩下的字母逐个逐个加入 5 × 5 的矩阵内，剩下的空间由未加入的英文字母依 a-z 的顺序加入。注意，将 q 去除，或将 i 和 j 视作同一字。
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

  **说人话版本**

  1. 先选一个密钥,比如说密钥是NSSCTF，然后我们把这个密钥填进一个5x5的表格里面，重复的字母不要。

     | N    | S    | C    | T    | F    |
     | ---- | ---- | ---- | ---- | ---- |
     |      |      |      |      |      |
     |      |      |      |      |      |
     |      |      |      |      |      |
     |      |      |      |      |      |

     

  2. 剩下的格子怎么填呢？按字母表A-Z依次填，还是老规矩，重复的字母不要。还要满足两个要求：①不要Q这个字母②I/J写在一起。

     | N    | S    | C    | T    | F    |
     | ---- | ---- | ---- | ---- | ---- |
     | A    | B    | D    | E    | G    |
     | H    | I/J  | K    | L    | M    |
     | O    | P    | Q    | R    | U    |
     | V    | W    | X    | Y    | Z    |

     这样就填好了

  3. 比如说我们要加密的句子是：“Reach the highest City”，我们把它两两分组

     ```
     RE AC HT HE HI GH ES TC IT Y
     ```

     这里Y落单了对吧？落单的字母我们在后面补X

  4. 我们来看第二组字母的相对位置

     ​	![image-20220523142043369](https://bestkasscn.oss-cn-hangzhou.aliyuncs.com/image-20220523142043369.png)

     A和C既不在同一行也不在同一列对吧？这个时候我们就要找两个字母让他们连起来是一个长方形，这里显然是N,D两个字母，但是先后顺序是什么呢？因为这一组字母中A在前面，所以我们以A这一行优先，跟R同一行的是D，所以第一组密文为DN

  5. 再来看一组同行的例子HI

     ![image-20220523142135341](https://bestkasscn.oss-cn-hangzhou.aliyuncs.com/image-20220523142135341.png)	

     对于这种情况，我们就去找他后面的那个字母，H -> I/J ，I/J -K ,所以密文是 I/J K

  6. 再来看一组同列的例子RE

     ![image-20220523142218258](https://bestkasscn.oss-cn-hangzhou.aliyuncs.com/image-20220523142218258.png)	

     还是去找他后面的字母 R -> Y,E -> L，密文为YL

  7. 这就是PlayFair的加密过程

  **Playfair密码的优点**

  Playfair密码与简单的单一字母替代法密码相比有了很大的进步

  虽然仅有26个字母，但有26×26＝676种字母对，因此，识别字母对要比单个字母要困难得多。

  一个明文字母有多种可能的代换密文字母，使得频率分析困难的多(hs成为BP,hq成为YP)

  Playfair密码过去长期被认为是不可破的。

  **加解密脚本**

  ```python
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
  
  
  plaintext = "HELLO WORLD"
  key = "SECRETKEY"
  ciphertext = playfair_encrypt(plaintext, key)
  decryptedtext = playfair_decrypt(ciphertext, key)
  print("Plaintext:", plaintext)
  print("Ciphertext:", ciphertext)
  print("Decrypted text:", decryptedtext)
  
  ```

- **棋盘密码**

  **原理**

  棋盘密码（也称为方格密码）是一种简单的加密技术，用于对短文本进行加密。它得名于它的工作原理类似于在棋盘上移动棋子。

  棋盘密码使用一个5×5的方格棋盘，其中每个方格填充了一个字母，通常是26个英文字母中的24个（字母"i"和"j"共用一个方格）。在加密消息时，将明文分成双字母组，例如“hello”将被分为“he”、“ll”和“o”。然后，对于每个双字母组，执行以下步骤：

  1. 如果双字母组中的两个字母相同，则在它们之间插入字母“x”（或“q”）来使它们不同。例如，“ll”会变成“lxl”。
  2. 如果双字母组中的两个字母不同，则找到它们在棋盘上的位置。将它们替换为另一对字母，方法是沿着相同的行（或列）移动一个方格，然后用该行（或列）中的下一个字母替换。如果该字母位于棋盘的边缘，则将其替换为该行（或列）的第一个字母。例如，如果双字母组是“he”，并且在棋盘上，h位于第2行第1列，e位于第1行第2列，那么可以将“he”替换为“dw”。
  3. 重复第2步，直到所有双字母组都已替换为新的双字母组。然后将所有双字母组连接起来，得到密文。

  解密消息时，只需使用相反的过程，即找到双字母组在棋盘上的位置，并向左或向上移动一个方格，然后用该行或列中的前一个字母替换。

  棋盘密码虽然简单，但已经被认为是不安全的加密方法。因此，现在很少用于实际的加密。

  **加解密脚本**

  ```python
  from pycipher import PolybiusSquare
  
  
  def polybius_encrypt(plaintext, key):
      polybius = PolybiusSquare(key)
      ciphertext = polybius.encipher(plaintext)
      return ciphertext
  
  
  def polybius_decrypt(ciphertext, key):
      polybius = PolybiusSquare(key)
      plaintext = polybius.decipher(ciphertext)
      return plaintext
  
  
  # 示例用法
  key = 'phqgiumeaylnofdxkrcvstzwb'
  plaintext = 'hello world'
  
  ciphertext = polybius_encrypt(plaintext, key)
  print(ciphertext)
  
  decrypted_text = polybius_decrypt(ciphertext, key)
  print(decrypted_text)
  
  ```
  
  
  
- **维吉尼亚密码**

  **原理**

  维吉尼亚密码（Vigenere）是使用一系列凯撒密码组成密码字母表的加密算法，属于多表密码的一种简单形式。

  ![维吉尼亚表格](https://ctf-wiki.org/crypto/classical/figure/vigenere1.jpg)

  下面给出一个例子
  
  ```
  明文：come greatwall
  密钥：crypto
  ```
  
  首先，对密钥进行填充使其长度与明文长度一样。
  
  | 明文 | c    | o    | m    | e    | g    | r    | e    | a    | t    | w    | a    | l    | l    |
  | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
  | 密钥 | c    | r    | y    | p    | t    | o    | c    | r    | y    | p    | t    | o    | c    |
  
  其次，查表得密文
  
  ![维吉尼亚加密](https://ctf-wiki.org/crypto/classical/figure/vigenere2.jpg)
  
  ```
  明文：come greatwall
  密钥：crypto
  密文：efkt zferrltzn
  ```
  
  **加解密脚本**
  
  ```python
  from string import ascii_uppercase, ascii_lowercase
  
  
  def vigenere_encrypt(plaintext: str, key: str) -> str:
      ciphertext = ''
      key_index = 0
      for char in plaintext:
          if char in ascii_uppercase:
              # 计算偏移量
              key_char = key[key_index % len(key)]
              shift = ord(key_char) - ord('A')
              # 加密字符
              ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
              key_index += 1
          elif char in ascii_lowercase:
              key_char = key[key_index % len(key)]
              shift = ord(key_char) - ord('a')
              # 加密字符
              ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
              key_index += 1
          else:
              ciphertext += char
      return ciphertext
  
  
  def vigenere_decrypt(ciphertext: str, key: str) -> str:
      plaintext = ''
      key_index = 0
      for char in ciphertext:
          if char in ascii_uppercase:
              # 计算偏移量
              key_char = key[key_index % len(key)]
              shift = ord(key_char) - ord('A')
              # 解密字符
              plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
              key_index += 1
          elif char in ascii_lowercase:
              # 计算偏移量
              key_char = key[key_index % len(key)]
              shift = ord(key_char) - ord('a')
              # 解密字符
              plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
              key_index += 1
          else:
              plaintext += char
      return plaintext
  ```
  
  
  
- **Autokey**

  **原理**

  Autokey加密算法是一种多表密码（Polyalphabetic Cipher）算法，它通过使用明文本身中的字符作为密钥的一部分，从而消除了像维吉尼亚密码那样的周期性密钥。

  具体来说，Autokey算法中，密钥不是固定的，而是随着明文的加密而不断增长。首先，从密钥中取出一个固定长度的字符串，称之为“种子”（seed），作为加密过程的起始密钥。接着，使用该密钥对明文进行加密。加密时，使用明文中的一个字符与密钥中的一个字符相加，然后将该值作为密文中的一个字符。使用的明文字符和密钥字符都要从表格中查找。

  在每个新的字符加密之后，将该字符添加到密钥的末尾，形成一个新的密钥。因此，后续加密过程中使用的密钥将会包含明文中前面加密过的字符。

  解密过程中，同样使用明文字符和密钥字符相减的方式，再查表格得到明文字符。

  Autokey算法的安全性依赖于密钥的长度，因此密钥必须足够长。然而，如果密钥太长，那么加密和解密的效率将会降低。因此，在实际应用中，需要根据需要平衡密钥长度和效率。

  **加解密脚本**

  ```python
  def autokey_encrypt(key:str, plaintext:str) -> str:
      key = key.upper()
      plaintext = plaintext.upper()
      ciphertext = []
      for i, c in enumerate(plaintext):
          if c == ' ':
              ciphertext.append(' ')
              continue
          k = ord(key[i % len(key)]) - ord('A')
          c = chr((ord(c) - ord('A') + k) % 26 + ord('A'))
          ciphertext.append(c)
          key += c if i < len(plaintext) - 1 else plaintext[i]
      return ''.join(ciphertext)
  
  
  def autokey_decrypt(key:str, ciphertext:str) -> str:
      key = key.upper()
      plaintext = []
      for i, c in enumerate(ciphertext):
          if c == ' ':
              plaintext.append(' ')
              continue
          k = ord(key[i % len(key)]) - ord('A')
          c = chr((ord(c) - ord('A') - k + 26) % 26 + ord('A'))
          plaintext.append(c)
          key += ciphertext[i] if i < len(ciphertext) - 1 else plaintext[i]
      return ''.join(plaintext)
  
  
  key = 'KEY'
  plaintext = 'HELLO WORLD'
  ciphertext = autokey_encrypt(key, plaintext)
  res = autokey_decrypt(key, ciphertext)
  print(ciphertext)
  print(res)
  ```

### 其他加密

- **培根密码**

  **原理**

  培根密码（Bacon cipher）是一种古典密码，它的原理是将一段明文（plaintext）通过替换成另一组字符的方式加密，从而形成密文（ciphertext）。这个替换规则是由英国哲学家、科学家培根（Francis Bacon）在16世纪提出的。

  具体来说，培根密码将明文中的每个字母转化为一组由A和B组成的5位二进制码（例如，字母A对应的二进制码是AAAAA，字母B对应的二进制码是AAAAB，以此类推）。这些二进制码可以用任何可以表示二进制的符号表示，例如用点和横线表示。然后，将这些二进制码与另一组由A和B组成的5位二进制码相对应，这组码被称为培根密码字母表（Baconian alphabet）。这个字母表通常有两种形式，分别称为普通字母表（plain alphabet）和扭曲字母表（distorted alphabet）。

  在加密时，将明文中的每个字母转换为对应的二进制码，并将这些二进制码替换为培根密码字母表中相应的二进制码。然后将这些二进制码转换为对应的字母即可得到密文。

  解密时，只需要将密文中的每个二进制码与培根密码字母表中的二进制码相匹配，然后将匹配的二进制码转换为对应的明文字母即可还原明文。

  **加解密脚本**

  ```python
  from string import ascii_lowercase
  
  bacon_table = {
      'a': 'AAAAA', 'g': 'AABBA', 'n': 'ABBAA', 't': 'BAABA',
      'b': 'AAAAB', 'h': 'AABBB', 'o': 'ABBAB', 'u': 'BAABB', 'v': 'BAABB',
      'c': 'AAABA', 'i': 'ABAAA', 'j': 'ABAAA', 'p': 'ABBBA', 'w': 'BABAA',
      'd': 'AAABB', 'k': 'ABAAB', 'q': 'ABBBB', 'x': 'BABAB',
      'e': 'AABAA', 'l': 'ABABA', 'r': 'BAAAA', 'y': 'BABBA',
      'f': 'AABAB', 'm': 'ABABB', 's': 'BAAAB', 'z': 'BABBB'
  }
  distorted_bacon_table = {
      'A': 'ABBAA', 'B': 'AABAB', 'C': 'BBAAB', 'D': 'BBAAA',
      'E': 'BAABB', 'F': 'BAAAA', 'G': 'AABBA', 'H': 'ABAAA',
      'I': 'ABBAB', 'J': 'AABAA', 'K': 'BBBAB', 'L': 'BBBAA',
      'M': 'BAAAB', 'N': 'ABABA', 'O': 'BABBA', 'P': 'BBAAB',
      'Q': 'BBABB', 'R': 'BAABA', 'S': 'AABBB', 'T': 'BABAB',
      'U': 'ABABB', 'V': 'ABBBB', 'W': 'BBBBA', 'X': 'BAABB',
      'Y': 'BAABA', 'Z': 'ABAAA'
  }
  
  
  def bacon_encrypt(plaintext: str, alphabet=None) -> str:
      """
      编码规则:i=j,u=v
      :param alphabet: 字母表规则，可任意设置
      :param plaintext:明文
      :return:
      """
      if alphabet is None: alphabet = bacon_table
      ciphertext = ''
      for s in plaintext.lower():
          if s in alphabet:
              ciphertext += ''.join(alphabet[s])
          else:
              pass
      return ciphertext
  
  
  def bacon_decrypt(ciphertext: str, alphabet=None) -> str:
      if alphabet is None: alphabet = bacon_table
      plaintext = ''
      for i in range(0, len(ciphertext), 5):
          for s in ascii_lowercase:
              if alphabet[s] == ciphertext[i:i + 5]:
                  plaintext += s
                  break
      return plaintext
  
  
  plaintext = 'this is a test flag'
  ciphertext = 'BAABAAABBBABAAABAAABABAAABAAABAAAAABAABAAABAABAAABBAABAAABABABABAAAAAAAABBA'
  print(bacon_encrypt(plaintext))
  print(bacon_decrypt(ciphertext))
  
  ```

  

- **栅栏密码**

  **原理**

  栅栏密码把要加密的明文分成 N 个一组，然后把每组的第 1 个字连起来，形成一段无规律的话。这里给出一个例子

  ```
  明文：THERE IS A CIPHER
  ```

  去掉空格后变为

  ```
  THEREISACIPHER
  ```

  分成两栏，两个一组得到

  ```
  TH ER EI SA CI PH ER
  ```

  先取出第一个字母，再取出第二个字母

  ```
  TEESCPE
  HRIAIHR
  ```

  连在一起就是

  ```
  TEESCPEHRIAIHR
  ```

  上述明文也可以分为 2 栏。

  ```
  THEREIS ACIPHER
  ```

  组合得到密文

  ```
  TAHCEIRPEHIESR
  ```

  **加解密脚本**

  ```python
  from pycipher.railfence import Railfence
  
  
  def railFence_encrypt(plaintext: str, key: int) -> str:
      """
      :param plaintext: 明文
      :param key:大于0的整数
      :return:
      """
      return Railfence(key).encipher(plaintext)
  
  
  def railFence_decrypt(ciphertext: str, key: int) -> str:
      """
  
      :param ciphertext:密文
      :param key: 大于0的整数
      :return:
      """
      return Railfence(key).decipher(ciphertext)
  
  
  def railfence_w_encrypt(plaintext: str, key: int) -> str:
      rails = [[] for _ in range(key)]
      rail, delta = 0, 1
      for ch in plaintext:
          rails[rail].append(ch)
          if rail == 0:
              delta = 1
          elif rail == key - 1:
              delta = -1
          rail += delta
      ciphertext = ''.join([ch for rail in rails for ch in rail])
      return ciphertext
  
  
  def railfence_w_decrypt(ciphertext: str, key: int) -> str:
      fence = [[None] * len(ciphertext) for _ in range(key)]
      rail, delta = 0, 1
      for i in range(len(ciphertext)):
          fence[rail][i] = 1
          if rail == 0:
              delta = 1
          elif rail == key - 1:
              delta = -1
          rail += delta
      index = 0
      for i in range(key):
          for j in range(len(ciphertext)):
              if fence[i][j] == 1:
                  fence[i][j] = ciphertext[index]
                  index += 1
      rail, delta = 0, 1
      plaintext = ""
      for i in range(len(ciphertext)):
          plaintext += fence[rail][i]
          if rail == 0:
              delta = 1
          elif rail == key - 1:
              delta = -1
          rail += delta
      return plaintext
  
  
  plaintext = "HELLO WORLD"
  key = 4
  
  # 加密
  ciphertext = railfence_w_encrypt(plaintext, key)
  print("密文：", ciphertext)
  
  # 解密
  plaintext = railfence_w_decrypt(ciphertext, key)
  print("明文：", plaintext)
  
  ```

- **列移位加密**

  **原理**

  列移位加密（Columnar Transposition Cipher）是一种简单的置换密码，通过对明文中的字符进行重新排列来生成密文。其基本原理是将明文按照一定的规则排列成一个矩阵，然后将矩阵的列按照一定的顺序排列，最后将排列后的矩阵中的字符按照列的顺序依次输出即可得到密文。

  具体步骤如下：

  1. 选择一个关键词作为列移位加密的密钥。

  2. 将明文按照密钥的字母顺序排列成一个矩阵。例如，如果密钥是“SECRET”，明文是“HELLO WORLD”，则将明文排列成一个 7 行 2 列的矩阵：

     ```
     rCopy codeS E C R E T
     H E L L O  
     W O R L D
     ```

  3. 将矩阵的列按照密钥的字母顺序排列。例如，如果密钥是“SECRET”，则将矩阵的列按照“S E C R E T”的顺序排列：

     ```
     rCopy codeS E C R E T
     L O H E L  
     D R W O L
     ```

  4. 将排列后的矩阵中的字符按照列的顺序依次输出，即得到密文：

     ```
     Copy code
     SLDDRO HLWEO EL
     ```

  注意：如果明文中的字符数不能完全填满矩阵，则可以用任意字符（如“X”）进行填充，以便构成完整的矩阵。

  解密过程类似，只需按照相同的密钥和步骤将密文转换成矩阵，然后将矩阵的列按照密钥的字母顺序重新排列，最后按照行的顺序依次输出即可得到原始明文。

  **加解密脚本**

  ```python
  from pycipher.columnartransposition import ColTrans
  
  
  def columnar_encrypt(plaintext: str, key: str) -> str:
      return ColTrans(key).encipher(plaintext)
  
  
  def columnar_decrypt(ciphertext: str, key: str) -> str:
      return ColTrans(key).decipher(ciphertext)
  
  
  plaintext = 'this is a test flag'
  ciphertext = columnar_encrypt(plaintext, 'German')
  print(columnar_encrypt(plaintext, 'German'))
  print(columnar_decrypt(ciphertext, 'German'))
  ```

- **云影密码**

  **原理**

  云影密码是一种古老的密码算法，它基于将文本围绕一根棒子上卷，然后从棒子上取下来的顺序来加密和解密文本。具体而言，该算法将明文分成多行，然后将每行字符从左到右写在一个棒子上，然后将棒子拿下来，以从上到下的顺序读取所有字符，以此生成密文。解密的过程是将密文放回原来的棒子上，并以从左到右的顺序读取所有字符，以此生成明文。

  **加解密算法**

  ````python
  def skytale_encrypt(plaintext: str, key: int) -> str:
      plaintext = plaintext.replace(" ", "").replace("\n", "")
      rows = (len(plaintext) + key - 1) // key
      padding = rows * key - len(plaintext)
      plaintext += "X" * padding
      ciphertext = ""
      for i in range(key):
          for j in range(rows):
              ciphertext += plaintext[j * key + i]
      return ciphertext
  
  
  def skytale_decrypt(ciphertext: str, key: int) -> str:
      rows = (len(ciphertext) + key - 1) // key
      plaintext = ""
      for i in range(rows):
          for j in range(key):
              index = j * rows + i
              if index < len(ciphertext):
                  plaintext += ciphertext[index]
      return plaintext
  
  
  plaintext = 'this is a test flag'
  key = 3
  ciphertext = skytale_encrypt(plaintext, key)
  print(ciphertext)
  print(skytale_decrypt(ciphertext, key))
  
  ````

- **与佛论禅**

  **原理**

  **加解密脚本**

  ```python
  """
  @FileName:yufolunchan.py
  @Description:与佛论禅密码
  @Author:bestkasscn
  @Time:2023/2/5
  @principle:
  """
  from Crypto.Cipher import AES
  from re import split
  from py7zr import SevenZipFile
  from io import BytesIO
  
  KEY = b'XDXDtudou@KeyFansClub^_^Encode!!'
  IV = b'Potato@Key@_@=_='
  
  foYue = [
      '滅', '苦', '婆', '娑', '耶', '陀', '跋', '多', '漫', '都', '殿', '悉', '夜', '爍', '帝', '吉',
      '利', '阿', '無', '南', '那', '怛', '喝', '羯', '勝', '摩', '伽', '謹', '波', '者', '穆', '僧',
      '室', '藝', '尼', '瑟', '地', '彌', '菩', '提', '蘇', '醯', '盧', '呼', '舍', '佛', '參', '沙',
      '伊', '隸', '麼', '遮', '闍', '度', '蒙', '孕', '薩', '夷', '迦', '他', '姪', '豆', '特', '逝',
      '朋', '輸', '楞', '栗', '寫', '數', '曳', '諦', '羅', '曰', '咒', '即', '密', '若', '般', '故',
      '不', '實', '真', '訶', '切', '一', '除', '能', '等', '是', '上', '明', '大', '神', '知', '三',
      '藐', '耨', '得', '依', '諸', '世', '槃', '涅', '竟', '究', '想', '夢', '倒', '顛', '離', '遠',
      '怖', '恐', '有', '礙', '心', '所', '以', '亦', '智', '道', '。', '集', '盡', '死', '老', '至']
  
  BYTEMARK = ['冥', '奢', '梵', '呐', '俱', '哆', '怯', '諳', '罰', '侄', '缽', '皤']
  
  ruShiWoWen = [
      '謹', '穆', '僧', '室', '藝', '瑟', '彌', '提', '蘇', '醯', '盧', '呼', '舍', '參', '沙', '伊',
      '隸', '麼', '遮', '闍', '度', '蒙', '孕', '薩', '夷', '他', '姪', '豆', '特', '逝', '輸', '楞',
      '栗', '寫', '數', '曳', '諦', '羅', '故', '實', '訶', '知', '三', '藐', '耨', '依', '槃', '涅',
      '竟', '究', '想', '夢', '倒', '顛', '遠', '怖', '恐', '礙', '以', '亦', '智', '盡', '老', '至',
      '吼', '足', '幽', '王', '告', '须', '弥', '灯', '护', '金', '刚', '游', '戏', '宝', '胜', '通',
      '药', '师', '琉', '璃', '普', '功', '德', '山', '善', '住', '过', '去', '七', '未', '来', '贤',
      '劫', '千', '五', '百', '万', '花', '亿', '定', '六', '方', '名', '号', '东', '月', '殿', '妙',
      '尊', '树', '根', '西', '皂', '焰', '北', '清', '数', '精', '进', '首', '下', '寂', '量', '诸',
      '多', '释', '迦', '牟', '尼', '勒', '阿', '閦', '陀', '中', '央', '众', '生', '在', '界', '者',
      '行', '于', '及', '虚', '空', '慈', '忧', '各', '令', '安', '稳', '休', '息', '昼', '夜', '修',
      '持', '心', '求', '诵', '此', '经', '能', '灭', '死', '消', '除', '毒', '害', '高', '开', '文',
      '殊', '利', '凉', '如', '念', '即', '说', '曰', '帝', '毘', '真', '陵', '乾', '梭', '哈', '敬',
      '禮', '奉', '祖', '先', '孝', '雙', '親', '守', '重', '師', '愛', '兄', '弟', '信', '朋', '友',
      '睦', '宗', '族', '和', '鄉', '夫', '婦', '教', '孫', '時', '便', '廣', '積', '陰', '難', '濟',
      '急', '恤', '孤', '憐', '貧', '創', '廟', '宇', '印', '造', '經', '捨', '藥', '施', '茶', '戒',
      '殺', '放', '橋', '路', '矜', '寡', '拔', '困', '粟', '惜', '福', '排', '解', '紛', '捐', '資']
  
  
  def DecryptFoYue(ciphertext):
      data = b''
      i = 0
      while i < len(ciphertext):
          if ciphertext[i] in BYTEMARK:
              i = i + 1
              data = data + bytes([foYue.index(ciphertext[i]) + 128])
          else:
              data = data + bytes([foYue.index(ciphertext[i])])
          i = i + 1
      cryptor = AES.new(KEY, AES.MODE_CBC, IV)
      result = cryptor.decrypt(data)
      flag = result[-1]
      if flag < 16 and result[-flag] == flag:
          result = result[:-flag]
      return result.decode('utf-16le')
  
  
  def DecryptRuShiWoWen(ciphertext):
      data = b''
      for i in ciphertext:
          data += bytes([ruShiWoWen.index(i)])
      cryptor = AES.new(KEY, AES.MODE_CBC, IV)
      fsevenZip = SevenZipFile(BytesIO(cryptor.decrypt(data)))
      zipContent = fsevenZip.readall()['default'].read()
      return zipContent
  
  
  if __name__ == '__main__':
      try:
          foYu = "佛曰：奢他奢所諳訶滅呐老至皤婆悉罰蒙怯諸侄遠諳知奢藐呐滅哆滅缽佛蘇諸薩大諳藐阿不有奢豆槃罰數怯室喝怯藝呐怖彌怯佛世滅怯耨冥無涅心佛無曰摩怖逝度無集呐耨羅輸罰帝奢朋冥究盧諸般參耨朋究寫瑟梵道梵遠勝涅皤婆怯醯者迦智奢遮缽姪俱朋世皤無舍寫呼悉迦集諳亦等冥若冥般心娑哆道冥倒俱故迦諳遮槃那"
  
          foYu = split("[:：]", foYu)
          if len(foYu) > 1:
              foYu = "".join(foYu[1:]).strip()
          else:
              foYu = foYu[0]
          print(DecryptFoYue(foYu))
      except:
          print(DecryptRuShiWoWen(foYu))
  
  ```

  

- **ADFGX**

  **原理**

  ADFGX密码是一种基于多表置换和替代的密码技术，由德国陆军在一战期间使用。

  其加密过程如下：

  1. 生成一个 5x5 的多表，包含字母 A-Z 和数字 0-9。在此基础上，加上字母 ADFGX。
  2. 将明文转换为大写字母，并且将 I/J 视为一个字符。然后使用多表中的字母进行置换，例如，字母 A 用 ADFGX 代替，字母 B 用 ADGGX 代替，以此类推。
  3. 将替换后的字母分组为两个一组，并将它们在多表中找到相应的行和列。这样就得到了一对坐标，即 ADFGX 字母对应的行和列。这两个坐标就是密文的一组。
  4. 重复步骤 2 和 3 直到整个明文都被转换成密文。

  解密过程与加密过程类似，只需要反向应用多表的置换和替换规则即可。

  由于 ADGFVX 密码比其他密码技术更加复杂，所以在一战期间它曾被广泛使用。但是，它并不是一种非常安全的密码技术，因为它的密钥空间较小，而且容易受到攻击。在现代密码学中，ADGFVX密码已经被更安全的密码技术所取代。

  **加解密脚本**

  ```python
  from pycipher import ADFGX
  
  
  def adfgx_encrypt(plaintext: str, key: str, keyword: str) -> str:
      return ADFGX(key, keyword).encipher(plaintext)
  
  
  def adfgx_decrypt(ciphertext: str, key: str, keyword: str) -> str:
      return ADFGX(key, keyword).decipher(ciphertext)
  
  
  key = 'PHQGMEAYNOKSFBDLRCIVUXWTZ'
  keyword = 'SPRING'
  
  plaintext = 'HELLO WORLD'
  
  # 加密
  ciphertext = ADFGX(key, keyword).encipher(plaintext)
  
  # 解密
  decryptedtext = ADFGX(key, keyword).decipher(ciphertext)
  
  print("Plaintext: ", plaintext)
  print("Ciphertext: ", ciphertext)
  print("Decryptedtext: ", decryptedtext)
  ```

  

- **ADFGVX**

  **原理**

  ADFGVX密码是一种基于置换和替换的加密方法，由德国军官弗里德里希·德尔巴赫在第一次世界大战期间发明。

  ADFGVX密码的加密过程包括以下步骤：

  1. 生成一个5x5的多表，其中包含字母A至Z和数字0至9，以及ADFGVX六个字母。这个表是由一个密钥和一个加密单元共同生成的。
  2. 将明文分割成单个字母，然后用多表中的对应字母进行替换。例如，字母A用ADFGVX替换，字母B用ADFGVX的下一个字母DF替换，以此类推。
  3. 将替换后的字母分组，每组包含两个字母。这些字母会在多表中找到对应的行和列，组成一个二维坐标，形成一个新的密文。
  4. 对于每个密文坐标，都用相应的ADFGVX字母来替换。例如，坐标(3,4)用字母G替换，坐标(1,1)用字母A替换。
  5. 最后，将所有替换后的字母组合在一起，形成一个密文。

  解密过程与加密过程类似，只是将加密和解密的步骤反过来执行。

  ADFGVX密码的安全性依赖于密钥的强度和多表的随机性，以及密文的长度。然而，由于现代密码破解技术的不断发展，ADFGVX密码已经不再被认为是一种安全的加密方法，因此在实际应用中已经被其他更加安全的加密方法所替代。

  **加解密脚本**

  ```python
  from pycipher import ADFGVX
  import random
  
  
  def adfgvx_encrypt(key: str, plaintext: str) -> str:
      """
  
      :param key: 密钥必须包含 36 个不同的字符
      :param plaintext:
      :return:
      """
      cipher = ADFGVX(key)
      return cipher.encipher(plaintext)
  
  
  def adfgvx_decrypt(key: str, ciphertext: str) -> str:
      """
  
      :param key: 密钥必须包含 36 个不同的字符
      :param ciphertext:
      :return:
      """
      cipher = ADFGVX(key)
      return cipher.decipher(ciphertext)
  
  
  def generate_adfgvx_test_cases(times=None) -> list:
      """
  
      :param times:生成多少组测试用例
      :return:
      """
      # generate some test cases
      test_cases = []
      for i in range(times or 3):
          # generate key
          key = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 36))
          # generate plaintext and ciphertext
          plaintext = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 10))
          ciphertext = adfgvx_encrypt(key, plaintext)
          # add test case
          test_case = {
              'key': key,
              'plaintext': plaintext,
              'ciphertext': ciphertext
          }
          test_cases.append(test_case)
      return test_cases
  ```
  
  

## 现代密码基础

### base家族

**base16**

**简介**：

在计算机中一个字节=8比特，base16以4个比特为一组进行切分，每一组内的4个比特可转换到指定的16个ASCII字符中的一个，将转换后的ASCII字符连接起来，就是编码后的数据。

**字典**：

```txt
'0123456789ABCDEF'
```

**实现**：

```python
def base16encode(plaintext):
    res = ''
    for s in plaintext:
        bin_1, bin_2 = bin(ord(s))[2:-4], bin(ord(s))[-4:]  # 将字符对应ascii码转成二进制
        res_1, res_2 = dir_base16[int(bin_1, 2)], dir_base16[int(bin_2, 2)]  # 与字典作映射
        res += ''.join(res_1 + res_2)
    return res


def base16decode(plaintext):
    plaintext = plaintext.upper()
    res = ''
    for i in range(0, len(plaintext), 2):
        bin_1, bin_2 = bin(dir_base16.index(plaintext[i])), bin(dir_base16.index(plaintext[i + 1]))[2:]
        while len(bin_2) != 4:
            bin_2 = '0' + bin_2  # 低位补齐4位
        res += ''.join(chr(int(bin_1 + bin_2, 2)))
    return res
```



### 初等数论

**欧几里得算法**

**扩展欧几里得算法**

**模逆元**

**中国剩余定理**

**费马定理**

**威尔逊定理**

### hash

### 常用工具

**ciphey**

**gmpy2**

**cryptodotome**

**sage**

**sympy**

**numpy**

**pwntools**

## 流密码

### LCG

## 对称密码

### DES

- **ECB模式**

  ECB（Electronic Codebook）是一种基础的加密模式，它将明文划分成固定长度的块，每个块独立地进行加密处理，因此同一块明文加密后的密文总是相同的。这种加密方式存在一些安全问题，容易受到以下攻击：

  1. 重放攻击（Replay Attack）：攻击者可以拦截ECB加密的密文，并重复发送到目标系统，目标系统对每个块进行解密，攻击者就能获取明文信息。

     当ECB模式用于数据加密时，如果同样的明文块被重复加密，会得到相同的密文块。这就给了攻击者一个机会，即将以前拦截的密文块重新发送到系统中，从而达到重复攻击的目的。

     重放攻击可能导致以下危害：

     1. 信息泄露：攻击者可以窃取敏感信息，例如密码、个人信息、财务信息等。
     2. 身份盗窃：攻击者可以重复执行某些操作，例如转移资金、修改账户信息、购买商品等，导致用户财产损失。
     3. 数据篡改：攻击者可以篡改已经传输的数据，例如更改订单信息、修改文件内容等，导致系统异常或数据不一致。
     4. 系统崩溃：攻击者可以向系统发送大量的重复请求，导致系统崩溃或停止工作。

  2. 字典攻击（Dictionary Attack）：攻击者可以通过拦截大量的密文，并尝试解密每个块，来生成一个字典表，之后再拦截到新的密文时，可以通过字典表轻易地获取明文信息。

  3. 选择明文攻击（Known Plaintext Attack）：攻击者通过获取部分明文和对应的密文，可以推断出加密算法的密钥，从而获取其他密文的明文信息。

  4. 明文分组攻击（Ciphertext Block Substitution Attack）：攻击者可以通过替换密文块，或者在密文中插入新块，来生成一个新的密文，但仍能够被正确地解密。这种攻击方式通常需要在已知明文块的前提下才能实现。

### AES

### TEA家族

- TEA

  **原理**

  TEA（Tiny Encryption Algorithm）是一个基于对称密钥的轻量级加密算法，由 David Wheeler 和 Roger Needham 在 1994 年提出。TEA 算法使用 64 位数据块和 128 位密钥，采用分组密码的模式进行加密。TEA 的主要优点是其简单、紧凑且易于实现，特别适合需要低资源消耗的加密场景。

  TEA 算法的工作原理如下：

  1. 将 64 位明文数据块分为两部分，左半部分为 v0，右半部分为 v1。
  2. 将 128 位密钥分为四个 32 位子密钥（K0，K1，K2，K3）。
  3. 选择一个常量 delta（0x9e3779b9），这是一个特殊的常数，它是黄金比例的倒数乘以 2^32。
  4. 进行 32 轮加密操作（默认轮数为 32，可以根据需要调整）： a. 将 delta 累加到一个名为 sum 的变量中。 b. 使用以下加密操作更新 v0 和 v1：
     - v0 = v0 + (((v1 << 4) + K0) ^ (v1 + sum) ^ ((v1 >> 5) + K1))
     - v1 = v1 + (((v0 << 4) + K2) ^ (v0 + sum) ^ ((v0 >> 5) + K3)) c. 每轮完成后，v0 和 v1 分别用于下一轮操作。
  5. 将 v0 和 v1 拼接成一个 64 位密文数据块。

  **加解密算法**

  ```python
  from typing import List
  import struct
  import secrets
  
  
  def generate_random_key(key_length=16):
      return secrets.token_bytes(key_length)
  
  
  def to_byte_blocks(s: str, block_size: int = 8) -> List[str]:
      while len(s) % block_size != 0:
          s += '\0'
      return [s[i:i + block_size] for i in range(0, len(s), block_size)]
  
  
  def from_byte_blocks(blocks: List[str]) -> str:
      return b''.join(blocks).decode("utf-8").rstrip('\0')
  
  
  def TEA_encrypt(plaintext: str, key: bytes) -> bytes:
      key_ints = struct.unpack(">4I", key)
      plaintext_blocks = to_byte_blocks(plaintext)
      ciphertext_blocks = []
  
      for block in plaintext_blocks:
          v0, v1 = struct.unpack(">2I", block.encode("utf-8"))
          delta = 0x9e3779b9
          sum_ = 0
  
          for _ in range(32):
              sum_ = (sum_ + delta) & 0xffffffff
              v0 += ((v1 << 4) + key_ints[0]) ^ (v1 + sum_) ^ ((v1 >> 5) + key_ints[1])
              v0 &= 0xffffffff
              v1 += ((v0 << 4) + key_ints[2]) ^ (v0 + sum_) ^ ((v0 >> 5) + key_ints[3])
              v1 &= 0xffffffff
  
          ciphertext_blocks.append(struct.pack(">2I", v0, v1))
  
      return b''.join(ciphertext_blocks)
  
  
  def TEA_decrypt(ciphertext: bytes, key: bytes) -> str:
      key_ints = struct.unpack(">4I", key)
      ciphertext_blocks = to_byte_blocks(ciphertext.decode("latin1"))
      plaintext_blocks = []
  
      for block in ciphertext_blocks:
          v0, v1 = struct.unpack(">2I", block.encode("latin1"))
          delta = 0x9e3779b9
          sum_ = (delta * 32) & 0xffffffff
  
          for _ in range(32):
              v1 -= ((v0 << 4) + key_ints[2]) ^ (v0 + sum_) ^ ((v0 >> 5) + key_ints[3])
              v1 &= 0xffffffff
              v0 -= ((v1 << 4) + key_ints[0]) ^ (v1 + sum_) ^ ((v1 >> 5) + key_ints[1])
              v0 &= 0xffffffff
              sum_ -= delta
  
          plaintext_blocks.append(struct.pack(">2I", v0, v1))
  
      return from_byte_blocks(plaintext_blocks)
  ```

  

- XTEA

  **原理**

  XTEA（Extended Tiny Encryption Algorithm）是一种对称加密算法，由 David Wheeler 和 Roger Needham 在 1997 年提出。XTEA 是 Tiny Encryption Algorithm（TEA）的改进版本，设计目的是解决 TEA 算法中的已知弱点。XTEA 使用 64 位数据块和 128 位密钥，采用分组密码模式进行加密。

  XTEA 算法的工作原理如下：

  1. 将 64 位明文数据块分为两部分，左半部分为 v0，右半部分为 v1。
  2. 将 128 位密钥分为四个 32 位子密钥（K0，K1，K2，K3）。
  3. 选择一个常量 delta（0x9e3779b9），这是一个特殊的常数，它是黄金比例的倒数乘以 2^32。
  4. 进行 32 轮加密操作（默认轮数为 32，可以根据需要调整）： a. 将 delta 累加到一个名为 sum 的变量中。 b. 使用以下加密操作更新 v0 和 v1：
     - v0 = v0 + (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key_ints[sum & 3])
     - v1 = v1 + (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key_ints[(sum >> 11) & 3]) c. 每轮完成后，v0 和 v1 分别用于下一轮操作。
  5. 将 v0 和 v1 拼接成一个 64 位密文数据块。

  **加解密算法**

  ```python
  import struct
  from typing import List
  
  
  def to_byte_blocks(s: str, block_size: int = 8) -> List[str]:
      while len(s) % block_size != 0:
          s += '\0'
      return [s[i:i + block_size] for i in range(0, len(s), block_size)]
  
  
  def from_byte_blocks(blocks: List[str]) -> str:
      return b''.join(blocks).decode("utf-8").rstrip('\0')
  
  
  def XTEA_encrypt(plaintext, key, num_rounds=32):
      key_ints = struct.unpack(">4I", key)
      plaintext_blocks = to_byte_blocks(plaintext)
      ciphertext_blocks = []
  
      for block in plaintext_blocks:
          v0, v1 = struct.unpack(">2I", block.encode('utf-8'))
          delta = 0x9e3779b9
          sum_ = 0
  
          for _ in range(num_rounds):
              sum_ = (sum_ + delta) & 0xffffffff
              v0 += ((v1 << 4) ^ (v1 >> 5)) + v1 ^ (sum_ + key_ints[sum_ & 3])
              v0 &= 0xffffffff
              v1 += ((v0 << 4) ^ (v0 >> 5)) + v0 ^ (sum_ + key_ints[(sum_ >> 11) & 3])
              v1 &= 0xffffffff
  
          ciphertext_blocks.append(struct.pack(">2I", v0, v1))
  
      return b''.join(ciphertext_blocks)
  
  
  def XTEA_decrypt(ciphertext, key, num_rounds=32):
      key_ints = struct.unpack(">4I", key)
      ciphertext_blocks = to_byte_blocks(ciphertext.decode("latin1"))
      plaintext_blocks = []
  
      for block in ciphertext_blocks:
          v0, v1 = struct.unpack(">2I", block.encode("latin1"))
          delta = 0x9e3779b9
          sum_ = (delta * num_rounds) & 0xffffffff
  
          for _ in range(num_rounds):
              v1 -= ((v0 << 4) ^ (v0 >> 5)) + v0 ^ (sum_ + key_ints[(sum_ >> 11) & 3])
              v1 &= 0xffffffff
              v0 -= ((v1 << 4) ^ (v1 >> 5)) + v1 ^ (sum_ + key_ints[sum_ & 3])
              v0 &= 0xffffffff
              sum_ -= delta
  
          plaintext_blocks.append(struct.pack(">2I", v0, v1))
  
      return from_byte_blocks(plaintext_blocks)
  ```

  

- XXTEA

  **原理**

  XXTEA（Extended Tiny Encryption Algorithm）是一种对称加密算法，由 David Wheeler 和 Roger Needham 在 1998 年提出。XXTEA 是 TEA 和 XTEA 加密算法的扩展，它改进了这些算法的弱点并提供了更好的安全性。XXTEA 算法与 TEA 和 XTEA 不同之处在于，它采用了可变长度的数据块（而不是固定的 64 位数据块）和 128 位密钥。

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

  加解密脚本
  
  ```python
  import xxtea
  
  
  def xxtea_encrypt(plain_text: str, key: str) -> bytes:
      # 填充key至16字节
      key = key.ljust(16, '\0')
      # 将明文转换成bytes类型
      plain_text_bytes = plain_text.encode('utf-8')
      # 使用xxtea进行加密
      cipher_bytes = xxtea.encrypt(plain_text_bytes, key)
      return cipher_bytes
  
  
  def xxtea_decrypt(cipher_bytes: bytes, key: str) -> str:
      # 填充key至16字节
      key = key.ljust(16, '\0')
      # 使用xxtea进行解密
      plain_text_bytes = xxtea.decrypt(cipher_bytes, key)
      # 将解密后的bytes转换成字符串
      plain_text = plain_text_bytes.decode('utf-8')
      return plain_text
  
  
  def test_xxtea():
      key = 'MyKey1234567890'
      plaintext = 'Hello, World!'
      ciphertext = xxtea_encrypt(plaintext, key)
      decrypted_text = xxtea_decrypt(ciphertext, key)
      assert decrypted_text == plaintext, "Decryption failed!"
      print("Encryption and decryption successful.")
  
  
  if __name__ == '__main__':
      test_xxtea()
  
  ```
  
  

**ECB攻击**

**CBC字节反转攻击**

## 非对称密码

### RSA

**素数分解**

**共模攻击**

**Rabin攻击**

**wiener攻击**

**coppersmith相关**

### ECC

**加密过程**

1. 选取一条椭圆曲线Ep(a,b)，并取椭圆曲线上一点作为基点P

2. 选定一个大数K作为私钥，并生成公钥Q = K*P

3. 加密：选择一个随机数r(r < n)，将消息M生成密文C

   密文是一个点对，C = （r*P，M * r*Q）

4. 解密：M = r * Q - K * (r * P) = M + r * (K * p) - K * (r * P) = M

**算法原理**

椭圆曲线公式：
$$
y^2 = ax^3 + bx^2 + cx + d
$$
函数图像：

![img](https://bestkasscn.oss-cn-hangzhou.aliyuncs.com/6534448-3f48559bcc4d4ceb.png)

椭圆曲线是连续的，并不适合加密，所以要把椭圆曲线变成离散的点

如何将椭圆曲线变成离散的点？定义在有限域上。

**域**：对集合中的元素进行加减乘除，结果不会超出集合，称为域。

有限域：如果域F中只包含有限个元素，则称为有限域。

**阶**：有限域中的元素的个数称为阶。

每个有限域的阶必为素数的幂，表示为
$$
p^n
$$
(p是素数，n是正整数，该有限域通常称为Galois域，记作
$$
GF(p^n)
$$
)

此时函数的表达式为
$$
y^2 = x^3 + ax + b (mod p^n)
$$
**有限域上的椭圆曲线运算**
$$
A(x_1,y_1) \qquad
B(x_2,y_2)\qquad
C(x_3,y_3)\\
x_3 ≡ k^2 - x_1 - x_2\ (mod p)\\
y_3 ≡ k(x_1 - x_3) - y_1\\
若 A = B，则K = 3*x_1^2 + \frac{3x_1^2 + a}{2y_1} \ (mod p)\\
若 A ≠ B，则K = \frac{y_2 - y_1}{x_2 - x_1} \ (mod p)
$$
举个例子
$$
y^2 = x^3 + x + 1 \ (mod 23),GF(23),基点A(0,1)\\
现在要计算2A\\
∵A = A,所以k = \frac{3*0^2 + 1}{2}\ (mod\ 23) \ = \frac{1}{2}\ mod \ 23\\
∴n ≡ \ \frac{1}{2} \ mod \ 23 \\
∴2n ≡ \ 1 \ mod \ 23\\
∴2n \ mod \ 23 \ = \ 1\\
∴n = 12\\
∴k \ = \ 12\\
x_3 = 12^2 - 0 - 0 = 144 \ mod \ 23 \ = \ 6 \\ 
y_3 = 12(0-6) - 1 \ mod \ 23 = -73 \ mod \ 23\\
$$
负数取模
$$
x \ mod \ y = x - y * [\frac{x}{y}](向下取整)\\
\ \ \ \ \ \ \ \ \ \ = -73 - 23 * (\frac{-73}{23})\\
\ = -73 + 24*4\\
= 19
$$
最终算出2A(6,19)

**python实现**

```python
import gmpy2
import random
from Crypto.Util.number import *
from secret import flag

# 计算两个点的和
def plus(P, Q, p, a):
    try:
        if P == Q:
            k = ((3 * P[0] ** 2 + a) * gmpy2.invert(2 * P[1], p)) % p
        else:
            k = (Q[1] - P[1]) * gmpy2.invert(Q[0] - P[0], p) % p
        x = (k ** 2 - P[0] - Q[0]) % p
        y = (k * (P[0] - x) - P[1]) % p
        return x, y
    except:
        pass

# 获得阶n
def get_n(P, Q, p, a):
    for i in range(99999):
        Q = plus(P, Q, p, a)
        if Q is None:
            return i
    return 99999

# 生成可用的所有基点
def get_G(a, b, p):
    try:
        G_list = []
        for x in range(99999):
            c = (x ** 3 + a * x + b) % p
            y = gmpy2.iroot(c, 2)
            if y[1]:
                G_list.append((x.real, int(y[0])))
        return list(set(G_list))
    except:
        pass

# 计算n * p
def get_np(P, Q, p, a, K):
    for i in range(K):
        Q = plus(P, Q, p, a)
    return Q

# 明文
m = bytes_to_long(flag.encode())
a = 1
b = 1
p = getPrime(200)
assert (4 * (a ** 3) + 27 * (b ** 2)) % p != 0
G = get_G(a, b, p)
P = get_G(a, b, p)[random.randint(0, 1)]
n = get_n(P, P, p, a)
r = random.randint(1, n)
K = random.randint(1, n)
Q = get_np(P, P, p, a, K)
rP = get_np(P, P, p, a, r)
rQ = get_np(Q, Q, p, a, r)
# 最终密文
C = ((int(rP[0]), int(rP[1])), int(rQ[0]) * m)
```



### 离散对数

### 格密码


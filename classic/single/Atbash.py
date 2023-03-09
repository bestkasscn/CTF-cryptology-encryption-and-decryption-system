from string import ascii_lowercase, ascii_uppercase

dir_atbash_lower = ascii_lowercase[::-1]
dir_atbash_upper = ascii_uppercase[::-1]


def atbash_attack(plaintext: str):
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
print(atbash_attack(plaintext))

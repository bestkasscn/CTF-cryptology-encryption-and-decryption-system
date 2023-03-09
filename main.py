import re
import math


def kasiski(s, min_num=3, outfile=None):
    is_debug = False

    debug = lambda *args, **kwargs: is_debug and print(*args, **kwargs)

    def normalize(s):
        s = s.strip().upper()
        s = re.sub(r'[^A-Z]+', '', s)
        return s

    s = normalize(s)
    out = ''

    matches = []
    found = {}
    for k in range(min_num, len(s) // 2):
        found[k] = {}
        shouldbreak = True
        for i in range(0, len(s) - k):
            v = s[i:i + k]
            if v not in found[k]:
                found[k][v] = 1
            else:
                found[k][v] += 1
                shouldbreak = False

        if shouldbreak:
            break

        for v in found[k]:
            if found[k][v] > 2:
                matches.append(v)

    out += "Length  Count  Word        Factor  Location (distance)\n"
    out += "======  =====  ==========  ======  ===================\n"
    keylens = {}
    for v in matches:
        k = len(v)
        p = []
        for i in range(len(s)):
            if s[i:i + k] == v:
                p.append(i)

        # assuming len(p) > 1
        factor = p[1] - p[0]
        for i in range(2, len(p)):
            factor = math.gcd(factor, p[i] - p[i - 1])

        locations = ""
        for i in range(len(p)):
            locations += "%d " % p[i]
            if i > 0:
                locations += "(%d) " % (p[i] - p[i - 1])

        out += "%6d  %5d  %10s  %6d  %s\n" % (k, found[k][v], v, factor, locations)

    if outfile is None:
        return out
    else:
        with open(outfile, 'w') as f:
            f.write(out)
        return None


input_str = 'Example input string'
min_length = 3
output_file = 'output.txt'

result = kasiski(input_str, min_length, output_file)

if result is not None:
    print(result)

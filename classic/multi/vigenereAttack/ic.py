import string
import processing
import freq_analysis as fa
from sys import maxsize
from const import EN_IC


def index_of_coincidence(letter_counts):
    numerator = sum([letter_counts[l]*(letter_counts[l]-1) for l in string.ascii_uppercase])
    text_size = sum(occurrences for occurrences in letter_counts.values())
    denominator = text_size*(text_size-1)
    return numerator/denominator


def find_key_length(ciphertext, max_key_length):
    min_diff = maxsize
    key_length = 0
    for candidate_length in range(1, max_key_length + 1):
        blocks = processing.get_blocks(text=ciphertext, size=candidate_length)
        columns = processing.get_columns(blocks)
        ics = [index_of_coincidence(letter_counts=fa.get_letter_counts(text=column)) for column in columns]
        delta_bar_ic = sum(ics) / len(ics)
        if EN_IC - delta_bar_ic < min_diff:
            min_diff = EN_IC - delta_bar_ic
            key_length = candidate_length
        print('当前密钥长度: ' + str(candidate_length) + '\n')
    return key_length

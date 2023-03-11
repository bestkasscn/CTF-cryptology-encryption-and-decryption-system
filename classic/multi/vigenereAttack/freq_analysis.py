import processing
import string
from const import EN_REL_FREQ


def get_letter_counts(text):
    text_upper = text.upper()
    letter_counts = {}
    for index, letter in enumerate(string.ascii_uppercase):
        letter_counts[letter] = text_upper.count(letter)
    return letter_counts


def get_letter_frequencies(text):
    letter_counts = get_letter_counts(text)
    frequencies = {letter: count/len(text) for letter, count in letter_counts.items()}
    return frequencies


def shift_text(text, amount):
    shifted = ''
    letters = string.ascii_uppercase
    for letter in text:
        shifted += letters[(letters.index(letter)-amount) % len(letters)]
    return shifted


def correlation(text, lf):
    return sum([(lf[letter]*EN_REL_FREQ[letter]) for letter in text])


def find_key_letter(text, lf):
    key_letter = ''
    max_corr = 0
    for count, letter in enumerate(string.ascii_uppercase):
        shifted = shift_text(text=text, amount=count)
        corr = correlation(text=shifted, lf=lf)
        if corr > max_corr:
            max_corr = corr
            key_letter = letter
    return key_letter


def restore_key(ciphertext, key_length):
    key = ''
    blocks = processing.get_blocks(text=ciphertext, size=key_length)
    columns = processing.get_columns(blocks)
    frequencies = get_letter_frequencies(text=ciphertext)
    for column in columns:
        key += find_key_letter(text=column, lf=frequencies)
    return key
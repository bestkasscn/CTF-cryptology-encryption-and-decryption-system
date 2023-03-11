from math import sqrt


def get_repeated_sequence_positions(text, sequence_length):
    sequence_positions = {}  # entries of sequence : [positions]
    for i, char in enumerate(text):
        next_sequence = text[i:i + sequence_length]
        if next_sequence in sequence_positions.keys():
            sequence_positions[next_sequence].append(i)
        else:
            sequence_positions[next_sequence] = [i]
    repeated_sequences = list(filter(lambda x: len(sequence_positions[x]) >= 2, sequence_positions))
    repeated_sequence_positions = [(seq, sequence_positions[seq]) for seq in repeated_sequences]
    return repeated_sequence_positions


def get_spacings(positions):
    return [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]


def get_factors(number):
    factors = set()
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return sorted(factors)


def get_candidate_key_lengths(factor_lists, max_key_length):
    all_factors = [factor_lists[lst][fac] for lst in range(len(factor_lists)) for fac in range(len(factor_lists[lst]))]
    # exclude factors larger than suspected max key length
    candidate_lengths = list(filter(lambda x: x <= max_key_length, all_factors))
    # sort by probability (descending)
    sorted_candidates = sorted(set(candidate_lengths), key=lambda x: all_factors.count(x), reverse=True)
    return sorted_candidates


def find_key_length(ciphertext, sequence_length, max_key_length):
    # find repeated sequences and their positions
    repeated_sequence_positions = get_repeated_sequence_positions(text=ciphertext, sequence_length=sequence_length)
    sequence_spacings = {}
    for sequence, positions in repeated_sequence_positions:
        sequence_spacings[sequence] = get_spacings(positions)
    # calculate spacings between positions of each repeated
    # sequence and factor out spacings
    factor_lists = []
    for spacings in sequence_spacings.values():
        for space in spacings:
            factor_lists.append(get_factors(number=space))
    # get common factors by descending frequency,
    # which constitute candidate key lengths
    candidate_key_lengths = get_candidate_key_lengths(factor_lists=factor_lists, max_key_length=max_key_length)
    key_length = candidate_key_lengths[0]
    return key_length

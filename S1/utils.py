import numpy as np
import pandas as pd

# verify 2 strings equal
def is_strs_equal(s1, s2):
    if s1 == s2:
        print("Correct!")
    else:
        print("Wrong answer.")

# input: byte strings b1, b2
# output: byte string b1 xor b2
def bytes_xor(b1, b2):
    return bytes([bit1 ^ bit2 for (bit1, bit2) in zip(b1, b2)])

# input: hex stirng h1, h2
# output: h1 xor h2 in bytes
def hex_xor(h1, h2):
    h1_bytes = bytes.fromhex(h1)
    h2_bytes = bytes.fromhex(h2)
    h1_xor_h2 = bytes_xor(h1_bytes, h2_bytes)
    return h1_xor_h2

# input: hex h1, str char1
# output: h1 xor char1 in bytes
def hex_xor_single_letter(h1, char1):
    h1_bytes = bytes.fromhex(h1)
    char1_bytes = bytes(char1, 'utf-8') * len(h1_bytes)
    h1_xor_char1 = bytes_xor(h1_bytes, char1_bytes)
    return h1_xor_char1

# input: none
# output: dict of letter frequency. 'a': 0.
def get_ENfreq_table():
    freq_table = pd.read_csv("freq_table.csv")
    letter = []
    frequency = []
    for i in freq_table['letter']:
        letter.append(i)
    for freq_str in freq_table['frequency']:
        freq_float = float(freq_str.replace('%',''))
        frequency.append(freq_float)
    freq_dict = dict(zip(letter, frequency))
    freq_dict[' '] = 20.0
    return freq_dict

# input: string
# output: scoring in float
def single_letter_scoring(some_str):
    freq_dict = get_ENfreq_table()
    score = 0
    for char in some_str:
        if char.upper() in freq_dict.keys():
            score += freq_dict[char.upper()]
    return score


# print(get_ENfreq_table())
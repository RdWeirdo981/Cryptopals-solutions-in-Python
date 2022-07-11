from math import floor
import pandas as pd
import string

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
    freq_dict[' '] = 10.0
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

# input: a encrypted str by a single char
# output: highest scoring one
def str_xor_char_attack(some_string):
    ascii_str = string.printable
    result_dict = {}
    for letter in ascii_str:
        letter_xor_input = hex_xor_single_letter(some_string, letter).decode('utf-8')
        result_score = single_letter_scoring(letter_xor_input)
        result_dict[(letter_xor_input, letter)] = result_score

    dict_ordered = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)
    return dict_ordered[0]

# input: a key word and a string
# output: an encrypted string
def key_word_encryption(keyword, pt):
    keyword_bytes = bytes(keyword,'utf-8')
    pt_bytes = bytes(pt, 'utf-8')
    len_keyword = len(keyword_bytes)
    len_pt = len(pt_bytes)
    keyword_ext = keyword_bytes * floor(len_pt/len_keyword)
    len_ext = len(keyword_ext)
    if len_ext != len_pt:
        diff = len_pt - len_ext
        keyword_ext = keyword_ext + keyword_bytes[:diff]
    if len(keyword_ext) == len_pt:
        output_bytes = bytes_xor(keyword_ext, pt_bytes)
        return output_bytes.hex()
    else:
        print("Error!")
        return

        
    
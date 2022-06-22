import string
from utils import hex_xor_single_letter, single_letter_scoring

ascii_str = string.ascii_letters
input_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

result_dict = {}

for letter in ascii_str:
    letter_xor_input = hex_xor_single_letter(input_str, letter).decode('utf-8')
    result_score = single_letter_scoring(letter_xor_input)
    result_dict[letter_xor_input] = result_score

dict_ordered = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)
print(dict_ordered[0])
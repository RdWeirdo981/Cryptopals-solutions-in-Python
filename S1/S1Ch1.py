import base64
from utils import is_strs_equal

original_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
raw_str = bytes.fromhex(original_str)
# hex string ==> byte string. automatically decoded when display. 
# 2 hex  ==> 1 bytes. 
# If you check len of original & raw, the len of original is 96 & the latter is 48.

str_to_byte = base64.b64encode(raw_str).decode()
# b64encode: byte str ==> byte str
# decode: byte str ==> general str (without b')

verify_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
is_strs_equal(verify_str, str_to_byte)
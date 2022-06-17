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
# output: hex string (in type str) h1 xor h2
def hex_xor(h1, h2):
    h1_bytes = bytes.fromhex(h1)
    h2_bytes = bytes.fromhex(h2)
    h1_xor_h2 = bytes_xor(h1_bytes, h2_bytes)
    return h1_xor_h2.hex()
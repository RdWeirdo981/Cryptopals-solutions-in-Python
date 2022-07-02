from utils import str_xor_char_attack

f = open('4.txt', 'r')
strings = f.readlines()
f.close()
# print(type(strings))

result_dict = {}

for index in range(len(strings)):
    try:
        str_decrypted = str_xor_char_attack(strings[index])
        result_dict[(index, str_decrypted[0])] = str_decrypted[1]
    except:
        pass

# dict_ordered = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)
# print(dict_ordered[0])
dict_ordered = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)
print(dict_ordered[0])
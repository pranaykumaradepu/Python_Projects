def encode_text(text):
    translation_map = {
        'a': '4', 'A': '4',
        'b': '8', 'B': '8',
        'c': 'G', 'C': 'G',
        'd': 'B', 'D': 'B',
        'e': '3', 'E': '3',
        'f': 'P', 'F': 'P',
        'g': 'C', 'G': 'C',
        'h': 'I', 'H': 'I',
        'i': '1', 'I': '1',
        'j': '2', 'J': '2',
        'k': 'k', 'K': 'K',
        'l': 'l', 'L': 'L',
        'm': 'W', 'M': 'W',
        'n': 'Z', 'N': 'Z',
        'o': '0', 'O': '0',
        'p': '9', 'P': '9',
        'q': 'q', 'Q': 'Q',
        'r': 'r', 'R': 'R',
        's': '5', 'S': '5',
        't': '7', 'T': '7',
        'u': 'n', 'U': 'n',
        'v': 'A', 'V': 'A',
        'w': 'M', 'W': 'M',
        'x': 'x', 'X': 'X',
        'y': 'h', 'Y': 'h',
        'z': 'N', 'Z': 'N'
    }
    return ''.join(translation_map.get(char, char) for char in text)

st = input("Enter your text: ")
encoded_data = encode_text(st)
print()
print(encoded_data)

# -----------------------------------------------------------------------------------------

# st=input("enter your text :")
# data=""
# for i in st:
#     if i=="a" or i=="A":
#         data+='4'
#     elif  i=="b" or i=='B':
#         data+="8"
#     elif  i=="c" or i=='C':
#         data+="G"
#     elif  i=="d" or i=='D':
#         data+="B"
#     elif  i=="e" or i=='E':
#         data+="3"
#     elif  i=="f" or i=='F':
#         data+="P"
#     elif  i=="g" or i=='G':
#         data+="C"
#     elif  i=="h" or i=='H':
#         data+="I"
#     elif  i=="i" or i=='I':
#         data+="1"
#     elif  i=="j" or i=='J':
#         data+="2"
#     elif  i=="k" or i=='K':
#         data+=i
#     elif  i=="l" or i=='L':
#         data+=i
#     elif  i=="m" or i=='M':
#         data+="W"
#     elif  i=="n" or i=='N':
#         data+="Z"
#     elif  i=="o" or i=='O':
#         data+="0"
#     elif  i=="p" or i=='P':
#         data+="9"
#     elif  i=="q" or i=='Q':
#         data+=i
#     elif  i=="r" or i=='R':
#         data+=i
#     elif  i=="s" or i=='S':
#         data+="5"
#     elif  i=="t" or i=='T':
#         data+="7"
#     elif  i=="u" or i=='U':
#         data+="n"
#     elif  i=="v" or i=='V':
#         data+="A"
#     elif  i=="w" or i=='W':
#         data+="M"
#     elif  i=="x" or i=='X':
#         data+=i
#     elif  i=="y" or i=='Y':
#         data+="h"
#     elif  i=="z" or i=='Z':
#         data+="N"
#     else:
#         data+=i
# print()
# print(data)
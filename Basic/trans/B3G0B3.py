def decode_text(text):
    translation_map = {
        '4': 'a', '8': 'b', 'G': 'c', 'B': 'd', '3': 'e',
        'P': 'f', 'C': 'g', 'I': 'h', '1': 'i', '2': 'j',
        'k': 'k', 'l': 'l', 'W': 'm', 'Z': 'n', '0': 'o',
        '9': 'p', 'q': 'q', 'r': 'r', '5': 's', '7': 't',
        'n': 'u', 'A': 'v', 'M': 'w', 'x': 'x', 'h': 'y',
        'N': 'z'
    }
    return ''.join(translation_map.get(char, char) for char in text)

st = input("Enter your text: ")
encoded_data = decode_text(st)
print()
print(decode_text(encoded_data))

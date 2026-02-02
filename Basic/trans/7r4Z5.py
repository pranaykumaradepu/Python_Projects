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
    # The return statement below processes each character of the input text using the translation_map.
    # It replaces each character with its corresponding value in the map and concatenates them into a single string.
    # If a character is not found in the translation_map, it is added to the result unchanged.
    return ''.join(translation_map.get(char, char) for char in text)

st = input("Enter your text: ")
encoded_data = encode_text(st)
print()
print(encoded_data)

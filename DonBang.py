def monoalphabetic_decrypt(ciphertext, key_mapping):
    inverse_mapping = {v: k for k, v in key_mapping.items()}
    plaintext = "".join(inverse_mapping.get(char, char) for char in ciphertext)
    return plaintext

key_mapping = {
    'A': 'X', 'B': 'Y', 'C': 'Z', 'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E',
    'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M',
    'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U',
    'Y': 'V', 'Z': 'W'
}

ciphertext = input("Nhập bản mã Monoalphabetic: ").upper()

plaintext = monoalphabetic_decrypt(ciphertext, key_mapping)
print("Bản rõ:", plaintext)

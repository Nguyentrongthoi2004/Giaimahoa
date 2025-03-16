def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext

key = input("Nhập khóa Vigenère: ").strip()
ciphertext = input("Nhập bản mã Vigenère: ").strip()

plaintext = vigenere_decrypt(ciphertext, key)
print("Bản rõ:", plaintext)

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text += new_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

key = input("Nhập khóa: ").strip()
ciphertext = input("Nhập bản mã: ").strip()

plaintext = vigenere_decrypt(ciphertext, key)
print("Bản rõ:", plaintext)

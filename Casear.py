def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char
    return plaintext


shift = int(input("Nhập khóa Caesar (số bước dịch): "))
ciphertext = input("Nhập bản mã Caesar: ")

plaintext = caesar_decrypt(ciphertext, shift)
print("Bản rõ:", plaintext)

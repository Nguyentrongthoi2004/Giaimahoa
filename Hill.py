import numpy as np

def text_to_matrix(key, size):
    key_numbers = [ord(char) - ord('a') for char in key]
    if len(key_numbers) < size * size:
        raise ValueError("Khóa quá ngắn! Cần ít nhất {} ký tự.".format(size * size))
    key_matrix = np.array(key_numbers[:size * size]).reshape(size, size)
    return key_matrix

def mod_inverse_matrix(matrix, mod=26):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)
    matrix_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % mod
    return matrix_inv

def hill_decrypt(ciphertext, key_matrix):
    ciphertext = [ord(c) - ord('a') for c in ciphertext]
    key_inv = mod_inverse_matrix(key_matrix)

    plaintext = ""
    size = len(key_matrix)

    for i in range(0, len(ciphertext), size):
        block = np.array(ciphertext[i:i+size])
        decrypted_block = np.dot(key_inv, block) % 26
        plaintext += "".join(chr(int(num) + ord('a')) for num in decrypted_block)

    return plaintext

key = input("Nhập khóa Hill: ").strip().lower()
size = int(len(key) ** 0.5)
key_matrix = text_to_matrix(key, size)

print("Ma trận khóa:")
print(key_matrix)

ciphertext = input("Nhập bản mã: ").strip().lower()
plaintext = hill_decrypt(ciphertext, key_matrix)

print("Bản rõ:", plaintext)

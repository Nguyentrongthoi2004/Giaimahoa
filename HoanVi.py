def get_key_order(key):
    return [i for _, i in sorted((char, i) for i, char in enumerate(key))]

def decrypt_transposition(ciphertext, key):
    key_order = get_key_order(key)
    num_cols = len(key)
    num_rows = -(-len(ciphertext) // num_cols)

    col_lengths = {col: len(ciphertext) // num_cols for col in range(num_cols)}
    for i in range(len(ciphertext) % num_cols):
        col_lengths[key_order[i]] += 1

    matrix = [[''] * num_cols for _ in range(num_rows)]

    idx = 0
    for step, col in enumerate(key_order):
        for row in range(num_rows):
            if col_lengths[col] > 0:
                matrix[row][col] = ciphertext[idx]
                idx += 1
                col_lengths[col] -= 1
        print(f"\nBước {step + 1} - Điền cột {col}:")
        for r in matrix:
            print(" ".join(r))

    print("\nBảng sau khi điền:")
    for r in matrix:
        print(" ".join(r))

    inv_order = [0] * num_cols
    for i, col in enumerate(key_order):
        inv_order[col] = i

    final_matrix = [[''] * num_cols for _ in range(num_rows)]

    print("\nQuá trình hoán vị các cột để khôi phục plaintext:")
    for step in range(num_cols):
        source_col = inv_order[step]
        for row in range(num_rows):
            final_matrix[row][step] = matrix[row][source_col]
        print(f"\nBước {step + 1} - Đưa cột {source_col} vào vị trí {step}:")
        for r in final_matrix:
            print(" ".join(cell if cell != '' else '_' for cell in r))

    final_text = "".join("".join(row) for row in final_matrix)
    return final_text

ciphertext = "oohorlttaregdy"
key = "victory"

print(f"\nGiải mã '{ciphertext}' với khóa '{key}':\n")
decrypted_text = decrypt_transposition(ciphertext, key)
print(f"\nVăn bản sau khi giải mã: {decrypted_text}")

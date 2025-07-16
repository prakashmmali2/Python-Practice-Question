# Impliement Hill Cipher Encription Decription 
import numpy as np

def mod_matrix(matrix, mod):
    return np.mod(matrix, mod)

def invert_matrix(matrix, mod):
    det = int(round(np.linalg.det(matrix))) % mod
    det_inv = pow(det, -1, mod)
    matrix_inv = det_inv * np.round(det) * np.linalg.inv(matrix)
    return mod_matrix(matrix_inv, mod)

def hill_cipher(text, key_matrix, mode='encrypt'):
    n = key_matrix.shape[0]
    text = text.upper().replace(' ', '')
    numbers = [ord(char) - ord('A') for char in text]
    
    if mode == 'encrypt':
        padded_length = len(numbers) + (n - len(numbers) % n) % n
        numbers += [0] * (padded_length - len(numbers))
        process = lambda block: mod_matrix(np.dot(key_matrix, block), 26)
    else:  # decrypt
        key_matrix_inv = invert_matrix(key_matrix, 26).astype(int)
        process = lambda block: mod_matrix(np.dot(key_matrix_inv, block), 26)

    result = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i + n])
        result.extend(process(block))
    
    return ''.join(chr(num + ord('A')) for num in result)

# Example usage
if __name__ == "__main__":
    key_matrix = np.array([[17,17,5], 
                           [21,18,21], 
                           [2,2,19]])
    
    plaintext = input("Enter the Plaintext: ")
    ciphertext = hill_cipher(plaintext, key_matrix, mode='encrypt')
    decrypted_text = hill_cipher(ciphertext, key_matrix, mode='decrypt')
    
    print("key Matrix : \n", key_matrix)
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {decrypted_text}")

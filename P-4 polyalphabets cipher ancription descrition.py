def vigenere_encrypt(plain, keyw):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plain = plain.upper().replace(" ", "")
    keyw = (keyw.upper() * (len(plain) // len(keyw))) + keyw.upper()[:len(plain) % len(keyw)]
    return ''.join(alpha[(alpha.index(p) + alpha.index(k)) % 26] for p, k in zip(plain, keyw))

def vigenere_decrypt(ciphert, keyw):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphert = ciphert.upper().replace(" ", "")
    keyw = (keyw.upper() * (len(ciphert) // len(keyw))) + keyw.upper()[:len(ciphert) % len(keyw)]
    return ''.join(alpha[(alpha.index(c) - alpha.index(k) + 26) % 26] for c, k in zip(ciphert, keyw))


message = input("Enter the Plaintext: ")
key = input("Enter the Key : ")

encrypted = vigenere_encrypt(message, key)
print(f"Encrypted: {encrypted}")

decrypted = vigenere_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

def mat(key):
 
    key = key.upper().replace('J', 'I')
    key = ''.join(sorted(set(key), key=key.index))
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix_string = key + ''.join([char for char in alphabet if char not in key])
    
    matrix = [list(matrix_string[i:i + 5]) for i in range(0, 25, 5)]
    return matrix

def pair(pair, matrix):
    row1, col1 = get_position(pair[0], matrix)
    row2, col2 = get_position(pair[1], matrix)
    
    if row1 == row2: 
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]
        
        
 
def get_position(letter, matrix):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == letter:
                return (i, j)

def prepare_message(message):
    message = message.upper().replace(' ', '').replace('J', 'I')
    prepared = []
    
    i = 0
    while i < len(message):
        if i + 1 < len(message):
            if message[i] == message[i + 1]:  # Same letter
                prepared.append(message[i] + 'X')
                i += 1
            else:
                prepared.append(message[i] + message[i + 1])
                i += 2
        else:
            prepared.append(message[i] + 'X')  # Odd length
            i += 1
            
    return prepared
    

def playfair_encrypt(message, key):
    matrix_cv = mat(key)
    message_pairs = prepare_message(message)
    
    encrypted_message = ""
    for pm in message_pairs:
        encrypted_message += pair(pm, matrix_cv)
        
    return encrypted_message
    
key = input("Enter the Key Value : ")
PT = input("Enter PlainText : ")
encrypted_text = playfair_encrypt(PT, key)
print(f"Encrypted Text: {encrypted_text}")


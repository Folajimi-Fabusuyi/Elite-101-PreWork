import random

ALPHABET = 'aefghijFGHIwxDklmJKLMNyzQRSTUbABCnopqrEPOdVWstuvcXYZ'
NUMERIC = '3601279845'
SYMBOLIC = '!+<>,^&*?:@#.$%-_=;'

def encrypt_password(password):
    password_characters = [char for char in password]
    key = str(random.randint(111, 999))
    #each different key is one digit from the overall key generated
    alphabet_key, numeric_key, symbolic_key = int(key[0]), int(key[1]), int(key[2])
    encrypted_password = []

    for char in password_characters:
        #for each charachter, gets new index using key corresponding to charachter's type and key
        if char in ALPHABET:
            alphabet_index = ALPHABET.index(char)
            new_char = alphabet_index + alphabet_key
            
            if new_char + ALPHABET.index(char) > len(ALPHABET) - 1:
                new_char = new_char - len(ALPHABET)
            encrypted_password.append(ALPHABET[new_char])

        elif char in NUMERIC:
            numeric_index = NUMERIC.index(char)
            new_char = numeric_index + numeric_key

            if new_char + NUMERIC.index(char) > len(NUMERIC) - 1:
                new_char = new_char - len(NUMERIC)
            encrypted_password.append(NUMERIC[new_char])
        
        elif char in SYMBOLIC:
            symbolic_index = SYMBOLIC.index(char)
            new_char = symbolic_index + symbolic_key

            if new_char + SYMBOLIC.index(char) > len(SYMBOLIC) - 1:
                new_char = new_char - len(SYMBOLIC)
            encrypted_password.append(SYMBOLIC[new_char])
    #list of password and key is returned for decrypting
    return [''.join(encrypted_password), key]

def decrypt_password(encrypted_password):
    decrypted_password = []
    alphabet_key, numeric_key, symbolic_key = int(encrypted_password[1][0]), int(encrypted_password[1][1]), int(encrypted_password[1][2])
    
    #Reverses the original lists and uses the key of each char to get original position
    for char in encrypted_password[0]:
        if char in ALPHABET:
            alphabet_index = ALPHABET[::-1].index(char)
            new_char = alphabet_index + alphabet_key
            
            if new_char + ALPHABET[::-1].index(char) > len(ALPHABET) - 1:
                new_char = new_char - len(ALPHABET)
            decrypted_password.append(ALPHABET[::-1][new_char])

        elif char in NUMERIC:
            numeric_index = NUMERIC[::-1].index(char)
            new_char = numeric_index + numeric_key

            if new_char + NUMERIC[::-1].index(char) > len(NUMERIC) - 1:
                new_char = new_char - len(NUMERIC)
            decrypted_password.append(NUMERIC[::-1][new_char])
        
        elif char in SYMBOLIC:
            symbolic_index = SYMBOLIC[::-1].index(char)
            new_char = symbolic_index + symbolic_key

            if new_char + SYMBOLIC[::-1].index(char) > len(SYMBOLIC) - 1:
                new_char = new_char - len(SYMBOLIC)
            decrypted_password.append(SYMBOLIC[::-1][new_char])

    return ''.join(decrypted_password)
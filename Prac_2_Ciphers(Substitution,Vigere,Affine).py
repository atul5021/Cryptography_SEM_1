#Substitutio Cipher

def encrypt_word(plain_text, key):
    cipher_text = ""

    for word in plain_text:
        for i in word:
            if i.isupper():
                val = ord(i) - 65
                enc_word = chr(65 + (val + key) % 26)
            else:
                val = ord(i) - 97
                enc_word = chr(97 + (val + key) % 26)

            cipher_text += enc_word

    print('Encrypted Text:', cipher_text)
    return cipher_text

def decrypt_word(cipher_text, key):
    plain_text = ""

    for word in cipher_text:
        for i in word:
            if i.isupper():
                val = ord(i) - 65
                enc_word = chr(65 + (val - key) % 26)
            else:
                val = ord(i) - 97
                enc_word = chr(97 + (val - key) % 26)

            plain_text += enc_word

    print("Decrypted text:", plain_text)

plain_text = input("Enter the plain text to be Encrypted: ").split()
key = int(input("Enter the key for shift cipher: "))

cipher_text = encrypt_word(plain_text, key)
decrypt_word(cipher_text, key)



############################################  END ############################################
#Vigenère Cipher

def vigenere_encrypt(plaintext, key):
    key = key.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.upper() in alphabet:
            shift = alphabet.index(key[key_index])
            if char.isupper():
                new_char = alphabet[(alphabet.index(char) + shift) % 26]
            else:
                new_char = alphabet[(alphabet.index(char.upper()) + shift) % 26].lower()
            ciphertext += new_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.upper() in alphabet:
            shift = alphabet.index(key[key_index])
            if char.isupper():
                new_char = alphabet[(alphabet.index(char) - shift) % 26]
            else:
                new_char = alphabet[(alphabet.index(char.upper()) - shift) % 26].lower()
            plaintext += new_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char

    return plaintext

# Example usage
key = "KEY"
plaintext = "HELLO WORLD"
ciphertext = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")

print("----------------------------------------------------------------------------------------------------------------------")
#Affine Cipher
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def affine_encrypt(plaintext, a, b):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""

    for char in plaintext:
        if char.upper() in alphabet:
            if char.isupper():
                new_char = alphabet[(a * alphabet.index(char) + b) % 26]
            else:
                new_char = alphabet[(a * alphabet.index(char.upper()) + b) % 26].lower()
            ciphertext += new_char
        else:
            ciphertext += char

    return ciphertext

def affine_decrypt(ciphertext, a, b):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    a_inverse = mod_inverse(a, 26)

    for char in ciphertext:
        if char.upper() in alphabet:
            if char.isupper():
                new_char = alphabet[(a_inverse * (alphabet.index(char) - b)) % 26]
            else:
                new_char = alphabet[(a_inverse * (alphabet.index(char.upper()) - b)) % 26].lower()
            plaintext += new_char
        else:
            plaintext += char

    return plaintext

# Example usage
a = 5
b = 8
plaintext = "HELLO WORLD"
ciphertext = affine_encrypt(plaintext, a, b)
decrypted_text = affine_decrypt(ciphertext, a, b)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")

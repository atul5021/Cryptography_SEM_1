# Shift Cipher
def cryptanalysis():
    cipher_test = input('Enter the cipher test for cryptanalysis :')

    for k in range(26):
        plain_text = ''

    for letter in cipher_test:
        if letter =='':
            plain_text+=letter
        else:
            c = ord(letter)-65
            e = (c-k)%26
            plain_text+=chr(e+65)
        print('With key = ',k,plain_text)
cryptanalysis()

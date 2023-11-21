def gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

def generateKeys():
    p = int(input('Enter the value of p (prime): '))
    q = int(input('Enter the value of q (prime): '))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 0
    for i in range(2, phi):
        if gcd(phi, i) == 1:
            e = i
            break
    d = 0
    for i in range(1, phi):
        if (e * i) % phi == 1:
            d = i
            break
    return (e, d, n)

def encryptText(pt, e, n, numflag):
    ct = ''
    if numflag:
        for letter in pt:
            M = ord(letter) - 49
            C = (M ** e) % n
            ct += chr(C + 49)
    else:
        for letter in pt:
            M = ord(letter) - 97
            C = (M ** e) % n
            ct += chr(C + 97)
    print('Encrypted Text : ', ct)
    return ct

def decryptText(ct, d, n, numflag):
    pt = ''
    if numflag:
        for letter in ct:
            C = ord(letter) - 49
            M = (C ** d) % n
            pt += chr(M + 49)
    else:
        for letter in ct:
            C = ord(letter) - 97
            M = (C ** d) % n
            pt += chr(M + 97)
    print('Decrypted Text : ', pt)

e, d, n = generateKeys()
pt = input('Enter the plain text to encrypt : ')
numflag = 1 if pt.isnumeric() else 0
enc = encryptText(pt, e, n, numflag)
decryptText(enc, d, n, numflag)

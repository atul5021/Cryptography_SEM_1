#ELGAMAL CRYPTOSYSTEM


def generate_e2(e1, d, p):
    e2 = (e1 ** d) % p
    return e2

def generate_c1(e1, r, p):
    c1 = (e1 ** r) % p
    return c1

def generate_c2(pt, e2, r, p):
    c2 = (pt * e2 ** r) % p
    return c2

def encryption(e1, d, p, r, pt):
    e2 = generate_e2(e1, d, p)
    c1 = generate_c1(e1, r, p)
    c2 = generate_c2(pt, e2, r, p)
    ct = (c1, c2)
    return ct

def decryption(c1, c2, d, p):
    temp = c1 ** d % p
    temp_inv = None
    for i in range(1, p):
        if (temp * i) % p == 1:
            temp_inv = i
            break
    dpt = (c2 * temp_inv) % p
    return dpt

p = int(input("Enter 1st part of public key: "))
e1 = int(input("Enter 2nd part of public key: "))
d = int(input("Enter a private key: "))
r = int(input("Enter a random integer key: "))
pt = int(input("Enter the plain text: "))

e2 = generate_e2(e1, d, p)
c1 = generate_c1(e1, r, p)
c2 = generate_c2(pt, e2, r, p)

encrypted_text = encryption(e1, d, p, r, pt)
print('Encrypted Text:', encrypted_text)

decrypted_text = decryption(c1, c2, d, p)
print('Decrypted Text:', decrypted_text)

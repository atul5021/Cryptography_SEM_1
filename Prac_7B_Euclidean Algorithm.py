# EUCLIDEAN ALGORITHM

def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
a=int(input('Enter a :'))
b=int(input('Enter b:'))
print('GCD of a and b : ',gcd(a,b))


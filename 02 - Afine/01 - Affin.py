from string import ascii_lowercase
from math import gcd

myAlphabet = ascii_lowercase

def  AffineEncode(plainText, a, b):
    if gcd(a, len(myAlphabet)) != 1:
        raise ValueError('a i {} nemaju zajednickih cinilaca. Ponovo'.format(len(myAlphabet)))
    text = (''.join(x for x in plainText if x.isalnum())).lower()
    # print(text)
    out = ''
    # count = 1

    for char in text:
        if char.isalpha():
            y = myAlphabet[((a * myAlphabet.index(char) + b) % len(myAlphabet))]
            out += y
        else:
            out += char

    return out

def AffineDecode(cipherText, a, b):
    if gcd(a, len(myAlphabet)) != 1:
        raise ValueError('a i {} nemaju zajednickih cinilaca. Ponovo'.format(len(myAlphabet)))
    
    msg = (''.join(x for x in cipherText if x.isalnum())).lower()

    # Potrebno je naci multiplikativni invez broja 'a' za a*a^(-1) = n*len(myAlphabet)+1
    n = 1
    mpkInverz = 1

    while True:
        if a * mpkInverz > len(myAlphabet)*n:
            if a*mpkInverz == len(myAlphabet)*n+1:
                break
            n += 1
        mpkInverz += 1

    if(a==1 and mpkInverz > 1):
        mpkInverz = mpkInverz % len(myAlphabet)

    out = ''


    for char in msg:
        if char.isalpha():
            d = myAlphabet[mpkInverz * (myAlphabet.find(char) - b) % len(myAlphabet)]
            out += d
        else:
            out += char

    return out

inputText = input('Unesite tekst za sifriranje: ')

keyA = int(input('Unesite vrednost a za kljuc K(a, b)'))
while gcd(keyA, len(myAlphabet)) != 1:
    keyA = int(input('a i {} nisu uzajamno prosti, pokusajte ponovo: '.format(len(myAlphabet))))
keyB = int(input('Unesite vrednost b za kljuc K(a, b)'))

encodeText = AffineEncode(inputText, keyA, keyB)
print(encodeText)

decodedText = AffineDecode(encodeText, keyA, keyB)
print(decodedText)
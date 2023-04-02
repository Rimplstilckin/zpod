# Generisemo kljuc na osnovu duzine unetog teksta
import string

myAlphabet = string.printable
myAlphabetLength = len(myAlphabet)

def genKey(message, keyWord):
    key = list(keyWord)
    if (len(message) <= len(keyWord)):
        return key
    else:
        for i in range(len(message) - len(keyWord)):
            key.append(key[i % len(keyWord)])
        return key
    
#Funkcija za sifriranje
def vigenereCipher(message, keyWord):
    cipherText = ''
    keyWordLength = len(keyWord)
    for i in range(keyWordLength):
        y = (myAlphabet.index(message[i]) + myAlphabet.index(keyWord[i])) % myAlphabetLength
        cipherText += myAlphabet[y]
    for i in range(keyWordLength, len(message)):
        y = (myAlphabet.index(message[i])) + myAlphabet.index(message[i-keyWordLength]) % myAlphabetLength
        cipherText += myAlphabet[y]
    return cipherText

#Funkcija za desifrovanje
def vigenereDecipher(cipherMessage, keyWord):
    decipherText = ''
    keyWordLength = len(keyWord)
    for i in range(keyWordLength):
        x = (myAlphabet.index(cipherMessage[i]) - myAlphabet.index(keyWord[i])) % myAlphabetLength
        decipherText += myAlphabet[x]
    for i in range(keyWordLength, len(cipherMessage)):
        x = (myAlphabet.index(cipherMessage[i])) - myAlphabet.index(cipherMessage[i-keyWordLength]) % myAlphabetLength
        decipherText += myAlphabet[x]
    return decipherText

def main():
    message = input('Unesite poruku: ')
    key = input('Unesite klucnu rec: ')

    cipheredText = vigenereCipher(message, key)
    print('Sifrat za uneti tekst:\n', message, '\nje:\n', cipheredText)

    decipheredText = vigenereDecipher(cipheredText, key)
    print('za sifrat: \n', cipheredText, '\nporuka je:\n', decipheredText)

if __name__ == "__main__" :
    main()
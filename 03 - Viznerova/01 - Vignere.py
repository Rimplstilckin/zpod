# Generisemo kljuc na osnovu duzine unetog teksta

def genKey(message, keyWord):
    key = list(keyWord)
    if (len(message) <= len(keyWord)):
        return key
    else:
        for i in range(len(message) - len(keyWord)):
            key.append(key[i % len(keyWord)])
        return key
    
#Funkcija za sifriranje
def vigenereCipher(message, key):
    cipherText = ''
    for i in range(len(message)):
        x = (ord(message[i]) - ord('a') + ord(key[i]) - ord('a')) % 26
        cipherText += chr(x + ord('a'))
    return cipherText

#Funkcija za desifrovanje
def vigenereDecipher(cipherMessage, key):
    decipherText = ''
    for i in range(len(cipherMessage)):
        x = (ord(cipherMessage[i]) - ord(key[i])) % 26
        decipherText += chr(x + ord('a'))
    return decipherText

message = input('Unesite poruku: ')
keyWord = input('Unesite klucnu rec: ')
key = genKey(message, keyWord)

cipheredText = vigenereCipher(message, key)
print('Sifrat za uneti tekst:\n', message, '\nje:\n', cipheredText)

decipheredText = vigenereDecipher(cipheredText, key)
print('za sifrat: \n', cipheredText, '\nporuka je:\n', decipheredText)
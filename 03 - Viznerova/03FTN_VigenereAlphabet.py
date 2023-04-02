# Primer analogan primeru 1, samo što koristimo alfabet 
# koji sadrži sve printabilne karaktere # i ne kreiramo 
# posebno ključ na osnovu ključne reči, 
# jer u slučaju veoma dugih poruka nema smisla kreirati 
# ključ iste dužine kao što je poruka, 
# već se šifriranje može uraditi efikasno i bez toga

import string

myAlphabet = string.printable
LengthMyAlphabet = len(myAlphabet)


# Funkcija za šifrovanje
def VigenereCiphier(message, keyWord):
    cipherText = ''
    keyWordLength = len(keyWord)
    for i in range(len(message)):
        y = (myAlphabet.index(message[i]) + myAlphabet.index(keyWord[i % keyWordLength])) % LengthMyAlphabet
        cipherText += myAlphabet[y]
    return cipherText

# Funkcija za dešifrovanje
def VigenereDeciphier(cipheredText, keyWord):
    decipherText = ''
    keyWordLength = len(keyWord)
    for i in range(len(cipheredText)):
        x = (myAlphabet.index(cipheredText[i]) - myAlphabet.index(keyWord[i % keyWordLength])) % LengthMyAlphabet
        decipherText += myAlphabet[x]
    return decipherText


def main():
    message = input('Unesite poruku: ')        
    key = input('Unesite ključnu reč: ')

    cipheredText = VigenereCiphier(message, key)
    print('Šifrat za uneti tekst\n', message, '\nje:\n ', cipheredText)

    decipheredText = VigenereDeciphier(cipheredText, key)
    print('Dešifrovan tekst za dati šifrat\n', cipheredText, '\nje:\n ', decipheredText)

if __name__ == "__main__":
    main()
import string

#myAlphabet = string.printable
myAlphabet = string.printable + "ŽžŠšĐđĆćČč"

def Encrypt(open_text, key):
    ciphered_text = ''
    for char in open_text:
        if (char in myAlphabet):
            ciphered_text += myAlphabet[(myAlphabet.find(char) + key) % len(myAlphabet)]
        else:
            ciphered_text += char

    # print("Šifrat je: \t\t", ciphered_text)
    return ciphered_text

def Decrypt(ciphered_text, key):
    deciphered_text = ''
    for char in ciphered_text:
        if (char in myAlphabet):
            deciphered_text += myAlphabet[(myAlphabet.find(char) - key) % len(myAlphabet)]
        else:
            deciphered_text += char

    # print("Dešifrovan tekst je: \t", deciphered_text)
    return deciphered_text


text = input("Unesite tekst za šifrovanje: ")
k = int(input("Unesite ključ (0-25): "))

ciphered_text = Encrypt(text, k)
print("Šifrat je: \t\t", ciphered_text)
deciphered_text = Decrypt(ciphered_text, k)
print("Dešifrovan tekst je: \t", deciphered_text)
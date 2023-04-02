
def Encrypt(open_text, key):
    ciphered_text = ''
    for char in open_text:
        if (char.isupper()):
            ciphered_text += chr((ord(char) - 65 + key) % 26 + 65)
        elif (char.islower()):
            ciphered_text += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            ciphered_text += char

    # print("Šifrat je: \t\t", ciphered_text)
    return ciphered_text

text = input("Unesite tekst za šifrovanje: ")
k = int(input("Unesite ključ (0-25): "))

ciphered_text = Encrypt(text, k)
print("Šifrat je: \t\t", ciphered_text)
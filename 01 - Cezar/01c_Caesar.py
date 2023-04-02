text = input("Unesite tekst za šifrovanje: ")
# k = 3
k = int(input("Unesite ključ (0-25): "))

ciphered_text = ''

for char in text:
    if (char.isupper()):
        ciphered_text += chr((ord(char) - 65 + k) % 26 + 65)
    elif (char.islower()):
        ciphered_text += chr((ord(char) - 97 + k) % 26 + 97)
    else:
        ciphered_text += char

print("Šifrat je: \t\t", ciphered_text)

deciphered_text = ''
for i in range(len(ciphered_text)):
    char = ciphered_text[i]
    if (char.isupper()):
        deciphered_text += chr((ord(char) - 65 - k) % 26 + 65)
    elif (char.islower()):
        deciphered_text += chr((ord(char) - 97 - k) % 26 + 97)
    else:
        deciphered_text += char


print("Dešifrovan tekst je: \t", deciphered_text)
text = input("Unesite tekst za šifrovanje: ")
# unos teksta za šifrovanje od strane korisnika
k = 3
# ključ, za originalnu Cezarovu šifru je 3

ciphered_text = ''
# prazan string u koji će se upisivati šifrat

for char in text:   # može ovako ili for i in range(len(text))
    if (char.isupper()):
        ciphered_text += chr((ord(char) - 65 + k) % 26 + 65)
    elif (char.islower()):
        ciphered_text += chr((ord(char) - 97 + k) % 26 + 97)
    else:
        ciphered_text += char

print("Šifrat je: \t\t", ciphered_text)

deciphered_text = ''
for i in range(len(ciphered_text)):
    char = ciphered_text[i] # ova i prethodna linija mogu da se zamene linijom 9
    if (char.isupper()):
        deciphered_text += chr((ord(char) - 65 - k) % 26 + 65)
    elif (char.islower()):
        deciphered_text += chr((ord(char) - 97 - k) % 26 + 97)
    else:
        deciphered_text += char


print("Dešifrovan tekst je: \t", deciphered_text)

# koja od sledeće 2 petlje je "efikasnija"?
# Mogu se obe ponoviti ogroman broj puta i izmeriti vreme izvršavanja,
# kao u primeru test_performance.py, mada u realnosti na performanse
# utiču i drugi faktori (keširanje, SMP, itd.)

# chars = ['A','B','a','b','c']

# for i in range (len(chars)):
#     print("char ", chars[i], "is ascii ", ord(chars[i]))

# for char in chars:
#     print("char ", char, "is ascii ", ord(char))
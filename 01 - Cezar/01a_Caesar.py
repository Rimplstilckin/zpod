text = input("UNESITE TEKST ZA ŠIFROVANJE: ")   # Unos teksta
k = int(input("Unesite ključ (0-25): "))        # Unos ključa

result = ""
# Prođemo sve karaktere u otvorenom tekstu
for i in range(len(text)):  # Može i direktno: for i in text...
    char = text[i]          # ... a potom: svugde umesto char koristiti 'i'
    # Šifriramo velika slova (slovo A = 65 u ASCII kodu)
    if (char.isupper()):
        result += chr((ord(char) + k - 65) % 26 + 65)
    # Šifriramo mala slova (slova A = 97 u ASCII kodu)
    else:
        result += chr((ord(char) + k - 97) % 26 + 97)

# Štampamo otvoreni tekst
print ("Otvoreni tekst je: ", text)
# Štampamo ključ
print ("Ključ tekst je: ", str(k))
# Štampamo šifrovan tekst
print ("Šifrat je: ", result)
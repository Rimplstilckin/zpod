cipher_text = "-v8sv1zQ1GIvuDvKr1;raKzKr1GFurKrBr{1BFAv1JL1GFDvIvEv1Qr1gvKMIKrB1L1in hh1JrKz{1FuI8rMrAL1Jv1L1AvuEFA1xILGz<"

import string

# Pretpostavimo da su za alfabet korišćeni svi printabilni ASCII karakteri.
tryAlphabet = string.printable

# Dešifrujemo poruku za sve moguće ključeve (1-25),
# tako što petlju u sledećem kodu stavimo unutar petlje
# u kojoj "key" uzima vrednosti od 1 do 25,
# pa ako dobijemo delimično čitljivu poruku, možemo proceniti 
# koji ključ je korišćen za šifrovanje, nakon čega na osnovu
# tako dešifrovanog teksta možemo pokušati da pogodimo tačan alfabet.
# Za konkretan primer znamo da je korišćen ključ 17, 
# jer je dobijen iz 04_Caesar_Alphabet2.py

key = 17
deciphered_text = ''
for char in cipher_text:
    if char in tryAlphabet:
        position = tryAlphabet.find(char)
        new_position = position - key
        if new_position < 0:
            new_position += len(tryAlphabet)
        deciphered_text += tryAlphabet[new_position]
    else:
        deciphered_text += ' '
print("Ključ: ", key, "\nOtvoren tekst:\n", deciphered_text)

# Izlaz:
'''
Ključ:  17 
Otvoren tekst:
 Ve|be[iz[predmeta[Za~tita[podataka,[koje[su[pomerene[za[♀etvrtak[u[16:00[sati,[odr|avaju[se[u[jednoj[grupi!
'''

# Iz delimično dešifrovanog teksta ne možemo sa sigurnošću zaključiti
# koji alfabet je korišćen, jer i ako znamo dodatne Unicode karaktere
# pored očiglednih ASCII karaktera, potrebno je više pokušaja da odredimo 
# njihov redosled u alfabetu. Ali, i na osnovu delimično dešifrovane poruke
# možemo videti da se pominje četvrtak u 16:00 sati.
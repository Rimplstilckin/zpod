message = 'PWNUYTLWFKNOF'               # šifrovan tekst
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # alfabet

# Za svaki broj od 0 do broja slova u alfabetu 
# (npr. od 0 do 26 za engleski alfabet)
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Hacking key #%s: %s' % (key, translated))
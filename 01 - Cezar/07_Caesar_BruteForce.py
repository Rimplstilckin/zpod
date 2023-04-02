sifrat = 'CDVWLWDqSRGDWDND'      # šifrovana poruka
abc26 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # ABCDEF

for kljuc in range(len(abc26)):
   poruka = ''
   for slovo in sifrat:
      if slovo in abc26:
         poz = abc26.find(slovo)
         # poz = (poz - kljuc) % len(abc26)
         poz = poz - kljuc
         if poz < 0:
            poz = poz+len(abc26)
         poruka += abc26[poz]
      else:
         poruka += ' '  # chr(ord(" "))
   print('Kljuc: ', kljuc, 'Otvoren tekst:', poruka)
import re as r
haslo = input('Proszę wprowadzić hasło: ')
mala_litera = bool(r.search('.[a-z]',haslo))
duza_litera = bool(r.search('.[:upper:]',haslo))
cyfra = bool(r.search('.[0-9]',haslo))
znak_specjalny = bool(r.search('.[$#@]',haslo))
dlugosc = len(haslo)>=6 and len(haslo)<=16

if mala_litera and duza_litera and cyfra and znak_specjalny and dlugosc:
    print('Podane hasło spełnia wymagania')
else:
    print('Podane hasło nie spełnia wymagań')
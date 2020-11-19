from szyfr_cezara import *
n = int(input("Proszę wprowadzić klucz szyfru: "))
tekst = input("Proszę wprowadzić tekst do zaszyfrowania: ")

print(szyfruj(tekst,n))
print(deszyfr(szyfruj(tekst,n),n))
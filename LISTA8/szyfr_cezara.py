import string
lista = string.ascii_uppercase
lista2 = string.ascii_lowercase

def szyfruj(tekst, kod):
    szyfr = ""

    for i in tekst:
        if str(i).upper() not in lista:
            szyfr = szyfr + i
        else:
            if str(i).isupper():
                n = kod + ord(i)
                if n > 90: n -= 26
                szyfr = szyfr + chr(n)
            else:
                n = kod + ord(str(i).upper())
                if n > 90: n -= 26
                szyfr = szyfr + str(chr(n)).lower()

    return szyfr

def deszyfr(tekst, kod):
    deszyfr = ""

    for i in tekst:
        if str(i).upper() not in lista:
            deszyfr = deszyfr + i
        else:
            if str(i).isupper():
                n = ord(i) - kod
                if n < 65: n += 26
                deszyfr = deszyfr + chr(n)
            else:
                n = ord(str(i).upper()) - kod
                if n < 65: n += 26
                deszyfr = deszyfr + str(chr(n)).lower()

    return deszyfr
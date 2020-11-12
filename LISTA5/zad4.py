def crypt(x):
    tekst = ''
    klucz = {"a": "y", "e": "i", "i": "o", "o": "a","y": "e"}
    for i in x:
        if i in klucz: tekst += klucz[i]
        else: tekst += i
    return tekst

def decrypt(x):
    tekst = ''
    klucz = {"y": "a", "i": "e", "o": "i", "a": "o", "e": "y"}
    for i in x:
        if i in klucz: tekst += klucz[i]
        else: tekst += i
    return tekst

print(crypt('siema ziomek'))
print(decrypt(crypt('siema ziomek')))
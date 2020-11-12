
def zamien(x):
    x = x.replace(' ','')
    jednosci = {'jeden':1,'dwa':2,'trzy':3,'cztery':4,'pięć':5, 'sześć':6, 'siedem':7, 'osiem':8, 'dziewięć':9}
    nascie = {'dziesięć':10,'jedenaście':11, 'dwanaście':12, 'trzynaćie':13, 'czternaście':14, 'piętnaście':15, 'szesnaście':16, 'siedemnaście':17, 'osiemnaście':18, 'dziewiętnaście':19, 'dwadzieścia':20}
    reszta = {'dwadzieścia':2, 'trzydzieści':3, 'czterdzieści':4, 'pięćdziesiąt':5}

    if x in jednosci: return jednosci[x]
    elif x in nascie: return nascie[x]
    else:
        temp = ''
        i = 0
        liczba = ''
        while temp not in reszta:
            temp += x[i]
            i += 1
        x = x[i:]
        liczba = str(reszta[temp]) + str(jednosci[x])
        return liczba

print(zamien('pięćdziesiąt dziewięć'))
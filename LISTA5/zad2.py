
def zamien(x):
    jednosci = {1:'jeden' , 2:'dwa', 3:'trzy', 4:'cztery', 5:'pięć', 6:'sześć', 7:'siedem', 8:'osiem',
                9:'dziewięć'}
    nascie = {10:'dziesięć', 11:'jedenaście', 12:'dwanaście', 13:'trzynaćie', 14:'czternaście', 15:'piętnaście',
              16:'szesnaście', 17:'siedemnaście', 18:'osiemnaście', 19:'dziewiętnaście', 20:'dwadzieścia'}
    dziesiatki = {2:'dwadzieścia', 3:'trzydzieści', 4:'czterdzieści', 5:'pięćdziesiąt', 6:'sześćdziesiąt',
                  7:'siedemdziesiąt', 8:'osiemdziesiąt', 9:'dziewięćdziesiąt'}
    setki = {1:'sto', 2:'dwieście', 3:'trzysta', 4:'czterysta', 5:'pięćset', 6:'sześćset', 7:'siedemset',
             8:'osiemset', 9:'dziewięćset'}

    liczba = ''
    if len(str(x)) == 4:
        if str(x)[1:] == '000':
            return 'tysiąc'
        liczba += 'tysiąc'
        if str(x)[2:] == '00':
            return liczba + setki[int(str(x)[1])]
        else:
            if str(x)[-1]=='0':
                return liczba + ' ' + setki[int(str(x)[1])] + ' ' + dziesiatki[int(str(x)[2])]
            else:
                return liczba + ' ' + setki[int(str(x)[1])] + ' ' + dziesiatki[int(str(x)[2])] + ' ' + jednosci[int(str(x)[3])]
    elif len(str(x)) == 3:
        if str(x)[1:] == '00':
            return liczba + setki[int(str(x)[1])]
        else:
            if str(x)[-1] == '0':
                return setki[int(str(x)[0])] + ' ' + dziesiatki[int(str(x)[1])]
            else:
                return setki[int(str(x)[0])] + ' ' + dziesiatki[int(str(x)[1])] + ' ' + jednosci[int(str(x)[2])]
    elif len(str(x)) == 2:
        if x in nascie: return nascie[x]
        if str(x)[-1] == '0':
            return dziesiatki[int(str(x)[0])]
        else:
            return dziesiatki[int(str(x)[0])] + ' ' + jednosci[int(str(x)[1])]
    else:
        return jednosci[x]

print(zamien(1458))
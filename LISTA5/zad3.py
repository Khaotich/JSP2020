def na_dziesietny(x):
    system = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    liczba = 0
    x = str(x).upper()
    for i in x:
        liczba+= system[i]
    return liczba

print(na_dziesietny('MMMDCCCLXXXVIII'))
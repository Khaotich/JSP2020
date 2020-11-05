def converter(wartosc, typ):
    import math as m
    if typ == 'deg': return m.radians(wartosc)
    elif typ == 'rad': return m.degrees(wartosc)
    else: return 'Podaną złe dane'

deg = int(input('Proszę wprowadzić wartość do konwersji: '))
typ = input('Proszę wprowadzić typ danych wyjściowych (deg/rad): ')

print(converter(deg,typ))
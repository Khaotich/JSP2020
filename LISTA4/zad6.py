def converter(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v

r = int(input('Proszę wprowadzić wartość r z zakresu (0,255): '))
g = int(input('Proszę wprowadzić wartość g z zakresu (0,255): '))
b = int(input('Proszę wprowadzić wartość b z zakresu (0,255): '))

print('HSV: ',converter(r,g,b))
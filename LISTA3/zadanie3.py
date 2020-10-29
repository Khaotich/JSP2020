from math import sqrt

a = float(input('Proszę wprowadzić współczynik a: '))
b = float(input('Proszę wprowadzić współczynik b: '))
c = float(input('Proszę wprowadzić współczynik c: '))

if a!=0:
    delta = b**2-(4*a*c)
    if delta>0:
        x1 = (-1*b-sqrt(delta))/(2*a)
        x2 = (-1*b+sqrt(delta))/(2*a)
        print("x1 =",x1)
        print("x2 =",x2)
    elif delta==0:
        x = (-1*b)/(2*a)
        print('x =',x)
    else:
        print('Podana funkcja kwadratowa nie posiada pierwaistków')
else:
    print('Podana funkcja nie jest funkcją kwadratową')
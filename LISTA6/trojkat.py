import math as m
def obwod(x,y,z):
    return x+y+z

def pole(x,y,z):
    p = obwod(x,y,z) / 2
    pole = round(m.sqrt(p * (p - x) * (p - y) * (p - z)), 4)
    return pole

def rodzaj_boki(x,y,z):
    if x == y == z: return "równoboczny"
    elif x==y or y==z or x==z: return "równoramieny"
    else: return "różnoboczny"

def rodzaj_katy(x,y,z):
    X = int(m.degrees(m.acos((z ** 2 + y ** 2 - x ** 2) / (2 * y * z))))
    Y = int(m.degrees(m.acos((z ** 2 + x ** 2 - y ** 2) / (2 * x * z))))
    Z = int(m.degrees(m.acos((x ** 2 + y ** 2 - z ** 2) / (2 * x * y))))

    if x == 90 or y == 90 or z == 90: return "prostokątny"
    elif x > 90 or y > 90 or z > 90: return "rozwartokątny"
    elif x < 90 and y < 90 and z < 90: return "ostrokątny"

def main(x,y,z):
    if x + y > z and x + z > y and y + z > x:
        print("Obwód trójkąta wynosi", obwod(x,y,z))
        print("Pole trójkąta wynosi", pole(x,y,z))
        print("Rodzaj trójkąta ze względu na boki to", rodzaj_boki(x,y,z))
        print("Rodzaj trójkąta ze względu na kąty to", rodzaj_katy(x,y,z))
    else:
        print("Z podanych boków nie da się złożyć trójkąta.")
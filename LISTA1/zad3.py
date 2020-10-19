import math as m
a = float(input("Podaj długość pierwszrgo boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
alfa = int(input("Podaj kąt między bokami: "))
alfa_radiany = m.radians(alfa)
pole = 0.5*a*b*m.sin(alfa_radiany)

print("Pole trójkąta wynosi:", pole)
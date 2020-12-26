from math import pi

class Kolo:
    def __init__(self, r):
        self.r = r

    def pole(self):
        print(pi*(self.r*self.r))

    def obwod(self):
        print(2*(pi*self.r))

kolo = Kolo(5)

kolo.pole()
kolo.obwod()
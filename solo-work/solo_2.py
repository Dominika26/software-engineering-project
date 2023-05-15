import math

class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a

    def obwod(self):
        return self.a + self.b + self.c

    def pole(self):
        return (self.a * self.h_a)/2

class Kolo:
    def __init__(self, r):
        self.promien = r

    def pole(self):
        return math.pi * pow(self.promien, 2)

    def obwod(self):
        return 2 * math.pi * self.promien

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)

# print(trojkat_rownoboczny.a)
print(trojkat_rownoboczny.obwod())
print(trojkat_rownoboczny.pole())

trojkat_Dominiki = Trojkat(8,6,10,4)

kolo_Dominiki = Kolo(4)
print(kolo_Dominiki.pole())
print(kolo_Dominiki.obwod())

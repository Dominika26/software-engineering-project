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

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)

# print(trojkat_rownoboczny.a)
print(trojkat_rownoboczny.obwod())
print(trojkat_rownoboczny.pole())

trojkat_Dominiki = Trojkat(8,6,10,4)



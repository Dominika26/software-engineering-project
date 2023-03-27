import math

# kwadrat

a = 10

obwod = a * 4
pole = pow(a, 2)

tekst = "Obwód kwadratu wynosi {}, a pole {}.".format(obwod, pole)
print(tekst)

# prostokat
a_p = 10
b_p = 5
obwod_prostokat = 2 * a_p + 2 * b_p
pole_prostokat = a_p * b_p
tekst_prostokat = "Obwód prostokąta wynosi {}, a pole {}.".format(obwod_prostokat, pole_prostokat)
print(tekst_prostokat)

# kolo
r = 5
obwod_kolo = math.pi * 2 * r
pole_kolo = math.pi * pow(r, 2)
tekst_kolo = "Obwód koła wynosi {}, a pole {}.".format(obwod_kolo, pole_kolo)
print(tekst_kolo)
# trapez
podst_1 = 28
podst_2 = 3
bok_1 = 20
bok_2 = 15
h = 12
obwod_trapez = podst_1 + podst_2 + bok_1 + bok_2
pole_trapez = ((podst_1+podst_2)*h)/2
tekst_trapez = "Obwód trapezu wynosi {}, a pole {}.".format(obwod_trapez, pole_trapez)
print(tekst_trapez)
# romb
a_romb = 7
h_romb = 10
pole_romb = a_romb * h_romb
obwod_romb = 4 * a_romb
tekst_romb = "Obwód rombu wynosi {}, a pole {}.".format(obwod_romb, pole_romb)
print(tekst_romb)





import math
# kwadrat

a = 10

obwod = a * 4
pole = pow(a, 2)

tekst = "Obwód kwadratu wynosi {}, a pole {}.".format(obwod, pole)
print(tekst)

#prostokat
a_p = 10
b_p = 5
obwod_prostokat = 2*a_p+2*b_p
pole_prostokat = a_p*b_p
tekst_prostokat = "Obwód prostokąta wynosi {}, a pole {}.".format(obwod_prostokat, pole_prostokat)
print(tekst_prostokat)

#kolo
r = 5
obwod_kolo = math.pi *2*r
pole_kolo = math.pi * pow(r, 2)
tekst_kolo = "Obwód koła wynosi {}, a pole {}.".format(obwod_kolo, pole_kolo)
print(tekst_kolo)
#trapez

#romb
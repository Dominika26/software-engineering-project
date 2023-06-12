import csv


class Pracownik():
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
        self.wynagrodzenie_netto = 0
        self.calkowity_koszt = 0
        self.skladki_na_zus = 0
        self.dochod = 0
        self.zaliczka_na_pit = 0
        self.skladka_zdrowotna = 0
        self.skladka_emerytalna = 0
        self.skladka_rentowa = 0
        self.skladka_wypadkowa = 0
        self.skladka_fp = 0
        self.skladka_fgsp = 0
        self.sklaska_ppk = 0

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def oblicz_wynagrodzenie_netto(self):
        # https: // ksiegowosc - budzetowa.infor.pl / kadry - i - place / wynagrodzenia / 5533738, Wzor - obliczania - pensji - netto - z - brutto - przyklad - kroki - algorytm - kalkulator - brutto - netto.html
        self.skladki_na_zus = self.wynagrodzenie_brutto * 0.1371
        self.skladka_zdrowotna = (self.wynagrodzenie_brutto - self.skladki_na_zus) * 0.09
        self.dochod = (self.wynagrodzenie_brutto - self.skladki_na_zus - 250)
        self.zaliczka_na_pit = round(self.dochod * 0.12 - 300, 2)

        self.wynagrodzenie_netto = (
                self.wynagrodzenie_brutto - self.skladki_na_zus - self.skladka_zdrowotna - self.zaliczka_na_pit)

        return self.wynagrodzenie_netto

    def oblicz_calkowity_koszt(self):
        # https: // poradnikprzedsiebiorcy.pl / -czy - wiesz - ile - wynosi - calkowity - koszt - zatrudnienia - pracownika
        self.skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976
        self.skladka_rentowa = self.wynagrodzenie_brutto * 0.065
        self.skladka_wypadkowa = self.wynagrodzenie_brutto * 0.0167
        self.skladka_fp = self.wynagrodzenie_brutto * 0.0245
        self.skladka_fgsp = self.wynagrodzenie_brutto * 0.001
        self.skladka_ppk = self.wynagrodzenie_brutto * 0.015

        self.calkowity_koszt = self.wynagrodzenie_brutto + self.skladka_emerytalna + self.skladka_rentowa + self.skladka_wypadkowa + self.skladka_fp + self.skladka_fgsp + self.skladka_ppk

        return self.calkowity_koszt


def oblicz_koszt_pracownikow(list):
    koszt_calkowity_pracownikow = 0
    for element in pracownicy:
        pracownik = Pracownik(element[0], element[1], element[2])
        koszt_calkowity_pracownikow = koszt_calkowity_pracownikow + pracownik.oblicz_calkowity_koszt()

    return koszt_calkowity_pracownikow


file = open("pracownicy.csv", "r")
pracownicy = list(csv.reader(file, delimiter=","))[1:]
file.close()

for i, pracownik in enumerate(pracownicy):
    pracownicy[i][2] = int(pracownik[2])

print(f"Całkowity koszt wszystkich pracowników wynosi: {round(oblicz_koszt_pracownikow(pracownicy), 2)}")

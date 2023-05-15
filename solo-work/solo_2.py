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
        return (self.a * self.h_a) / 2


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

trojkat_Dominiki = Trojkat(8, 6, 10, 4)

kolo_Dominiki = Kolo(4)
print(kolo_Dominiki.pole())
print(kolo_Dominiki.obwod())

print("----------------------")
class Student():
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []
    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.numer_indeksu}"

    def __int__(self):
        return 0

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny)/len(self.oceny)

student = Student("Dominika", "Smoczyńska", "555555")
student.dodaj_ocene(5)
student.dodaj_ocene(4.5)
print(student)
print(int(student))

print(student.zwroc_srednia())
print(student.oceny)

class Szkola():
    def __init__(self, nazwa, patron, adres):
        self.nazwa = nazwa
        self.patron = patron
        self.adres = adres
        self.sale = []
        self.nauczyciele = []
        self.klasy = []
        self.klasy_nauczyciele = {}
        self.nauczyciel_wynagrodzenie = {}

    def __str__(self):
        return f"{self.nazwa} --- patron: {self.patron} --- adres: {self.adres}"

    def dodaj_klase(self, klasa):
        if klasa not in self.klasy:
            self.klasy.append(klasa)
        else:
            print("Taka klasa już istnieje!")

    def dodaj_nauczyciela(self, nauczyciel):
        if nauczyciel not in self.nauczyciele:
            self.nauczyciele.append(nauczyciel)
        else:
            print("Taki nauczyciel już istnieje!")

    def przypisz_wychowawce_do_klasy(self, nauczyciel, klasa):
        if nauczyciel not in self.klasy_nauczyciele.values():
            self.klasy_nauczyciele[klasa] = nauczyciel
        else:
            print(f"Nauczyciel {nauczyciel} jest już wychowawcą!")


    def wypisz_klasy(self):
        print("Klasy w szkole: ")
        for klasa, nauczyciel in self.klasy_nauczyciele.items():
            print(f"Klasa: {klasa} - wychowawca: {nauczyciel}")

    def dodaj_wynagrodzenie_nauczyciela(self, nauczyciel, wynagrodzenie):
        if nauczyciel in self.nauczyciele:
            self.nauczyciel_wynagrodzenie[nauczyciel] = wynagrodzenie

    def srednie_wynagrodzenie_nauczycieli(self):
        suma = 0
        for value in self.nauczyciel_wynagrodzenie.values():
            suma = suma + value
        return suma / len(self.nauczyciel_wynagrodzenie)

szkola = Szkola("Szkoła Podstawowa nr 61", "Bohaterzy Westerplatte", "ul. Krucza 5, Bydgoszcz")
print(szkola)
szkola.dodaj_klase("1a")
szkola.dodaj_klase("2b")
szkola.dodaj_nauczyciela("Maciej Bąk")
szkola.dodaj_nauczyciela("Irena Kolano")
szkola.dodaj_wynagrodzenie_nauczyciela("Maciej Bąk", 5000)
szkola.dodaj_wynagrodzenie_nauczyciela("Irena Kolano", 6000)
print(f"Średnie wynagrodzenie nauczycieli wynosi: {szkola.srednie_wynagrodzenie_nauczycieli()}")
szkola.przypisz_wychowawce_do_klasy("Maciej Bąk", "1a")
szkola.przypisz_wychowawce_do_klasy("Irena Kolano", "2b")
szkola.przypisz_wychowawce_do_klasy("Maciej Bąk", "2b")

szkola.wypisz_klasy()



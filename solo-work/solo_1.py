# zadanie 1.1

hello = "Hello"
student = "Ola"

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("{} {}".format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imie")
print("Hello Ola")
print("{} {}".format(hello, student))

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

# policz liczbe studentow w tablicy studenci
# oczekiwany rezultat: Liczba studentow wynosi: 4
liczba_studentow = 0
print("Liczba studentow wynosi: 0")

liczba_studentow = len(studenci)
print("Liczba studentów wynosi: {}".format(liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

# za pomoca petli i print przywitaj sie z kazdym studentem
# z tabeli studenci osobno
# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek
print("Hello Ania")

for student in studenci:
    print("Hello {}".format(student))

# zadanie 1.5

liczba = 3
potega = 4

wynik = 0

# oczekiwany rezultat:
# Wynik wynosi: 81
print("Wynik wynosi: 0")

wynik = pow(3,4)
print("Wynik wynosi: {}".format(wynik))

# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0

# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

liczba_nawiasow_otwierajacych = ciag_znakow.count('(')
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

# oczekiwany rezultat:
# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

posortowani_studenci = sorted(studenci)
print("Alfabetyczna lista studentow wynosi: ")
for student in posortowani_studenci:
    print(student)

# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

# oczekiwany rezultat:
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
# Anna Szczesny
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

studenci.sort(key=lambda s: s.split()[1])

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.9

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
print("Liczba studentow na N wynosi: 0")

for student in studenci:
    nazwisko = student.split()[1]
    if nazwisko[0] == 'N':
        liczba_n += 1

print("Liczba studentow na N wynosi: {}".format(liczba_n))
